#Particle_framework V1.0 by Adam Odell to be run with Fallout.py
#Licensed under a MIT License
#This file contains the class Particle, which contains functions to move the 
#particles dependent on both wind direction and 'random' and fall, the rate the 
#particles fall at dependet on building heigh and 'random'

import random 

class Particle :
    '''This class contains all the functions to move the particles'''
    def __init__(self, environment, bomb_y, bomb_x, building_height, ia,):
         self.environment = environment 
         self.y = bomb_y
         self.x = bomb_x
         self.z = building_height
         self.id = ia
         
    
    def __str__(self):
        """
        This function creates an id for agents 

        Returns
        id of each agent 
        x = position
        y = position
        store = number of agents in  store 
        -------
        TYPE
            DESCRIPTION.

        """
        return "id = " + str(self.id) + ", x =" + str(self.x) + ", y =" + str(self.y) + ", height =" + str(self.z)
         
    def move (self, wind_direction):
            """
        This function moves the Particles in a random direction dependent on the wind speed or a random factor and  
        changes self.x or self.y repsecively. 

        Parameters
        ----------
        wind_direction : Text string
            The direction of the wind as selected by the user in the GUI,

        Returns
        -------
        None.

        """        
            direction = random.randint(0,100)
            
            if wind_direction == 'East':
                if direction < 75:
                    self.x = (self.x + 1) % len(self.environment[0])
                elif direction in range (76, 80):
                    self.x = (self.x - 1) % len(self.environment[0])
                elif direction in range (81, 90): 
                    self.y = (self.y + 1) % len(self.environment)
                else: 
                    self.y = (self.y -1) % len(self.environment)
            if wind_direction == 'West':
                if direction < 75:
                    self.x = (self.x - 1) % len(self.environment[0])
                elif direction in range (76, 80):
                    self.x = (self.x + 1) % len(self.environment[0])
                elif direction in range (81, 90): 
                    self.y = (self.y + 1) % len(self.environment)
                else: 
                    self.y = (self.y -1) % len(self.environment)
            if wind_direction == 'South':
                if direction < 75:
                    self.y = (self.y - 1) % len(self.environment)
                elif direction in range (76, 80):
                    self.y = (self.y + 1) % len(self.environment)
                elif direction in range (81, 90): 
                    self.x = (self.x + 1) % len(self.environment[0])
                else: 
                    self.x = (self.x -1) % len(self.environment[0])
            if wind_direction == 'North':
                if direction < 75:
                    self.y = (self.y + 1) % len(self.environment)
                elif direction in range (76, 80):
                    self.y = (self.y - 1) % len(self.environment)
                elif direction in range (81, 90): 
                    self.x = (self.x + 1) % len(self.environment[0])
                else: 
                    self.x = (self.x -1) % len(self.environment[0])
                
            
    def fall (self,building_height):
        """
        This function determines if the particle falls or rises dependent on the height of the building and
        then changes self.z
        
        Parameters 
        Building Height: Integer
            Integer entred into the GUI by the user. 
   
        Returns
        -------
        None.

        """
        elevation = random.randint(0,100)
        
        if self.z >= building_height: 
            if elevation <= 20:
                self.z = (self.z + 1)
            elif elevation in range (21, 30):
                self.z = self.z 
            else:
                self.z = (self.z - 1) 
        else:
            self.z = (self.z - 1) 
