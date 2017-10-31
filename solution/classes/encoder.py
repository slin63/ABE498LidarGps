import numpy as np
from math import radians, cos, sin, asin, sqrt
from scipy.integrate import simps

class Encoder(object):
    def __init__(self, pos_data=None, theta_init=0, x_init=0, y_init=0):
        self.pos_data = pos_data
        self.theta_init = theta_init
        self.x_init = x_init
        self.y_init = y_init

    def num_integrate(self, start=0, end=None):
        if end is None:
            end = len(self.pos_data)

        # Units: degrees
        theta = self.theta_init
        x = self.x_init
        y = self.y_init

        # dt: in seconds, assume constant dt between measurements (although not true)
        dt = .200
        step = start

        velocity = self._get_series_from_pos_data(field="velocity", type=float)
        theta_dot = self._get_series_from_pos_data(field="theta_dot", type=float)
        time = self._get_series_from_pos_data(field="sys_time_ms", type=float, factor=0.001)

        while step != end:
            # Find changing x, y, theta
            x_dot = velocity[step] * cos(theta) * dt
            y_dot = velocity[step] * sin(theta) * dt
            t_dot = theta_dot[step]

            theta += t_dot * dt
            x += x_dot
            y += y_dot

            step += 1

        return x, y, theta

    def final_displacement(self):
        lat1 = float(self.pos_data[0].latitude_deg)
        lon1 = float(self.pos_data[0].longitude_deg)

        lat2 = float(self.pos_data[-1].latitude_deg)
        lon2 = float(self.pos_data[-1].longitude_deg)

        R = 6372.8 # in KM

        dLat = radians(lat2 - lat1)
        dLon = radians(lon2 - lon1)
        lat1 = radians(lat1)
        lat2 = radians(lat2)

        a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
        c = 2*asin(sqrt(a))

        return R * c

    def _get_series_from_pos_data(self, field, type, factor=1):
        series_l = []
        for pos in self.pos_data:
            data = type(getattr(pos, field)) * factor
            series_l.append(data)

        return series_l

    def set_pos_data(self, pos_data):
        self.pos_data = pos_data

    def __repr__(self):
        return("# Of data points: {0}".format(len(pos_data)))
