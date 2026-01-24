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
    "Ruby",
    "Swim",
    "Sprint",
    "Jump",
    "Chests & Barrels",
    "Progressive Tools",
    "Progressive Weapons",
    "Progressive Smelting",
    "Progressive Armor",
    "Progressive Archery"
]

bl_progression_index = len(progression) - 1

bl_progression = [
    # Ability
    "Sleeping",
    "Wither Summoning",
    "Villager Trading",
    "Piglin Bartering",
    # Station
    "Brewing",
    "Enchanting",
    "Smithing",
    "Other Crafting Stations",
    # Recipe
    "Bucket Recipes",
    "Flint and Steel Recipes",
    "Minecart Recipes",
    "Brush Recipes",
    "Spyglass Recipes",
    "Shear Recipes",
    "Eye of Ender Recipes",
    "Fishing Rod Recipes",
    "Glass Bottle Recipes",
    "Resource Compacting Recipes",
    "Shield Recipes"
]

useful_index = len(bl_progression) + bl_progression_index

useful = [
    # Materials
    "4 Emeralds",
    "8 Emeralds",
    "Netherite Scrap",
    "Redstone Dust",
    "Lapis Lazuli",
    "Ender Pearls",

    # ENCHANTS
    "Looting III",
    "Sharpness III",
    "Silk Touch",
    "Channeling",
    "Piercing IV",
    "Unbreaking I",
    "Unbreaking II",
    "Unbreaking III",

    # POTIONS
    "Potion of Fire Resistance",
    "Potion of Swiftness",
    "Potion of Luck",
    "Potion of Healing",
    "Strong Potion of Healing",

    # Ore
    "Iron Ore Vein",
    "Gold Ore Vein",
    "Diamond Ore Vein",
    "Emerald Ore Vein",

    "Large Iron Ore Vein",
    "Large Gold Ore Vein",
    "Large Diamond Ore Vein",
    "Large Emerald Ore Vein",

    # Misc
    "Saddle"
]

filler_index = len(useful) + useful_index

filler = [
    # Experience
    "5 Experience",
    "10 Experience",
    "1 Experience Level",
    "2 Experience Levels",
    "5 Experience Levels",
    # Arrows
    "1 Arrow",
    "8 Arrows",
    "16 Arrows",
    "32 Arrows",
    # Blocks
    "Wooden Planks",
    "Stone",
    "Andesite",
    "Diorite",
    "Granite",
    # Ore
    "Coal Ore Vein",
    "Large Coal Ore Vein",

    # Foods
    "Apples",
    "Golden Carrots",
    "Baked Potatos",
    "Cookies",

    "Steak",
    "Porkchops",
    "Chicken",
    "Mutton",

    "Rotten Flesh",
    "Tropical Fish",
    "Pufferfish",
    "Poisonous Potato",
    "Suspicious Stew",
    # MISC
    "Random Dye",
    "Strong Potion of Harming"
]

traps_index = len(filler) + filler_index

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
    bl_progression_part = get_items_part(ItemClassification.progression, len(items), bl_progression)
    items += bl_progression_part.items
    useful_part = get_items_part(ItemClassification.useful, len(items), useful)
    items += useful_part.items
    filler_part = get_items_part(ItemClassification.filler, len(items), filler)
    items += filler_part.items
    traps_part = get_items_part(ItemClassification.trap, len(items), traps)
    items += traps_part.items
    return items

# This returns an MCItemPart, which is a list of items and an index for the next list's item ids
def get_items_part(item_type: ItemClassification, new_index: int, names: list[str]):
    return MCItemPart([MCItem(name, item_type, index + new_index + 1) for index, name in enumerate(names)], new_index + len(names))


item_table: list[MCItem] = get_item_table()
