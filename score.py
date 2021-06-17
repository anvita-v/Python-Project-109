import pandas as pd 
import statistics
import csv

df = pd.read_csv("data.csv")

reading_list = df["reading score"].to_list()
writing_list = df["writing score"].to_list()

reading_mean = statistics.mean(reading_list)
writing_mean = statistics.mean(writing_list)

reading_median = statistics.median(reading_list)
writing_median = statistics.median(writing_list)

reading_mode = statistics.mode(reading_list)
writing_mode = statistics.mode(writing_list)

reading_stdev = statistics.stdev(reading_list)
writing_stdev = statistics.stdev(writing_list)

r_first_stdev_start, r_first_stdev_end = reading_mean - reading_stdev, reading_mean + reading_stdev
r_second_stdev_start, r_second_stdev_end = reading_mean - (2*reading_stdev), reading_mean + (2*reading_stdev)
r_third_stdev_start, r_third_stdev_end = reading_mean - (3*reading_stdev), reading_mean + (3*reading_stdev)


w_first_stdev_start, w_first_stdev_end = writing_mean - writing_stdev, writing_mean + writing_stdev
w_second_stdev_start, w_second_stdev_end = writing_mean - (2*writing_stdev), writing_mean + (2*writing_stdev)
w_third_stdev_start, w_third_stdev_end = writing_mean - (3*writing_stdev), writing_mean + (3*writing_stdev)

r_data_list_within_first_stdev = [result for result in reading_list if result > r_first_stdev_start and result < r_first_stdev_end]
r_data_list_within_second_stdev = [result for result in reading_list if result > r_second_stdev_start and result < r_second_stdev_end]
r_data_list_within_third_stdev = [result for result in reading_list if result > r_third_stdev_start and result < r_third_stdev_end]

w_data_list_within_first_stdev = [result for result in writing_list if result > w_first_stdev_start and result < w_first_stdev_end]
w_data_list_within_second_stdev = [result for result in writing_list if result > w_second_stdev_start and result < w_second_stdev_end]
w_data_list_within_third_stdev = [result for result in writing_list if result > w_third_stdev_start and result < w_third_stdev_end]

print("mean, median, mode of reading is {}, {} and {} respectivly".format(reading_mean, reading_median, reading_mode))
print("mean, median, mode of writing is {}, {} and {} respectivly".format(writing_mean, writing_median, writing_mode))

print("-----------")

print("{}% of data for reading lies within 1 standard deviation".format(len(r_data_list_within_first_stdev)*100.0/len(reading_list)))
print("{}% of data for reading lies within 2 standard deviation".format(len(r_data_list_within_second_stdev)*100.0/len(reading_list)))
print("{}% of data for reading lies within 3 standard deviation".format(len(r_data_list_within_third_stdev)*100.0/len(reading_list)))

print("-----------")

print("{}% of data for writing lies within 1 standard deviation".format(len(w_data_list_within_first_stdev)*100.0/len(writing_list)))
print("{}% of data for writing lies within 2 standard deviation".format(len(w_data_list_within_second_stdev)*100.0/len(writing_list)))
print("{}% of data for writing lies within 3 standard deviation".format(len(w_data_list_within_third_stdev)*100.0/len(writing_list)))


