class Character :
    def __init__(self,name,weapon):
        self.name = name
        self.weapon = weapon

    def intro(self) :
        print("name :",self.name)
        print("weapon:",self.weapon)

    
class Action(Character) :
    step = 0
    def move_forward(self,n):
        self.step +=n
        print("current location is %d"%self.step)
    def move_backward(self,n):
        self.step -=n
        print("current location is %d"%self.step) 
    def turn_r(self):
        print("turn right")
    def turn_l(self):
         print("turn left")
         
lugo = Action("Lugo","gun")
lugo = Action(10,7,)
lugo.intro()
lugo.move_forward(10)
lugo.move_backward(3)
lugo.turn_r()
lugo.turn_l()


    
