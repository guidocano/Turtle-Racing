import turtle
import time
import random
import sys


WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
choice = ""


while True:


# START

    def start():
        global choice
        choice = ""
        choice = input("What do you want to do? (race/farm/exit) ")
        if choice == "race":
            return
        elif choice == "farm":
            return
        elif choice == "exit":
            print("See you next time!")
            time.sleep(2)
            sys.exit()
        else:
            start()

# END START

# TURTLE RACE

    def get_number_of_racers():
        racers = 0
        while True:
            racers = input('Enter the number of racers (2-10): ')
            if racers.isdigit():
                racers = int(racers)
            else:
                print('Please insert a number between 2 and 10.')
                continue

            if 2 <= racers <= 10:
                return racers
            else:
                print('Number not in range. Try again!')
                

    def race(colors):
        turtles = create_turtles(colors)

        while True:
            for racer in turtles:
                distance = random.randrange(1,25)
                racer.forward(distance)

                x, y = racer.pos()
                if y >= HEIGHT // 2 - 10:
                    time.sleep(1)
                    turtle.bye()
                    return colors[turtles.index(racer)]

    def create_turtles(colors):
        turtles = []
        spacingx =  WIDTH // (len(colors) +1)
        for i, color in enumerate(colors):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.left(90)
            racer.penup()
            racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
            racer.pendown()
            turtles.append(racer)

        return turtles

    def init_turtle():
        screen = turtle.Screen()
        screen.setup(WIDTH, HEIGHT)
        screen.title('Turtle Racing!')

# END TURTLE RACE


# TURTLE FARM

    def farm(colors):
        turtles = create_turtles_farm(colors)

        while True:
            for racer in turtles:
                distance = random.randrange(0,8)
                direction = random.randrange(140, 220)
                racer.forward(distance)

                x, y = racer.pos()
                if y >= HEIGHT // 2 - 10 or y <= -HEIGHT // 2 + 10 or x >= WIDTH // 2 - 10 or x <= -WIDTH // 2 + 10:
                    racer.left(direction)
                    racer.forward(20)

                

    def create_turtles_farm(colors):
        turtles = []
        spacingx =  WIDTH // (len(colors) +1)
                
        for i, color in enumerate(colors):
            turtle.hideturtle()
            turtle.write("Just chilling...", move=False, align='center', font=("Arial", 16, "normal"))
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.penup()
            positionx = random.randrange(-WIDTH//2 + 20,WIDTH//2 - 20)
            coin = random.randrange(0,360)
            racer.left(coin)
            racer.setpos(-WIDTH//2 + (i+1) * spacingx, positionx)
            racer.pendown()
            turtles.append(racer)

        return turtles

    def init_turtle_farm():
        screen = turtle.Screen()
        screen.setup(WIDTH, HEIGHT)
        screen.title('Turtle Farm')

# END TURTLE FARM


# MENU

    start()
    if choice == "race":

        racers = get_number_of_racers()
        init_turtle()

        random.shuffle(COLORS)
        colors = COLORS[:racers]

        winner = race(colors)
        print("The winner is the " + winner + " turtle!")
        time.sleep(1)
        print("Congratulations " + winner + "!")
        time.sleep(1)
        turtle.TurtleScreen._RUNNING = True

        
    elif choice == "farm":
        print("Welcome to Turtle Farm.")
        time.sleep(1)
        print("Close window to exit.")
        racers = 10
        
        init_turtle_farm()

        random.shuffle(COLORS)
        colors = COLORS[:racers]

        farm(colors)
        


# END MENU




    # turtle.clearscreen()
    # turtle.hideturtle()
    # turtle.write("Preparing Turtles...", move=False, align='center', font=("Arial", 16, "normal"))
    









# racer = turtle.Turtle()
# racer.speed(1)
# racer.shape('turtle')
# racer.color('cyan')
# racer.forward(100)
# racer.left(90)
# racer.forward(100)
# racer.right(90)
# racer.backward(100)
