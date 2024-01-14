def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def draw_square():
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() != True:
    jump()

# another way with neglation
# while not at_goal():
#     jump()
