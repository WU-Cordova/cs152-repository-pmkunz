from enum import Enum
from CharacterType import CharacterType

class CharacterType (Enum ) :
    WARRIOR = "Warrior"
    MAGE = "Mage"
    ROGUE = "Rogue"

# Instantiating an Enum member
my_character_type = CharacterType.WARRIOR

# Accessing name and value
print(my_character_type)           # Output: CharacterType.WARRIOR
print(my_character_type.name)      # Output: "WARRIOR"
print(my_character_type.value)     # Output: "Warrior"