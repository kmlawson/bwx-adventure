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
    """Adds invisible object to be created and added to inventory"""
    if location.name == "Forest Path at Top of the Stairs":
        game.output("You are in luck, the blueberries are in season. You pick a handfull.",FEEDBACK)
        berries = location.add_object(blueberries)
        game.player.act_take1(game.player,'blueberries',True) # add_to_inventory(berries)
        # game.player.act_take1(,'blueberries',"")
        # hero.add_to_inventory(location.contents[blueberries])
    elif location.name == "Glade":
        game.output("You are in luck, the raspberries are in season. You pick a handfull.",FEEDBACK)
        berries = location.add_object(raspberries)
        game.player.act_take1(game.player,'raspberries',True)
        # game.player.add_to_inventory(berries)
    elif location.name == "Grassy Hill":
        game.output("You pick a handful of small wild strawberries growing along the trail.",FEEDBACK)
        berries = location.add_object(strawberries)
        game.player.act_take1(game.player,'strawberries',True)
        # game.player.add_to_inventory(berries)
    elif location.name == "Hall of Laozi - Garden Entrance":
        game.output("You pick a peach from the peach tree.",FEEDBACK)
        newpeach = location.add_object(peach)
        game.player.act_take1(game.player,'peach',True)
    elif location.name == "Hall of Kongzi - Island Pavilion":
        game.output("You pluck a feather from the white goose.",FEEDBACK)
        newfeather = location.add_object(feather)
        game.player.act_take1(game.player,'feather',True)
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
# ## Location: Hall Entrance
# ######################################################

hallentrance = game.new_location(
"In Front of the Hall",
"""You stand before a large walled compound. To the east and west the
forest looks impenetrable but the wooden gates to the compound lie to
the north and look cracked open.
""", "in")

# ######################################################
# ## Location: Inner Courtyard
# ######################################################


innercourtyard = game.new_location(
"Inner Courtyard",
"""This is the inner courtyard of the hall. It is a wide cobble-stoned area
and there is a bit of dust in the air kicked up by a boy who is methodically
sweeping the area. You see a door to the west and a gate into a garden area
to the east.
""", "in")


# ######################################################
# ## Location: Laozi 1 - Garden Entrance
# ######################################################

def read_sign(game,thing):
  if 'sign' in game.player.location.descriptions:
    game.output("============== \n"+game.player.location.descriptions['sign']+"\n==============",DESCRIPTION)
    return True
  else:
    game.output("You don't see a sign.")

def read_carving(game,thing):
  if 'carving' in game.player.location.descriptions:
    game.output("============== \n"+game.player.location.descriptions['carving']+"\n==============",DESCRIPTION)
    return True
  else:
    game.output("You don't see a rock carving.")

def read_scroll(game,thing):
  if 'scroll' in game.player.location.descriptions:
    game.output("============== \n"+game.player.location.descriptions['scroll']+"\n==============",DESCRIPTION)
    return True
  else:
    game.output("You don't see a scroll hanging here.")

laozione = game.new_location(
"Hall of Laozi - Garden Entrance",
"""You are on a path in what looks like it was meant to be a garden, but
the bushes and trees are growing wild. Bees are enjoying the
many blossoming flowers that fill this area. There is a gate leading
to a courtyard to the west. There is a peach tree here. The gate looks
like it has writing on it. The garden path continues to the north.  You
also see a sign sticking out of one of the bushes.
""", "in")

laozione.descriptions = {'sign':"""The sign says:
"To know you don't know is best.
Not to know you don't know is a flaw
Therefore, the Sage's not being flawed
Stems from his recognizing a flaw as a flaw.
Therefore, he is flawless. ch 71 (g)\"
""",
'bees':'The bees are happily flying from flower to flower, ignoring you.',
'flowers':'There are all sorts of different flowers, in no particular pattern, all growing wild.',
'trees':'A variety of trees, none of which steam sturdy to climb in.',
'gate':"""
On the gate is written:
"The Way of Heaven is like the flexing of a bow.
The high it presses down; the low it raises up.
From those with a surplus it takes away; to those without enough it adds on.
Therefore the Way of Heaven—
Is to reduce the excessive and increase the insufficient ch 77 (u)\"
"""}
laozione.add_phrase("read sign",read_sign)
laozione.add_phrase("pick fruit",pick_berries)
laozione.add_phrase("pick peaches",pick_berries)
laozione.add_phrase("pick peach",pick_berries)
laozione.add_phrase("pick a peach",pick_berries)

# ######################################################
# ## Location: Laozi 2 - A Field of Reeds
# ######################################################

laozitwo = game.new_location(
"Hall of Laozi - Field of Reeds and Lilies",
"""You are on a path in the midst of a field of reeds in shallow
water on one side of the trail with wild lilies on the other.
The path continues south towards a garden and the main path
goes to the west towards the edge of a lake. The path also
splits off towards the north, towards a river.  You see a sign
sticking out of the water. There is also a bench here that looks
like it has some writing on it. Jesus is sitting on the bench
and appears to be enjoying the warm wind.
""", "in")
laozitwo.descriptions = {'sign':"""
The sign says:
"When people are born, they're supple and soft;
When they die, they end up stretched out firm and rigid...
Therefore we say that the firm and rigid are companions of death,
While the supple, the soft, the weak, and the delicate are
companions of life... ch 76 (w)\"
""",
'reeds':"""The reeds make a delightful noise as they bend, unharmed
by even the strongest of winds that blow against them.""",
'bench':"""The bench is made of some twisted pieces of wood,
but grown to be shaped in a form perfect for sitting on. On the
bench is written:

When twisted, you'll be upright;
When hollowed out, you'll be full;
When worn out, you'll be renewed;
When you have little, you'll attain much;
With much, you'll be confused. ch 22 (m)"""}

laozitwo.add_phrase("read sign",read_sign)
laozitwo.add_phrase("sit bench",Say('You sit down and have a nice wee rest next to Jesus.'))
laozitwo.add_phrase("sit on bench",Say('You sit down and have a nice wee rest next to Jesus.'))

# ######################################################
# ## Location: Laozi 3 - Lake Side
# ######################################################

def ride_crane(game,thing):
  """Teleports the player to a random location"""
  game.output("""
You step out into the lake and easily mount a very tame and helpfully
still crane. It looks like it has done this before. It then flies high
into the sky and flies a great circle around the entire area. Now you
can see the structure of all the land below. The building compound is
to your west, and looks divided into two parts, with small buildings
connected by passageways and courtyards. To your north you see a
platform off a cliff and a small hut and cave hugging the side of the
mountainside. To your south you see the reed field, garden, and
further south from there, the road you came from. Flying east you see
a river, with a massive stone bridge over it, to north of which there
is a forest, where you can make out monkeys jumping from tree to tree.
To the north of the forest you can make out a well, next to which
there is a massive turtle. Beyond the turtle is a wide ocean.
Just as the crane finishes its massive sweep it dives suddenly down
and, picking a place almost at random shakes you off and drops you
onto the ground.""",FEEDBACK)
  time.sleep(0.5)
  possible_locations=[]
  for place in game.location_list:
    if "Well" in place.name:
      continue
    elif "Guardroom" in place.name:
      continue
    elif "Machine Room" in place.name:
      continue
    else:
      possible_locations.append(place)
  game.player.location = random.choice(possible_locations)
  game.output("\nYou have been transported randomly to:",FEEDBACK)
  game.output(game.player.location.name,CONTENTS)
  where = game.player.location.describe(game.player, game.player.flag('verbose'))
  if where:
    game.output("")
    game.output(where)
    game.output("")

laozithree = game.new_location(
"Hall of Laozi - Lake Side",
"""You stand on the edge of a large lake that stretches off to the west.
The lake is clear and beautiful with large fish swimming about in it.
Some huge cranes stand in the water near the shore, and one of them
appears to have a saddle on it. There is a sign sticking out of the water
By the shore there is a stone basin that also has some writing on it.
The path continues up a mountain to the north and east towards a field.

""", "in")
laozithree.descriptions = {'sign':"""
The sign says:
"In the whole world, nothing is softer and weaker than water,
And yet for attacking the hard and strong, nothing can beat it ch 78 (b)\"
""",
'lake':"The lake is huge and filled with fish.",
'cranes':"""The cranes are majestic creatures.  One of them,
wearing a saddle, has a faint glow to it.""",
'crane':"""The cranes are majestic creatures.  One of them,
wearing a saddle, has a faint glow to it.""",
'fish':"The fish are deep down but the water is so clear you can see them.",
'basin':"""
On the basin is written:
"If you take muddy water and still it,
it gradually becomes clear.
If you bring something to rest in order to move it,
it gradually comes alive. ch 15 (u)\"
"""
}

laozithree.add_phrase("read sign",read_sign)
laozithree.add_phrase("ride crane",ride_crane)
laozithree.add_phrase("get on crane",ride_crane)
laozithree.add_phrase("mount crane",ride_crane)
laozithree.add_phrase("swim",Say("You take a lovely swim in the lake."))
laozithree.add_phrase("swim lake",Say("You take a lovely swim in the lake."))
laozithree.add_phrase("swim in lake",Say("You take a lovely swim in the lake."))

# ######################################################
# ## Location: Laozi 4 - Cliff Platform
# ######################################################


laozifour = game.new_location(
"Hall of Laozi - Cliff Platform",
"""You are on a mountainside, standing on a beautiful wooden
platform that stretches off a steep cliff. There is a sign
posted here, and beyond the platform, you can get a great
view of the lake down below. The path continues north up
the mountain.
""", "on")
laozifour.descriptions = {'sign':"""
The sign says:
"Regard the small as large and the few as many,
And repay resentment with kindness.
Plan for the difficult while it is easy;
Act on the large while it's minute.
The most difficult things in the world
begin as things that are easy;
The largest things in the world
arise from the minute.
Therefore the Sage, to the end does
not strive to do the great,
And as a result, he is able to
accomplish the great... ch 63 (t)"
"""}
laozifour.add_phrase("read sign",read_sign)


# ######################################################
# ## Location: Laozi 5 - Hermitage
# ######################################################

laozifive = game.new_location(
"Hall of Laozi - Hermitage",
"""You are standing near the top of the steep tree-covered mountain,
with many more forested rounded peaks stretching up to the sky around
you. The path comes to an end at a small hermitage cottage that
appears to be empty except for a scroll attached firmly to the wall and
you can also make out a door inside the hermitage going to the west.
There is a sign here and a cave to the north.
""", "in")
laozifive.descriptions = {'sign':"""
The sign says:
"The Sage accumulates nothing.
Having used what he had for others,
He has even more.
Having given what he had to others,
What he has is even greater. ch 81 (v)\"
""",
'scroll':"""
The scroll says:
He does not show himself off; therefore he becomes prominent
He does not put himself on display; therefore he brightly shines
He does not brag about himself; therefore he receives credit
He does not praise his own deeds; therefore he can long endure
It is only because he does not compete that, therefore,
no one else is able to compete with him. ch 33 (f) \"
"""}
laozifive.add_phrase("read sign",read_sign)
laozifive.add_phrase("read scroll",read_scroll)

# ######################################################
# ## Location: Laozi 6 - Cave
# ######################################################


laozisix = game.new_location(
"Hall of Laozi - Cave",
"""You are inside a shallow cave brightly lit by the setting
sun. Inside there are a collection of old things, some of
which lie on the ground. There is also a sign here on the wall.
""", "in")
laozisix.descriptions = {'sign':"""
The sign says:
"It is precisely where there is nothing,
that we find the usefulness of the wheel.
We fire clay and make vessels;
It is precisely where there's no substance,
that we find the usefulness of clay pots.
We chisel out doors and windows;
It is precisely in these empty spaces,
that we find the usefulness of the room.
Therefore, we regard having something as beneficial;
But having nothing as useful. ch 11 (k)"
""",'ground':"Nothing of interest here."}
laozisix.add_phrase("read sign",read_sign)

# ######################################################
# ## Location: Kongzi 1 Courtyard
# ######################################################

confuciusone = game.new_location(
"Hall of Kongzi - Courtyard",
"""You find yourself in a pleasant three sided courtyard. An open main gate
leads south towards another courtyard and building. There is a door to a house
to the north and another door into a building on the west. There is also a
door to the east. There is a sign here and a stone with a carving on it.
""", "in")
confuciusone.descriptions = {'sign':"""
The sign says:
"The Master said, A clever tongue and fine appearance are rarely signs of
Goodness 1.1 (a)"
""",
'carving':"""The carving reads:
"The Master said When you see someone who is worthy, concentrate upon
becoming their equal; when you see someone who is unworthy, use this as an
opportunity to look within yourself. 4.17 (r)"
"""}
confuciusone.add_phrase("read sign",read_sign)
confuciusone.add_phrase("read carving",read_carving)
confuciusone.add_phrase("look stone",read_carving)

# ######################################################
# ## Location: Kongzi 2 Library
# ######################################################

# Add a librarian character here that is more meaningful

