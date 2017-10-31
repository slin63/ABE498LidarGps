from parsers.parse_csv import parse_csv_to_object, clean_leading_whitespace
from classes.pos_data import PositionData
from classes.encoder import Encoder


# x_dot = v cos(theta)
# y_dot = v sin(theta)
# theta_dot = w

# U_l and U_r are the velocities for right and left encoders
# V = 1/2 (U_l + U_r)
# w = 1 / L (U_l - U_r), L = 13 inches


if __name__ == '__main__':
    FILE_DIR = "/Users/sSDSD/Documents/ABE498/Lab2/q1/gps_data.csv"
    ATTRIBUTES = ["sys_time_ms", "mhe_yaw_rad", "latitude_deg",
    "longitude_deg", "enc_speed_left_m_s", "enc_speed_right_m_s"]
    OBJ = PositionData

    # First, purge the csv file of these weird whitespaces.
    clean_leading_whitespace(csv=FILE_DIR)

    # Convert csv rows into python objects.
    pos_data = parse_csv_to_object(FILE_DIR, OBJ, ATTRIBUTES, ',')

    # Store all data into a wrapper class with data analysis functions
    encoder = Encoder(pos_data)

    # Numerically integrate the data
    print(encoder.num_integrate())
    print(encoder.final_displacement() * 1000)


