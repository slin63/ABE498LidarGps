from math import sin, cos

class PositionData(object):
    def __init__(self, sys_time_ms=None, traj_error_x_m=None, traj_error_y_m=None, mhe_dx_m=None, mhe_dy_m=None, mhe_yaw_rad=None, mhe_speed_m_s=None, latitude_deg=None, longitude_deg=None, enc_speed_left_m_s=None, enc_speed_right_m_s=None):
        # Unparsed data from CSV
        self.sys_time_ms = sys_time_ms
        self.mhe_dx_m = mhe_dx_m
        self.mhe_dy_m = mhe_dy_m
        self.mhe_speed_m_s = mhe_speed_m_s
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.mhe_yaw_rad = mhe_yaw_rad
        self.enc_speed_left_m_s = enc_speed_left_m_s
        self.enc_speed_right_m_s = enc_speed_right_m_s
        self.vector = None

        # Integration factors
        self.velocity = None
        self.x_dot = None
        self.y_dot = None
        self.theta_dot = None

        # L = 13 inches, 0.3302 meters
        self.L = 0.3302

    def init_params(self):
        self.velocity = 0.5 * (float(self.enc_speed_right_m_s) + float(self.enc_speed_left_m_s))
        self.theta_dot = (float(self.enc_speed_left_m_s) - float(self.enc_speed_right_m_s)) / self.L

    def __repr__(self):
        return("t = {0}. v = <{1}, {2}>, |v| = {3}\n\tLat/Long = <{4}, {5}>".format(
                  self.sys_time_ms, self.mhe_dx_m, self.mhe_dy_m, self.mhe_speed_m_s, self.latitude_deg, self.longitude_deg))


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<{0}, {1}>".format(x, y)