confuciustwo = game.new_location(
"Hall of Kongzi - Library",
"""You find yourself what must be the library. The place is divided into sections
corresponding to the medium the works are preserved in. In one section there
are a pile of upper ox leg bones, or the scapula, in roughly a triangular shape.
There are also a pile of pieces of the bottom bellies of turtles, plastrons. Both
of these have carved letters on them, but with many more rounded shapes than
the characters you have seen on the scrolls, stone carvings, and signs
elsewhere. Then there is a section of the library that has a large collection
of rolled up bundles. Some of these are in silk, but most of them are large
rolls of bamboo slips. It looks like some of these rolls are grouped together
as pieces of a single work. Finally, in a newer section of the library there
are works in paper. Some of these paper book, the ones that look older, are
rolls of paper, and it looks like the pages are pasted together end to end in
a way that makes them look like a rolled up scroll. Finally there is a section
with more familiar looking paper books: pieces of folded paper stitched
together with a silk cord. Some of these are on their own, others in boxes
collecting a few of them together.

The librarian is here, dusting off things and organising the messy collection of
bones and turtle belly texts. You see an open door to a courtyard to the east,
an archway to the west, and a door to the north.

There is a sign here, and also a scroll hanging here.
""", "in")
confuciustwo.add_phrase("read sign",read_sign)
confuciustwo.add_phrase("read scroll",read_scroll)
confuciustwo.add_phrase("talk librarian",Say("The librarian gives you smile but waves you away, 'I'm busy!'"))
confuciustwo.descriptions = {'sign':"""
The sign says:
"The Master said I am not someone who was born with knowledge. I simply
love antiquity, and diligently look there for knowledge. (z)"
""",
'librarian':"""The librarian looks very busy, there is no end to her work.""",
'plastrons':"These are written in a very cold script that you struggle to read.",
'plastron':"These are written in a very cold script that you struggle to read.",
'bones':"These are written in a very cold script that you struggle to read.",
'paper':"The librarian tells you that the library is not open today so leave them alone.",
'rolls':"The librarian tells you that the library is not open today so leave them alone.",
'silk':"The librarian tells you that the library is not open today so leave them alone.",
'slips':"The librarian tells you that the library is not open today so leave them alone.",
'bamboo slips':"The librarian tells you that the library is not open today so leave them alone.",
'scroll':"""The scroll reads:
"The Master said, 'Learn as if you will never catch up, and as if you
feared losing what you have already attained.' 8.17 (n)"
""",
'books':"""Alas, the librarian is very protective of his books and stops you
from going any closer."""}

# ######################################################
# ## Location: Kongzi 3 School Entrance ######################################################

confuciusthree = game.new_location(
"Hall of Kongzi - School Entrance",
"""You are in a small courtyard. A gate to the south leads into a large hall
where you see many people sitting down. The gate has a piece of paper on it that
says, 'Silence! Exam in progress!' To the east is a door into another building
and you hear what sounds like a large group of people reciting something there.
You see a sign here, and also a scroll hanging on the wall of the courtyard.
""", "in")
confuciusthree.descriptions = {'sign':"""
The sign says:
"The Master said, 'A gentleman helps others to realize their good
qualities, rather than their bad. A petty person does the opposite.' 12.16
(m)"
""",
'scroll':"""The scroll reads:
"The Master said, 'Demand much of yourself, but ask little of others, and
you will keep resentment at a distance.' 15.15 (a)"
"""}
confuciusthree.add_phrase("read sign",read_sign)
confuciusthree.add_phrase("read scroll",read_scroll)

# ######################################################
# ## Location: Kongzi 4 Reception Room
# ######################################################


confuciusfour = game.new_location(
"Hall of Kongzi - Reception Room ",
"""This building looks like a kind of reception room for guests. There is a short
table here on the wooden floor. There is a sign here and a scroll hanging from
the wall. Through an archway to the east you can see a shrine of some kind. There
is a door to the south, and another archway to the west leading into a garden.
""", "in")
confuciusfour.descriptions = {'sign':"""
The sign says:
"The Master said, 'Do not be concerned about whether or not others know you; be concerned about whether or not you know others.' 1.16 (i)"
""",
'scroll':"""The scroll reads:
"The Master said The gentleman understands rightness, whereas the petty person understands profit" 4.16 (c)"
""",
'carving':"""The carving reads:
"Beneficial types of friendship number three, as do harmful
types of friendship. Befriending the upright, those who are true to their
word, or those of broad learning - these are the beneficial types of
friendship. Befriending clever flatterers, skillful dissemblers,or the
smoothly glib - these are the harmful types of friendship. 16.4 (w)"
"""}

confuciusfour.add_phrase("read sign",read_sign)
confuciusfour.add_phrase("read scroll",read_scroll)

# ######################################################
# ## Location: Kongzi 5 Interior Garden
# ######################################################

confuciusfive = game.new_location(
"Hall of Kongzi - Interior Garden ",
"""This is a beautiful walled garden, perfectly manicured. The garden is like a
small world in miniature, with tiny hills, pathways, groups of trees looking like
a forest, and flowering bushes everywhere. There is a path going southwest on a
bridge to an island in the garden and an archway to the east. There is a sign
in the garden and also a stone with a carving on it.
""", "in")
confuciusfive.descriptions = {'sign':"""
The sign says:
"The Master said When walking with two other people, I will always find a
teacher among them. I focus on those who are good and seek to emulate them,
and focus on those who are bad in order to be reminded of what needs to be
changed in myself. 7.22 (b)"
""",
'bridge':"""This beautiful small four pillared bridge arches nicely and leads
to the southwest.""",
'island':"You can see an island with a pavilion to the southwest.",
'hills':"The hills are small mounds but look like little mountains.",
'trees':"The dwarf trees are grouped together like little forests in the landscape.",
'bushes':"Some of the bushes are flowering, while others are a bright green.",
'carving':"""The carving reads:
"The Master said Do I possess wisdom? No, I do not. A common fellow asked a
question of me, and I came up completely empty. But I discussed the problem
with him from beginning until end until we finally got to the bottom of it.
9.8 (g)"
"""}
confuciusfive.add_phrase("read sign",read_sign)
confuciusfive.add_phrase("read carving",read_carving)
confuciusfive.add_phrase("look stone",read_carving)

# ######################################################
# ## Location: Kongzi 6 Study
# ######################################################

# Would be cool to add a write_letter function here checking
# for brush, ink, and paper, then allowing players to write
# whatever they want on a letter that can be dropped somewhere
# or perhaps used for some task. Again more complicated by
# difficulty of handling player input across multiple commands

# Currently the ink, brush, and paper aren't used for anything

confuciussix = game.new_location(
"Hall of Kongzi - Study ",
"""This small room looks like a study of some kind. There is a low table on the
floor, with some writing supplies on it for writting letters and such. There is
a sign here and a scroll hanging on the wall. There is a door to the north.
""", "in")
confuciussix.descriptions = {'sign':"""
The sign says:
"Every day I examine myself on three counts: in my dealings with others,
have I in any way failed to be dutiful? In my interactions with friends and
associates, have I in any way failed to be trustworthy? Finally, have I in
any way failed to repeatedly put into practice what I teach? 1.4 (w)"
""",
'scroll':"""The scroll reads:
"The Master said By nature people are similar; they diverge as the result of practice. 17.2 (e)"
"""}
confuciussix.add_phrase("read sign",read_sign)
confuciussix.add_phrase("read scroll",read_scroll)
confuciussix.add_phrase("write letter",Say("You don't have great calligraphy \nskills but write a nice wee letter with the brush and ink."))
confuciussix.add_phrase("write",Say("You don't have great calligraphy \nskills but write a nice wee letter with the brush and ink."))


# ######################################################
# ## Location: Kongzi 7 Island Pavilion
# ######################################################

# Player can pluck the goose here and get the magic feather than
# is one of the ways to get down the well

confuciusseven = game.new_location(
"Hall of Kongzi - Island Pavilion",
"""You are in an island pavilion, offering a tranquil view over a pond in a garden
You see a sign here and there is a carving on a rock. There is a bridge to the
northeast and a covered bridge to the east ending at an archway. There is a white
Chinese goose on the edge of the island and two mandarin ducks are playing in
the water.
""", "in")
confuciusseven.descriptions = {'sign':"""
The sign says:
"To learn and then have occasion to practice what you have learned - is
this not satisfying? To have friends arrive from afar - is this not a joy?
To be patient even when others do not understand - is this not the mark of
a gentleman? 1.1 (x)"
""",
'ducks':"""The ducks look like a very strange pair together with their very different looking
plumage, but it is clear that really love each other.""",
'duck':"""The ducks look like a very strange pair together with their very different looking
plumage, but it is clear that really love each other.""",
'bridge':"""The bridges here are lovely arched structures but small, just enough
for a single person to pass over. One of them is covered to the east and the
other one goes to the rest of the garden to the northeast.""",
'goose':"""The goose looks very tame and friendly. It has a faint glow to it. A
few of its feathers looks like they are about to fall off and would be easy to
pluck.""",
'carving':"""The carving reads:
"What I do not wish others to do unto me, I also wish not to do unto others 5.12 (y)"
"""}
confuciusseven.add_phrase("read sign",read_sign)
confuciusseven.add_phrase("take feathers",pick_berries)
confuciusseven.add_phrase("take goose feathers",pick_berries)
confuciusseven.add_phrase("take goose feather",pick_berries)
confuciusseven.add_phrase("take feather",pick_berries)
confuciusseven.add_phrase("pluck feathers",pick_berries)
confuciusseven.add_phrase("pluck goose feathers",pick_berries)
confuciusseven.add_phrase("pluck goose feather",pick_berries)
confuciusseven.add_phrase("pluck feather",pick_berries)
confuciusseven.add_phrase("pick feathers",pick_berries)
confuciusseven.add_phrase("pick goose feathers",pick_berries)
confuciusseven.add_phrase("pick goose feather",pick_berries)
confuciusseven.add_phrase("pick feather",pick_berries)
confuciusseven.add_phrase("read carving",read_carving)
confuciusseven.add_phrase("look rock",read_carving)

# ######################################################
# ## Location: Kongzi 8 Exam Room
# ######################################################

# It would have been cool to add a "take_exam" task here
# But it was going to be a bit time consuming to handle
# the player answers to a series of questions given the way
# this module handles user input. Might be cool to add this
# and make use of the pen and paper they can pick up in the
# study. The magical feather, for example, could be the award
# for a passing of the exam.

confuciuseight = game.new_location(
"Hall of Kongzi - Exam Room",
"""There is complete silence here as you enter. There are perhaps twenty students
sitting in little cells along the wall that each have their own table board
stretching from one little wall on their left to a wall on the right that
blocks their view of the other students. The entire environment is quite stressful. There is a sign here, and also a scroll hanging on the wall. There is a gate to the north.
""", "in")
confuciuseight.descriptions = {'sign':"""
The sign says:
"The Master said Look at the means a man employs, observe the basis from
which he acts, and discover where it is that he feels at ease. Where can he
hide? Where can he hide? 2.10 (d)"
""",
'scroll':"""The scroll reads:
"The Master said The gentleman is broad and not partial; the petty person
is partial and not broad" 2:14 (s)"
"""}
confuciuseight.add_phrase("read sign",read_sign)
confuciuseight.add_phrase("read scroll",read_scroll)
confuciuseight.add_phrase("take exam",Say("You sit down to take the exam with the other\nstudents but quickly realize you have a clue how to answer all these questions!"))

# ######################################################
# ## Location: Kongzi 9 School Hall
# ######################################################

confuciusnine = game.new_location(
"Hall of Kongzi - School Hall",
"""This large hall contains a group of students sitting on the floor. The
students appear to be reciting some old text together to practice it. The
teacher at the front is listening attentively and occasionally stops them to
comment on the meaning of a phrase and reflect on principals. There is a sign
here and a scroll hanging on the wall.
""", "in")
confuciusnine.descriptions = {'sign':"""
The sign says:
"If you learn without thinking about what you have
learned, you will be lost. If you think without learning, however, you will
fall into danger. 2.15 (q)"
""",
'teacher':"When you look closely you can see that the teacher is in fact a woman\n in disguise!",
'students':"""At first glance, these students look like boys, but on closer
examination you can see that all the students are in fact girls in disguise! The
whole hall is full of rebel girls attending a school where usually only boys
were allowed!""",
'text':"""The text they are reciting looks like it is entitled 'Biographies of Exemplary Women Who Subverted the Patriarchy'""",
'scroll':"""The scroll reads:
"This is wisdom: to recognize what you know as what you know, and recognize what you do not know as what you do not know. 2.17 (e)"
"""}
confuciusnine.add_phrase("read sign",read_sign)
confuciusnine.add_phrase("read scroll",read_scroll)

# ######################################################
# ## Location: Kongzi 10 Ancestral Shrine
# ######################################################

confuciusten = game.new_location(
"Hall of Kongzi - Ancestral Shrine ",
"""This is an ancestral shrine. There is some incense burning here and a series
of tablets representing various ancestors, with their names carved on them. You see a sign here, and also a rock with a carving on it. There is a door to the north and an archway to the west.
""", "in")
confuciusten.descriptions = {'sign':"""The sign says:
"Loving Goodness without balancing it with a love for learning will result
in the vice of foolishness. Loving wisdom without balancing it with a love
for learning will result in the vice of deviance. Loving trustworthiness
without balancing it with a love for learning will result in the vice of
harmful rigidity. Loving uprightness without balancing it with a love for
learning will result in the vice of intolerance. Loving courage without
balancing it with a love for learning will result in the vice of
unruliness. Loving resoluteness without balancing it with a love for
learning will result in the vice of willfulness. 17.8 (l)"
""",
'shrine':"Just your run of the mill ancestral shrine.",
'incense':"The smell of the incense is lovely.",
'tablets':"Lots of names on here written in Chinese.",
'carving':"""The carving reads:
"Fan Chi asked about Goodness
The Master replied 'Care for others'
He then asked about wisdom.
The Master replied, 'Know others.' (y)"
"""}
confuciusten.add_phrase("read sign",read_sign)
confuciusten.add_phrase("read carving",read_carving)
confuciusten.add_phrase("look rock",read_carving)


# ######################################################
# ## Location: Mengzi 1 Courtyard
# ######################################################

