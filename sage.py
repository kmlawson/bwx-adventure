#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: et sw=2 ts=2 sts=2

from advent import *
# for cloud9
# from advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player, Verb, Say, SayOnNoun, SayOnSelf
# from advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

# comment this line out to skip the devtools for environments like trinket
# import advent_devtools

# Set up the game you are going to build on.
# my_game is a top-level container for everything in the game.
game = Game("Hall of Sages")

# Create some interesting locations. Locations need a name
# and a description of any doorways or connections to the room, like this:
# variable_name = Location('The Name", "The description")
# The triple quotes (""") below are a way to make multi-line strings in Python.
# The final argument is which word to use in the location title in place of "in"
# in the phrase "You are in the..."

# METHODS ###################################

# def healme(self,amount,m  §essage):
#     self.hero.health=self.hero.health+amount
#     if self.hero.health>25:
#         hero.health=25
#     if message:
#         self.output(message,FEEDBACK)
#     self.output("Your health is now: "+str(self.hero.health),FEEDBACK)
#     return TRUE

# LOCATIONS #######################################################

# ## Location: Stairs

stairs = game.new_location(
"Stone Stairs at the End of the Garden",
"""You stand in the garden of your cottage, which lies nestled on a hill deep in the forest. There used to be stone boulder at the edge of your garden, but today, you noticed that a stairway has been carved into the boulder, leading upwards into the forest.
""", "by")
stairs.descriptions = {'garden':'You keep a simple garden with herbs and hearty vegetables. Some areas definitely in need of weeding.',
'cottage':'You have locked up the cottage as you begin your new adventure.',
'stairs':'Some moss covered stairs leading up into the forest up the hill.',
'vegetables':'Some potatoes gone wild, a few failed tomato plants, squash now rotting, and various kinds of beans are growing in the garden.'}



# ## Location: forestpath

def pick_berries(game,location):
    if location.name == "Forest Path at Top of the Stairs":
        game.output("You are in luck, the blueberries are in season. You pick a handfull.",CONTENTS)
        berries = location.add_object(blueberries)
        hero.act_take1(hero,'blueberries',"")
        # hero.add_to_inventory(location.contents[blueberries])
    elif location.name == "Glade":
        game.output("You are in luck, the raspberries are in season. You pick a handfull.",CONTENTS)
        raspberries = Food("raspberries","some delicious raspberries picked from the forest",Say("Tart and delicious!"))
        hero.add_to_inventory(raspberries)
    elif location.name == "Grassy Hill":
        game.output("You pick a handfull of small wild strawberries growing along the trail.",CONTENTS)
        strawberries = Food("strawberries","some delicious tiny strawberries picked from the forest",Say("So sweet!"))
        hero.add_to_inventory(strawberries)
    return True

forestpath = game.new_location(
"Forest Path at Top of the Stairs",
"""You stand in a forest path, between bushes of blueberries. There are some stone stairs leading down, and the forest path leads a stone structure towards the north. The forest stretches to the west and east of you.
""", "on")

# forestpath.sentences["hello"]="Amazing!"
forestpath.add_phrase("pick blueberries",pick_berries)
forestpath.add_phrase("pick berries",pick_berries)
forestpath.add_phrase("pick some berries",pick_berries)
forestpath.add_phrase("get berries",pick_berries)
# forestpath.add_phrase("get blueberries",pick_berries)
forestpath.descriptions = {'berries': 'These blueberries look delicious, and found everywhere in the forest here',
'blueberries': 'These blueberries look delicious, and found everywhere in the forest here',
'stairs': 'These stairs are covered in moss, with a few marks of someone who passed recently.',
'structure': 'You can just make out the top of a very large building to the north, which looks like it is covered in vegetation and moss',
'east':'You spot a glade through the trees to the east by a deer path.',
'west':'You can make out a grassy hill through the trees by a trail to the west.',
'down':'You can just make out your cottage and garden down the stairs.',
'north':'You can just make out the top of a very large building to the north, which looks like it is covered in vegetation and moss',
'forest': """At first glance, the forest looks impenetrable, but when you look closer
you can see that there are trails leading off in both east and west directions"""}

