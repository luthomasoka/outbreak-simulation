import turtle
import random
import time

def main():
    # Defines screen object
    sc = turtle.Screen()
    sc.setup(500, 500)
    sc.bgcolor("black")
    sc.tracer(0)
    persons = []

    # Appends turtle object to persons list
    for _ in range(25):
        persons.append(turtle.Turtle())

    mass = 13
    
    # Randomly selects an infected object   
    infected = random.randint(0, len(persons))

    # Defines each objects appearance, placement and speed
    for index, person in enumerate(persons):
        person.shape("circle")
        person.shapesize(mass/20)
        if index != infected:
            person.color("orange")
        else:
            person.color("cyan")
        person.penup()
        person.speed(0)
        person.radius = mass/2

        # Places each person in random positions on screen
        x = random.randint(-190, 190)
        y = random.randint(-100, 200)
        
        person.goto(x, y)
        person.dy = random.randint(-4, 4)
        person.dx = random.randint(-4, 4)

    # gets current time    
    startTime = time.time()

    while True:
        sc.update()
        timeTaken = time.time() - startTime

        for index, person in enumerate(persons):

            # ball movement
            person.sety(person.ycor() + person.dy)
            person.setx(person.xcor() + person.dx)

            # bottom and ceiling collision
            person.dy = bottom_ceiling_collision(person)

            # wall collision
            person.dx = wall_collision(person)
                
            # collision Detection
            for i in range(0, len(persons)):
                for j in range(i + 1, len(persons)):
                    if persons[i].distance(persons[j]) < (persons[i].radius + persons[j].radius):
                        temp_dx = persons[i].dx
                        temp_dy = persons[i].dy
                        
                        persons[i].dx = persons[j].dx
                        persons[i].dy = persons[j].dy
                        
                        persons[j].dx = temp_dx
                        persons[j].dy = temp_dy

                        sc.onkeypress(lambda i=i, infect=infected, obj=persons[j]: single_infection(i, infect, obj), key='1')

                        sc.onkeypress(lambda a=persons[i], b=persons[j]: multiple_infections(a, b), key='2')
                        

        sc.onkeypress(lambda objs=persons: stop_movement(objs), key='0')

        sc.title(f"Outbreak Simulation: Time Taken - {int(round(timeTaken, 2))} sec")

        sc.listen()
                        

def bottom_ceiling_collision(obj):
    """ Reverses the direction of the object
    when it collides with the floor or the 
    ceiling

    parameter: The turtle object
    return: The turtle object's vertical velocity
    """

    if obj.ycor() < -240 or obj.ycor() > 240:
        obj.dy *= -1
    return obj.dy


def wall_collision(obj):
    """ Reverses the direction of the object
    when it collides with the right or the 
    left side wall

    parameter: The turtle object
    return: The turtle object's horizontal velocity
    """

    if obj.xcor() > 240 or obj.xcor() < -240:
        obj.dx *= -1
    return obj.dx


def multiple_infections(obj_a, obj_b):
    """ Changes the color of the second object
    to the same color of the first.

    Parameters
    a: First object
    b: second object that is collided with
    """

    if obj_a.color() == ("cyan", "cyan"):
        obj_b.color("cyan")
    elif obj_b.color() == ("cyan", "cyan"):
        obj_a.color("cyan")


def single_infection(iterator, infected, obj):
    """ If the iterator object is infected
    the color of the object it collided with 
    should change

    parameters
    iterator:The current object the iterator
    on
    infected: The object that is currently infected
    obj: The object that is collided with
    """

    if iterator == infected:
        obj.color("cyan")


def stop_movement(objs):
    """ Stops the movement of some
    of the turtle objects in the list

    Parameter
    objs: list that has all the objects
    """

    for i in range(10):
        objs[i].dx = 0
        objs[i].dy = 0


if __name__ == "__main__":
    main()