menciusone = game.new_location(
"Hall of Mengzi - Courtyard",
"""You find yourself in a Courtyard.  There is a rock with a carving. There is
also a sticker stuck on the wall. There are lots of exits here. There are
stairs going up and down. There are also doors going north, south, east, and
west.""", "in")
menciusone.descriptions = {'carving':"""
The carving reads:
"The best teachings are those that discuss what is near but with
significance that is far-reaching. The best Way is the one that preserves
what is crucial but has broad application. Although the teachings of a
gentleman come from nowhere but his bosom, the Way exists in them. The
gentleman maintains his own self-cultivation and so the world is at peace.
The problem with other people is that they abandon their own fields and
weed the fields of others. They demand much of others, while putting little
responsibility on themselves. 7B32.1 (t)"
""",'sticker':"I went to Qi to reform the king, but all I was left with was this stupid sticker."}
menciusone.add_phrase("read carving",read_carving)
menciusone.add_phrase("look rock",read_carving)

# ######################################################
# ## Location: Mengzi 2 Workshop
# ######################################################

menciustwo = game.new_location(
"Hall of Mengzi - Workshop",
"""This workshop has all sorts of materials and tools for doing artisan work. Looks like everyone has gone home for lunch at the moment. There is a chest here.
There is a door to the east. There is a sign here and a scroll hanging from the wall.
""", "in")
menciustwo.descriptions = {'sign':"""
The sign says:
"When Heaven is about to bestow a great responsibility on a particular
person, it will always first subject one's heart and resolution to
bitterness, belabor one's muscles and bones, starve one's body and flesh,
deprive one's person, and thwart and bring chaos to what one does. By means
of these things it perturbs one's heart, thoughens one's nature, and
provides those things of which one is incapable. One must often make
mistakes, and only then can one improve. One must be troubled in one's
heart and vexed in one's deliberations, and only then rise up. These things
must show in one's face and be expressed in one's voice, and then others
will see them in you. 6B15.2 (c)"
""",
'materials':"A mix of raw materials for making stuff. Not of much use to you.",
'tools':"All sorts of tools, most of which you can't identify and should probably\nnot steal.",
'scroll':"""The scroll reads:
"This is the Way of the people: those who have a constant livelihood have a constant heart; those who lack a constant livelihood lack a constant heart. No one who fails to have a constant heart will avoid dissipation and evil. When they thereupon sink into crime, to go and punish them is to trap the people. When there are benevolent people in positions of authority, how is it possible for them to trap the people? 3A3.3 (u)"
"""}
menciustwo.add_phrase("read sign",read_sign)
menciustwo.add_phrase("read scroll",read_scroll)


# ######################################################
# ## Location: Mengzi 3 Farm
# ######################################################

def look_cart(game,thing):
  if game.player.location.flag('fixed'):
    game.output("The cart looks a bit banged up, but is in working order.",DESCRIPTION)
  else:
    game.output("This cart has seen better days, one of the wheels is completely broken.")

def fix_cart(game,thing):
  """If the player has a wheel, will fix it and give player rope and information"""
  if game.player.location.flag('fixed'):
    game.output("The cart already looks fixed, you see one wheel that is new.",DESCRIPTION)
    return True
  if "wheel" in game.player.inventory:
    game.player.location.set_flag('fixed')
    game.output("Your wheel fits perfectly on the new cart and you attach it easily.",DESCRIPTION)
    game.output("""The Farmer from Song says:
Thank you so much for fixing my cart. I'm pretty useless at this farming
business. Just the other day Mengzi reprimanded me after my crops withered
due to me trying to pull the plants up grow them faster saying,"One must
work at it, but do not assume success. One should not forget the heart, but
neither should one 'help' it grow. Those in the world who do not 'help' the
sprouts to grow are few. Those who abandon them, thinking it will not help,
are those who do not weed their sprouts."

In thanks for your fixing this cart, let me give you some of my rope.
Perhaps it will help you?
""",FEEDBACK)
    game.output("The man gives you some rope.",CONTENTS)
    newrope = game.player.location.add_object(Object("rope","a long piece of rope."))
    game.player.act_take1(game.player,'rope',True)
    game.player.remove_from_inventory(wheel)
  else:
    game.output("Looks like you need a wheel to get this cart working again.",FEEDBACK)

menciusthree = game.new_location(
"Hall of Mengzi - The Farm",
"""You are standing in a small farm. There is a field here that has been well
ploughed. You can see small sprouts sticking out of the ground. There is a sign here and a stone with a carving. There is a gate to the north, a door to the south, and a door to the west. There is a farmer here standing next to a cart.
""", "in")
menciusthree.descriptions = {'sign':"""
The sign says:
"In years of plenty, most young men are gentle; in years of poverty, most
young men are violent. It is not that the potential that Heaven confers on
them varies like this. They are like this because of what sinks and drowns
their hearts. Consider barley. Sow the seeds and cover them. The soil is
the same and the time of planting is also the same. They grow rapidly, and
by the time of the summer solstice they have all ripened. Although there
are some differences, these are due to the richness of the soil and to
unevenness in the rain and in human effort... 6A7.1 (j)"
""",
'sprouts':"These young plants are growing well given the good environment.",
'field':"A well-ploughed field with some sprouts growing out but you can't tell\nwhat is growing here.",
'carving':"""The carving reads:
"All humans have hearts that are not unfeeling toward others...Suppose someone suddenly saw a child about to fall into a well: anyone in such a situation would have a feeling of alarm and compassion...From this we can see that if one is without the feeling of compassion, one is not human...The feeling of compassion is the sprout of benevolence... 2A6 (g)"
"""}
menciusthree.add_phrase("read sign",read_sign)
menciusthree.add_phrase("read carving",read_carving)
menciusthree.add_phrase("look rock",read_carving)
menciusthree.add_phrase("fix cart",fix_cart)
menciusthree.add_phrase("fix wheel",fix_cart)
menciusthree.add_phrase("fix cart wheel",fix_cart)
menciusthree.add_phrase("put wheel cart",fix_cart)
menciusthree.add_phrase("put wheel on cart",fix_cart)
menciusthree.add_phrase("give wheel farmer",fix_cart)
menciusthree.add_phrase("give farmer wheel",fix_cart)
menciusthree.add_phrase("look cart",look_cart)
menciusthree.add_phrase("look wheel",look_cart)


# ######################################################
# ## Location: Mengzi 4 Water Wheel
# ######################################################

# If you want to add more puzzles, have the player harvest something
# from the farm, bring it here and grind the grains down to give to
# the cook in exchange for something

menciusfour = game.new_location(
"Hall of Mengzi - Water Wheel",
"""You stand on a path next to a small stream. The water comes flowing down from
a hill to the north and falls onto a large horizontally laying water wheel which
turns and releases the water as it continues along the path. The water mill is
attached to a device used for crushing grains. You see a sign here. To the north
the path continues to a small house which smells delicious. A mountain trail
continues to the west.  There is a gate to the east and a door to the south.
""", "in")
menciusfour.descriptions = {'sign':"""
The sign says:
"Gaozi said, "Human nature is like swirling water. Make an opening for it
on the eastern side, then it flows east. Make an opening for it on the
western side, then it flows west. Human nature not distinguishing between
good and not good is like water not distinguishing between eastern and
western."

Mengzi replied, "Water surely does not distinguish between east and west.
But doesn't it distinguish between upward and downward? Human nature being
good is like water tending downward. There is not human who does not tend
toward goodness. There is no water that does not tend downward. Now, by
striking water and making it leap up, you can cause it to go past your
forehead. If you guid it by damming it, you can cause it to remain on a
mountaintop. But is this the nature of water? It is only that way because
of the circumstances. When humans are cause to not be good, it is only
because their nature is the same way. 6A2.1 (p)"
"""}
menciusfour.add_phrase("read sign",read_sign)

# ######################################################
# ## Location: Mengzi 5 Tower
# ######################################################

menciusfive = game.new_location(
"Hall of Mengzi - Tower",
"""You are standing in a small tower. There is a bell here. From the tower you
have a nice view of the land around. You can see more buildings and forest to
the south. To the east you can make out a big lake, a river, and a mountain. On
the mountain you see a platform and a small hut. There is a sign here and a scroll hanging from one of the pillars of the tower. There are stairs going down.
""", "in")
menciusfive.descriptions = {'sign':"""
The sign says:
"Mengzi said, 'There are Heavenly honors, and there are human honors.
Benevolence, righteousness, devotion, faithfulness, delighting in goodness
without tiring - these are Heavenly honors. Being a duke, High Minister, or
Chief Counselor - these are human honors. The ancients cultivated Heavenly
honors, and human honors followed upon them. Nowadays, people cultivate
Heavenly honors because they want human honors. So when they have obtained
the human honors, they cast away the Heavenly honors. This is the extreme
of confusion! In the end they will lose everything.' 6A16.1 (h)"
""",
'bell':"The bell has a large ringer on it and looks like it would give a nice big sound if rung.",
'scroll':"""The scroll reads:
"Mengzi said, 'Benevolence will overcome what is not benevolent just as
water overcomes fire. Nowadays, those who practice benevolence are like
someone who tries to save a wagonload of burning firewood with a single
glass of water. When the fire is not extinguished, they claim that water
cannot overcome fire...' 6A18.1 (g)"
"""}
menciusfive.add_phrase("read sign",read_sign)
menciusfive.add_phrase("ring bell",Say("You give the bell a nice ring. It creates a satisfyingly massive vibration through to your very bones."))
menciusfive.add_phrase("read scroll",read_scroll)

# ######################################################
# ## Location: Mengzi Basement
# ######################################################

menciussix = game.new_location(
"Hall of Mengzi - Basement ",
"""You are in a dark basement, lit only by some light from the stairs leading up.
You can make out a sign here, and a scroll hanging on the wall by the stairs.
Beyond in the basement it looks like there are various things in storage here,
dusty and all covered up.
""", "in")
menciussix.descriptions = {'sign':"""
The sign says:
"If one loves others and they are not affectionate to oneself, one should
examine one's own benevolence. If one rules over others and they are
unruly, one should examine one's own wisdom. If one treats others with
propriety and they do not respond, one should examine one's own reverence.
If in one's actions one does not succeed, one should always seek for it in
oneself. If one is proper oneself, the world will turn to him. 4A4.1 (i)"
""",
'scroll':"""The scroll reads:
"Just as one who is well supplied with wealth cannot be killed by a bad
year, so one who is well supplied with Virtue cannot be disordered by an
evil era. 7B10.1 (h)"
"""}
menciussix.add_phrase("read sign",read_sign)
menciussix.add_phrase("read scroll",read_scroll)

# ######################################################
# ## Location: Mengzi 7 Archery Hall
# ######################################################

menciusseven = game.new_location(
"Hall of Mengzi - Archery Hall",
"""You are in a hall for archery. There is a target some dozen meters
away from where you are standing. There is a sign here and also a
scroll that is hanging on the wall of the hall. There is a gate to
the west and a gate to the south.
""", "in")
menciusseven.descriptions = {'sign':"""
The sign says:
"Benevolence is like archery. An archer corrects himself and only then
shoots. If he shoots but does not hit the mark, he does not resent the one
who defeats him but simply turns and seeks for it in himself. 2A7.5 (d)"
""",
'target':"""Approaching the target you see that in the very center there is a mysterious looking
hole. You also notice a tiny sign below the target that says, 'Strike true,
and you will thereafter travel far.'""",
'scroll':"""The scroll reads:
"If one makes others submit with power, their hearts do not submit. Power
is inadequate to make their hearts submit. If one makes others submit with
Virtue, they are pleased in their hearts and genuinely submit, like the
seventy disciples who served Kongzi. 2A3.2 (n)"
"""}
menciusseven.add_phrase("read sign",read_sign)

# ######################################################
# ## Location: Mengzi 8 Mountain Path
# ######################################################

menciuseight = game.new_location(
"Hall of Mengzi - Mountain Path",
"""You are on a path on a small mountain behind Mengzi's home. The path is steep
and eventually comes to an end at a nice viewing platform. You are still low enough that you can smell the food coming from a kitchen somewhere down below. There is a sign here and a rock with a carving on it.
""", "in")
menciuseight.descriptions = {'sign':"""
The sign says:
"Mountain paths become roads if they are used frequently. But if they are
not used for a while they become overgrown with brush and weeds... 7B21.1 (q)"
""",
'carving':"""The carving reads:
"For cultivating the heart, nothing is better than having few desires. If
someone has few desires, although there will be times when he does not
persevere, they will be few. If someone has many desires, although there
will be times when he perseveres, they will be few. 7B35.1 (v)"
"""}
menciuseight.add_phrase("read sign",read_sign)
menciuseight.add_phrase("read carving",read_carving)
menciuseight.add_phrase("look rock",read_carving)


# ######################################################
# ## Location: Zhuangzi 1 - Riverside
# ######################################################

def swim_river(game,thing):
  """Gives player 1-5 damage for swimming in fast rocky river"""
  game.output("""You enter the fast moving river and are immediately pulled
towards the many rocks in its middle. You are certainly being jostled and
shaken about, but I think Zhuangzi was not being literal when he suggests
this. You are soon banging up against the rocks and just barely manage to
climb out of the river before getting mushed in the rapids.""",FEEDBACK)
  time.sleep(0.3)
  damage=random.randint(1,5)
  game.output('The bruises and cuts do '+str(damage)+' points of damage to you.',FEEDBACK)
  game.player.health-=damage
  game.output('Your health is now: '+str(game.player.health), CONTENTS)

