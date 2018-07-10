def game():
    #↓ This is the Character "Super" Class
    class Character(object):
        def __init__(self, health, active, inactive):
            #↓ Keeps track of character's health
            self.health = health
            #↓ Current active character "flag"
            #↓ Keeps track of active character
            #↓ Only one character can be active @ any given time
            self.active = active
            #↓ Inactive / Benched character "flag"
            #↓ Keeps track of benched characters
            #↓ Benched characters regenerate health 3x faster
            self.inactive = inactive
        #↓ Regenerate 1/100 health per second for active character 
        def regenerate_health_active(self):
        #↓ Regenerate 3/100 health per second for inactive / benched characters
        def regenerate_health_inactive(self):
    #↓ Animal sub class
    class Animal(Character):
    #↓ Humanoid sub class
    class Humanoid(Character):
    #↓ Robot sub class
    class Robot(Character):