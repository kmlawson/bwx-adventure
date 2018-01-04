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
"""You stand in the garden of your cottage, which lies nestled on 
a hill deep in the forest. There used to be stone boulder at the 
edge of your garden, but today, you noticed that a stairway has been 
carved into the boulder, leading upwards into the forest.
""", "by")
stairs.descriptions = {'garden':'You keep a simple garden with herbs and hearty vegetables. Some areas definitely in need of weeding.',
'cottage':'You have locked up the cottage as you begin your new adventure.',
'stairs':'Some moss covered stairs leading up into the forest up the hill.',
'vegetables':'Some potatoes gone wild, a few failed tomato plants, squash now rotting, and various kinds of beans are growing in the garden.'}


hero = game.new_player(stairs)

# ## Location: forestpath

def pick_berries(game,location):
    if location.name == "Forest Path at Top of the Stairs":
        game.output("You are in luck, the blueberries are in season. You pick a handfull.",CONTENTS)
        berries = location.add_object(blueberries)
        game.player.add_to_inventory(berries)
        # game.player.act_take1(,'blueberries',"")
        # hero.add_to_inventory(location.contents[blueberries])
    elif location.name == "Glade":
        game.output("You are in luck, the raspberries are in season. You pick a handfull.",CONTENTS)
        berries = location.add_object(raspberries)
        game.player.add_to_inventory(berries)
    elif location.name == "Grassy Hill":
        game.output("You pick a handfull of small wild strawberries growing along the trail.",CONTENTS)
        berries = location.add_object(strawberries)
        game.player.add_to_inventory(berries)    
    return True

forestpath = game.new_location(
"Forest Path at Top of the Stairs",
"""You stand in a forest path, between bushes of blueberries. There 
are some stone stairs leading down, and the forest path leads a large 
structure towards the north. The forest stretches to the west and east 
of you.
""", "on")

# def flip_coin(game, thing):
  # if not "coin" in game.player.inventory:
    # game.output("The coin is on the ground!")
    # return
  # if random.random() > 0.5:
    # game.output("The coin shows heads.")
  # else:
    # game.output("The coin shows tails.")
# coin = forestpath.new_object("coin", "a small coin")
# hero.add_phrase("flip coin", flip_coin, [coin])

forestpath.add_phrase("pick blueberries",pick_berries)
forestpath.add_phrase("pick berries",pick_berries)
forestpath.add_phrase("pick some berries",pick_berries)
forestpath.add_phrase("get berries",pick_berries)
forestpath.add_phrase("take berries",pick_berries)
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
"""Surrounded by brush on all sides except a thin deer's trail to the 
west, this glade allows a little bit of light into an otherwise 
relatively dark forest beyond. The way is blocked in most directions 
by thick raspberry canes.
""","in")

foresteast.add_phrase("pick raspberries",pick_berries)
foresteast.add_phrase("pick berries",pick_berries)
foresteast.add_phrase("pick some berries",pick_berries)
foresteast.add_phrase("get berries",pick_berries)
foresteast.add_phrase("take berries",pick_berries)
foresteast.add_phrase("get raspberries",pick_berries)
foresteast.add_phrase("take raspberries",pick_berries)
foresteast.descriptions = {'berries':'Some thick canes filled with raspberries that look great, but not the easiest to pick.',
'forest':'The forest here is dense and impossible to get through in most directions.',
'trail':'The trail has deer tracks and what definitely look like squirrel tracks on them.',
'raspberries':'Some thick canes filled with raspberries that look great, but not the easiest to pick.'}

# ## Location: forestwest
forestwest = game.new_location(
"Grassy Hill",
"""A grassy hill emerges from the surrounding forest. A few flat stones 
can be found on top. The path and the edges of the forest are lined with 
ferns and some wild strawberries. You can see someone sitting on the stones
writing something with a brush.
""","in")

forestwest.add_phrase("pick strawberries",pick_berries)
forestwest.add_phrase("pick berries",pick_berries)
forestwest.add_phrase("pick some berries",pick_berries)
forestwest.add_phrase("get berries",pick_berries)
forestwest.add_phrase("take berries",pick_berries)
forestwest.add_phrase("get strawberries",pick_berries)
forestwest.add_phrase("take strawberries",pick_berries)

# ######################################################
# ## Location: Hell Entrance
# ######################################################