# ## Location: foresteast
foresteast = game.new_location(
"Glade",
"""Surrounded by brush on all sides except a thin deer's trail to the west, this glade allows a little bit of light into an otherwise relatively dark forest beyond. The way is blocked in most directions by thick raspberry canes.
""","in")

foresteast.add_verb(Say('The door makes a hollow sound.', 'knock'))
foresteast.add_phrase("pick raspberries",pick_berries)
foresteast.add_phrase("pick berries",pick_berries)
foresteast.add_phrase("pick some berries",pick_berries)
foresteast.add_phrase("get berries",pick_berries)
foresteast.add_phrase("get raspberries",pick_berries)
foresteast.descriptions = {'berries':'Some thick canes filled with raspberries that look great, but not the easiest to pick.',
'forest':'The forest here is dense and impossible to get through in most directions.',
'trail':'The trail has deer tracks and what definitely look like squirrel tracks on them.',
'raspberries':'Some thick canes filled with raspberries that look great, but not the easiest to pick.'}

# ## Location: forestwest
forestwest = game.new_location(
"Grassy Hill",
"""A grassy hill emerges from the surrounding forest. A few flat stones can be found on top. The path and the edges of the forest are lined with ferns and some wild strawberries.
""","in")

forestwest.add_phrase("pick strawberries",pick_berries)
forestwest.add_phrase("pick berries",pick_berries)
forestwest.add_phrase("pick some berries",pick_berries)
forestwest.add_phrase("get berries",pick_berries)
forestwest.add_phrase("get strawberries",pick_berries)

# ## Location: Hall Entrance

hallentrance = game.new_location(
"Front of the Hall",
"""Hall Entrance
""", "in")

# ## Location: Inner Courtyard

innercourtyard = game.new_location(
"Inner Courtyard",
"""
""", "in")

# ## Location: 

laozione = game.new_location(
"Hall of Laozi - Garden Entrance",
"""
""", "in")

# ## Location: 

laozitwo = game.new_location(
"Hall of Laozi - Pavilion",
"""
""", "in")

# ## Location: 

laozithree = game.new_location(
"Hall of Laozi - Cliff Platform",
"""
""", "in")


# ## Location: 

laozifour = game.new_location(
"Hall of Laozi - Cloud",
"""
""", "in")


# ## Location: 

laozifive = game.new_location(
"Hall of Laozi - Mountain Top",
"""
""", "in")


# ## Location: 

laozisix = game.new_location(
"Hall of Laozi - Hermitage",
"""
""", "in")



# ## Location: 

confuciusone = game.new_location(
"Hall of Kongzi - ",
"""
""", "in")



# ## Location: 

confuciustwo = game.new_location(
"Hall of Kongzi - ",
"""
""", "in")



# ## Location: 

confuciusthree = game.new_location(
"Hall of Kongzi - ",
"""
""", "in")



# ## Location: 

confuciusfour = game.new_location(
"Hall of Kongzi - ",
"""
""", "in")



# ## Location: 

confuciusfive = game.new_location(
"Hall of Kongzi - ",
"""
""", "in")

# ## Location: 

confuciussix = game.new_location(
"Hall of Kongzi - ",
"""
""", "in")

# ## Location: 

confuciusseven = game.new_location(
"Hall of Kongzi - ",
"""
""", "in")

# ## Location: 

confuciuseight = game.new_location(
"Hall of Kongzi - ",
"""
""", "in")

# ## Location: 

confuciusnine = game.new_location(
"Hall of Kongzi - ",
"""
""", "in")

# ## Location: 

confuciusten = game.new_location(
"Hall of Kongzi - ",
"""
""", "in")


# ## Location: 

menciusone = game.new_location(
"Hall of Mengzi - ",
"""
""", "in")



# ## Location: 

menciustwo = game.new_location(
"Hall of Mengzi - ",
"""
""", "in")



# ## Location: 

menciusthree = game.new_location(
"Hall of Mengzi - ",
"""
""", "in")



# ## Location: 

menciusfour = game.new_location(
"Hall of Mengzi - ",
"""
""", "in")

# ## Location: 

