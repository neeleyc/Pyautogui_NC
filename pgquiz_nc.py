import pyautogui as pg
import time

points = 0

# Question
answer = pg.prompt(
"""
Which would you rather do?

a)Go shopping all day with your best friend
b)Work all day to become a buisness man
c)Some sort of revenge on someone
d)Play lacrosse 


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points +=4


# Question
answer = pg.prompt(
"""
Which school would you rather go to?

a)NYU
b)Colombia


"""
    )

# Give points
if answer == "a":
    points += 4
elif answer == "b":
    points += 6


# Question
answer = pg.prompt(
"""
Which last name would you want to have?

a)Van der Woodsen
b)Bass
c)Waldorf
d)Archibald 


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points +=4


# Question
answer = pg.prompt(
"""
Where would you travel for spring break with your family?

a)Palm beach
b)NYC
c)Paris 
d)The hamptons


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points +=4



# Question
answer = pg.prompt(
"""
What would your job be?

a)Writer 
b)Owner of a hotel/ buisness man
c)Fashion designer
d)Athlete 


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points +=4


# Question
answer = pg.prompt(
"""
What eye and hair color combination would you want to have?

a)Blonde hair, blue eyes 
b)Black hair, brown eyes
c)Brown hair, brown eyes
d)Light Brown hair, blue eyes 


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points +=4


# Question
answer = pg.prompt(
"""
What part of NY would you live in?

a)Upper East Side
b)Upper West Side
c)Lower East Side
d)Brooklyn


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points +=4

# Question
answer = pg.prompt(
"""
What is your favorite color?

a)Pink
b)Black
c)Purple
d)Blue


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points +=4
    

# END OF SURVEY

pg.alert ("You are...")

#Serena Van der Woodsen
if points < 7:
    pg.alert("Serena Van der Woordsen")

#Chuck Bass
if points >=7 and points <13:
    pg.alert("Chuck Bass")

#Blaire Waldorf
if points >= 14 and points <20:
    pg.alert("Blaire Waldorf")

#Nate Archibald
if points >= 20 and points <30:
    pg.alert ("Nate Archibald")
    




