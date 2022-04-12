import random 

class particle :
    '''This class contains all the functions to move the particles'''
     def __init__(self, environment, agents, y, x, ia, wolfs):
         self.environment = environment 
         self.y = y
         self.x = x
         self.z = z
         self.id = ia
    
     def __str__(self):
        """
        This function creates an id for particles 

        Returns
        id of each agent 
        x = North south positom
        y = East West position
        z = Elevation
       
        -------
        TYPE
            DESCRIPTION.

        """
        return "id = " + str(self.id) + ", x =" + str(self.x) + ", y =" + str(self.y) + ", z =" + str(self.z)
         
        def move :
            random.x = random.randint(0,100)
            random.y = random.randint(0,100)
            random.z = random.randint(0,100)
            if random.x => 5 :
                self.x = (self.x - 1)
            else:
                self.x = (self.x + 1)
            
            if random.y = < 75:
                self.y = (self.y + 1)
            else:
                self.y = (self.y - 1)
                
            if random.z = > 20:
                self.z = (self.z + 1)
            elif random in range (21, 30 [,1]):
                self.z = self.z
            else 
                self.z = (self.z - 1)