menciusfive = game.new_location(
"Hall of Mengzi - ",
"""
""", "in")

# ## Location: 

menciussix = game.new_location(
"Hall of Mengzi - ",
"""
""", "in")

# ## Location: 

menciusseven = game.new_location(
"Hall of Mengzi - ",
"""
""", "in")

# ## Location: 

menciuseight = game.new_location(
"Hall of Mengzi - ",
"""
""", "in")


# ## Location: 

zhuangzione = game.new_location(
"Hall of Zhuangzi - ",
"""
""", "in")



# ## Location: 

zhuangzitwo = game.new_location(
"Hall of Zhuangzi - ",
"""
""", "in")


# ## Location: 

zhuangzithree = game.new_location(
"Hall of Zhuangzi - ",
"""
""", "in")


# ## Location: 

zhuangzifour = game.new_location(
"Hall of Zhuangzi - ",
"""
""", "in")


# ## Location: 

zhuangzifive = game.new_location(
"Hall of Zhuangzi - ",
"""
""", "in")


# ## Location: 

zhuangzisix = game.new_location(
"Hall of Zhuangzi - ",
"""
""", "in")


# ## Location: 

zhuangziseven = game.new_location(
"Hall of Zhuangzi - ",
"""
""", "in")


# ## Location: 

zhuangzieight = game.new_location(
"Hall of Zhuangzi - ",
"""
""", "in")


# ## Location: 

guardroom = game.new_location(
"Guardroom",
"""
""", "in")


# ## Location: 

machineroom = game.new_location(
"Machine Room",
"""
""", "in")

# CONNECTIONS #######################################################

game.new_connection("stairs", stairs, forestpath, UP)
game.new_connection("west trail", forestpath,forestwest,WEST)
game.new_connection("east trail", forestpath,foresteast,EAST)
game.new_connection("north trail", forestpath,hallentrance,NORTH)
game.new_connection("Iron Gate", hallentrance,innercourtyard,NORTH)
game.new_connection("curtain", innercourtyard,guardroom,NORTH)
game.new_connection("Metal Door", guardroom,machineroom,NORTH)
game.new_connection("wooden door", innercourtyard,laozione,EAST)
game.new_connection("path", laozione,laozitwo,NORTH)
game.new_connection("path", laozitwo,laozithree,WEST)
game.new_connection("path", laozithree,laozifour,WEST)
game.new_connection("path", laozifour,laozifive,WEST)
game.new_connection("path", laozifour,laozisix,SOUTH)
game.new_connection("path", laozitwo,zhuangzione,NORTH)
game.new_connection("Stone Bridge", zhuangzione,zhuangzitwo,NORTH)
game.new_connection("Stone Bridge", zhuangzitwo,zhuangzithree,NORTH)
game.new_connection("Stone Bridge", zhuangzithree,zhuangzifour,NORTH)
game.new_connection("Ladder", zhuangzifour,zhuangzifive,DOWN)
game.new_connection("Boat", zhuangzithree,zhuangzisix,EAST)
game.new_connection("path", zhuangzisix,zhuangziseven,SOUTH)
game.new_connection("path", zhuangzisix,zhuangzieight,NORTH)
game.new_connection("path", innercourtyard,confuciusone,WEST)
game.new_connection("path", confuciusone,confuciustwo,WEST)
game.new_connection("path", confuciusone,confuciusthree,SOUTH)
game.new_connection("path", confuciusone,confuciusfour,NORTH)
game.new_connection("path", confuciustwo,confuciusfive,NORTH)
game.new_connection("path", confuciustwo,confuciussix,SOUTH)
game.new_connection("path", confuciustwo,confuciusseven,WEST)
game.new_connection("path", confuciusthree,confuciuseight,SOUTH)
game.new_connection("path", confuciusthree,confuciusnine,WEST)
game.new_connection("path", confuciusthree,confuciusnine,EAST)
game.new_connection("path", confuciusfour,confuciusten,EAST)
game.new_connection("path", confuciusfour,menciusone,WEST)
game.new_connection("path", menciusone,menciustwo,WEST)
game.new_connection("path", menciusone,menciusthree,SOUTH)
game.new_connection("path", menciusone,menciusfour,NORTH)
game.new_connection("path", menciusfour,menciusseven,EAST)
game.new_connection("path", menciusfour,menciuseight,WEST)
game.new_connection("path", menciusone,menciusfive,UP)
game.new_connection("path", menciusone,menciussix,DOWN)

