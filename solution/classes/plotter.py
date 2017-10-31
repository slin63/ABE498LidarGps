import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np

# Actively updating plots in matplotlib
# https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib

# Class to visualize LidarData using a constantly updating Matplotlib graph
class LidarVisualizer(object):
    def __init__(self, lidar_data_l):
        self.lidar_data_l = lidar_data_l

    # https://stackoverflow.com/questions/42722691/python-matplotlib-update-scatter-plot-from-a-function
    # http://block.arch.ethz.ch/blog/2016/08/dynamic-plotting-with-matplotlib/
    def visualize(self, speed=10):
        print("visualizing")
        resized_data_set = self._size_down_series(self.lidar_data_l, speed)

        fig, ax = plt.subplots()

        init_frame = self.lidar_data_l[0]
        init_x = np.array(init_frame.range_coordinate_x)
        init_y = np.array(init_frame.range_coordinate_y)

        sc = ax.scatter(init_x, init_y)

        plt.xlim(-2000, 20000)
        plt.ylim(-20000, 20000)


        for frame in resized_data_set[1:]:
            x = np.array(frame.range_coordinate_x)
            y = np.array(frame.range_coordinate_y)
            ax.set_title('t = {0} [ms]'.format(frame.time))

            sc.set_offsets(np.c_[x,y])
            fig.canvas.draw_idle()
            plt.pause(0.001)

        plt.waitforbuttonpress()

    # 2x speed: Delete 1/2 entries
    # Nx speed: Delete (n-1)/n entries
    def _size_down_series(self, series, factor):
        out_series = []
        count = 0
        count_max = factor

        for val in series:
            if count == count_max:
                out_series.append(val)
                count = 0
            else:
                count += 1

        return out_series

    def __repr__(self):
        return len(self.lidar_data_l)
