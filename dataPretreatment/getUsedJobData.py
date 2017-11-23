# -*- coding:utf-8 -*-
# __author__ = 'cm'
import csv


if __name__ == '__main__':
    # open file named job.csv
    readfilename = '../dataset/job.csv'
    openRfile = open(readfilename,'r')
    reader = csv.reader(openRfile)
    # creat a new file to save data
    wirtefilename = '../dataset/real_job.csv'
    openWfile = open(wirtefilename,'wb')
    writer = csv.writer(openWfile)
    for row in reader:
        new_R =[row[3],row[0],row[1],row[2],row[4],row[5],row[7],row[8],row[9],row[11]]
        # new_R.append(row[3],row[0],row[1],row[2],row[4],row[5],row[7],row[8],row[9],row[11])
        writer.writerow(new_R)
    openRfile.close()
    openWfile.close()