hallentrance = game.new_location(
"Front of the Hall",
"""You stand before a large walled compound. To the east and west the
forest looks impenetrable but the wooden gates to the compound lie to
the north and look cracked open. 
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

# ######################################################
# ## Location: Kitchen
# ######################################################

def eat_soup(game,thing):
  if game.player.health<16: 
     game.player.health+=5
     game.output("\nThe soup is not only delicious but has a healing effect. Your health has increased and is now: ",FEEDBACK)
     game.output(str(game.player.health))
  else:
    game.output("This healing soup is delicious but you are already good and healthy.",FEEDBACK)
    
def make_smoothie(game,thing):
  berrycount=0
  if "blueberries" in game.player.inventory: berrycount+=1
  if "strawberries" in game.player.inventory: berrycount+=1
  if "raspberries" in game.player.inventory: berrycount+=1
  if berrycount==0:
    game.output("To make a blender you need to be carrying some fruit or berries.",FEEDBACK)
    return True
  else:
    newsmoothie = game.player.location.add_object(smoothie)
    newsmoothie.set_var('berrycount',berrycount)
    game.player.add_to_inventory(newsmoothie)
    singleplural = 'type'
    if berrycount>1: singleplural = 'types'
    game.output("You created a new smoothie which contains "+str(berrycount)+' '+singleplural+' of berries.',FEEDBACK)

kitchen = game.new_location(
"Kitchen",
"""
As soon as you enter the room you smell a delightful array of aromas coming from a pot over the fire. Some vegetables are cut up on a long table and there is a blender there as well. Finally you see how the people of the hall are fed. There is a man standing near them tending to the food.""", "in")
kitchen.descriptions = {'blender': 'This electric blender looks like it would be great to make smoothies with if you had some fruit or berries.',
    'vegetables': 'A healthy array of vegetables.',
    'pot': 'Looks like some kind of soup being made here, which looks fantastic.',
    'soup': 'This smells like a vegetable and herbed filled concoction. Looks great.',
    'table': 'A nice long wooden table that provides a good workspace for cooking.'}

kitchen.add_phrase("make smoothie",make_smoothie)
kitchen.add_phrase("make smoothy",make_smoothie)
kitchen.add_phrase("make smoothies",make_smoothie)
kitchen.add_phrase("blend smoothie",make_smoothie)
kitchen.add_phrase("blend berries",make_smoothie)
kitchen.add_phrase("eat soup",eat_soup)
kitchen.add_phrase("drink soup",eat_soup)
kitchen.add_phrase("try soup",eat_soup)

# ######################################################
# ## Location: Machine Room
# ######################################################

def check_dials(game,thing):
  theroom = game.player.location
  game.output("""
You pull the lever and hear a clicking of gears shifting behind each of
the letter dials in turn.
""",DESCRIPTION)
  correctcount=0
  for x in ['dial1','dial2','dial3','dial4','dial5','dial6','dial7','dial8','dial9','dial10','dial11','dial12','dial13','dial14','dial15']:
    if theroom.var(x)==theroom.var(x+'a'):
      correctcount=correctcount+1
  if correctcount==15:
    game.output("""
You feel a huge shaking under ground as the steam builds up through
the entire machine. Each of the dials lights up a bright red and
begin to spin wildly. Steam floods into the steam gauge and pushes
it all the way to 15 and through the top of the gauge, which explodes,
sending some glass and steam flying in all directions. The dials
begin to slowly lower into the ground and a new long bar of metal
rises slowly out of the ground until it reaches your full height.
On the sign is written:

      ===========  Look in your old closet :)  =============

""",FEEDBACK)
    game.output("The Hall of Sages is complete!",DESCRIPTION)
    game.player.set_flag('win')
  elif correctcount==0:
    game.output("You see the steam from behind the steam gauge flush, but the gauge remains at zero.",FEEDBACK)
  else:
    game.output("""
You feel a rumbling as steam flows through the machine and into the steam gauge. 
The gauge slowly pushes up from 0 and settles at the new value of:""",FEEDBACK)
    game.output('    === '+str(correctcount)+' ===',CONTENTS)
    game.output("After revealing the new value on the gauge, it slowly begins to return to 0")

def list_dials(game,thing):
  theroom = game.player.location
  print("""
