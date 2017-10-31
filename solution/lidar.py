# Use solution from #1 to gather extra information for #2
# LiDAR     Lab:     The     LiDAR     lab     contains     the     time-stamped     Each LiDAR file contains   1081   elements, being the first a timestamp in the same time frame as sys_time_ms from the other file. Every  other  element  has  a  respective  angle  of  reading,  starting  with -135degree  and ending with 134.75degreewith 0.25 degree angular resolution

from parsers.parse_csv import parse_csv_to_object, clean_leading_whitespace, parse_csv_with_constructor
from classes.lidar_data import LidarData
from classes.plotter import LidarVisualizer
from classes.encoder import Encoder


if __name__ == '__main__':
    FILE_DIR = "/Users/sSDSD/Documents/ABE498/Lab2/q2/lidar_data.csv"
    OBJ = LidarData

    # First, purge the csv file of these weird whitespaces.
    clean_leading_whitespace(csv=FILE_DIR)

    # Convert csv rows into python objects.
    lidar_data = parse_csv_with_constructor(FILE_DIR, OBJ, ',')

    visualizer = LidarVisualizer(lidar_data)

    visualizer.visualize()