zhuangzione = game.new_location(
"Hall of Zhuangzi - Beside the River Hao",
"""You find yourself at the bank of a river. There is a warm wind and the
sun is beaming down on the rocks of the river. There is a bridge over the
river to the north and a path to the south here. There is a sign here and
a carving on a rock.
""", "in")
zhuangzione.descriptions = {'sign':"""The sign says:
"Forget what year it is, forget what should or should not be. Let yourself
be jostled and shaken by the boundlessness - for that is how to be lodged
securely in the boundlessness! 2:45 (j)"
""",
'river':"""The river is pretty fast moving and filled with rocks.""",
'carving':"""The carving reads:
"What man knows is far less than what he does not know. The time he exists
is insignificant compared to the time he does not exist. It is because he
tries to exhaust this vastness with this meagerness that he bewilders and
frustrates himself. 17 (f)"
"""}
zhuangzione.add_phrase("read sign",read_sign)
zhuangzione.add_phrase("read carving",read_carving)
zhuangzione.add_phrase("look rock",read_carving)
zhuangzione.add_phrase("swim in river",swim_river)
zhuangzione.add_phrase("swim river",swim_river)
zhuangzione.add_phrase("swim",swim_river)


# ######################################################
# ## Location: Zhuangzi 2 - Stone Bridge
# ######################################################

zhuangzitwo = game.new_location(
"Hall of Zhuangzi - The Stone Bridge ",
"""You stand on a large stone bridge over the river. Lots of small fish
can be seen in the fast flowing river down below. On the side in  the
center of the bridge is a sign. There is also a man here leaning on the
side of the bridge and looking into the water. To the south is the riverside
and to the north you see a bamboo grove.
""", "in")
zhuangzitwo.descriptions = {'sign':"""The sign says:
"Zhuangzi and Huizi were strolling along the bridge over the Hao River.
Zhuangzi said, "The minnows swim about so freely, following the openings
wherever they take them. Such is the happiness of fish."
Huizi said, "You are not a fish, so whence do you know the happiness of
fish?" Zhuangzi said, "You are not I, so whence do you know I don't know
the happiness of fish?"
Huizi said, "I am not you, to be sure, so I don't know what it is to be
you. But by the same token, since you are certainly not a fish, my point
about your inability to know the happiness of fish stands intact."
Zhuangzi said, "Let's go back to the starting point. You said, 'Whence do
you know the happiness of fish?' Since your question was premised on your
knowing that I know it, I must have known it from here, up above the Hao
River. 17 (c)"
""",
'minnows':"These small fish can be seen just below the surface of the\n water. You can't help thinking that they look happy and free.",
'fish':"These small fish can be seen just below the surface of the\n water. You can't help thinking that they look happy and free.",
}
zhuangzitwo.add_phrase("read sign",read_sign)
zhuangzitwo.add_phrase("swim in river",swim_river)
zhuangzitwo.add_phrase("swim river",swim_river)
zhuangzitwo.add_phrase("swim",swim_river)
zhuangzitwo.add_phrase("jump into river",swim_river)
zhuangzitwo.add_phrase("jump in the river",swim_river)
zhuangzitwo.add_phrase("jump river",swim_river)

# ######################################################
# ## Location: Zhuangzi 3 - Bamboo Grove
# ######################################################

zhuangzithree = game.new_location(
"Hall of Zhuangzi - Bamboo Grove",
"""You stand in a bamboo grove. You hear the rustling of the bamboo leaves
high above you as it sways in the wind but also the creaking and crackling
of the bamboo stalks as they bend. There is an occasional hoot or scream
coming from a large number of monkeys that you can just make out far above
you. You see a sign here and also a rock with a carving on it.
""", "in")
zhuangzithree.descriptions = {'sign':"""The sign says:
"What is this thing known as Three in the Morning? A monkey trainer was
distributing chestnuts. He said, 'I'll give you three in the morning and
four in the evening.' The monkeys were furious. 'Well then,' he said, 'I'll
give you four in the morning and three in the evening.' The monkey were
delighted. This change of description and arrangement caused no loss, but
in one case it brought anger and in another delight. He just went by the
rightness of their present 'this.' Thus, the Sage uses various rights and
wrongs to harmonize with others and yet remains at rest in the middle of
Heaven the Potter's Wheel. This is called 'Walking Two Roads' (u)"
""",
'carving':"""The carving reads:
"Do you know what it is that undermines real Virtuosity, and for what
purpose, on the contrary, 'cleverness' comes forth? Virtuosity is
undermined by getting a name for it. Cleverness comes forth from conflict.
For a good name is most essentially a way for people to one-up each other,
and cleverness is most essentially a weapon for winning a fight. Both are
inauspicious implements, not the kind of thing that can be used to perfect
your own behavior. 4.3 (s)"
"""}
zhuangzithree.add_phrase("read sign",read_sign)
zhuangzithree.add_phrase("read carving",read_carving)
zhuangzithree.add_phrase("look rock",read_carving)


# ######################################################
# ## Location: Zhuangzi 4 - Meditation Hall
# ######################################################

def attach_rope(game,thing):
  """Attaches rope to the well and flags it for safe descent"""
  if not "rope" in game.player.inventory:
    game.output("You don't have any rope in your inventory. Sure would be useful.")
    return True
  game.player.remove_from_inventory(game.player.inventory['rope'])
  game.player.location.descriptions['well']="""The well is quite small but looks very deep. You can just make out
something moving at the bottom. The well is so small the huge turtle wouldn't be
able to fit down it though a human being probably could. The sides look very
slippery and looks like it would be dangerous to jump down or climb down the
well. There is a round pole across the well and a rope is tied onto it, hanging
down into the well."""
  game.player.location.set_flag('roped')
  game.output("""You tie the rope to the wooden poll that stretches across the well
and secure it well. It should now be safe to climb down the well.""", FEEDBACK)


def enter_well(game,thing):
  """Fall down the well and die unless rope is tied or magic feather present"""
  if game.player.location.flag('roped'):
    game.output("You grab a hold of the rope and rappel down into the well.", FEEDBACK)
    game.player.location = well
    where = game.player.location.describe(game.player, game.player.flag('verbose'))
    if where:
      game.output("")
      game.output(where)
      game.output("")
  elif "feather" in game.player.inventory:
    game.output("""As you jump into the well, your magic feather begins to glow
and instead of falling like stone, you drift from left to right, falling slowly
and safely down the shaft of the well.""",FEEDBACK)
    game.player.location = well
    where = game.player.location.describe(game.player, game.player.flag('verbose'))
    if where:
      game.output("")
      game.output(where)
      game.output("")
  else:
    game.output("Aaaaaaaaaahhhhhhhhhh! You fall down the deep well and perish.",FEEDBACK)
    game.player.health=-1

def meditate(game,thing):
  if game.player.health<16:
       game.player.health+=3
       game.output("\nYou sit in stillness and find your center. You pass an hour in silence and let go of the world. \nYou feel refreshed and your health is now: ",FEEDBACK)
       game.output(str(game.player.health)+"\n",CONTENTS)
  else:
      game.output("""Already in great health, you sit in stillness and find your center. You pass an hour in silence and let go of the world.""",FEEDBACK)

zhuangzifour = game.new_location(
"Hall of Zhuangzi - Meditation Hall",
"""You find yourself in a tranquil hall of meditation, a covered space open
on all sides and surrounded by a garden. There is a sign here and there is a
scroll hanging on one of the pillars of the hall. There is a path north from
the hall, as well as a path into the bamboo grove to the south and to the east
towards a pond. Nearby you see a stone well. Next to it there is a huge turtle
looking down into well with a sad look.
""", "in")
zhuangzifour.descriptions = {'sign':"""The sign says:
"But to liberate your body from always having to be doing something, there
is nothing more effective than letting go of the world. When you let go of
the world, you are free of entanglements. Free of entanglements, you are
balanced and untilting. Balanced and untilting, you are unborn along with
each presence that confronts you. With such rebirth, you have done about
all that can be done. (d)"
""",
'well':"""The well is quite small but looks very deep. You can just make out
something moving at the bottom. The well is so small the huge turtle wouldn't be
able to fit down it though a human being probably could. The sides look very
slippery and looks like it would be dangerous to jump down or climb down the
well. There is a round pole across the well that something could be tied to.""",
'scroll':"""The scroll reads:
"The long is not excessive and the short is not deficient. The duck's neck
may be short but lengthening it would surely vex him; the swan's neck may
be long, but cutting it short would surely sorrow here. What is long in its
inborn nature is not to be cut short, and what is short in its inborn
nature is not to be lengthened. For there is nothing there that needs to be
excised or worried over. (i)"
"""}
zhuangzifour.add_phrase("read sign",read_sign)
zhuangzifour.add_phrase("read scroll",read_scroll)
zhuangzifour.add_phrase("meditate",meditate)
zhuangzifour.add_phrase("go well",enter_well)
zhuangzifour.add_phrase("jump into well",enter_well)
zhuangzifour.add_phrase("jump well",enter_well)
zhuangzifour.add_phrase("down",enter_well)
zhuangzifour.add_phrase("d",enter_well)
zhuangzifour.add_phrase("climb well",enter_well)
zhuangzifour.add_phrase("climb down well",enter_well)
zhuangzifour.add_phrase("enter well",enter_well)
zhuangzifour.add_phrase("tie rope",attach_rope)
zhuangzifour.add_phrase("attach rope",attach_rope)
zhuangzifour.add_phrase("attach rope pole",attach_rope)
zhuangzifour.add_phrase("tie rope pole",attach_rope)
zhuangzifour.add_phrase("use rope",attach_rope)


# ######################################################
# ## Location: Zhuangzi 5 Pond
# ######################################################

zhuangzifive = game.new_location(
"Hall of Zhuangzi - The Pond ",
"""This is a quiet misty place. There is almost no sound to be heard other
than the rustling of some bushes in the wind, and the occasional sound of a
small creature or two in a pond here. There is a stone here with a carving on
it and a sign as well. There is a path back to the west but the other directions
are blocked with thick bamboo.
""", "in")
zhuangzifive.descriptions = {'sign':"""The sign says:
"...People cannot see their reflections in running water, but only in still
water. Only stillness can still the multitude to the point of genuine
stillness. Though all life-forms receive their vitality from the earth, it
remains constantly replete only in the pine and the cypress, so they remain
lush and green both summer and winter. 5.9 (n)"
""",
'pond':"A calm dark pond with some lily pads, and insects buzzing around.",
'carving':"""The carving reads:
"Good fortune comes to roost in stillness. To lack this stillness is called
scurrying around even when sitting down. Allow your ears and eyes to open
inward and thereby place yourself beyond your mind's understanding
consciousness. Even the ghosts and spirits will then seek refuge in you,
human beings all the more so! 4:12 (u)"
"""}
zhuangzifive.add_phrase("read sign",read_sign)
zhuangzifive.add_phrase("look stone",read_carving)
zhuangzifive.add_phrase("read carving",read_carving)
zhuangzifive.add_phrase("swim",Say("You take a nice swim in the pond."))
zhuangzifive.add_phrase("swim pond",Say("You take a nice swim in the pond."))


# ######################################################
# ## Location: Zhuangzi 6 Ancient Forest
# ######################################################

zhuangzisix = game.new_location(
"Hall of Zhuangzi - Ancient Forest",
"""You find yourself deep in a dark and tranquil forest. You can hear the sounds
of birds up in the trees above. There is a sign here. To the south you can hear
the sounds of a waterfall. The trail also continues further to the east.
""", "in")
zhuangzisix.descriptions = {'sign':"""The sign says:
"The tailorbird lives in the depths of a vast forest but uses no more than
a single branch to make its nest. When the beaver drinks from the river, it
takes only enough to fill its belly. 1.10 (z)"
"""}
zhuangzisix.add_phrase("read sign",read_sign)


# ######################################################
# ## Location: Zhuangzi 7 Waterfalls
# ######################################################

zhuangziseven = game.new_location(
"Hall of Zhuangzi - Waterfalls ",
"""You are standing in front of a beautiful waterfall. In front of the waterfall
you can see thousands of butterflies flapping about and visiting the many flowers
that grow along the edge of the water here. You see a sign here and a stone with
a carving on it.
""", "in")
zhuangziseven.descriptions = {'sign':"""The sign says:
"Once Zhuang Zhou dreamt he was a butterfly, fluttering about joyfully just
as a butterfly would. He followed his whims exactly as he liked and knew
nothing about Zhuang Zhou. Suddenly he awoke, and there he was, the
startled Zhuang Zhou in the flesh. He did not know if Zhou had been
dreaming he was a butterfly, or if a butterfly was now dreaming it was
Zhou. Surely, Zhou and a butterfly count as two distinct identities! Such
is what we call the transformation of one thing into another. 2:49 (y)"
""",
'waterfall':"""The waterfall is powerful and a rainbow is reflected on its surface.
You don't see anything behind it but rock.""",
'carving':"""The carving reads:
"Hence, all things are neither formed nor destroyed, for these two also
open into each others, connecting to form a oneness. It is only someone who
really gets all the way through them that can see how the two sides open
into each other to form a oneness. 2.22 (v)"
"""}
zhuangziseven.add_phrase("read sign",read_sign)
zhuangziseven.add_phrase("look stone",read_carving)
zhuangziseven.add_phrase("read carving",read_carving)
zhuangziseven.add_phrase('swim',Say("You take a refreshing swim in front of the waterfall and enjoy the spray that comes off it."))

# ######################################################
# ## Location: Zhuangzi 8 Glade
# ######################################################

