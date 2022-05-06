
import csv
import matplotlib
import matplotlib.pyplot
import particle_framework



#Open text files needed for writing
f1 = open('coordinates.txt', 'w', newline='')
f2 = open('density.txt', 'w', newline='')

#Create lists 
environment = []
particles = []
Final = [] 
final = environment



#Read text file and create environment text file.
f = open('wind.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:	
    rowlist = []
    for value in row:
        rowlist.append(value)			# A list of rows
    environment.append(rowlist)				# A list of value				
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.

#Set the number of bacteria and building height and read enviornment list to determine bombing point
num_of_bacteria = 3000
bomb_y = environment.index(max(environment))
bomb_x = environment[bomb_y].index(255.0)
building_height = 75

#Create the particles contiang building height 
for i in range(num_of_bacteria):
    particles.append(particle_framework.Particle(environment, bomb_y, bomb_x, building_height,i))



# Initialise as a list of lists with all values = 0
density = []
nrows = 300
ncols = 300
for y in range (0, nrows):
  row = []
  for x in range (0, ncols):
    row.append(0)
  density.append(row)



#move the particles using move function side to side and up or down using move 
#and fall functions when the elevtion is above zero
for i in range(num_of_bacteria):
    #print(str(particles[i]))
    while particles[i].z > 0:
         particles[i].move()
         particles[i].fall()
    #add data to 'data' (2d array)
    #for i in range(num_of_bacteria):
    density[particles[i].y][particles[i].x] = density[particles[i].y][particles[i].x] + 1
    f1.write(str(particles[i])+'\n')

    f2.write(str(density))

#Create density plot containg the locations of particles and bombing point 
matplotlib.pyplot.imshow(density,'YlOrBr')
matplotlib.pyplot.scatter(bomb_x,bomb_y)
matplotlib.pyplot.annotate("Bombing Point",((bomb_x +6),(bomb_y +4)))
f1.close()
f2.close()
    
print('all done')


    #Remove particles that have left the boundary 
    #matplotlib.pyplot.scatter(particles[i].x,particles[i].y)


  


