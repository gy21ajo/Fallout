# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 11:57:58 2022

@author: odell
"""
import csv
import matplotlib

environment = []


f = open('Wind.Raster.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:	
    rowlist = []
    for value in row:
        rowlist.append(value)			# A list of rows
    environment.append(rowlist)				# A list of value				
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
     
        
print(environment)

#matplotlib.pyplot.xlim(0, len(environment[0]))
#matplotlib.pyplot.ylim(0, len(environment))
#matplotlib.pyplot.imshow(environment)
