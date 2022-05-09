#Fallout V1.0 by Adam Odell (05/2022)
#A agent based model used for tracking bioligal weapon fallout according to wind direction.
# This file creates a GUI to run the model from, calls functions from particle_framework to run the model,
# writes the results to two text files called 'coordinates' and density and the displays
# the results on a graph



import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import particle_framework
import tkinter as tk  
from tkinter import ttk

#Open text files needed for writing
f1 = open('coordinates.txt', 'w', newline='')
f2 = open('density.txt', 'w', newline='')



#create GUI window

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 700, height = 380, bg='blue')
root.wm_title("Run Model")
canvas1.pack()

# Create labels and input boxes
title1 = tk.Label(root,text='Biological Weapon Tracking' )
title1.config(font=('helvetica', '12','bold'))
canvas1.create_window(350,20, window=title1)

label1 = tk.Label(root, text='Height of Building: Must be in range 1-100  and whole intergers only')
label1.config(font=('helvetica', 10))
canvas1.create_window(350, 80, window=label1)

entry1 = tk.Entry (root) 
canvas1.create_window(350, 120, window=entry1)

label3 = tk.Label(root, text='Number of Bacteria')
canvas1.create_window(350,160, window=label3)



#create current value label
# slider current value
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(round(current_value.get()))


def slider_changed(event):
    value_label.configure(text=get_current_value())


# value label
value_label = ttk.Label(
    root,
    text=get_current_value()
)
canvas1.create_window(350, 225, window=value_label)


#Create Slider for building height 
slider = ttk.Scale(
    root, 
    from_=1,
    to=4000,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
    
)
canvas1.create_window(350, 200, window=slider)




label2 = tk.Label(root, text='Select wind direction')
label2.config(font=('helvetica', 10))
canvas1.create_window(350, 260, window=label2)

# Create drop down menu to select wind direction
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


# Create function than runs the model. 

def run ():
    if float(entry1.get()) in range (1, 100, 1):
        #Create lists 
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
        
        #Create the particles contiang building height, bomb location and environment 
        for i in range(num_of_bacteria):
            particles.append(particle_framework.Particle(environment, bomb_y, bomb_x, building_height,i,))
        
           
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
            #print(str(particles[i]))
            while particles[i].z > 0:
                 particles[i].move(wind_direction)
                 particles[i].fall(building_height)
            #add data to 'data' (2d array)
            density[particles[i].y][particles[i].x] = density[particles[i].y][particles[i].x] + 1
            #Write results to fles including density map and Particles[i] string
            f1.write(str(particles[i])+'\n')
            f2.write(str(density))
            
        
        #Create density plot containg the locations of particles and bombing point 
        matplotlib.pyplot.imshow(density,'YlOrBr')
        matplotlib.pyplot.scatter(bomb_x,bomb_y,marker='X', color='RED',label='Bombing Point')
        matplotlib.pyplot.legend()
        
    else:
        print('Building height value out of range')
   
#Create button Used to run the Model
button1 = tk.Button(root, text='Run Model',bg='green',command=run)
canvas1.create_window(350, 360, window=button1)


tk.mainloop() 
f1.close()
f2.close()
print('Model Complete')






  


