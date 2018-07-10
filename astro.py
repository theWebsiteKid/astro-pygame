import time

def game():
    #↓ Character superclass
    class Character(object):
        def __init__(self, health, active, inactive):
            #↓ Keeps track of characters' health
            self.health = health
            #↓ Current active character "flag"
            #↓ Keeps track of active character
            #↓ Only one character can be active @ any given time
            self.active = active
            #↓ Inactive / Benched character "flag"
            #↓ Keeps track of benched characters
            #↓ Benched characters regenerate health 3x faster
            self.inactive = inactive
        #↓ Game clock, tracks passing time in seconds
        def game_clock(seconds):
            start = time.time()
            elapsed = 0
            while elapsed < seconds:
                elapsed = time.time() - start
                print "seconds count: %02d" % (elapsed)
                time.sleep(1)
            print "game_clock finished!"
        #↓ Regeneration clock, tracks passing time in seconds
        def regeneration_clock(seconds):
            start = time.time()
            elapsed = 0
            while elapsed < seconds:
                elapsed = time.time() - start
                print "seconds count: %02d" % (elapsed)
                time.sleep(1)
            print "regeneration_clock finished!"
        #↓ Regenerate 1/100 health per second for active character 
        def regenerate_health_active(self):
            if self.active is True:
                self.health += (1 every second)
            else:
                pass
        #↓ Regenerate 3/100 health per second for inactive / benched characters
        def regenerate_health_inactive(self):
            if self.inactive is True:
                self.health += (3 every second)
            else:
                pass
    #↓ Animal character subclass
    class Animal(Character):
    #↓ Human character subclass
    class Human(Character):
    #↓ Robot character subclass
    class Robot(Character):