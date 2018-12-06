import pyautogui as pg
import webbrowser as wb
import time as t

points = 0

show = pg.prompt("What is your favorite show?")

if show == "South Park":
    pg.alert("SAME")
    wb.open( "https://www.youtube.com/watch?v=S8p22rtNMoM")
    t.sleep(3)
    points += 5
elif show == "Family Guy":
    pg.alert("Noice")
    wb.open( "https://www.youtube.com/watch?v=Y9j3heYZAk8")
    t.sleep(3)
    points += 5
elif show == "Rick and Morty":
    pg.alert("I'm pickle Rick")
    wb.open( "https://www.youtube.com/watch?v=tZp8sY06Qoc")
    t.sleep(3)
    points += 7
elif show == "The Cleaveland Show":
    pg.alert("Rolo is the best")
    wb.open( "https://www.youtube.com/watch?v=LNDXrKBOKrw")
    t.sleep(3)
    points += 3
elif show == "Pepe Pig":
    pg.alert("I love that show")
    wb.open( "https://www.youtube.com/watch?v=DP1pQkm9Op0")
    t.sleep(3)
    points -= 5
elif show == "Impractical Jokers":
    pg.alert("Kate likes that show")
    wb.open( "https://www.youtube.com/watch?v=sZDLA35-JZQ")
    t.sleep(3)
    points -= 3
else:
    pg.alert("OK, bud")

person = pg.prompt("Who's the best person in school?")

if person == "Kate":
    pg.alert("#Oof")
    wb.open( "https://www.youtube.com/watch?v=2hCpFQG1-q8")
    t.sleep(3)
    points += 5
elif person == "Todd":
    pg.alert("#NOICE")
    points += 7
elif person == "Nicky":
    pg.alert("Ok Kicky")
    points -= 3
elif person == "Sofia":
    pg.alert("Sofia is smart")
    points -= 3
elif person == "Teddy":
    pg.alert("I hit him with a squah ball")
    points += 1
elif person == "Tobey":
    pg.alert("YAY")
    points += 2
elif person == "Field":
    pg.alert("Cool")
    points -= 3
elif person == "Matt":
    pg.alert("He's the best")
    points += 5
else:
    pg.alert("Well")

fortnite = pg.prompt("What's the best Fortnite dance?")

if fortnite == "Star Power":
    pg.alert("Cool")
    wb.open( "https://www.youtube.com/watch?v=VCpKPvxlQqc")
    t.sleep(3)
elif fortnite == "Ture Heart":
    pg.alert("My favorite dance")
    wb.open( "https://www.youtube.com/watch?v=9roYSa8pOXI")
    t.sleep(3)
    points += 2
elif fortnite == "Best Mates":
    pg.alert("I like that too")
    wb.open( "https://www.youtube.com/watch?v=KSeiXnobx5A")
    t.sleep(3)
    points += 1
elif fortnite == "Groove Jam":
    pg.alert("Good Choice")
    wb.open( "https://www.youtube.com/watch?v=kELYv8_Bb9s")
    t.sleep(3)
elif fortnite == "Boneless":
    pg.alert("Ryan likes that dance")
    wb.open( "https://www.youtube.com/watch?v=XLx00osTmYA")
    t.sleep(3)
    points -= 5
elif fortnite == "The Worm":
    pg.alert("I don't have that one")
    wb.open( "https://www.youtube.com/watch?v=jQwWi48vJ9k")
    t.sleep(3)
    points += 3
else:
    pg.alert("Noooooooo")

sport = pg.prompt("What's the best sport")

if sport == "soccer":
    pg.alert("AWAY from pressure")
    wb.open( "https://www.youtube.com/watch?v=xYswEFtjSnI")
    t.sleep(3)
    points -= 5
elif sport == "Hockey":
    pg.alert("best sport")
    wb.open( "https://www.youtube.com/watch?v=hBo7vVzOjCE")
    t.sleep(3)
    points += 7
elif sport == "Lacrosse":
    pg.alert("good choice")
    wb.open( "https://www.youtube.com/watch?v=C52jkR8fYdE")
    t.sleep(3)
    points += 3
elif sport == "Squash":
    pg.alert("I hit Teddy D with a squash ball")
elif sport == "Gymnastics":
    pg.alert("Have you seen the fail videos?")
    wb.open( "https://www.youtube.com/watch?v=PH7M7q6akss")
    t.sleep(3)
    points -= 5
elif sport == "Football":
    pg.alert("Quarter Back?")
    points += 2
else:
    pg.alert("Hockey is better")

food = pg.prompt("What is the best food?")

if food == "Pizza":
    pg.alert("Dude, actually?")
    points += 3
elif food == "Ice Cream":
    pg.alert("Noice!")
    points += 5
elif food == "Pasta":
    pg.alert("All carbs")
elif food == "Chips":
    pg.alert("Salty")
    points -= 2
elif food == "Snadwiches":
    pg.alert("Not my favorite")
    points -= 5
elif food == "Chicken Casserole":
    pg.alert("That's what's for lunch!")
    points += 10
else:
    pg.alert("Nice food")

pg.alert("Your score is" + str (points))
    