# OBJECT FUNCTIONS #######################################################

def output_health(self,actor):
    game.output("Your Health Level is: ",CONTENTS)
    game.output(str(hero.health))
    return True

def show_help(self,actor):
    game.output("""Welcome to the Hall of Sages. A range of commands are accepted in this game.
Verbs of movement: north, south, east, west, up, down; Actions: drink, eat,
inventory, health, examine (objects in your inventory), look (at things around
you: use single words), read, take, drop, attack, kill, pet, talk, pick, unlock,
and so on. Use 'q' or 'quit' to exit the game.""",CONTENTS)

def read(self,actor,noun, words):
    if noun or words:
        return False
    if self.name =='letter':
        self.game.output("""
Hello Liam. Or should I say Ásjá, the third son of Fenrir,
son of Loki, brother of the treacherous Sköll, and the hateful Hati.
All three of you are wolves, to be sure, but while Sköll chases the
sun and Hati chases the moon; while your father, the ferocious Fenrir
waits to pounce on Odin himself at Ragnarok; while your grandfather
Loki deceives and plots, you have a very different fate. Even your
name reveals as much: Ásjá, it means guardian — one who gives aid
and protects others.""",CONTENTS)
        if not hero.flag('invigorated'):
            hero.health=hero.health+10
            self.game.output("\nYou feel strengthened in your resolve. Your health has increased and is now: ",CONTENTS)
            self.game.output(str(hero.health))
            hero.set_flag('invigorated')
        else:
            self.game.output("\nYou still feel a tingle of excitement as you reread the letter.",CONTENTS)
    return True

# OBJECTS #######################################################

blueberries=Food("blueberries","some delicious blueberries picked from the forest",Say("Yummy!"))
raspberries=Food("raspberries","some delicious raspberries picked from the forest",Say("Tart and delicious!"))
letter = hallentrance.add_object(Object("letter","a piece of pale rough-textured paper with handwriting on it. A letter it would appear, addressed to one Liam, and signed, Konrad"))
letter.add_verb(Verb(read, "read"))

# ACTORS #######################################################

hero = Player()
hero.health = 10
hero.add_phrase("health",output_health)
hero.add_phrase("help",show_help)
hero.add_phrase("h",show_help)

# Actor - Squirrel

squirrel = Animal("squirrel")
squirrel.description = "A small red squirrel darting around looking for food."
squirrel.add_phrase("look at squirrel",Say(squirrel.description))
squirrel.add_phrase("look squirrel",Say(squirrel.description))
squirrel.set_location(forestpath)
squirrel.set_allowed_locations([stairs,forestpath,foresteast,forestwest])
squirrel.add_verb(SayOnSelf("The squirrel bounces away.", "pet"))
squirrel.add_verb(SayOnSelf("It is just too fast for you and flees.", "kill"))
squirrel.add_verb(SayOnSelf("It is just too fast for you.", "attack"))
squirrel.add_verb(SayOnSelf("The squirrel looks bemused at your attempt to communicate.", "talk"))
squirrel.add_trade(letter, None,
                 Say("The squirrel takes the bluerries and eats them greedily."))
squirrel.set_location(forestpath)

game.add_actor(hero)
game.add_actor(squirrel)

def say(self,actor, noun, words):
  if not words:
    words = noun
  else:
    words = noun.title() + ' ' + ' '.join(words)
  self.game.output('You say, "' + words + '"', CONTENTS)
  if words in self.location.sentences:
    self.game.output(self.location.sentences[words],FEEDBACK)
  return True

# Now that we have created our game and everything in it, we can start the game!

# Start on the stairs
hero.set_location(stairs)

def update():
  return False
  # if (game.entering_location(hallentrance)):
    # if (game.inventory_contains([letter])):
      # game.output("You feel an urge to read the letter.")



# Start playing.
game.run(update)