Each of the dials is set to a letter from a to z.
The dials currently have the following settings:
""")
  for x in ['dial1','dial2','dial3','dial4','dial5','dial6','dial7','dial8','dial9','dial10','dial11','dial12','dial13','dial14','dial15']:
    if theroom.var(x):
      print x+':'+theroom.var(x)
    else:
      print x+':a'


def turn_dial(self,actor,noun,words):
  words=' '.join(words).replace("to ","")
  diallist=['dial1','dial2','dial3','dial4','dial5','dial6','dial7','dial8','dial9','dial10','dial11','dial12','dial13','dial14','dial15']
  if noun not in diallist:
    print 'If you wish to turn a dial, you must identify it, e.g. turn dial1 to t or turn dial10 to f'
    return True
  else:
    if len(words)>1:
      print 'Too many characters. You can turn the dial to any single letter from a to z, e.g. turn dial1 to f or turn dial7 to z'
      return True
    elif len(words)<1:
      print 'What do you want to turn the dial to? Any letter from a to z, e.g. turn dial2 to t'
      return True
    else:
      if words in 'abcdefghijklmnopqrstuvwxyz':
        self.set_var(noun,words)
        print noun.title()+' has been turned to: '+self.var(noun)
        return True
      else:
        print 'The dial contains only the letters from a to z'
        return True

machineroom = game.new_location(
"Machine Room",
"""
This room has a radically different appearance to the rest of the hall.
It is as if you have travelled hundreds of years forward. In the center
of the room is a large forest of steaming pipes and gears.  Directly in
front of you, however, are fifteen combination dials covered in letters.
To the right of all the dials is a large lever under a steam gauge.
""", "in")
machineroom.descriptions = {'pipes': 'There are a confusing mix of pipes, some leaking a bit of water, and others a bit of steam.',
    'gears': 'The gears appear to be constantly turning, but you don\'t know why or how.',
    'lever': 'This lever appears connected to the dials somehow. Looks like you can "pull" it.',
    'gauge': 'The steam gauge looks like it goes from 0 to 15. It is currently at 0.'}

machineroom.set_var('dial1','a')
machineroom.set_var('dial1a','z')
machineroom.set_var('dial2','a')
machineroom.set_var('dial2a','v')
machineroom.set_var('dial3','a')
machineroom.set_var('dial3a','b')
machineroom.set_var('dial4','a')
machineroom.set_var('dial4a','t')
machineroom.set_var('dial5','a')
machineroom.set_var('dial5a','y')
machineroom.set_var('dial6','a')
machineroom.set_var('dial6a','h')
machineroom.set_var('dial7','a')
machineroom.set_var('dial7a','n')
machineroom.set_var('dial8','a')
machineroom.set_var('dial8a','x')
machineroom.set_var('dial9','a')
machineroom.set_var('dial9a','r')
machineroom.set_var('dial10','a')
machineroom.set_var('dial10a','c')
machineroom.set_var('dial11','a')
machineroom.set_var('dial11a','p')
machineroom.set_var('dial12','a')
machineroom.set_var('dial12a','i')
machineroom.set_var('dial13','a')
machineroom.set_var('dial13a','q')
machineroom.set_var('dial14','a')
machineroom.set_var('dial14a','e')
machineroom.set_var('dial15','a')
machineroom.set_var('dial15a','w')
machineroom.add_verb(Verb(turn_dial,'turn'))
machineroom.add_phrase("look at dials",list_dials)
machineroom.add_phrase("look dials",list_dials)
machineroom.add_phrase("pull lever",check_dials)

# CONNECTIONS #######################################################

game.new_connection("stairs", stairs, forestpath, UP)
game.new_connection("west trail", forestpath,forestwest,WEST)
game.new_connection("east trail", forestpath,foresteast,EAST)
game.new_connection("north trail", forestpath,hallentrance,NORTH)
game.new_connection("Iron Gate", hallentrance,innercourtyard,NORTH)
game.new_connection("curtain", innercourtyard,guardroom,NORTH)
game.new_connection("stairs",hallentrance,kitchen,DOWN)
game.new_connection("stairs",hallentrance,machineroom,UP)
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
and so on. In general, leave out prepositions whenever possible. Use 'about' to
learn more about this game. Use 'q' or 'quit' to exit the game.
""",DESCRIPTION)

def show_about(self,actor):
    game.output("""

The Hall of Sages is based on the python module created by Gever Tulley,
Brightworks (sfbrightworks.org). This adventure was written by Konrad
Lawson (muninn.net) in 2017. The link to the open source code on GitHub is
available on request.

The selection of short quotes from the Chinese
classics found within the game use or modify, in the spirit of fair use, the
excellent translations found in:

Confucius Analects with Selections from Traditional Commentaries
translated by Edward Slingerland (2003)

Mengzi with Selections from Traditional Commentaries
translated by Bryan W. Van Norden (2008)

Zhuangzi The Essential Writings with Selections from Traditional Commentaries
translated by Brook Ziporyn (2009)

Lao Tzu: Te-Tao Ching - A New Translation
Based on the Recently Discovered Ma-wang-tui Texts
translated by Robert G. Henricks (1992)
""",DESCRIPTION)

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
raspberries = Food("raspberries","some delicious raspberries picked from the forest",Say("Tart and delicious!"))
strawberries = Food("strawberries","some delicious tiny strawberries picked from the forest",Say("So sweet!"))
letter = hallentrance.add_object(Object("letter","a piece of pale rough-textured paper with handwriting on it. A letter it would appear, addressed to one Liam, and signed, KML"))

