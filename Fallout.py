#Fallout V1.0 by Adam Odell (05/2022)
#Licensed under a MIT License 
#A agent based model used for tracking bioligal weapon fallout according to wind direction.
# This file creates a GUI to run the model from, calls functions from the class particle_framework to run the model,
# writes the results to two text files called 'coordinates' and density and the displays
# the results on a graph


import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
from matplotlib.figure import Figure 
import particle_framework
import tkinter as tk  
from tkinter import ttk
import time 
from tkinter import *

#Open text files needed for writing
f1 = open('coordinates.txt', 'w', newline='')
f2 = open('density.txt', 'w', newline='')

#create GUI window
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 700, height = 500)
root.wm_title("Run Model")
canvas1.pack()

# Create labels and input boxes for building height
title1 = tk.Label(root,text='Biological Weapon Tracking' )
title1.config(font=('helvetica', '12','bold'))
canvas1.create_window(350,20, window=title1)

label1 = tk.Label(root, text='Height of Building (m): Must be in range 1-100  and whole intergers only')
label1.config(font=('helvetica', 10))
canvas1.create_window(350, 80, window=label1)

entry1 = tk.Entry (root) 
canvas1.create_window(350, 120, window=entry1)

label3 = tk.Label(root, text='Number of Bacteria')
canvas1.create_window(350,160, window=label3)

fig = Figure(figsize=(5, 4), dpi=100)


#This sections creates a sliding bar to select number of bacteria and displays the current value
# slider current value
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(round(current_value.get()))

def slider_changed(event):
    value_label.configure(text=get_current_value())


#Create Slider for building height 
slider = ttk.Scale(
    root, 
    from_=1,
    to=4000,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value,
)
canvas1.create_window(350, 200, window=slider)

# value label
value_label = ttk.Label(root, text=get_current_value())
canvas1.create_window(350, 225, window=value_label)

label2 = tk.Label(root, text='Select wind direction')
label2.config(font=('helvetica', 10))
canvas1.create_window(350, 260, window=label2)

# This sections Createas a drop down menu to select wind direction from a variable
# calleds options
 
options = ["North",
           "East",
           "South",
           "West"]

variable = tk.StringVar(root)
variable.set(options[0])
w = tk.OptionMenu(root, variable, *options)
w.config(font=('Helvetica', 10))
w.pack()
canvas1.create_window(350, 300, window=w)

#When this function is called it opens a pop up window informing the user of a
#a error associated with building height input.
def open_popup():
   """
    This Function creates a pop up window which informs the user about a error
    associated with the input of building height

    Returns
    -------
    None.

    """ 
   top = Toplevel(root)
   top.geometry("750x250")
   top.title("Error")
   Label(top, text= 'Error with inputting building height. \n Please enter a integer between 1 and 100', font=('Helvetica 10 bold')).place(x=150,y=80)


#This function runs the model when called from the button on the GUI

def run ():
    """
    This Function is called when the 'Run Model' button is pressed on the GUI 
    and contains the code which calls functions from particle_framework to
    run the model, write the text files and plot the graphs. 

    Returns
    -------
    None.

    """
    #The first section trys to convert the input into a integer. If this is not possible
    # it skips this section and returns an error message 
    try:
        int(entry1.get())
            
   #This section checks if the building height is in the correct range
        if int(entry1.get()) in range (1, 101, 1):
            #Create lists for all the variables needed
            start = time.time()
            environment = []
            particles = []
                
            #Read text file and create environment variable
            f = open('wind.txt', newline='') 
            reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:	
                rowlist = []
                for value in row:
                    rowlist.append(value)			# A list of rows
                environment.append(rowlist)				# A list of value				
            f.close() 	# Don't close until you are done with the reader;
            		# the data is read on request.
            
            #Set the number of bacteria, building height, wind direction and read enviornment list to determine bombing point
            num_of_bacteria = int(slider.get()) #int(entry1.get()) 
            bomb_y = environment.index(max(environment))
            bomb_x = environment[bomb_y].index(255.0)
            building_height = (int(entry1.get()))
            wind_direction = variable.get()
            
            #Test comment used to test the  location of the bombing.
            #print(bomb_y,bomb_x)
            
            #Create the particles contiang building height, bomb location and environment 
            for i in range(num_of_bacteria):
                particles.append(particle_framework.Particle(environment, bomb_y, bomb_x, building_height,i,))
                # Test comment used to check the wind.txt is reading correctly
                # assert particles[i].z == building_height, "Elevation should equal building height"
                # assert particles[i].x == 50, "x should equal 50"
                # assert particles[i].y == 150, "y should equal 150"
               
            # Initialise as a list of lists with all values = 0 to repsent 2d array
            density = []
            nrows = 300
            ncols = 300
            for y in range (0, nrows):
              row = []
              for x in range (0, ncols):
                row.append(0)
              density.append(row)
            
               
               
            #move the particles using move function side to side and up or down according to wind_direction
            #and fall functions when the elevtion is above zero
            for i in range(num_of_bacteria):
                while particles[i].z > 0:
                     particles[i].move(wind_direction)
                     particles[i].fall(building_height)
                #add data to 'data' (2d array)
                density[particles[i].y][particles[i].x] = density[particles[i].y][particles[i].x] + 1
                #Write results to fles including density map and Particles[i] string
                f1.write(str(particles[i])+'\n')
                f2.write(str(density))
            
            # Test Comment to check particles are stopping movement when they reach the ground (z=0)
            # assert particles[i].z == 0, "Elevation should = 0"
            
            
            #Create density plot containg the locations of particles and bombing point 
            matplotlib.pyplot.imshow(density,'YlOrBr')
            matplotlib.pyplot.scatter(bomb_x,bomb_y,marker='X', color='RED',label='Bombing Point')
            matplotlib.pyplot.legend()
            matplotlib.pyplot.show()
            
            #Final model checks including end of timing and pritning.   
            end = time.time()
            print(f"Runtime of the program is {end - start}")
            label4 = tk.Label(root, text='Model complete. Please run again or close all figures down')
            label4.config(font=('helvetica', 10),bg='green')
            canvas1.create_window(350, 450, window=label4)
        else:
            open_popup()
    except ValueError:
       open_popup()
              
        
#Create button Used to run the Model and call the run function
button1 = tk.Button(root, text='Run Model',command=run)
canvas1.create_window(350, 360, window=button1)

#close and end loop
tk.mainloop() 
f1.close()
f2.close()
print('Programme Complete')







  