zhuangzieight = game.new_location(
"Hall of Zhuangzi - The Useless Tree in the Glade ",
"""You are standing in a glade where the sunlight streams down onto a grassy
patch in the middle of the forest. Here you see a massive gnarled tree, a maze of
convoluted branches with a strangely shaped trunk. Next to the tree there is a
sign. Nearby there is also a stone with a carving on it.
""", "in")
zhuangzieight.descriptions = {'sign':"""The sign says:
"Huizi said to Zhuangzi: I have a huge tree which people call the Stink
Tree. The trunk is swollen and gnarled...Even if it were growing right in
the road, a carpenter would not give it so much as a second glance...
Zhuangzi says, "...You,...have this big tree, and you worry that it's
useless. Why not plant it in our homeland of not-even-anything, the vast
wilds of open nowhere? Then you could loaf and wander there, doing lots of
nothing there at its side, and take yourself a nap, far-flung and
unfettered, there beneath it. It will never be cut down by ax or saw.
Nothing will harm it. Since it has nothing for which it can be used, what
could entrap or afflict it? 1.14 (o)"
""",
'tree':"A massive gnarled tree, a maze of convoluted branches with a strangely shaped trunk.",
'carving':"""The carving reads:
"Carpenter Shi was traveling in Qi when he came upon the tree of the shrine
at the Qu Yuan bend. Itw as over a hundred arms spans round, so large that
thousands of oxen could shade themselves beneath it. It overstretched the
surrounding hills, its lowest branches hundreds of feet from the ground, at
least a dozen of which could have been hollowed out to make into ships. It
was surrounded by marveling sightseers, but the carpenter walked past it
without a second look.

Carpenter Shi said, "...This is worthless lumber! As a ship it would soon
sink, as a coffin it would soon rot, as a tool it would soon break...This
is a talentless, worthless tree. It is precisely because it is so useless
that it has lived so long."

Back home, Carpenter Shi saw the tree in a dream..."What do you want to
compare me to, one of those cultivated trees?...Their large branches are
bent; their small branches are pruned. Thus do their abilities embitter
their lives. That is why they die young, failing to fully live out their
natural life spans. They batter themselves with the vulgar conventions of
the world - and all other creatures do the same. As for me, I've been
working on being useless for a long time. It almost killed me, but I've
finally managed it - and it is a great use to me! If I were useful, do you
think I could have grown to be so great? 4.18 (g)"
"""}
zhuangzieight.add_phrase("read sign",read_sign)
zhuangzieight.add_phrase("read carving",read_carving)
zhuangzieight.add_phrase("look stone",read_carving)
zhuangzieight.add_phrase("take nap",Say("You take a relaxing nap in the shade of the big tree."))
zhuangzieight.add_phrase("nap",Say("You take a relaxing nap in the shade of the big tree."))
zhuangzieight.add_phrase("take a nap",Say("You take a relaxing nap in the shade of the big tree."))


# ######################################################
# ## Location: Well
# ######################################################

well  = game.new_location(
"Hall of Zhuangzi - Well ",
"""You find yourself at the bottom of a deep well covered in some mud but not
much water. Here you see a small frog just hanging out. Looking closely at the
sides of the well you can see small handles on the wall of the well that will
allow you to climb back up. There is also an archway leading to a passageway
heading north lit by torches. By the light of the torches you can see there is
a sign attached to the wall of the well.
""", "in")
well.descriptions = {'sign':"""The sign says:
"Have you ever heard the story about the frog in the sunken well? He said
to the tortoise of the Eastern Ocean, "How happy I am! I jump about on the
railings and beams of the well and rest on the ledges left by missing tiles
along its walls. When I splash into the water, it supports my armpits and
holds up my chin, and when I tread in the mud, it submerges my feet up to
the ankles. The surrounding crabs and tadpoles are certainly no match for
me! For to have such mastery over one whole puddle of water like this,
possessing all the joy of this sunken well - that is perfection! Why don't
you come in and have a look sometime?" But before the tortoise could even
get his left foot in, his right knee was stuck in the opening. So he pulled
himself back out and told the frog about the ocean:

"Its vastness exceeds a distance of a thousand miles; its depth is beyond
the measure of a thousand fathoms. In Yu's time the lands were flooded for
nine years, but its waters did not rise. In Tang's day there were seven
droughts in eight years, but its shores did not recede. Unpushed and
unpulled by either a moment or an aeon, unreceded and unadvanced by either
little or much - that is the great joy of the Eastern Ocean!"

"When the well-frog heard this, he was cast into uncontainable
astonishment, shrinking into utter discouragement... 17 (r)"
"""}
well.add_phrase("read sign",read_sign)


# ######################################################
# ## Location: Guardroom
# ######################################################

def pass_statue(game,thing):
  """Gives the player 1-5 damage for trying to pass the guardian"""
  if game.player.location.flag('guarded'):
    game.output("""
As you try to walk passed the guardian and approach the archway,
the statue suddenly swings its antlers down and slashes at you.
The sharp antlers cut through your clothes and deep into your skin.""",FEEDBACK)
    damage=random.randint(1,5)
    game.output('The cut does '+str(damage)+' points of damage to you.',FEEDBACK)
    game.player.health-=damage
    game.output('Your health is now: '+str(game.player.health), CONTENTS)
  else:
    game.player.set_location(machineroom)

guardroom = game.new_location(
"Guardroom",
"""You are standing in a cold stone room, dark except for two small torches
that give you a bit of light. To your north is an archway through which you
can just make out what looks like a big steam driven machine. In front of
the archway, however, is a large statue that looks like it is made out of
wood. It looks like a pillar, at the top of which is a demonic looking face.
Its fiery eyes are alive and follow your movements. Above its head, two deer-like
antlers extend and loom over you.
""", "in")
guardroom.set_flag('guarded')

guardroom.descriptions = {'archway': 'This open archway is the entrance to the machine room to the north',
    'machine': 'You can\'t see it clearly from here, you will have to go into the room to the north.',
    'torches': 'The two torches are firmly attached to the wall',
    'statue': 'The statue is positioned in such a way that you cannot pass north without coming in range of its large antlers, should the statue move.',
    'antlers': 'The huge antlers are sharp and look like they would hurt if they came your way.'}

guardroom.add_phrase("north",pass_statue)
guardroom.add_phrase("n",pass_statue)


# ######################################################
# ## Location: Kitchen
# ######################################################

def eat_soup(game,thing):
  """Heals the player if they are carrying a bowl"""
  if not "bowl" in game.player.inventory:
    game.output("That soup looks great, but piping hot. A bowl would be helpful here.")
    return True
  if game.player.health<16:
     game.player.health+=5
     game.output("\nThe soup is not only delicious but has a healing effect. \nYour health has increased and is now: ",FEEDBACK)
     game.output(str(game.player.health)+"\n",CONTENTS)
  else:
    game.output("This healing soup is delicious but you are already good and healthy.",FEEDBACK)

def make_smoothie(game,thing):
  """Makes a smoothie if the player has berries and cup

It will make a smoothie that remembers how many kinds of berries it has, since the guardian will only accept a smoothie with three kinds of berries or fruit as price of passage"""
  berrycount=0
  if "blueberries" in game.player.inventory: berrycount+=1
  if "strawberries" in game.player.inventory: berrycount+=1
  if "raspberries" in game.player.inventory: berrycount+=1
  if "peach" in game.player.inventory: berrycount+=1
  if berrycount==0:
    game.output("To make a smoothie you need to be carrying some fruit or berries.",FEEDBACK)
    return True
  else:
    if not "cup" in game.player.inventory or "glass" in game.player.inventory:
      game.output("""To make a smoothie you need to be carrying some kind
of vessel to carry the smoothie in once it has been blended.""",FEEDBACK)
      return True
    newsmoothie = game.player.location.add_object(smoothie)
    newsmoothie.set_var('berrycount',berrycount)
    game.player.act_take1(game.player,'smoothie',True)
    if "cup" in game.player.inventory:
      game.player.remove_from_inventory(cup)
    else:
      game.player.remove_from_inventory(glass)
    if "blueberries" in game.player.inventory: game.player.remove_from_inventory(blueberries)
    if "strawberries" in game.player.inventory: game.player.remove_from_inventory(strawberries)
    if "raspberries" in game.player.inventory: game.player.remove_from_inventory(raspberries)
    if "peach" in game.player.inventory: game.player.remove_from_inventory(peach)
    singleplural = 'type'
    if berrycount>1: singleplural = 'types'
    game.output("You created a new smoothie which contains "+str(berrycount)+' '+singleplural+' of berries and fruit.',FEEDBACK)

kitchen = game.new_location(
"Kitchen",
"""
As soon as you enter the room you smell a delightful array of aromas coming
from a pot over the fire. Some vegetables are cut up on a long table and
there is a blender there as well. Finally you see how the people of the
hall are fed. There is a man standing near them tending to the food.
You see a doors to the south, west, east, and north.""", "in")
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
kitchen.add_phrase("get soup",eat_soup)
kitchen.add_phrase("take soup",eat_soup)
kitchen.add_phrase("drink soup",eat_soup)
kitchen.add_phrase("try soup",eat_soup)

# ######################################################
# ## Location: Machine Room
# ######################################################

def check_dials(game,thing):
  """Checks to see if current dial settings matches the answers

If the player has chosen the right answers they win the game and are given some final text."""
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

      ===========  YOU HAVE WON THE GAME  =============

""",FEEDBACK)
    # Replace "YOU HAVE WON THE GAME" with your own secret message
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
  """Lists the current settings for the dials"""
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
  """Turns one of the dials to a new letter"""
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
game.new_connection("iron gate", hallentrance,innercourtyard,NORTH)
game.new_connection("tunnel", well,guardroom,NORTH)
game.new_connection("Metal Door", guardroom,machineroom,NORTH)
game.new_connection("garden gate", innercourtyard,laozione,EAST)
game.new_connection("path", laozione,laozitwo,NORTH)
game.new_connection("path", laozitwo,laozithree,WEST)
game.new_connection("path", zhuangzione,laozifour,WEST)
game.new_connection("path", laozithree,laozifour,NORTH)
game.new_connection("path", laozifour,laozifive,NORTH)
game.new_connection("path", laozifive,laozisix,NORTH)
game.new_connection("path", laozitwo,zhuangzione,NORTH)
game.new_connection("stone bridge", zhuangzione,zhuangzitwo,NORTH)
game.new_connection("stone bridge", zhuangzitwo,zhuangzithree,NORTH)
game.new_connection("path", zhuangzithree,zhuangzifour,NORTH)
game.new_connection("path", zhuangzifour,zhuangzifive,EAST)
game.new_connection("well", zhuangzifour,well,DOWN)
game.new_connection("path", zhuangzithree,zhuangzisix,EAST)
game.new_connection("path", zhuangzisix,zhuangziseven,SOUTH)
game.new_connection("path", zhuangzisix,zhuangzieight,EAST)
game.new_connection("door", innercourtyard,confuciusone,WEST)
game.new_connection("door", confuciusone,confuciustwo,WEST)
game.new_connection("gate", confuciusone,confuciusthree,SOUTH)
game.new_connection("door", confuciusone,confuciusfour,NORTH)
game.new_connection("door", confuciustwo,confuciusfive,NORTH)
game.new_connection("door", confuciusfive,confuciusseven,SOUTHWEST)
game.new_connection("archway", confuciusfour,confuciusfive,WEST)
game.new_connection("door", confuciustwo,confuciussix,SOUTH)
game.new_connection("archway", confuciustwo,confuciusseven,WEST)
game.new_connection("gate", confuciusthree,confuciuseight,SOUTH)
game.new_connection("gate", confuciusthree,confuciusnine,EAST)
game.new_connection("archway", confuciusfour,confuciusten,EAST)
game.new_connection("door", confuciusfour,menciusone,NORTH)
game.new_connection("door", menciusone,menciustwo,WEST)
game.new_connection("door", confuciusten,menciusthree,NORTH)
game.new_connection("door", menciusone,menciusthree,EAST)
game.new_connection("door", menciusone,menciusfour,NORTH)
game.new_connection("gate", menciusthree,menciusseven,NORTH)
game.new_connection("gate", menciusfour,menciusseven,EAST)
game.new_connection("path", menciusfour,menciuseight,WEST)
game.new_connection("door", kitchen,menciusfour,SOUTH)
game.new_connection("door", kitchen,confuciuseight,WEST)
game.new_connection("door", kitchen,zhuangzieight,NORTH)
game.new_connection("door", kitchen,laozifive,EAST)
game.new_connection("stairs", menciusone,menciusfive,UP)
game.new_connection("stairs", menciusone,menciussix,DOWN)

# OBJECT FUNCTIONS #######################################################

def output_health(self,actor):
    game.output("Your Health Level is: ",FEEDBACK)
    game.output(str(hero.health)+'\n',CONTENTS)
    return True

def show_hint(self,actor):
  hints=['Not all objects in rooms are laying on the ground',
      'Talk to characters to find out things.',
      'Some things you read have a letter inside of (parentheses) - those letters are important \nfor completing the game.',
      'If you hang around and do things in room while another character is there, \nthey may say interesting things: sometimes humorous, sometimes philosophical, \nbut sometimes they will give you clues too.',
      'Sometimes objects in one area of the game help you in another area.',
      'To keep from getting lost, make a map to keep track of what goes where.',
      'Read the signs and scrolls and carvings, maybe some match parts of your \ntranslations?',
      'Some things you read have a letter inside of (parentheses) - those letters are important \nfor completing the game.',
      'Some things you read have a letter inside of (parentheses) - those letters are important \nfor completing the game.',
      'Some things you read have a letter inside of (parentheses) - those letters are important \nfor completing the game.',
      'When you have collected all the code letters to match your translations \nmake sure you keep them in the right order.',
      'When you do things, leave out all extra words like "to" and "the" and \nother prepositions etc.',
      'There are things you do in the game that can harm you, but also places\nthat have the possibility of healing you.',
      'Some rooms have lots of descriptions of things you can look at, but others \ndo not have much at all. But keep looking at things you find!']
  game.output(random.choice(hints),FEEDBACK)
def show_help(self,actor):
    game.output("""Welcome to the Hall of Sages. A range of commands are accepted in this game.
