import random 

class Particle :
    '''This class contains all the functions to move the particles'''
    def __init__(self, environment, bomb_y, bomb_x, building_height, ia, ):
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
         
    def move (self):
            direction = random.randint(0,100)
            
            
            if direction < 75:
                self.x = (self.x + 1) % len(self.environment[0])
            elif direction in range (76, 80):
                self.x = (self.x - 1) % len(self.environment[0])
            elif direction in range (81, 90): 
                self.y = (self.y + 1) % len(self.environment)
            else: 
                self.y = (self.y -1) % len(self.environment)

                    
            
    def fall (self):
        elevation = random.randint(0,100)
        
        if self.z >= 75: 
            if elevation <= 20:
                self.z = (self.z + 1)
            elif elevation in range (21, 30):
                self.z = self.z 
            else:
                self.z = (self.z - 1) 
        else:
            self.z = (self.z - 1) 