def look_smoothie(game,thing):
  berrycount=thing.var('berrycount')
  singleplural = 'type'
  if berrycount>1: singleplural = 'types'
  game.output("A delicious looking smoothie with "+str(berrycount)+' '+singleplural+' of berries.',FEEDBACK)


smoothie = Drink("smoothie","A delicious smoothie made from berries",Say("Delicious!"),Object("empty smoothie glass", "An empty smoothie glass"))
smoothie.set_var('berrycount',0)
smoothie.add_phrase("look smoothie",look_smoothie)
letter.add_verb(Verb(read, "read"))

################################################################
################################################################
################################################################
################################################################
# ACTORS #######################################################
################################################################
################################################################
################################################################
################################################################

hero.health = 10
hero.add_phrase("health",output_health)
hero.add_phrase("help",show_help)
hero.add_phrase("about",show_about)
hero.add_phrase("h",show_help)

# #####################################
# Actor - Cook Meng Shen
# #####################################


cook = Animal("man")
cook.description = "A short-tempered looking man, dressed in Tang dynasty robes, busily rushing around the kitchen."
cook.add_phrase("look at man",Say(cook.description))
cook.add_phrase("look man",Say(cook.description))
cook.set_location(kitchen)
cook.set_allowed_locations([kitchen])
cook.add_phrase("kill man",Say("He easily dodges your clumsy blows."))
cook.add_phrase("attack man",Say("He easily dodges your clumsy blows."))
cook.add_phrase("talk man",Say("""
"Hello there, I am the one and only Meng Shen, the master cook. My food
is the best medicine for an ailing body. 

Here, I used to cook food from all manner of meats from ducks to camels,
but when I asked Mengzi for a little help, that pretentious scoundrel
told me, 'Gentlemen cannot bear to see animals die if they have seen them
living. If they hear their cries of suffering, they cannot bear to eat their
flesh. Hence, gentlemen keep their distance from the kitchen.'

So, you know what I did? We went full on vegetarian cuisine: no cries or 
suffering here. And yet, for some reason, I still get no help from Mengzi!"

He goes back to work.

"""))

# #####################################
# Actor - Historian Ban Zhao
# #####################################


banzhao = Animal("woman")
banzhao.description = "A woman wearing the robes of a scholar sits on a rock writing a book on a roll of silk."
banzhao.add_phrase("look at woman",Say(banzhao.description))
banzhao.add_phrase("look woman",Say(banzhao.description))
banzhao.set_location(forestwest)
banzhao.set_allowed_locations([forestwest])
banzhao.add_phrase("kill woman",Say("She easily dodges your clumsy blows."))
banzhao.add_phrase("attack woman",Say("She easily dodges your clumsy blows."))
banzhao.add_phrase("talk woman",Say("""
The woman looks up from her book and says, "Hello, my name is Ban Zhao, the
historian.  So you are another one of these adventurers who wants to explore
the hall of sages, eh? Even if you find all the code letters for the cipher,
the machine room to decode it is guarded by an ancient tomb demon. It is
pointless to try and fight it, but I have heard that it is rather fond of
fruit smoothies."

She then looks back down and continues writing, mumbling to herself in an
angry tone, "I could write another grand history, but no, they want me
to write a stupid book telling women how to be good obedient wives, grr..."

"""))

# #####################################
# Actor - Squirrel
# #####################################

squirrel = Animal("squirrel")
squirrel.description = "A small red squirrel darting around looking for food."
squirrel.add_phrase("look at squirrel",Say(squirrel.description))
squirrel.add_phrase("look squirrel",Say(squirrel.description))
squirrel.set_location(forestpath)
squirrel.set_allowed_locations([stairs,forestpath,foresteast,forestwest])
squirrel.add_verb(SayOnSelf("The squirrel bounces away.", "pet"))
squirrel.add_verb(SayOnSelf("It is just too fast for you and flees.", "kill"))
squirrel.add_verb(SayOnSelf("It is just too fast for you.", "attack"))
squirrel.add_phrase("talk squirrel",Say("The squirrel says, \"Don't fall into the well! You'll need something to help you down!\""))
squirrel.set_location(forestpath)

game.add_actor(squirrel)
game.add_actor(banzhao)
game.add_actor(cook)

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
# hero.set_location(stairs)

def update():
  if (game.entering_location(machineroom)):
      list_dials(game,'test')

# Start playing.
game.run(update)