Verbs of movement: north, south, east, west, up, down; Actions: drink, eat,
inventory, health, examine (objects in your inventory), look (at things around
you: use single words), read, take, drop, attack, pet, talk, feed, fix, pick,
turn, give, swim, use, and so on. In general, leave out prepositions whenever
possible. Use 'hint' to get some tips and hints. Use 'about' to learn more about
this game. Use 'q' or 'quit' to exit the game.
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


# OBJECTS #######################################################

blueberries=Food("blueberries","some delicious blueberries picked from the forest",Say("Yummy!"))
raspberries = Food("raspberries","some delicious raspberries picked from the forest",Say("Tart and delicious!"))
strawberries = Food("strawberries","some delicious tiny strawberries picked from the forest",Say("So sweet!"))
peach = laozione.add_object(Food("peach","a delicious peach",Say("Juicy!")))
feather = Object("feather","a feather with a slight glow to it.")
feather.add_phrase("hold feather",Say("You hold up the glowing feather."))
feather.add_phrase("use feather",Say("You hold up the glowing feather."))
emptyglass = guardroom.add_object(Object("glass","an empty glass that smells like a combination of different berries."))
wheel = laozisix.add_object(Object("wheel","A small wheel for a cart."))
cup = laozisix.add_object(Object("cup","A large cup, perfect for holding a nice big drink."))
claybowl = laozisix.add_object(Object("bowl","An empty clay bowl."))
book = confuciustwo.add_object(Object("book","a book with the title 'Mozi'"))
book.add_phrase("read book",Say("""Looks like a philosophy book about someone named 'Master Mo.'
Looks like some impressive and interesting stuff. You wonder why Mozi wasn't
given his own hall here?"""))
brush = confuciussix.add_object(Object("brush","a simple writing brush."))
ink = confuciussix.add_object(Object("ink bottle","a bottle of writing ink."))
paper = confuciussix.add_object(Object("paper","a simple piece of writing paper."))
arrow = menciusseven.add_object(Object("arrow","a sharp arrow."))
greatarrow = Object("glowing arrow","an arrow that has a faint glow to it.")
key = confuciussix.add_object(Object("key","a small iron key."))
chest = menciustwo.add_object(Container("chest", "a long thin chest"))
chest.new_object("bow","A beautifully crafted wood composite bow")
chest.make_requirement(key)
bow = chest.new_object("bow","A beautifully crafted wood composite bow")

def look_smoothie(game,thing):
  """Reports how many berry types are found in the smoothie"""
  berrycount=thing.var('berrycount')
  singleplural = 'type'
  if berrycount>1: singleplural = 'types'
  game.output("A delicious looking smoothie with "+str(berrycount)+' '+singleplural+' of berries.',FEEDBACK)


smoothie = Drink("smoothie","A delicious smoothie made from fruit",Say("Delicious!"),Object("empty smoothie glass", "an empty smoothie glass"))
smoothie.set_var('berrycount',0)
smoothie.add_phrase("look smoothie",look_smoothie)


def shoot_arrow(game,thing):
  """Shoots an arrow, shoots arrow at target in archery hall, or teleportation arrow"""
  if not "bow" in game.player.inventory or (not "arrow" in game.player.inventory and not "glowing arrow" in game.player.inventory):
    game.output("You need a bow and arrow before you can shoot it.")
    return True
  # TELEPORTATION ARROW IS PRESENT, TELEPORT PLAYER TO RANDOM PLACE:
  if "glowing arrow" in game.player.inventory:
    game.output("""You fire your glowing arrow and as soon as the bow releases the arrow you feel
like you are pulled along with the bow. You are transported to a new place!""",FEEDBACK)
    possible_locations=[]
    for place in game.location_list:
      if "Well" in place.name:
        continue
      elif "Guardroom" in place.name:
        continue
      elif "Machine Room" in place.name:
        continue
      else:
        possible_locations.append(place)
    game.player.location = random.choice(possible_locations)
    game.output("\nYou have been transported randomly to:",FEEDBACK)
    game.output(game.player.location.name+'\n',CONTENTS)
    where = game.player.location.describe(game.player, game.player.flag('verbose'))
    if where:
      game.output("")
      game.output(where)
      game.output("")

    time.sleep(0.2)
    droppedarrow=game.player.remove_from_inventory(greatarrow)
    game.player.location.add_object(droppedarrow)
    game.output("\nYour glowing arrow drops to the ground.",CONTENTS)
    return True

  if not game.player.location.name == "Hall of Mengzi - Archery Hall":
    game.output("You shoot the arrow. You are still a beginner, however, so \nit doesn't go very far.",FEEDBACK)
    if "arrow" in game.player.inventory:
      droppedarrow = game.player.remove_from_inventory(arrow)
      game.player.location.add_object(droppedarrow)
  else:
    game.output("You shoot the arrow at the target.")
    time.sleep(0.1)
    hitlocation = random.random()
    if hitlocation < 0.15:
      game.output("""Your arrow hits exactly in the middle of the target!""",FEEDBACK)
      time.sleep(0.1)
      game.output("Your arrow drops to the ground, but now begins to glow faintly!",CONTENTS)
      game.player.remove_from_inventory(arrow)
      game.player.location.add_object(greatarrow)
      game.output("There is an glowing arrow here!",CONTENTS)
    elif hitlocation < 0.25:
      game.output("Oooh, sooo close! You almost hit the middle of the target!",FEEDBACK)
      time.sleep(0.15)
      game.output("Keep trying, you may hit the middle!",FEEDBACK)
      time.sleep(0.1)
      droppedarrow=game.player.remove_from_inventory(arrow)
      game.player.location.add_object(droppedarrow)
      game.output("There is an arrow here.",CONTENTS)
    elif hitlocation < 0.45:
      game.output("Good shot! You hit the target but not close to the middle.",FEEDBACK)
      time.sleep(0.1)
      droppedarrow=game.player.remove_from_inventory(arrow)
      game.player.location.add_object(droppedarrow)
      game.output("There is an arrow here.",CONTENTS)
    elif hitlocation < 0.75:
      game.output("Well, you hit the target but only on the edge.",FEEDBACK)
      time.sleep(0.1)
      droppedarrow=game.player.remove_from_inventory(arrow)
      game.player.location.add_object(droppedarrow)
      game.output("There is an arrow here.",CONTENTS)
    else:
      game.output("Doh! You missed the target!",FEEDBACK)
      time.sleep(0.1)
      droppedarrow=game.player.remove_from_inventory(arrow)
      game.player.location.add_object(droppedarrow)
      game.output("\nYour arrow drops to the ground.",FEEDBACK)
      game.output("There is an arrow here.",CONTENTS)


################################################################
################################################################
################################################################
################################################################
# ACTORS #######################################################
################################################################
################################################################
################################################################
################################################################

hero.health = 12
hero.add_phrase("health",output_health)
hero.add_phrase("help",show_help)
hero.add_phrase("about",show_about)
hero.add_phrase("hint",show_hint)
hero.add_phrase("h",show_help)
hero.add_phrase("shoot arrow",shoot_arrow)
hero.add_phrase("shoot bow",shoot_arrow)

# #####################################
# Actor - Zhuangzi
# #####################################

zhuangzi = Animal("Zhuangzi")
zhuangzi.description = """Looks like a jolly fellow with a great sense of humor"""
zhuangzi.talkativeness = 0.5
zhuangzi.add_phrase("look at Zhuangzi",Say(zhuangzi.description))
zhuangzi.add_phrase("look Zhuangzi",Say(zhuangzi.description))
zhuangzi.randomphrases = ["""You hear the piping of man but not yet
the piping of the earth. You hear the piping of the earth but not yet
the piping of Heaven""",
"""Human interactions, when handled face-to-face,
are founded on mutual trust. But when handled at a distance, they must depend
on words to establish reciprocal loyalty. These words have to be transmitted
by someone, and there is nothing in the world more difficulty than
communicating mutual esteem or mutual anger between two people. The esteem
gets exaggerated into flattery and the anger into insult. These exaggerations
then become outright lies, and once the lying starts trustworthiness is lost,
and then the ability to communicate is destroyed—and perhaps the messenger as
well.""",
"""Wherever debate shows one of two
alternatives to be right, something remains undistinguished and unshown. What
is it? The sage hides it in his embrace, while the masses of people debate
it, trying to demonstrate it to one another. Thus I say that demonstration by
debate always leaves something unseen.""",
"""Human speech is not just a blowing of air.
Speech has something of which it speaks, something it refers to. Yes, but
what it refers to is pecurliarly unfixed.""",
"""To use this horse to show that a horse is not a horse
is no match for using not-this-horse to show that a horse is not a horse.
Heaven and earth are one finger. All things are one horse.""",
"""Now I have said something.
But I do not-yet know: has what I have said really said anything? Or has it
not really said anything?""",
"When words demonstrate by debate, they fail to communicate.",
"""I'm going to try speaking some reckless words. How about listening just
as recklessly?""",
"""He looks on the alterations of all things as his own fate,
and thus holds fast to their source."""]
reply = """Zhuangzi says, "Hello there, welcome to my hall. Rinse out your mind,
cleanse your seminal spirit until it gleams like snow, and smash
your understanding."""
zhuangzi.add_phrase("talk Zhuangzi",Say(reply))
zhuangzi.add_phrase("talk zhuangzi",Say(reply))
zhuangzi.add_phrase("kill Zhuangzi",Say("He easily dodges your clumsy blows."))
zhuangzi.add_phrase("attack Zhuangzi",Say("He easily dodges your clumsy blows."))
zhuangzi.set_location(zhuangzione)
zhuangzi.set_allowed_locations([zhuangzione,zhuangzitwo,zhuangzithree,zhuangzifour,zhuangzifive,zhuangzisix,zhuangziseven,zhuangzieight,well,kitchen])

# #####################################
# Actor - Laozi
# #####################################

laozi = Animal("Laozi")
laozi.description = """A old man with a very long wispy beard split into
three parts and a bald head. He is carrying a large fan.
"""
laozi.talkativeness = 0.5
laozi.add_phrase("look at Laozi",Say(laozi.description))
laozi.add_phrase("look Laozi",Say(laozi.description))
laozi.randomphrases = ["""If your desires are great, you're bound to be extravagant;
If you store much away, you're bound to lose a great deal.
Therefore, if you know contentment, you'll not be disgraced.""",
"""The softest, most pliable thing in the world
runs roughshod over the firmest thing in the world.
That which has no substance gets into that which has no spaces or cracks.""",
"""To understand others is to be knowledgeable;
To understand yourself is to be wise;
To conquer others is to have strength;
To conquer yourself is to be strong.
To know when you have enough is to be rich.""",
"""A Way that can be followed is not a constant Way.
A name that can be named is not a constant name.""",
"""Everyone in the world knows that when the beautiful
strives to be beautiful, it is repulsive.""",
"""One who is good at traveling leaves no tracks or traces.""",
"""Sages do not have constant hearts of their own;
They take the people's hearts as their hearts.""",
"""What is at peace is easy to secure.
What has yet to begin is easy to plan for."""]
reply = """Laozi says, "Hello and welcome to my hall. Take my crane for a
ride, you'll never guess where you will end up."""
laozi.add_phrase("talk Laozi",Say(reply))
laozi.add_phrase("talk laozi",Say(reply))
laozi.add_phrase("kill Laozi",Say("He easily dodges your clumsy blows."))
laozi.add_phrase("attack Laozi",Say("He easily dodges your clumsy blows."))
laozi.set_location(laozione)
laozi.set_allowed_locations([laozione,laozitwo,laozithree,laozifour,laozifive,laozisix,kitchen])

# #####################################
# Actor - Mengzi
# #####################################

mengzi = Animal("Zhuangzi")
mengzi.description = """Looks like a man dressed in Ying style robes. He has a plaster on his nose."""
mengzi.talkativeness = 0.6
mengzi.add_phrase("look at man",Say(mengzi.description))
mengzi.add_phrase("look man",Say(mengzi.description))
mengzi.randomphrases = ["Mom is wandering around here somewhere.",
"""I hope Zhuangzi isn't using overly
fine nets in his pond.""",
"""Zhuangzi told me that he was climbing his
tree yesterday and that he found a fish there.
I think he was making fun of me.""",
"""I say all humans have hearts that are not unfeeling,
but the custodian asked me, 'What about psychopaths?'
I just smiled and kept walking.""",
"""I've got some new ideas about how to
layout the farm.""",
"""Things interact with other things and simply lead them along. But the function of the heart is to reflect. If it reflects, then it will get it. If it does not reflect, then it will not get it.""",
"""There is no greater delight than to turn toward oneself and discover Genuineness. Nothing will get one closer to benevolence than to force oneself to act out of sympathetic understanding."""]
reply = """Mengzi says, "Hello there and welcome to my hall. I must run along,
I'm trying to find something to see if I can help my farmer."""
mengzi.add_phrase("talk Mengzi",Say(reply))
mengzi.add_phrase("talk mengzi",Say(reply))
mengzi.add_phrase("kill Mengzi",Say("He easily dodges your clumsy blows."))
mengzi.add_phrase("attack Mengzi",Say("He easily dodges your clumsy blows."))
mengzi.set_location(menciusone)
mengzi.set_allowed_locations([menciusone,menciustwo,menciusthree,menciusfour,menciusfive,menciussix,menciusseven,kitchen])

# #####################################
# Actor - Kongzi
# #####################################

