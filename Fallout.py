# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 11:57:58 2022

@author: odell
"""
import csv
import matplotlib

environment = []


# f = open('Wind.Raster.txt', newline='') 
# reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# for row in reader:	
#     rowlist = []
#     for value in row:
#         rowlist.append(value)			# A list of rows
#     environment.append(rowlist)				# A list of value				
# f.close() 	# Don't close until you are done with the reader;
# 		# the data is read on request.

file1 = open('Wind.Raster.txt')
environment = file1.readlines()
print(environment)
file1.close()

matplotlib.pyplot.imshow(environment)