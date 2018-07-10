# Key mapping for character swap
KEY_Z = 122
KEY_X = 120
KEY_C = 99

# Key mapping for special moves
KEY_SPACE = 32

# Character superclass
class Character(object):
    def __init__(self, health, active, inactive):
        # Keeps track of characters' health
        self.health = health
        # Current active character "flag"
        # Keeps track of active character
        # Only one character can be active @ any given time
        self.active = active
        # Inactive / Benched character "flag"
        # Keeps track of benched characters
        # Benched characters regenerate health 3x faster
        self.inactive = inactive
    # Regenerate 1/100 health per second for active character 
    def regenerate_health_active(self):
        if self.active is True:
            self.health += (1)
        else:
            pass
    # Regenerate 3/100 health per second for inactive / benched characters
    def regenerate_health_inactive(self):
        if self.inactive is True:
            self.health += (3)
        else:
            pass
# Animal character subclass
class Animal(Character):
# Human character subclass
class Human(Character):
# Robot character subclass
class Robot(Character):