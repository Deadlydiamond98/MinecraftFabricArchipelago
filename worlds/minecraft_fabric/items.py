from dataclasses import dataclass
from BaseClasses import ItemClassification

@dataclass
class MCItem:
    name: str
    item_type: ItemClassification
    item_id: int

@dataclass
class MCItemPart:
    items: list[MCItem]
    last_index: int

# Items that can be added ##############################################################################################

progression = [
    "Apple"
]

useful_index = len(progression) - 1

useful = [
    "5 Experience",
    "10 Experience",
    "1 Experience Level",
    "2 Experience Levels",
    "5 Experience Levels",
    "4 Emeralds",
    "8 Emeralds",
    "Rotten Flesh",
    "1 Arrow",
    "8 Arrows",
    "16 Arrows",
    "32 Arrows"
]

traps_index = len(useful) + useful_index

traps = [
    "Reverse Controls Trap",
    "Inverted Mouse Trap",
    "Ice Trap",
    "Random Status Trap",
    "Stun Trap",
    "TNT Trap",
    "Teleport Trap",
    "Bee Trap",
    "Literature Trap"
]

end_index = len(traps) + traps_index

# Helper methods #######################################################################################################

# initializes the item table
def get_item_table():
    items = []

    progression_part = get_items_part(ItemClassification.progression, 0, progression)
    items += progression_part.items
    useful_part = get_items_part(ItemClassification.useful, len(items), useful)
    items += useful_part.items
    traps_part = get_items_part(ItemClassification.trap, len(items), traps)
    items += traps_part.items

    return items

# This returns an MCItemPart, which is a list of items and an index for the next list's item ids
def get_items_part(item_type: ItemClassification, new_index: int, names: list[str]):
    return MCItemPart([MCItem(name, item_type, index + new_index + 1) for index, name in enumerate(names)], new_index + len(names))


item_table: list[MCItem] = get_item_table()
