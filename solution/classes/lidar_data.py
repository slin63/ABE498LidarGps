from math import sin, cos, radians


class LidarData(object):
    def __init__(self, lidar_str):
        self.lidar_l = self._parse_lidar_str(lidar_str)
        self.time = self.lidar_l[0]
        self.distance_map = self._parse_lidar_dist(self.lidar_l[1:])
        self.range_coordinate_x, self.range_coordinate_y = self._range_coordinate_series()

    def _parse_lidar_dist(self, lidar_l):
        START_ANGLE = -135
        END_ANGLE = 134.75
        RESOLUTION = 0.25

        current_angle = START_ANGLE
        angle_dict = {}
        index = 0

        while current_angle != END_ANGLE + RESOLUTION:
            angle_dict[current_angle] = int(lidar_l[index])

            index += 1
            current_angle += RESOLUTION

        return angle_dict

    # Work through all distance/angle pairs in the distance map
    # And create vectors for each.
    def _range_coordinate_series(self):
        x_series = []
        y_series = []

        for angle in self.distance_map:

            x = self.distance_map[angle] * cos(radians(angle))
            y = self.distance_map[angle] * sin(radians(angle))

            x_series.append(x)
            y_series.append(y)

        return x_series, y_series

    def _parse_lidar_str(self, lidar_str)   :
        return lidar_str.split(',')

    def __repr__(self):
        return "LiDar"


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<{0}, {1}>".format(self.x, self.y)