kongzi = Animal("Kongzi")
kongzi.description = """Looks like a man dressed in Ying style robes. He has a plaster on his nose."""
kongzi.talkativeness = 0.6
kongzi.add_phrase("look at Kongzi",Say(kongzi.description))
kongzi.add_phrase("look Kongzi",Say(kongzi.description))
kongzi.randomphrases = ["""A person without concern for what is far away
is sure to encounter worries close at hand""",
"""I have heard it said that the gentleman
aids the needy but does not help the rich to become richer.""",
"""Look at the means a man employs,
observe the basis from which he acts,
and discover where it is that he feels at ease.
Where can he hide? Where can he hide?""",
"""Observe closely the sort of mistakes a person makes
then you will know his character.""",
"""The gentleman understands rightness,
whereas the petty person understands profit.""",
"""What I do not wish others to do unto me,
I also wish not to do unto others.""",
"""Is Goodness really so far away?
If I simply desire Goodness, I will find that it is already here.""",
"""A gentlmean helps others to realize
their good qualities, rather than their bad.
A petty person does the opposite.""",
"""Fan Chi asked me about Goodness,
and I replied, 'Care for others.'
He asked about wisdom and I replied,
'Know others.'""",
"""The gentleman harmonizes and does not
merely agree. The petty person agrees,
but he does not harmonize."""]
reply = """Kongzi says, "Hello, and welcome to my hall. If Laozi has a magic
crane, I have a magic goose."""
kongzi.add_phrase("talk Kongzi",Say(reply))
kongzi.add_phrase("talk kongzi",Say(reply))
kongzi.add_phrase("kill Kongzi",Say("He easily dodges your clumsy blows."))
kongzi.add_phrase("attack Kongzi",Say("He easily dodges your clumsy blows."))
kongzi.set_location(confuciusone)
kongzi.set_allowed_locations([confuciusone,confuciustwo,confuciusthree,confuciusfour,confuciusfive,confuciussix,confuciusseven,confuciuseight,confuciusnine,confuciusten])

# #####################################
# Actor - Mengzi's Mother
# #####################################

mom = Animal("mom")
mom.description = """You see a strong woman, with wise eyes and arms that
look like they have years of weaving experience."""
mom.talkativeness = 0.4
mom.add_phrase("look at mom",Say(mom.description))
mom.add_phrase("look mom",Say(mom.description))
mom.randomphrases = ["""Imagine how much more genuinely educational
this place would have been if it was a "The Hall of Moms" instead of
a "Hall of Sages"? But then I am guessing fewer kids would enter.
""",
"""Where do you think Mengzi got all his best
ideas from, eh? Ya, you are looking at her.""",
"""Mengzi's book mentions mothers half a dozen times,
but the only time I show up is when it talks about
him mourning my passing. Anything about how I was
always right? No. Any credit for my ideas? No."""]
reply = """Welcome to our hall. I am Mengzi's mother. The histories never
bothered to give me a name, so you can just call me mom. Mengzi used to be a
little rascal but I got him sorted. I had to move three times in order to find
a good profession for him. We used to live near a graveyard, then a market,
and since neither of those places are particularly suitable for a career in
my opinion, we settled down near a school. Though I'm not sure the school down
south from here is turning out to be the kind of place Mengzi had in mind."""
mom.add_phrase("talk mom",Say(reply))
mom.add_phrase("kill mom",Say("She easily dodges your clumsy blows."))
mom.add_phrase("attack man",Say("She easily dodges your clumsy blows."))
mom.set_location(menciusone)
mom.set_allowed_locations([menciusone,menciustwo,menciusthree,menciusfour,menciusfive,menciussix,menciusseven])

# #####################################
# Actor - Mozi
# #####################################

mozi = Animal("Mozi")
mozi.description = """You see a strong woman, with wise eyes and arms that
look like they have years of weaving experience."""
mozi.talkativeness = 0.4
mozi.add_phrase("look at Mozi",Say(mozi.description))
mozi.add_phrase("look Mozi",Say(mozi.description))
mozi.randomphrases = ["Where is my hall? I should get a hall too!",
"""All these Confucians favor their families first.
I condemn partiality. Replace partiality with impartiality.""",
"""Everyone seems to agree that killing someone
is wrong. But then killing ten people would be ten times as bad,
and killing a hundred a hundred times as bad. Instead, we find
people praising this when it comes to a war. Makes no sense to me.""",
"""Look at all these fancy dressed scholars
in these halls. What is the purpose of clothes? To protect us
from the cold of winter and the heat of summer. If we
eliminated extravagance we could feed more people.""",
"""Universal love and peace are what I'm about.
But I condemn all music. Of no benefit to the people.""",
"""Whoever criticizes others must have something to replace them. Criticism
without suggestion is like trying to stop flood with flood and put out fire
with fire. It will surely be without worth."""]
reply = """Hello, I am the philosopher Mozi, the Sage of universal love.
I would welcome you to my hall, but I am afraid I don't seem to have one."""
mozi.add_phrase("talk Mozi",Say(reply))
mozi.add_phrase("talk mozi",Say(reply))
mozi.add_phrase("kill Mozi",Say("He easily dodges your clumsy blows."))
mozi.add_phrase("attack Mozi",Say("He easily dodges your clumsy blows."))
mozi.set_location(kitchen)
allowlocations=[]
for place in game.location_list:
  if "Well" in place.name or "Guardroom" in place.name or "Machine Room" in place.name:
    continue
  else:
    allowlocations.append(place)
mozi.set_allowed_locations(allowlocations)


# #####################################
# Actor - Examiner
# #####################################

def beat_talker(game,thing):
  game.output("""As soon as you open your mouth, the examiner whips out his
massive stick and begins to beat you with it.""",FEEDBACK)
  time.sleep(0.3)
  damage=random.randint(1,2)
  game.output('\nThe beating does '+str(damage)+' points of damage to you.',FEEDBACK)
  game.player.health-=damage
  game.output('\nYour health is now: \n'+str(game.player.health)+"\n", CONTENTS)


examiner = Animal("examiner")
examiner.description = """Looks like a very serious school teacher wielding a very big stick."""
examiner.talkativeness = 0.6
examiner.randomphrases = ["Shhhhhh!","Ssssshhhhhhhhhhhh!","Shh!","Quiet!","Silence!"]
examiner.add_phrase("look at examiner",Say(examiner.description))
examiner.add_phrase("look examiner",Say(examiner.description))
examiner.add_phrase("talk examiner",beat_talker)
examiner.add_phrase("kill examiner",Say("He easily dodges your clumsy blows."))
examiner.add_phrase("attack examiner",Say("He easily dodges your clumsy blows."))
examiner.set_location(confuciuseight)
examiner.set_allowed_locations([confuciuseight,confuciusthree])


# #####################################
# Actor - Huizi
# #####################################

huizi = Animal("man")
huizi.description = """Looks like a man dressed in Ying style robes. He has a plaster on his nose."""
huizi.talkativeness = 0.6
huizi.add_phrase("look at man",Say(huizi.description))
huizi.add_phrase("look man",Say(huizi.description))
huizi.randomphrases = ["Zhuangzi's words really are completely useless.",
    "Everyone remembers Zhuangzi, but don't realize how much he was inspired \n by me.",
    "I need to get Carpenter Shi to chop this plaster off with his ax.",
    "Silly Zhuangzi, he even thinks he knows what the fish are feeling."]
reply = """Hello, my name is Huizi. I am a man of Ying. It is my job to
keep Zhuangzi on his toes in our conversations together. You know he is full
of all sorts of nonsense ideas."""
huizi.add_phrase("talk man",Say(reply))
huizi.add_phrase("kill man",Say("He easily dodges your clumsy blows."))
huizi.add_phrase("attack man",Say("He easily dodges your clumsy blows."))
huizi.set_location(zhuangzitwo)
huizi.set_allowed_locations([zhuangzitwo])

# #####################################
# Actor - Cook Meng Shen
# #####################################


cook = Animal("man")
cook.description = "A short-tempered looking man, dressed in Tang dynasty robes, busily rushing around the kitchen."
cook.talkativeness = 0.6
cook.randomphrases = ["""This kitchen is like the center of the universe, you
can reach any of the four halls from here.""",
"""Kitchens really have a way of bringing the people together, the only place
where all those sages can end up in the same place. The Hundred Schools may
never be reunited into one philosophy, but they definitely all love my soup.
""",
"Laozi flies in here on his crane when he gets the munchies.",
"""I once suggested to Zhuangzi that he make a new parable about the frog
in the pot. He may not be able to see the fire, but he's gonna get cooked
anyways. Zhuangzi said I was too pessimistic about life.""",
"""Kongzi said there is a joy to be had in plain food, but I sure see him
hanging around here a lot when I make some delicious spicy curry."""]
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
banzhao.talkativeness = 0.4
banzhao.randomphrases = ["""I could write another grand history, but no,
they want me to write a stupid book telling women how to be good
obedient wives, grr...""",
"""If only they would let me write a book for
Empress Deng, called, 'Lessons for a Dangerous Dowager Empress'""",
"""If only they would let me rename this silly
'Lessons for Women' book to, 'Lessons for Nasty Women'"""]
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
"""))

# #####################################
# Actor - Teacher
# #####################################

teacher = Animal("teacher")
teacher.talkativeness = 0.8
teacher.randomphrases = ["""The first way is called 'Lighting the Candle':
You will be trained to recognize the patriarchy, but more importantly, you will
be trained to make men recognize the patriarchy and the foundation of idiocy it
is built upon. You will find some allies among them who will join you in the
fight.""",
"""The second way is called 'Herding the Horses':
You will be sent forth to seize power in all fields of public life. Once you
occupy the halls of power, you can help tear down the patriarchy.""",
"""The third way is called 'Walking the Dog':
You will disguise yourself and pretend to submit, ruling in the domestic sphere
as wives, mothers, and filial daughters. From this position, called 'The Painted
Pillar' you will be at the
heart of things where you can find ways to exert great power from behind the
walls.""",
"""The fourth way is called 'Flight of the Heron':
Direct conflict is not always worth it. In this way, you will be taught how to
find your own path, and fly high and far on your own individual journey."""]
teacher.description = "This teacher is a woman dressed in confucian robes."
teacher.add_phrase("look at teacher",Say(teacher.description))
teacher.add_phrase("look teacher",Say(teacher.description))
teacher.set_location(confuciusnine)
teacher.set_allowed_locations([confuciusnine])
teacher.add_phrase("kill teacher",Say("She easily dodges your clumsy blows."))
teacher.add_phrase("attack teacher",Say("She easily dodges your clumsy blows."))
teacher.add_phrase("talk teacher",Say("""Welcome to my school. Here I am teaching a new generation
of young women who will soon destroy the male-dominated world of the four halls
completely. I will instruct them in the four ways to subvert the patriarchy and
send them forth to all the other halls. Stay a while and you may learn some of
them.
"""))


# #####################################
# Actor - Tortoise
# #####################################


tortoise= Animal("tortoise")
tortoise.talkativeness = 0.2
tortoise.randomphrases = ["""I am about to give up on this frog. It just won't listen to what I'm saying.""","""I think I'm going back to the Eastern Ocean.""","If only I could fly like the fish Kun, that becomes the bird Peng.",
"""Zhuangzi says my friend, the turtle of Chu, drags his backside through the mud. I wonder if I drag my backside through the mud too?""","""They say I am from the Eastern Sea, but aren't tortoises land creatures? I'm sure Zhuangzi
would just tell me to chill and not worry about it."""]
tortoise.description = "This is a massive tortoise that looks like it is talking to the well."
tortoise.add_phrase("look at tortoise",Say(tortoise.description))
tortoise.add_phrase("look tortoise",Say(tortoise.description))
tortoise.set_location(zhuangzifour)
tortoise.set_allowed_locations([zhuangzifour])
tortoise.add_phrase("kill tortoise",Say("It is practically indestructible."))
tortoise.add_phrase("attack tortoise",Say("It is practically indestructible."))
tortoise.add_phrase("talk tortoise",Say("""The tortoise sighs and says, "There is a frog down there who
seems to think it is at the center of the universe. I can't seem to convince it
otherwise."
"""))

# #####################################
# Actor - Farmer
# #####################################


farmer = Animal("farmer")
farmer.description = """This farmer is looking distraught and sad, leaning over
his cart, which has a broken wheel. The farmer says, 'If only I could fix my
cart, I could continue my work'"""
farmer.add_phrase("look at farmer",Say(farmer.description))
farmer.add_phrase("look farmer",Say(farmer.description))
farmer.set_location(menciusthree)
farmer.set_allowed_locations([menciusthree])
farmer.add_phrase("kill farmer",Say("He easily dodges your blows."))
farmer.add_phrase("attack farmer",Say("He easily dodges your blows."))
farmer.add_phrase("talk farmer",Say("""The farmer sighs and says, "All I need to do is to replace this wheel and I could get back to work."
"""))


# #####################################
# Actor - Frog
# #####################################


frog = Animal("frog")
frog.talkativeness = 0.8
frog.randomphrases = ["""What is so great about an ocean anyways?""",
"""Zhuangzi and the tortoise give me a hard time about the limits of my space,
but this makes no sense to me. He doesn't give the tailorbird or the beaver
a hard time for their limited ambitions?""",
"""If Zhuangzi can know that the fish are happy, how does
he know that I don't know that this well is better than the Eastern Ocean?""",
"""This well sure is cool.""",
"""I used to be more of a frog in a pond type,
but the insects down here are way more tasty.""",
"""Frog in a pond? No one remembers them;
frog in a well? Immortalized by a crazy philosopher.""",
"""Doesn't that tortoise know that frogs and salt water
don't mix? No oceans for me, bud.""",
"""'uncontainable astonishment,' it says,
'shrinking into utter discouragement' - what complete nonsense.
'uncontainable laughter,' and 'utter disgust,' are more like it!""",
"""What do tortoises know about oceans anyways?""",
"""The only thing that could be cooler than a frog in a well,
would be *two* frogs in a well!""",
"""Laozi told me:
"If your desires are great, you're bound to be extravagant;
If you store much away, you're bound to lose a great deal.
Therefore, if you know contentment, you'll not be disgraced."
So, like, I'm totally content in this well, see?"""]
frog.description = "This frog looks pretty chill, and really happy in the well."
frog.add_phrase("look at frog",Say(frog.description))
frog.add_phrase("look frog",Say(frog.description))
frog.set_location(well)
frog.set_allowed_locations([well])
frog.add_phrase("kill frog",Say("It just bounces out of your way."))
frog.add_phrase("attack frog",Say("It just bounces out of your way."))
frog.add_phrase("talk tortoise",Say("""The frog says: Hello there. Thanks for not dying on the way down. I get a bit tired dodging the idiots who jump down
here, not to mention the clean up afterwards. If you are headed to the machine
room, I hope you brought a gift for the guardian?
"""))

