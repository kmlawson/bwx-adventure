office_door.set_flag('locked')
def pick_lock(game, thing):
  game.output("you slip the hairpin into the lock and skillfully pick it open")
  thing.unset_flag('locked')
office_door.add_phrase('pick lock', pick_lock, [hairpin])
key.add_phrase("rub key", Say("You rub the key, but fail to shine it."))

def flip_coin(game, thing):
  if not "coin" in game.player.inventory:
    game.output("The coin is on the ground!")
    return
  if random.random() > 0.5:
    game.output("The coin shows heads.");
  else:
    game.output("The coin shows tails.");

player.add_phrase("flip coin", flip_coin, [coin])

# ANIMALS:

bat = Animal("bat")
bat.set_location(office)

# custom verbs available when the bat is present.
# SayOnSelf triggers when the bat is the noun, for example: "swat bat"
bat.add_verb(SayOnSelf("The bat flaps frantically up out of your reach.", "swat"))

# we can also restrict the movement of any actor using set_allowed_locations.
# the following line will prevent the bat from going anywhere besides the
# office and the vestibule:
bat.set_allowed_locations([office, vestibule])



# command the cat and have an object appear
def cat_bark(self, actor, noun, words):
  actor.location.add_object(Object("hairball", "gooey hairball"))
  actor.output("The cat barks and coughs and something splats on the floor.")
  return True
cat.add_verb(Verb(cat_bark, 'bark'))

# custom phrases available when the cat is present.
# for example: "hi cat"
cat.add_phrase("hi cat", Say("The cat looks at you disinterestedly."))


# FOOD:

office.add_object(Food("donut",
                       "a chocolate covered donut with pink sprinkles",
                       Say("yummy!")))


file_cabinet = office.add_object(Container("file cabinet",
                                           "a rusty old metal file cabinet"))
file_cabinet.new_object("secret plan",
"""secret plans to convert Brightworks into a
military academy for cyber-warfare specialists""")
file_cabinet.make_requirement(key)

keys = Object("keys", "a rusty old ring of skeleton keys")
monkey.add_to_inventory(keys)
banana = Food("banana", "a nice ripe banana",
              Say("mmmmm, banana!"),
              Object("banana peel", "a very slippery banana peel"))
sidewalk.add_object(banana)
monkey.add_trade(banana, keys,
                 Say("The monkey takes the banana and drops a set of keys"))
monkey.add_trade(keys, banana,
                 Say("The monkey takes the keys and drops a banana"))


sidewalk.add_object(Drink("vial",
                          "a small vial of dark sinister looking liquid",
                          Die("choking violently and collapsing onto the floor..."),
                          Object("empty vial", "an empty vial with an acrid odor")))

bear = Animal("sleeping bear")
bear.set_location(vestibule)
bear.set_allowed_locations([vestibule])
game.add_actor(bear)
bear.add_phrase("wake bear",
                Die("mauled viciously by the angry bear who then falls back asleep."))

dragon = Actor("tiny dragon")
dragon.set_location(office)
game.add_actor(dragon)
shield = vestibule.new_object("shield", "a shiny bronze sheild")
sword = office.new_object("sword", "a rusty old sword")
def fight_dragon(game, thing):
  if not "shield" in game.player.inventory:
    game.output("You try to stab the dragon with the sword, but it flames you.")
    player.terminate()
  else:
    game.output("Using the shield to avoid the dragon's flames you kill it with the sword.")
    dragon.terminate()
dragon.add_phrase("fight dragon", fight_dragon)


def scream(self, actor, noun, words):
  all_words = [noun] + words
  print "You hear a scream '%s'." % ' '.join(all_words)
  return True

sidewalk.add_verb(Verb(scream, 'scream'))

def throw(self, actor, noun, words):
  if noun and actor.get_verb('drop').act(actor, noun, words):
     print 'The %s bounces and falls to the floor' % noun
     return True
  else:
     print 'You hurt your arm.'
     return False

hero.add_verb(Verb(throw, 'throw'))


def update():
  if (game.entering_location(reception)):
    if (game.inventory_contains([pebble])):
      game.output("The pebble you picked up is suddenly feeling warm to the touch!")