# #####################################
# Actor - Squirrel
# #####################################

squirrel = Animal("squirrel")
squirrel.talkativeness = 0.2
squirrel.randomphrases = ['Where did I leave those chestnuts?',
    'I am so sick of berries.',
    'I am glad those sages dropped squirrel meat from the menu.',
    'Get out of my way!',
    "I'm going to be late!"]
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

# #####################################
# Actor - Monkey
# #####################################

def monkey_steal(game,thing):
  """Checks for random event in which monkey steals random player item

If a random event is triggered the monkey will select a random item from the player's inventory and steal it. It will drop it if fed by fruit or berries"""
  chancestolen=0.5 # baseline 40% chance of having something stolen
  if monkey.flag('fed'):
    chancestolen=0.05 # lower this to 15% chance if already fed once
  if monkey.flag('stolen'):
    chancestolen=0.05 # lower it if something is already stolen
  if random.random() < chancestolen: # 1 in 2 chance of something getting stolen
    if len(game.player.inventory)>0: # They are carrying something
      targetobject = random.choice(game.player.inventory.keys())
      game.player.location.add_object(game.player.remove_from_inventory(game.player.inventory[targetobject]))
      monkey.act_take1(monkey,targetobject,True)
      time.sleep(0.2)
      game.output("""
Oh no!! The monkey has stolen your """+targetobject+"""! Perhaps if you feed the monkey it will drop your item?
""",FEEDBACK)
      monkey.set_flag('stolen')
    else:
      game.output("""The monkey takes a swipe at your inventory pouch!!!
It looks very disappointed to find that it was empty.""",FEEDBACK)

def monkey_feed(game,thing):
  """Feeds the monkey fruit from the player's inventory

If the player has a peach or a kind of berries they can feed the monkey. The monkey will then drop the stolen item in the room."""
  if not monkey.flag('stolen') or monkey.flag('fed'):
    game.output("The monkey doesn't seem very hungry.")
  else:
    # The monkey has stolen something and hasn't been fed
    if "peach" in game.player.inventory:
      givenobject=game.player.inventory.pop('peach', None)
    elif "strawberries" in game.player.inventory:
      givenobject=game.player.inventory.pop('strawberries', None)
    elif "blueberries" in game.player.inventory:
      givenobject=game.player.inventory.pop('blueberries', None)
    else:
      game.output("The monkey doesn't seem interested in that object. Maybe some fruit?")
      return True
  game.output("The monkey eagerly devours your gift and returns your item.")
  if len(monkey.inventory)<1:
    game.output("Error: nothing found in the monkey's inventory",DEBUG)
  else:
    monkey.unset_flag('stolen')
    monkey.set_flag('fed')
    stolenitem=monkey.inventory.popitem()
    game.player.location.contents[stolenitem[0]]=stolenitem[1]
    # game.player.add_to_inventory(stolenitem)
    game.output("The monkey drops your:",FEEDBACK)
    game.output(stolenitem[0],CONTENTS)

monkey = Animal("monkey")
monkey.description = "A cheeky looking monkey who is eyeing your possessions as you move."
monkey.randomphrases = ["""Zhuangzi said that when a sage is born, great robbers
arise. You are looking at one. There is no age of the sage, without it also being
the age of the monkey!""","""Some people call me Zhi, Robber Zhi!""","Don't worry Kongzi, I am no thief of virtue!",
"""Mengzi says that I am devoted to profit from the moment I wake up. Not true! I steal, because I am a thief, profit has nothing to do with it!""",
"""Once I pretended to be a student of Mengzi and stole some awesome sandals."""]
monkey.add_phrase("look at monkey",Say(monkey.description))
monkey.add_phrase("look monkey",Say(monkey.description))
monkey.set_allowed_locations([zhuangzithree,zhuangzisix,zhuangzieight])
monkey.set_location(zhuangzithree)
monkey.add_phrase("feed monkey",monkey_feed)
monkey.add_phrase("feed monkey peach",monkey_feed)
monkey.add_phrase("feed monkey berries",monkey_feed)
monkey.add_phrase("give monkey berries",monkey_feed)
monkey.add_phrase("give monkey peach",monkey_feed)
monkey.add_phrase("give monkey fruit",monkey_feed)
monkey.add_phrase("give peach to monkey",monkey_feed)
monkey.add_phrase("give berries to monkey",monkey_feed)
monkey.add_phrase("give berries monkey",monkey_feed)
monkey.add_phrase("give peach monkey",monkey_feed)
monkey.add_phrase("give peach monkey",monkey_feed)
monkey.add_phrase("kill monkey",Say("The monkey laughs, 'Haha, catch me if you can!"))
monkey.add_phrase("attack monkey",Say("The monkey laughs, 'Haha, carch me if you can!'"))

# #####################################
# Actor - Custodian
# #####################################

custodian = Animal("custodian")
custodian.description = "This young boy seems to dance as he sweeps the well-trafficked courtyard"
custodian.talkativeness = 0.8
custodian.sayverbs+=['grumbles','sighs to himself and says']
custodian.randomphrases = ["""I'm done cleaning up for after those
Daoists to the East, they are always making such a mess and
getting in my way.""",
    "That machine room needs a good sweep, but the guardian doesn't let me past.",
    "Is it lunchtime yet?",
    """All these moral lessons posted about,
but someone forgot to include 'Clean up after yourself!'""",
    "I need a vacation!",
    "Doo dee doo doo",
    """Zip-a-dee-doo-dah, zip-a-dee-ay
My, oh, my, what a wonderful day Plenty of sunshine headin' my way
Zip-a-dee-doo-dah, zip-a-dee-ay!""",
    "I wonder what Meng Shen has got cooking in the kitchen today?"]


custodian.add_phrase("look at custodian",Say(custodian.description))
custodian.add_phrase("look custodian",Say(custodian.description))
custodian.add_phrase("look boy",Say(custodian.description))
custodian.set_allowed_locations([innercourtyard])
custodian.add_verb(SayOnSelf("The custodian bounces away.", "pet"))
custodian.add_verb(SayOnSelf("It is just too fast for you and flees.", "kill"))
custodian.add_verb(SayOnSelf("It is just too fast for you.", "attack"))
custodian.add_phrase("talk custodian",Say("""The custodian leans in and whispers to you:
"Make note of the letters at the end of the quotes, if the quote is one of the chosen, you will need the letter, and use it in the right order!\"
"""))
custodian.set_location(innercourtyard)

# #####################################
# Actor - Jesus
# #####################################

jesus = Animal("Jesus")
jesus.description = "J.C. looks like he is just taking a breather on the bench."
jesus.talkativeness = 0.8
jesus.set_allowed_locations([laozitwo])
jesus.randomphrases = ["""The wind blows wherever it pleases.
You hear its sound, but you cannot tell
where it comes from or where it is going.
So it is with everyone born of the Spirit""",
    """Consider the lilies of the field, how they grow;
they neither toil nor spin.""",
    """If anyone strikes you on the cheek, offer the other also;
and from anyone who takes away your coat do not withhold even your shirt.""",
    """Glad there are no fig trees here.
I just really don't like fig trees.
Maybe it's the smell?""",
"""I say,'Do to others as you would have them do to you,' and Confucius says,
'Do not impose upon others what you yourself do not desire.' I wonder if these
mean the same thing?"""]
jesus.set_location(laozitwo)
jesus.add_phrase("look at jesus",Say(monkey.description))
jesus.add_phrase("look jesus",Say(monkey.description))
reply = """Jesus smiles at you and says, "You know these
Daoists make a lot of sense and we seem to agree
on quite a bit, but I've been trying out some new
parables on them about good and evil and they don't
seem to like them much. Mengzi, on the other hand,
really liked my new mustard seed parable. He seems
to like agriculture metaphors. Confucius also
seems to have a version of the Golden Rule."
"""
jesus.add_phrase("talk jesus",Say(reply))
jesus.add_phrase("talk Jesus",Say(reply))

# #####################################
# Actor - Tomb Demon
# #####################################

def give_smoothie(game,thing):
  """Gives a smoothie to the guardian.

If the smoothie contains 3 kinds of berries or fruit, it will allow the player to pass through to the machine room"""
  if not "smoothie" in game.player.inventory:
    game.output("You do not currently have a smoothie to give away.",DESCRIPTION)
  else:
    givensmoothie=game.player.inventory.pop('smoothie', None)
    if givensmoothie.var('berrycount')<3:
      game.output("""
The guardian demon gratefully takes the smoothie and drinks it down, saying,
"Delicious, my thanks. I like them even more when they have more different kinds of fruit or berries!"
""",FEEDBACK)
    else:
      game.output("""
The guardian demon gratefully takes the smoothie and drinks it down, saying,
"That was one truly amazing berry smoothie, with all my favorite flavors!
In thanks to you, I will allow you to pass north into the machine room
whenever you like."
""",FEEDBACK)
      game.player.location.unset_flag('guarded')
      time.sleep(1)
      game.output("The guardian steps to the side and the way north through the archway is now clear!",DESCRIPTION)


    # berrycount+=1

tombdemon = Animal("tomb demon")
tombdemon.set_location(guardroom)
tombdemon.set_allowed_locations([guardroom])
tombdemon.add_phrase("attack tomb-demon",
                Die("""impaled on the sharp antlers of the demon as you launch yourself
in a desperate attack against it."""))
tombdemon.add_phrase("attack statue",
                Die("""impaled on the sharp antlers of the demon as you launch yourself
in a desperate attack against it."""))
tombdemon.add_phrase("attack tomb demon",
                Die("""impaled on the sharp antlers of the demon as you launch yourself
in a desperate attack against it."""))
tombdemon.add_phrase("attack demon",
                Die("""impaled on the sharp antlers of the demon as you launch yourself
in a desperate attack against it."""))
tombdemon.add_phrase("talk tomb demon",Say("""
The tomb demon says, "I am the guardian of the machine. I'm afraid I can't let you pass."""))
tombdemon.add_phrase("talk demon",Say("""
The tomb demon says, "I am the guardian of the machine. I'm afraid I can't let you pass."""))
tombdemon.add_phrase("talk statue",Say("""
The tomb demon says, "I am the guardian of the machine. I'm afraid I can't let you pass."""))
tombdemon.description = """The tomb demon is a large statue that looks like it is
made out of wood. It looks like a pillar, at the top of which is a demonic
looking face. Its fiery eyes are alive and follow your movements. Above its
head, two deer-like antlers extend and loom over you. It is positioned in such
a way that you cannot pass north without coming in range of its large antlers,
should the statue move. It looks a little hungry.
"""
tombdemon.add_phrase("give smoothie demon",give_smoothie)
tombdemon.add_phrase("give smoothie statue",give_smoothie)
tombdemon.add_phrase("give smoothie tomb demon",give_smoothie)
tombdemon.add_phrase("give smoothie guardian",give_smoothie)
tombdemon.add_phrase("give demon smoothie",give_smoothie)
tombdemon.add_phrase("give statue smoothie",give_smoothie)
tombdemon.add_phrase("give tomb demon smoothie",give_smoothie)
tombdemon.add_phrase("give guardian smoothie",give_smoothie)
tombdemon.add_phrase("look at demon",Say(monkey.description))
tombdemon.add_phrase("look at tomb demon",Say(tombdemon.description))
tombdemon.add_phrase("look tomb demon",Say(tombdemon.description))
tombdemon.add_phrase("look demon",Say(tombdemon.description))
tombdemon.add_phrase("look guardian",Say(tombdemon.description))
tombdemon.add_phrase("look statue",Say(tombdemon.description))

# #### ADD ACTORS


game.add_actor(custodian)
game.add_actor(jesus)
game.add_actor(squirrel)
game.add_actor(banzhao)
game.add_actor(cook)
game.add_actor(tombdemon)
game.add_actor(huizi)
game.add_actor(monkey)
game.add_actor(tortoise)
game.add_actor(frog)
game.add_actor(teacher)
game.add_actor(farmer)
game.add_actor(examiner)
game.add_actor(mozi)
game.add_actor(mengzi)
game.add_actor(kongzi)
game.add_actor(zhuangzi)
game.add_actor(laozi)
game.add_actor(mom)

def say(self,actor, noun, words):
  if not words:
    words = noun
  else:
    words = noun.title() + ' ' + ' '.join(words)
  self.game.output('You say, "' + words + '"', CONTENTS)
  if words in self.location.sentences:
    self.game.output(self.location.sentences[words],FEEDBACK)
  return True


def update():
  if (game.entering_location(machineroom)):
    list_dials(game,'test')
  elif  (game.entering_location(zhuangzifour)):
    if (game.inventory_contains([feather])):
      game.output("Your feather suddenly feels warm in your pocket.")
  if game.player.location == monkey.location:
    monkey_steal(game,'test')


# Start playing.
game.run(update)
