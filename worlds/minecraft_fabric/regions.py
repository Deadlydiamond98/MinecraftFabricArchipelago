from __future__ import annotations


from typing import TYPE_CHECKING, Optional


from worlds.minecraft_fabric.vanilla_logic import *


if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


from BaseClasses import Region, Location, CollectionState, Entrance
from worlds.minecraft_fabric.locations import location_table




########################################################################################################################
# Create Regions #######################################################################################################
########################################################################################################################


def get_goal_condition(world, state):
   goal_id = world.options.goal_condition.value

   # I wish Python had Switch Case Statements :,(
   if goal_id == 0: # Ender Dragon
       return canGoalEnderDragon(world, state)
   elif goal_id == 1: # Wither
       return canGoalWither(world, state)
   elif goal_id == 2: # Both Bosses
       return canBeatDragonAndWither(world, state)
   elif goal_id == 4: # Ruby Hunt
       return canCompleteRubyHunt(world, state)


   # Since Advancements are Locations, just make game try to reach end of game
   return canAccessVanillaEndGame(world, state)


def create_regions(world: FabricMinecraftWorld):
   # Menu Region (always available)
   create_locations_advanced(world, "Menu", {
       "Stone Age": 0,
       "Voluntary Exile": 0,
       "Monster Hunter": 0,
       "The Parrots and the Bats": 0,
       "You've Got a Friend in Me": 0,
       "Best Friends Forever": 0,
       "A Seedy Place": 0,
       "Hero of the Village": 0,
       "Postmortal": 2,
       "Getting Wood": 0,
       "Benchmarking": 0,
       "Time to Mine!": 0,
       "Time to Farm!": 0,
       "Bake Bread": 0,
       "Time to Strike!": 0,
       "Cow Tipper": 0,
       "When the Squad Hops into Town": 1,
       "Whatever Floats Your Goat!": 2,
       "Sneak 100": 2,
       "It Spreads": 2,


       "Dirt (Itemsanity)": 5,
       "Coarse Dirt (Itemsanity)": 5,
       "Podzol (Itemsanity)": 5,
       "Rooted Dirt (Itemsanity)": 5,
       "Mud (Itemsanity)": 5,
       "Oak Planks (Itemsanity)": 5,
       "Spruce Planks (Itemsanity)": 5,
       "Birch Planks (Itemsanity)": 5,
       "Jungle Planks (Itemsanity)": 5,
       "Acacia Planks (Itemsanity)": 5,
       "Cherry Planks (Itemsanity)": 5,
       "Dark Oak Planks (Itemsanity)": 5,
       "Mangrove Planks (Itemsanity)": 5,
       "Bamboo Planks (Itemsanity)": 5,
       "Bamboo Mosaic (Itemsanity)": 5,
       "Oak Sapling (Itemsanity)": 5,
       "Spruce Sapling (Itemsanity)": 5,
       "Birch Sapling (Itemsanity)": 5,
       "Jungle Sapling (Itemsanity)": 5,
       "Acacia Sapling (Itemsanity)": 5,
       "Cherry Sapling (Itemsanity)": 5,
       "Dark Oak Sapling (Itemsanity)": 5,
       "Mangrove Propagule (Itemsanity)": 5,
       "Sand (Itemsanity)": 5,
       "Red Sand (Itemsanity)": 5,
       "Gravel (Itemsanity)": 5,
       "Oak Log (Itemsanity)": 5,
       "Spruce Log (Itemsanity)": 5,
       "Birch Log (Itemsanity)": 5,
       "Jungle Log (Itemsanity)": 5,
       "Acacia Log (Itemsanity)": 5,
       "Cherry Log (Itemsanity)": 5,
       "Dark Oak Log (Itemsanity)": 5,
       "Mangrove Log (Itemsanity)": 5,
       "Mangrove Roots (Itemsanity)": 5,
       "Muddy Mangrove Roots (Itemsanity)": 5,
       "Block of Bamboo (Itemsanity)": 5,
       "Stripped Oak Log (Itemsanity)": 5,
       "Stripped Spruce Log (Itemsanity)": 5,
       "Stripped Birch Log (Itemsanity)": 5,
       "Stripped Jungle Log (Itemsanity)": 5,
       "Stripped Acacia Log (Itemsanity)": 5,
       "Stripped Cherry Log (Itemsanity)": 5,
       "Stripped Dark Oak Log (Itemsanity)": 5,
       "Stripped Mangrove Log (Itemsanity)": 5,
       "Stripped Oak Wood (Itemsanity)": 5,
       "Stripped Spruce Wood (Itemsanity)": 5,
       "Stripped Birch Wood (Itemsanity)": 5,
       "Stripped Jungle Wood (Itemsanity)": 5,
       "Stripped Acacia Wood (Itemsanity)": 5,
       "Stripped Cherry Wood (Itemsanity)": 5,
       "Stripped Dark Oak Wood (Itemsanity)": 5,
       "Stripped Mangrove Wood (Itemsanity)": 5,
       "Block of Stripped Bamboo (Itemsanity)": 5,
       "Oak Wood (Itemsanity)": 5,
       "Spruce Wood (Itemsanity)": 5,
       "Birch Wood (Itemsanity)": 5,
       "Jungle Wood (Itemsanity)": 5,
       "Acacia Wood (Itemsanity)": 5,
       "Cherry Wood (Itemsanity)": 5,
       "Dark Oak Wood (Itemsanity)": 5,
       "Mangrove Wood (Itemsanity)": 5,
       "Sandstone (Itemsanity)": 5,
       "Chiseled Sandstone (Itemsanity)": 5,
       "Cut Sandstone (Itemsanity)": 5,
       "White Wool (Itemsanity)": 5,
       "Orange Wool (Itemsanity)": 5,
       "Magenta Wool (Itemsanity)": 5,
       "Light Blue Wool (Itemsanity)": 5,
       "Yellow Wool (Itemsanity)": 5,
       "Lime Wool (Itemsanity)": 5,
       "Pink Wool (Itemsanity)": 5,
       "Gray Wool (Itemsanity)": 5,
       "Light Gray Wool (Itemsanity)": 5,
       "Cyan Wool (Itemsanity)": 5,
       "Purple Wool (Itemsanity)": 5,
       "Blue Wool (Itemsanity)": 5,
       "Brown Wool (Itemsanity)": 5,
       "Red Wool (Itemsanity)": 5,
       "Dandelion (Itemsanity)": 5,
       "Poppy (Itemsanity)": 5,
       "Blue Orchid (Itemsanity)": 5,
       "Allium (Itemsanity)": 5,
       "Azure Bluet (Itemsanity)": 5,
       "Red Tulip (Itemsanity)": 5,
       "Orange Tulip (Itemsanity)": 5,
       "White Tulip (Itemsanity)": 5,
       "Pink Tulip (Itemsanity)": 5,
       "Oxeye Daisy (Itemsanity)": 5,
       "Cornflower (Itemsanity)": 5,
       "Lily of the Valley (Itemsanity)": 5,
       "Brown Mushroom (Itemsanity)": 5,
       "Red Mushroom (Itemsanity)": 5,
       "Sugar Cane (Itemsanity)": 5,
       "Pink Petals (Itemsanity)": 5,
       "Bamboo (Itemsanity)": 5,
       "Oak Slab (Itemsanity)": 5,
       "Spruce Slab (Itemsanity)": 5,
       "Birch Slab (Itemsanity)": 5,
       "Jungle Slab (Itemsanity)": 5,
       "Acacia Slab (Itemsanity)": 5,
       "Cherry Slab (Itemsanity)": 5,
       "Dark Oak Slab (Itemsanity)": 5,
       "Mangrove Slab (Itemsanity)": 5,
       "Bamboo Slab (Itemsanity)": 5,
       "Bamboo Mosaic Slab (Itemsanity)": 5,
       "Mud Brick Slab (Itemsanity)": 5,
       "Red Sandstone Slab (Itemsanity)": 5,
       "Cut Red Sandstone Slab (Itemsanity)": 5,
       "Chiseled Bookshelf (Itemsanity)": 5,
       "Torch (Itemsanity)": 5,
       "Crafting Table (Itemsanity)": 5,
       "Ladder (Itemsanity)": 5,
       "Granite (Itemsanity)": 5,
       "Polished Granite (Itemsanity)": 5,
       "Diorite (Itemsanity)": 5,
       "Polished Diorite (Itemsanity)": 5,
       "Andesite (Itemsanity)": 5,
       "Polished Andesite (Itemsanity)": 5,
       "Deepslate (Itemsanity)": 5,
       "Cobbled Deepslate (Itemsanity)": 5,
       "Polished Deepslate (Itemsanity)": 5,
       "Calcite (Itemsanity)": 5,
       "Tuff (Itemsanity)": 5,
       "Dripstone Block (Itemsanity)": 5,
       "Cobblestone (Itemsanity)": 5,
       "Block of Amethyst (Itemsanity)": 5,
       "Moss Carpet (Itemsanity)": 5,
       "Moss Block (Itemsanity)": 5,
       "Big Dripleaf (Itemsanity)": 5,
       "Spore Blossom (Itemsanity)": 5,
       "Azalea (Itemsanity)": 5,
       "Flowering Azalea (Itemsanity)": 5,
       "Sandstone Slab (Itemsanity)": 5,
       "Cut Sandstone Slab (Itemsanity)": 5,
       "Cobblestone Slab (Itemsanity)": 5,
       "Cobblestone Stairs (Itemsanity)": 5,
       "Snow (Itemsanity)": 5,
       "Snow Block (Itemsanity)": 5,
       "Cactus (Itemsanity)": 5,
       "Clay (Itemsanity)": 5,
       "Oak Fence (Itemsanity)": 5,
       "Spruce Fence (Itemsanity)": 5,
       "Birch Fence (Itemsanity)": 5,
       "Jungle Fence (Itemsanity)": 5,
       "Acacia Fence (Itemsanity)": 5,
       "Cherry Fence (Itemsanity)": 5,
       "Dark Oak Fence (Itemsanity)": 5,
       "Mangrove Fence (Itemsanity)": 5,
       "Bamboo Fence (Itemsanity)": 5,
       "Pumpkin (Itemsanity)": 5,
       "Carved Pumpkin (Itemsanity)": 5,
       "Jack o'Lantern (Itemsanity)": 5,
       "Packed Mud (Itemsanity)": 5,
       "Mud Bricks (Itemsanity)": 5,
       "Deepslate Bricks (Itemsanity)": 5,
       "Cracked Deepslate Bricks (Itemsanity)": 5,
       "Deepslate Tiles (Itemsanity)": 5,
       "Cracked Deepslate Tiles (Itemsanity)": 5,
       "Chiseled Deepslate (Itemsanity)": 5,
       "Melon (Itemsanity)": 5,
       "Mud Brick Stairs (Itemsanity)": 5,
       "Lily Pad (Itemsanity)": 5,
       "Sandstone Stairs (Itemsanity)": 5,
       "Oak Stairs (Itemsanity)": 5,
       "Spruce Stairs (Itemsanity)": 5,
       "Birch Stairs (Itemsanity)": 5,
       "Jungle Stairs (Itemsanity)": 5,
       "Acacia Stairs (Itemsanity)": 5,
       "Cherry Stairs (Itemsanity)": 5,
       "Dark Oak Stairs (Itemsanity)": 5,
       "Mangrove Stairs (Itemsanity)": 5,
       "Bamboo Stairs (Itemsanity)": 5,
       "Bamboo Mosaic Stairs (Itemsanity)": 5,
       "Cobblestone Wall (Itemsanity)": 5,
       "Red Sandstone Wall (Itemsanity)": 5,
       "Granite Wall (Itemsanity)": 5,
       "Mud Brick Wall (Itemsanity)": 5,
       "Andesite Wall (Itemsanity)": 5,
       "Sandstone Wall (Itemsanity)": 5,
       "Diorite Wall (Itemsanity)": 5,
       "Cobbled Deepslate Wall (Itemsanity)": 5,
       "Polished Deepslate Wall (Itemsanity)": 5,
       "Deepslate Brick Wall (Itemsanity)": 5,
       "Deepslate Tile Wall (Itemsanity)": 5,
       "Hay Bale (Itemsanity)": 5,
       "White Carpet (Itemsanity)": 5,
       "Orange Carpet (Itemsanity)": 5,
       "Magenta Carpet (Itemsanity)": 5,
       "Light Blue Carpet (Itemsanity)": 5,
       "Yellow Carpet (Itemsanity)": 5,
       "Lime Carpet (Itemsanity)": 5,
       "Pink Carpet (Itemsanity)": 5,
       "Gray Carpet (Itemsanity)": 5,
       "Light Gray Carpet (Itemsanity)": 5,
       "Cyan Carpet (Itemsanity)": 5,
       "Purple Carpet (Itemsanity)": 5,
       "Blue Carpet (Itemsanity)": 5,
       "Brown Carpet (Itemsanity)": 5,
       "Red Carpet (Itemsanity)": 5,
       "Sunflower (Itemsanity)": 5,
       "Lilac (Itemsanity)": 5,
       "Rose Bush (Itemsanity)": 5,
       "Peony (Itemsanity)": 5,
       "Red Sandstone (Itemsanity)": 5,
       "Chiseled Red Sandstone (Itemsanity)": 5,
       "Cut Red Sandstone (Itemsanity)": 5,
       "Red Sandstone Stairs (Itemsanity)": 5,
       "Bone Block (Itemsanity)": 5,
       "White Concrete (Itemsanity)": 5,
       "Orange Concrete (Itemsanity)": 5,
       "Magenta Concrete (Itemsanity)": 5,
       "Light Blue Concrete (Itemsanity)": 5,
       "Yellow Concrete (Itemsanity)": 5,
       "Lime Concrete (Itemsanity)": 5,
       "Pink Concrete (Itemsanity)": 5,
       "Gray Concrete (Itemsanity)": 5,
       "Light Gray Concrete (Itemsanity)": 5,
       "Cyan Concrete (Itemsanity)": 5,
       "Purple Concrete (Itemsanity)": 5,
       "Blue Concrete (Itemsanity)": 5,
       "Brown Concrete (Itemsanity)": 5,
       "Red Concrete (Itemsanity)": 5,
       "White Concrete Powder (Itemsanity)": 5,
       "Orange Concrete Powder (Itemsanity)": 5,
       "Magenta Concrete Powder (Itemsanity)": 5,
       "Light Blue Concrete Powder (Itemsanity)": 5,
       "Yellow Concrete Powder (Itemsanity)": 5,
       "Lime Concrete Powder (Itemsanity)": 5,
       "Pink Concrete Powder (Itemsanity)": 5,
       "Gray Concrete Powder (Itemsanity)": 5,
       "Light Gray Concrete Powder (Itemsanity)": 5,
       "Cyan Concrete Powder (Itemsanity)": 5,
       "Purple Concrete Powder (Itemsanity)": 5,
       "Blue Concrete Powder (Itemsanity)": 5,
       "Brown Concrete Powder (Itemsanity)": 5,
       "Red Concrete Powder (Itemsanity)": 5,
       "Polished Granite Stairs (Itemsanity)": 5,
       "Polished Diorite Stairs (Itemsanity)": 5,
       "Granite Stairs (Itemsanity)": 5,
       "Andesite Stairs (Itemsanity)": 5,
       "Polished Andesite Stairs (Itemsanity)": 5,
       "Diorite Stairs (Itemsanity)": 5,
       "Cobbled Deepslate Stairs (Itemsanity)": 5,
       "Polished Deepslate Stairs (Itemsanity)": 5,
       "Deepslate Brick Stairs (Itemsanity)": 5,
       "Deepslate Tile Stairs (Itemsanity)": 5,
       "Polished Granite Slab (Itemsanity)": 5,
       "Polished Diorite Slab (Itemsanity)": 5,
       "Granite Slab (Itemsanity)": 5,
       "Andesite Slab (Itemsanity)": 5,
       "Polished Andesite Slab (Itemsanity)": 5,
       "Diorite Slab (Itemsanity)": 5,
       "Cobbled Deepslate Slab (Itemsanity)": 5,
       "Polished Deepslate Slab (Itemsanity)": 5,
       "Deepslate Brick Slab (Itemsanity)": 5,
       "Deepslate Tile Slab (Itemsanity)": 5,
       "Scaffolding (Itemsanity)": 5,
       "Lever (Itemsanity)": 5,
       "TNT (Itemsanity)": 5,
       "Oak Button (Itemsanity)": 5,
       "Spruce Button (Itemsanity)": 5,
       "Birch Button (Itemsanity)": 5,
       "Jungle Button (Itemsanity)": 5,
       "Acacia Button (Itemsanity)": 5,
       "Cherry Button (Itemsanity)": 5,
       "Dark Oak Button (Itemsanity)": 5,
       "Mangrove Button (Itemsanity)": 5,
       "Bamboo Button (Itemsanity)": 5,
       "Oak Pressure Plate (Itemsanity)": 5,
       "Spruce Pressure Plate (Itemsanity)": 5,
       "Birch Pressure Plate (Itemsanity)": 5,
       "Jungle Pressure Plate (Itemsanity)": 5,
       "Acacia Pressure Plate (Itemsanity)": 5,
       "Cherry Pressure Plate (Itemsanity)": 5,
       "Dark Oak Pressure Plate (Itemsanity)": 5,
       "Mangrove Pressure Plate (Itemsanity)": 5,
       "Bamboo Pressure Plate (Itemsanity)": 5,
       "Oak Door (Itemsanity)": 5,
       "Spruce Door (Itemsanity)": 5,
       "Birch Door (Itemsanity)": 5,
       "Jungle Door (Itemsanity)": 5,
       "Acacia Door (Itemsanity)": 5,
       "Cherry Door (Itemsanity)": 5,
       "Dark Oak Door (Itemsanity)": 5,
       "Mangrove Door (Itemsanity)": 5,
       "Bamboo Door (Itemsanity)": 5,
       "Oak Trapdoor (Itemsanity)": 5,
       "Spruce Trapdoor (Itemsanity)": 5,
       "Birch Trapdoor (Itemsanity)": 5,
       "Jungle Trapdoor (Itemsanity)": 5,
       "Acacia Trapdoor (Itemsanity)": 5,
       "Cherry Trapdoor (Itemsanity)": 5,
       "Dark Oak Trapdoor (Itemsanity)": 5,
       "Mangrove Trapdoor (Itemsanity)": 5,
       "Bamboo Trapdoor (Itemsanity)": 5,
       "Oak Fence Gate (Itemsanity)": 5,
       "Spruce Fence Gate (Itemsanity)": 5,
       "Birch Fence Gate (Itemsanity)": 5,
       "Jungle Fence Gate (Itemsanity)": 5,
       "Acacia Fence Gate (Itemsanity)": 5,
       "Cherry Fence Gate (Itemsanity)": 5,
       "Dark Oak Fence Gate (Itemsanity)": 5,
       "Mangrove Fence Gate (Itemsanity)": 5,
       "Bamboo Fence Gate (Itemsanity)": 5,
       "Oak Boat (Itemsanity)": 5,
       "Spruce Boat (Itemsanity)": 5,
       "Birch Boat (Itemsanity)": 5,
       "Jungle Boat (Itemsanity)": 5,
       "Acacia Boat (Itemsanity)": 5,
       "Cherry Boat (Itemsanity)": 5,
       "Dark Oak Boat (Itemsanity)": 5,
       "Mangrove Boat (Itemsanity)": 5,
       "Bamboo Raft (Itemsanity)": 5,
       "Apple (Itemsanity)": 5,
       "Arrow (Itemsanity)": 5,
       "Coal (Itemsanity)": 5,
       "Amethyst Shard (Itemsanity)": 5,
       "Wooden Sword (Itemsanity)": 5,
       "Wooden Shovel (Itemsanity)": 5,
       "Wooden Pickaxe (Itemsanity)": 5,
       "Wooden Axe (Itemsanity)": 5,
       "Wooden Hoe (Itemsanity)": 5,
       "Stick (Itemsanity)": 5,
       "Bowl (Itemsanity)": 5,
       "Mushroom Stew (Itemsanity)": 5,
       "String (Itemsanity)": 5,
       "Feather (Itemsanity)": 5,
       "Gunpowder (Itemsanity)": 5,
       "Wheat Seeds (Itemsanity)": 5,
       "Wheat (Itemsanity)": 5,
       "Bread (Itemsanity)": 5,
       "Flint (Itemsanity)": 5,
       "Raw Porkchop (Itemsanity)": 5,
       "Painting (Itemsanity)": 5,
       "Oak Sign (Itemsanity)": 5,
       "Spruce Sign (Itemsanity)": 5,
       "Birch Sign (Itemsanity)": 5,
       "Jungle Sign (Itemsanity)": 5,
       "Acacia Sign (Itemsanity)": 5,
       "Cherry Sign (Itemsanity)": 5,
       "Dark Oak Sign (Itemsanity)": 5,
       "Mangrove Sign (Itemsanity)": 5,
       "Bamboo Sign (Itemsanity)": 5,
       "Oak Hanging Sign (Itemsanity)": 5,
       "Spruce Hanging Sign (Itemsanity)": 5,
       "Birch Hanging Sign (Itemsanity)": 5,
       "Jungle Hanging Sign (Itemsanity)": 5,
       "Acacia Hanging Sign (Itemsanity)": 5,
       "Cherry Hanging Sign (Itemsanity)": 5,
       "Dark Oak Hanging Sign (Itemsanity)": 5,
       "Mangrove Hanging Sign (Itemsanity)": 5,
       "Bamboo Hanging Sign (Itemsanity)": 5,
       "Snowball (Itemsanity)": 5,
       "Leather (Itemsanity)": 5,
       "Paper (Itemsanity)": 5,
       "Book (Itemsanity)": 5,
       "Egg (Itemsanity)": 5,
       "Cocoa Beans (Itemsanity)": 5,
       "White Dye (Itemsanity)": 5,
       "Orange Dye (Itemsanity)": 5,
       "Magenta Dye (Itemsanity)": 5,
       "Light Blue Dye (Itemsanity)": 5,
       "Yellow Dye (Itemsanity)": 5,
       "Lime Dye (Itemsanity)": 5,
       "Pink Dye (Itemsanity)": 5,
       "Gray Dye (Itemsanity)": 5,
       "Light Gray Dye (Itemsanity)": 5,
       "Cyan Dye (Itemsanity)": 5,
       "Purple Dye (Itemsanity)": 5,
       "Blue Dye (Itemsanity)": 5,
       "Brown Dye (Itemsanity)": 5,
       "Red Dye (Itemsanity)": 5,
       "Bone Meal (Itemsanity)": 5,
       "Bone (Itemsanity)": 5,
       "Sugar (Itemsanity)": 5,
       "Cookie (Itemsanity)": 5,
       "Melon Slice (Itemsanity)": 5,
       "Pumpkin Seeds (Itemsanity)": 5,
       "Melon Seeds (Itemsanity)": 5,
       "Raw Beef (Itemsanity)": 5,
       "Raw Chicken (Itemsanity)": 5,
       "Rotten Flesh (Itemsanity)": 5,
       "Ender Pearl (Itemsanity)": 5,
       "Spider Eye (Itemsanity)": 5,
       "Fermented Spider Eye (Itemsanity)": 5,
       "Item Frame (Itemsanity)": 5,
       "Carrot (Itemsanity)": 5,
       "Potato (Itemsanity)": 5,
       "Poisonous Potato (Itemsanity)": 5,
       "Pumpkin Pie (Itemsanity)": 5,
       "Raw Rabbit (Itemsanity)": 5,
       "Rabbit's Foot (Itemsanity)": 5,
       "Rabbit Hide (Itemsanity)": 5,
       "Leather Horse Armor (Itemsanity)": 5,
       "Raw Mutton (Itemsanity)": 5,
       "White Banner (Itemsanity)": 5,
       "Orange Banner (Itemsanity)": 5,
       "Magenta Banner (Itemsanity)": 5,
       "Light Blue Banner (Itemsanity)": 5,
       "Yellow Banner (Itemsanity)": 5,
       "Lime Banner (Itemsanity)": 5,
       "Pink Banner (Itemsanity)": 5,
       "Gray Banner (Itemsanity)": 5,
       "Light Gray Banner (Itemsanity)": 5,
       "Cyan Banner (Itemsanity)": 5,
       "Purple Banner (Itemsanity)": 5,
       "Blue Banner (Itemsanity)": 5,
       "Brown Banner (Itemsanity)": 5,
       "Red Banner (Itemsanity)": 5,
       "Beetroot (Itemsanity)": 5,
       "Beetroot Seeds (Itemsanity)": 5,
       "Beetroot Soup (Itemsanity)": 5,
       "Phantom Membrane (Itemsanity)": 5,
       "Composter (Itemsanity)": 5,
       "Bell (Itemsanity)": 5,
       "Sweet Berries (Itemsanity)": 5,
       "Glow Berries (Itemsanity)": 5,
       "Pointed Dripstone (Itemsanity)": 5
   })


   # REQUIRES NETHER ACCESS
   create_locations_and_connect(world, "Menu", "NetherAccess", {
       "We Need to Go Deeper": 0,
       "Return to Sender": 0,
       "Those Were the Days": 0,
       "Subspace Bubble": 0,
       "A Terrible Fortress": 0,
       "Uneasy Alliance": 0,
       "Spooky Scary Skeleton": 0,
       "Into Fire": 0,
       "The Power of Books": 0,
       "With Our Powers Combined!": 1,
       "Hot Tourist Destinations": 2,


       "Crimson Planks (Itemsanity)": 5,
       "Warped Planks (Itemsanity)": 5,
       "Crimson Stem (Itemsanity)": 5,
       "Warped Stem (Itemsanity)": 5,
       "Stripped Crimson Stem (Itemsanity)": 5,
       "Stripped Warped Stem (Itemsanity)": 5,
       "Stripped Crimson Hyphae (Itemsanity)": 5,
       "Stripped Warped Hyphae (Itemsanity)": 5,
       "Crimson Hyphae (Itemsanity)": 5,
       "Warped Hyphae (Itemsanity)": 5,
       "Crimson Fungus (Itemsanity)": 5,
       "Warped Fungus (Itemsanity)": 5,
       "Crimson Roots (Itemsanity)": 5,
       "Warped Roots (Itemsanity)": 5,
       "Weeping Vines (Itemsanity)": 5,
       "Twisting Vines (Itemsanity)": 5,
       "Crimson Slab (Itemsanity)": 5,
       "Warped Slab (Itemsanity)": 5,
       "Quartz Slab (Itemsanity)": 5,
       "Crimson Fence (Itemsanity)": 5,
       "Warped Fence (Itemsanity)": 5,
       "Netherrack (Itemsanity)": 5,
       "Soul Sand (Itemsanity)": 5,
       "Soul Soil (Itemsanity)": 5,
       "Basalt (Itemsanity)": 5,
       "Polished Basalt (Itemsanity)": 5,
       "Soul Torch (Itemsanity)": 5,
       "Glowstone (Itemsanity)": 5,
       "Crimson Stairs (Itemsanity)": 5,
       "Warped Stairs (Itemsanity)": 5,
       "Blackstone Wall (Itemsanity)": 5,
       "Polished Blackstone Wall (Itemsanity)": 5,
       "Polished Blackstone Brick Wall (Itemsanity)": 5,
       "Chiseled Quartz Block (Itemsanity)": 5,
       "Block of Quartz (Itemsanity)": 5,
       "Quartz Bricks (Itemsanity)": 5,
       "Quartz Pillar (Itemsanity)": 5,
       "Quartz Stairs (Itemsanity)": 5,
       "Nether Wart Block (Itemsanity)": 5,
       "Warped Wart Block (Itemsanity)": 5,
       "Polished Blackstone Button (Itemsanity)": 5,
       "Crimson Button (Itemsanity)": 5,
       "Warped Button (Itemsanity)": 5,
       "Polished Blackstone Pressure Plate (Itemsanity)": 5,
       "Crimson Pressure Plate (Itemsanity)": 5,
       "Warped Pressure Plate (Itemsanity)": 5,
       "Crimson Door (Itemsanity)": 5,
       "Warped Door (Itemsanity)": 5,
       "Crimson Trapdoor (Itemsanity)": 5,
       "Warped Trapdoor (Itemsanity)": 5,
       "Crimson Fence Gate (Itemsanity)": 5,
       "Warped Fence Gate (Itemsanity)": 5,
       "Nether Quartz (Itemsanity)": 5,
       "Crimson Sign (Itemsanity)": 5,
       "Warped Sign (Itemsanity)": 5,
       "Crimson Hanging Sign (Itemsanity)": 5,
       "Warped Hanging Sign (Itemsanity)": 5,
       "Clay Ball (Itemsanity)": 5,
       "Glowstone Dust (Itemsanity)": 5,
       "Blaze Rod (Itemsanity)": 5,
       "Ghast Tear (Itemsanity)": 5,
       "Nether Wart (Itemsanity)": 5,
       "Blaze Powder (Itemsanity)": 5,
       "Magma Cream (Itemsanity)": 5,
       "Fire Charge (Itemsanity)": 5,
       "Spectral Arrow (Itemsanity)": 5,
       "Soul Campfire (Itemsanity)": 5,
       "Shroomlight (Itemsanity)": 5,
       "Blackstone (Itemsanity)": 5,
       "Blackstone Slab (Itemsanity)": 5,
       "Blackstone Stairs (Itemsanity)": 5,
       "Gilded Blackstone (Itemsanity)": 5,
       "Polished Blackstone (Itemsanity)": 5,
       "Polished Blackstone Slab (Itemsanity)": 5,
       "Polished Blackstone Stairs (Itemsanity)": 5,
       "Chiseled Polished Blackstone (Itemsanity)": 5,
       "Polished Blackstone Bricks (Itemsanity)": 5,
       "Polished Blackstone Brick Slab (Itemsanity)": 5,
       "Polished Blackstone Brick Stairs (Itemsanity)": 5
   }, lambda state: canAccessNether(world, state))


   # REQUIRES END ACCESS
   create_locations_and_connect(world, "NetherAccess", "EndAccess", {
       "Free the End": 0,
       "The Next Generation": 0,
       "Remote Getaway": 0,
       "The City at the End of the Game": 0,
       "Sky's the Limit": 0,
       "Great View From Up Here": 0,
       "Eye Spy": 0,
       "The End?": 0,


       "Dragon Egg (Itemsanity)": 5,
       "End Stone (Itemsanity)": 5,
       "End Stone Bricks (Itemsanity)": 5,
       "End Stone Brick Wall (Itemsanity)": 5,
       "End Stone Brick Stairs (Itemsanity)": 5,
       "End Stone Brick Slab (Itemsanity)": 5,
       "Elytra (Itemsanity)": 5,
       "Eye of Ender (Itemsanity)": 5,
       "End Crystal (Itemsanity)": 5,
       "Chorus Fruit (Itemsanity)": 5,
       "Shulker Shell (Itemsanity)": 5
   }, lambda state: canAccessEnd(world, state))


   # REQUIRES STONE TOOLS
   create_locations_and_connect(world, "Menu", "HasStoneTools", {
       "Getting an Upgrade": 0,


       "Lapis Lazuli (Itemsanity)": 5,
       "Raw Iron (Itemsanity)": 5,
       "Raw Copper (Itemsanity)": 5,
       "Stone Sword (Itemsanity)": 5,
       "Stone Shovel (Itemsanity)": 5,
       "Stone Pickaxe (Itemsanity)": 5,
       "Stone Axe (Itemsanity)": 5,
       "Stone Hoe (Itemsanity)": 5
   },  lambda state: canUseStoneTools(world, state))


   # REQUIRES LEATHER ARMOR
   create_locations_and_connect(world, "Menu", "HasLeatherArmor", {
       "Light as a Rabbit": 2,


       "Leather Cap (Itemsanity)": 5,
       "Leather Tunic (Itemsanity)": 5,
       "Leather Pants (Itemsanity)": 5,
       "Leather Boots (Itemsanity)": 5
   }, lambda state: canWearLeatherArmor(world, state))


   # REQUIRES SMELTING
   create_locations_and_connect(world, "HasStoneTools", "CanSmeltItems", {
       "Acquire Hardware": 0,
       "Hot Topic": 0,


       "Stone (Itemsanity)": 5,
       "Glass (Itemsanity)": 5,
       "Tinted Glass (Itemsanity)": 5,
       "Stone Slab (Itemsanity)": 5,
       "Smooth Stone Slab (Itemsanity)": 5,
       "Brick Slab (Itemsanity)": 5,
       "Stone Brick Slab (Itemsanity)": 5,
       "Bricks (Itemsanity)": 5,
       "Smooth Red Sandstone (Itemsanity)": 5,
       "Smooth Sandstone (Itemsanity)": 5,
       "Smooth Stone (Itemsanity)": 5,
       "Decorated Pot (Itemsanity)": 5,
       "Furnace (Itemsanity)": 5,
       "Stone Bricks (Itemsanity)": 5,
       "Cracked Stone Bricks (Itemsanity)": 5,
       "Chiseled Stone Bricks (Itemsanity)": 5,
       "Iron Bars (Itemsanity)": 5,
       "Chain (Itemsanity)": 5,
       "Glass Pane (Itemsanity)": 5,
       "Brick Stairs (Itemsanity)": 5,
       "Stone Brick Stairs (Itemsanity)": 5,
       "Smooth Basalt (Itemsanity)": 5,
       "Brick Wall (Itemsanity)": 5,
       "Stone Brick Wall (Itemsanity)": 5,
       "White Terracotta (Itemsanity)": 5,
       "Orange Terracotta (Itemsanity)": 5,
       "Magenta Terracotta (Itemsanity)": 5,
       "Light Blue Terracotta (Itemsanity)": 5,
       "Yellow Terracotta (Itemsanity)": 5,
       "Lime Terracotta (Itemsanity)": 5,
       "Pink Terracotta (Itemsanity)": 5,
       "Gray Terracotta (Itemsanity)": 5,
       "Light Gray Terracotta (Itemsanity)": 5,
       "Cyan Terracotta (Itemsanity)": 5,
       "Purple Terracotta (Itemsanity)": 5,
       "Blue Terracotta (Itemsanity)": 5,
       "Brown Terracotta (Itemsanity)": 5,
       "Green Terracotta (Itemsanity)": 5,
       "Red Terracotta (Itemsanity)": 5,
       "Terracotta (Itemsanity)": 5,
       "White Stained Glass (Itemsanity)": 5,
       "Orange Stained Glass (Itemsanity)": 5,
       "Magenta Stained Glass (Itemsanity)": 5,
       "Light Blue Stained Glass (Itemsanity)": 5,
       "Yellow Stained Glass (Itemsanity)": 5,
       "Lime Stained Glass (Itemsanity)": 5,
       "Pink Stained Glass (Itemsanity)": 5,
       "Gray Stained Glass (Itemsanity)": 5,
       "Light Gray Stained Glass (Itemsanity)": 5,
       "Cyan Stained Glass (Itemsanity)": 5,
       "Purple Stained Glass (Itemsanity)": 5,
       "Blue Stained Glass (Itemsanity)": 5,
       "Brown Stained Glass (Itemsanity)": 5,
       "Green Stained Glass (Itemsanity)": 5,
       "Red Stained Glass (Itemsanity)": 5,
       "White Stained Glass Pane (Itemsanity)": 5,
       "Orange Stained Glass Pane (Itemsanity)": 5,
       "Magenta Stained Glass Pane (Itemsanity)": 5,
       "Light Blue Stained Glass Pane (Itemsanity)": 5,
       "Yellow Stained Glass Pane (Itemsanity)": 5,
       "Lime Stained Glass Pane (Itemsanity)": 5,
       "Pink Stained Glass Pane (Itemsanity)": 5,
       "Gray Stained Glass Pane (Itemsanity)": 5,
       "Light Gray Stained Glass Pane (Itemsanity)": 5,
       "Cyan Stained Glass Pane (Itemsanity)": 5,
       "Purple Stained Glass Pane (Itemsanity)": 5,
       "Blue Stained Glass Pane (Itemsanity)": 5,
       "Brown Stained Glass Pane (Itemsanity)": 5,
       "Green Stained Glass Pane (Itemsanity)": 5,
       "Red Stained Glass Pane (Itemsanity)": 5,
       "White Glazed Terracotta (Itemsanity)": 5,
       "Orange Glazed Terracotta (Itemsanity)": 5,
       "Magenta Glazed Terracotta (Itemsanity)": 5,
       "Light Blue Glazed Terracotta (Itemsanity)": 5,
       "Yellow Glazed Terracotta (Itemsanity)": 5,
       "Lime Glazed Terracotta (Itemsanity)": 5,
       "Pink Glazed Terracotta (Itemsanity)": 5,
       "Gray Glazed Terracotta (Itemsanity)": 5,
       "Light Gray Glazed Terracotta (Itemsanity)": 5,
       "Cyan Glazed Terracotta (Itemsanity)": 5,
       "Purple Glazed Terracotta (Itemsanity)": 5,
       "Blue Glazed Terracotta (Itemsanity)": 5,
       "Brown Glazed Terracotta (Itemsanity)": 5,
       "Green Glazed Terracotta (Itemsanity)": 5,
       "Red Glazed Terracotta (Itemsanity)": 5,
       "Stone Stairs (Itemsanity)": 5,
       "Smooth Sandstone Stairs (Itemsanity)": 5,
       "Smooth Red Sandstone Stairs (Itemsanity)": 5,
       "Smooth Red Sandstone Slab (Itemsanity)": 5,
       "Smooth Sandstone Slab (Itemsanity)": 5,
       "Tripwire Hook (Itemsanity)": 5,
       "Stone Button (Itemsanity)": 5,
       "Stone Pressure Plate (Itemsanity)": 5,
       "Heavy Weighted Pressure Plate (Itemsanity)": 5,
       "Iron Door (Itemsanity)": 5,
       "Iron Trapdoor (Itemsanity)": 5,
       "Charcoal (Itemsanity)": 5,
       "Iron Ingot (Itemsanity)": 5,
       "Copper Ingot (Itemsanity)": 5,
       "Cooked Porkchop (Itemsanity)": 5,
       "Golden Apple (Itemsanity)": 5,
       "Brick (Itemsanity)": 5,
       "Steak (Itemsanity)": 5,
       "Cooked Chicken (Itemsanity)": 5,
       "Cauldron (Itemsanity)": 5,
       "Flower Pot (Itemsanity)": 5,
       "Baked Potato (Itemsanity)": 5,
       "Cooked Rabbit (Itemsanity)": 5,
       "Rabbit Stew (Itemsanity)": 5,
       "Armor Stand (Itemsanity)": 5,
       "Cooked Mutton (Itemsanity)": 5,
       "Smoker (Itemsanity)": 5,
       "Blast Furnace (Itemsanity)": 5,
       "Campfire (Itemsanity)": 5,
       "Green Wool (Itemsanity)": 5,
       "Green Carpet (Itemsanity)": 5,
       "Green Concrete (Itemsanity)": 5,
       "Green Concrete Powder (Itemsanity)": 5,
       "Green Banner (Itemsanity)": 5,
       "Green Dye (Itemsanity)": 5
   }, lambda state: canSmelt(world, state))




   # REQUIRES SHIELD
   create_locations_and_connect(world, "CanSmeltItems", "HasShield", {
       "Not Today, Thank You": 0,


       "Shield (Itemsanity)": 5
   }, lambda state: canUseShield(world, state))


   # REQUIRES IRON TOOLS
   create_locations_and_connect(world, "CanSmeltItems", "HasIronTools", {
       "Isn't It Iron Pick": 0,
       "Diamonds!": 0,
       "Sound of Music": 2,


       "Jukebox (Itemsanity)": 5,
       "Redstone Dust (Itemsanity)": 5,
       "Redstone Torch (Itemsanity)": 5,
       "Redstone Repeater (Itemsanity)": 5,
       "Piston (Itemsanity)": 5,
       "Dropper (Itemsanity)": 5,
       "Target (Itemsanity)": 5,
       "Lightning Rod (Itemsanity)": 5,
       "Note Block (Itemsanity)": 5,
       "Light Weighted Pressure Plate (Itemsanity)": 5,
       "Diamond (Itemsanity)": 5,
       "Emerald (Itemsanity)": 5,
       "Raw Gold (Itemsanity)": 5,
       "Gold Ingot (Itemsanity)": 5,
       "Golden Sword (Itemsanity)": 5,
       "Golden Shovel (Itemsanity)": 5,
       "Golden Pickaxe (Itemsanity)": 5,
       "Golden Axe (Itemsanity)": 5,
       "Golden Hoe (Itemsanity)": 5,
       "Iron Sword (Itemsanity)": 5,
       "Iron Shovel (Itemsanity)": 5,
       "Iron Pickaxe (Itemsanity)": 5,
       "Iron Axe (Itemsanity)": 5,
       "Iron Hoe (Itemsanity)": 5,
       "Compass (Itemsanity)": 5,
       "Clock (Itemsanity)": 5
   }, lambda state: canUseIronTools(world, state))


   # REQUIRES IRON ARMOR
   create_locations_and_connect(world, "CanSmeltItems", "HasIronArmor", {
       "Suit Up": 0,


       "Iron Helmet (Itemsanity)": 5,
       "Iron Chestplate (Itemsanity)": 5,
       "Iron Leggings (Itemsanity)": 5,
       "Iron Boots (Itemsanity)": 5
   }, lambda state: canWearIronArmor(world, state))


   # REQUIRES GOLD ARMOR
   create_locations_and_connect(world, "CanSmeltItems", "HasGoldArmor", {
       "Golden Helmet (Itemsanity)": 5,
       "Golden Chestplate (Itemsanity)": 5,
       "Golden Leggings (Itemsanity)": 5,
       "Golden Boots (Itemsanity)": 5
   }, lambda state: canWearGoldArmor(world, state))


   # REQUIRES DIAMOND TOOLS
   create_locations_and_connect(world, "HasIronTools", "HasDiamondTools", {
       "Ice Bucket Challenge": 0,
       "Obsidian (Itemsanity)": 5,


       "Diamond Sword (Itemsanity)": 5,
       "Diamond Shovel (Itemsanity)": 5,
       "Diamond Pickaxe (Itemsanity)": 5,
       "Diamond Axe (Itemsanity)": 5,
       "Diamond Hoe (Itemsanity)": 5
   }, lambda state: canUseDiamondTools(world, state))


   # REQUIRES DIAMOND ARMOR
   create_locations_and_connect(world, "HasIronTools", "HasDiamondArmor", {
       "Cover Me with Diamonds": 0,


       "Diamond Helmet (Itemsanity)": 5,
       "Diamond Chestplate (Itemsanity)": 5,
       "Diamond Leggings (Itemsanity)": 5,
       "Diamond Boots (Itemsanity)": 5
   }, lambda state: canWearDiamondArmor(world, state))


   # REQUIRES ARMOR TRIMS
   create_locations_and_connect(world, "CanSmeltItems", "CanSmithItems", {
       "Crafting a New Look": 0,


       "Smithing Table (Itemsanity)": 5
   }, lambda state: canGetAndUseArmorTrims(world, state))


   # REQUIRES NETHERITE TOOLS
   create_locations_and_connect(world, "CanSmithItems", "HasNetheriteTools", {
       "Serious Dedication": 1
   }, lambda state: canUseNetheriteTools(world, state))


   # REQUIRES NETHERITE TOOLS
   create_locations_and_connect(world, "CanSmithItems", "HasNetheriteArmor", {
       "Cover Me in Debris": 1
   }, lambda state: canWearNetheriteArmor(world, state))


   # REQUIRES BOW
   create_locations_and_connect(world, "Menu", "HasBow", {
       "Take Aim": 0,
       "Bullseye": 0,
       "Sniper Duel": 0,


       "Bow (Itemsanity)": 5
   }, lambda state: canUseBow(world, state))


   # REQUIRES CROSSBOW
   create_locations_and_connect(world, "CanSmeltItems", "HasCrossbow", {
       "Ol' Betsy": 0,
       "Who's the Pillager Now?": 0,
       "Arbalistic": 0,
       "Two Birds, One Arrow": 1,


       "Crossbow (Itemsanity)": 5
   }, lambda state: canUseCrossBow(world, state))


   # REQUIRES MINECART
   create_locations_and_connect(world, "CanSmeltItems", "HasMinecart", {
       "On A Rail": 0,


       "Rail (Itemsanity)": 5,
       "Minecart (Itemsanity)": 5,
       "Minecart with TNT (Itemsanity)": 5,
       "Minecart with Furnace (Itemsanity)": 5
   }, lambda state: canUseMinecart(world, state))


   # REQUIRES FISHING
   create_locations_and_connect(world, "Menu", "HasFishing", {
       "Fishy Business": 0,
       "A Complete Catalogue": 1,


       "Carrot on a Stick (Itemsanity)": 5,
       "Fishing Rod (Itemsanity)": 5
   }, lambda state: canUseFishingRod(world, state))


   # REQUIRES BRUSH
   create_locations_and_connect(world, "CanSmeltItems", "HasBrush", {
       "Respecting the Remnants": 0,
       "Careful Restoration": 0,


       "Brush (Itemsanity)": 5
   }, lambda state: canUseBrush(world, state))


   # REQUIRES FLINT AND STEEL
   create_locations_and_connect(world, "CanSmeltItems", "HasFlintAndSteel", {
       "Flint and Steel (Itemsanity)": 5
   }, lambda state: canUseFlintAndSteel(world, state))




   # REQUIRES CHESTS
   create_locations_and_connect(world, "Menu", "HasChests", {
       "When Pigs Fly": 0,
       "Overpowered": 2,


       "Chest (Itemsanity)": 5,
       "Saddle (Itemsanity)": 5,
       "Oak Boat with Chest (Itemsanity)": 5,
       "Spruce Boat with Chest (Itemsanity)": 5,
       "Birch Boat with Chest (Itemsanity)": 5,
       "Jungle Boat with Chest (Itemsanity)": 5,
       "Acacia Boat with Chest (Itemsanity)": 5,
       "Cherry Boat with Chest (Itemsanity)": 5,
       "Dark Oak Boat with Chest (Itemsanity)": 5,
       "Mangrove Boat with Chest (Itemsanity)": 5,
       "Bamboo Raft with Chest (Itemsanity)": 5,
       "Enchanted Golden Apple (Itemsanity)": 5,
       "Iron Horse Armor (Itemsanity)": 5,
       "Golden Horse Armor (Itemsanity)": 5,
       "Diamond Horse Armor (Itemsanity)": 5,
       "Name Tag (Itemsanity)": 5,
       "Barrel (Itemsanity)": 5
   }, lambda state: canAccessChests(world, state))


   # REQUIRES TRADING
   create_locations_and_connect(world, "Menu", "HasTrading", {
       "What a Deal!": 0,
       "Star Trader": 0
   }, lambda state: canTrade(world, state))


   # REQUIRES ENCHANTING
   create_locations_and_connect(world, "HasDiamondTools", "HasEnchanting", {
       "Enchanter": 0,
       "Librarian": 0,
       "Total Beelocation": 0,
       "Surge Protector": 1,


       "Grass Block (Itemsanity)": 5,
       "Coal Ore (Itemsanity)": 5,
       "Iron Ore (Itemsanity)": 5,
       "Deepslate Iron Ore (Itemsanity)": 5,
       "Copper Ore (Itemsanity)": 5,
       "Deepslate Copper Ore (Itemsanity)": 5,
       "Gold Ore (Itemsanity)": 5,
       "Deepslate Gold Ore (Itemsanity)": 5,
       "Redstone Ore (Itemsanity)": 5,
       "Deepslate Redstone Ore (Itemsanity)": 5,
       "Emerald Ore (Itemsanity)": 5,
       "Lapis Lazuli Ore (Itemsanity)": 5,
       "Deepslate Lapis Lazuli Ore (Itemsanity)": 5,
       "Deepslate Diamond Ore (Itemsanity)": 5,
       "Bookshelf (Itemsanity)": 5,
       "Ice (Itemsanity)": 5,
       "Brown Mushroom Block (Itemsanity)": 5,
       "Red Mushroom Block (Itemsanity)": 5,
       "Mushroom Stem (Itemsanity)": 5,
       "Sculk (Itemsanity)": 5,
       "Sculk Vein (Itemsanity)": 5,
       "Sculk Catalyst (Itemsanity)": 5,
       "Sculk Shrieker (Itemsanity)": 5,
       "Enchanting Table (Itemsanity)": 5,
       "Anvil (Itemsanity)": 5,
       "Chipped Anvil (Itemsanity)": 5,
       "Damaged Anvil (Itemsanity)": 5,
       "Packed Ice (Itemsanity)": 5,
       "Blue Ice (Itemsanity)": 5,
       "Lectern (Itemsanity)": 5,
       "Sculk Sensor (Itemsanity)": 5,
       "Calibrated Sculk Sensor (Itemsanity)": 5,
       "Bee Nest (Itemsanity)": 5,
       "Small Amethyst Bud (Itemsanity)": 5,
       "Medium Amethyst Bud (Itemsanity)": 5,
       "Large Amethyst Bud (Itemsanity)": 5,
       "Amethyst Cluster (Itemsanity)": 5
   }, lambda state: canEnchant(world, state))


   # REQUIRES BUCKET
   create_locations_and_connect(world, "CanSmeltItems", "HasBucket", {
       "Birthday Song": 0,
       "Hot Stuff": 0,
       "The Lie": 0,
       "Bukkit Bukkit": 2,


       "Bucket (Itemsanity)": 5,
       "Water Bucket (Itemsanity)": 5,
       "Lava Bucket (Itemsanity)": 5,
       "Milk Bucket (Itemsanity)": 5,
       "Cake (Itemsanity)": 5
   }, lambda state: canUseBucket(world, state))


   # REQUIRES BREWING
   create_locations_and_connect(world, "NetherAccess", "HasBrewing", {
       "Local Brewery": 0,
       "Zombie Doctor": 0,
       "A Furious Cocktail": 1,


       "Brewing Stand (Itemsanity)": 5
   }, lambda state: canBrew(world, state))


   # REQUIRES BARTERING
   create_locations_and_connect(world, "NetherAccess", "HasBartering", {
       "Oh Shiny": 0
   }, lambda state: canBarter(world, state))


   # REQUIRES SLEEP
   create_locations_and_connect(world, "Menu", "HasSleep", {
       "Sweet Dreams": 0,


       "White Bed (Itemsanity)": 5,
       "Orange Bed (Itemsanity)": 5,
       "Magenta Bed (Itemsanity)": 5,
       "Light Blue Bed (Itemsanity)": 5,
       "Yellow Bed (Itemsanity)": 5,
       "Lime Bed (Itemsanity)": 5,
       "Pink Bed (Itemsanity)": 5,
       "Gray Bed (Itemsanity)": 5,
       "Light Gray Bed (Itemsanity)": 5,
       "Cyan Bed (Itemsanity)": 5,
       "Purple Bed (Itemsanity)": 5,
       "Blue Bed (Itemsanity)": 5,
       "Brown Bed (Itemsanity)": 5,
       "Red Bed (Itemsanity)": 5
   }, lambda state: canSleep(world, state))


   # REQUIRES SPYGLASS
   create_locations_and_connect(world, "CanSmeltItems", "HasSpyglass", {
       "Is It a Bird?": 0,


       "Spyglass (Itemsanity)": 5
   }, lambda state: canUseSpyglass(world, state))


   # REQUIRES GLASS BOTTLES
   create_locations_and_connect(world, "CanSmeltItems", "HasBottles", {
       "Sticky Situation": 0,
       "Bee Our Guest": 0,


       "Honey Block (Itemsanity)": 5,
       "Glass Bottle (Itemsanity)": 5,
       "Honey Bottle (Itemsanity)": 5
   }, lambda state: canUseBottles(world, state))


   # REQUIRES SWIMMING
   create_locations_and_connect(world, "Menu", "HasSwim", {
       "A Throwaway Joke": 0,
       "Glow and Behold!": 0,
       "The Healing Power of Friendship!": 0,


       "Sea Pickle (Itemsanity)": 5,
       "Black Wool (Itemsanity)": 5,
       "Kelp (Itemsanity)": 5,
       "Black Carpet (Itemsanity)": 5,
       "Black Stained Glass (Itemsanity)": 5,
       "Black Stained Glass Pane (Itemsanity)": 5,
       "Black Concrete (Itemsanity)": 5,
       "Black Concrete Powder (Itemsanity)": 5,
       "Ink Sac (Itemsanity)": 5,
       "Glow Ink Sac (Itemsanity)": 5,
       "Black Dye (Itemsanity)": 5,
       "Book and Quill (Itemsanity)": 5,
       "Glow Item Frame (Itemsanity)": 5,
       "Black Banner (Itemsanity)": 5,
       "Trident (Itemsanity)": 5,
       "Nautilus Shell (Itemsanity)": 5
   }, lambda state: canSwim(world, state))


   # REQUIRES WITHER SUMMONING
   create_locations_and_connect(world, "NetherAccess", "CanSummonWither", {
       "Withering Heights": 0,


       "Wither Rose (Itemsanity)": 5,
       "Nether Star (Itemsanity)": 5
   }, lambda state: canGoalWither(world, state))


   # REQUIRES BEACON
   create_locations_and_connect(world, "CanSummonWither", "CanUseBeacon", {
       "Bring Home the Beacon": 0,
       "Beaconator": 1,


       "Beacon (Itemsanity)": 5
   }, lambda state: canPlaceBeacon(world, state))


   # REQUIRES CRYING OBSIDIAN
   create_locations_and_connect(world, "HasBartering", "CanGetCryingObsidian", {
       "Who is Cutting Onions?": 0,
       "Not Quite \"Nine\" Lives": 0,


       "Crying Obsidian (Itemsanity)": 5,
       "Respawn Anchor (Itemsanity)": 5
   }, lambda state: canGetCryingObsidian(world, state))


   # REQUIRES SHEARS
   create_locations_and_connect(world, "CanSmeltItems", "HasShears", {
       "Grass (Itemsanity)": 5,
       "Fern (Itemsanity)": 5,
       "Dead Bush (Itemsanity)": 5,
       "Small Dripleaf (Itemsanity)": 5,
       "Mossy Cobblestone (Itemsanity)": 5,
       "Mossy Stone Bricks (Itemsanity)": 5,
       "Vines (Itemsanity)": 5,
       "Glow Lichen (Itemsanity)": 5,
       "Mossy Cobblestone Wall (Itemsanity)": 5,
       "Mossy Stone Brick Wall (Itemsanity)": 5,
       "Mossy Stone Brick Stairs (Itemsanity)": 5,
       "Mossy Cobblestone Stairs (Itemsanity)": 5,
       "Mossy Stone Brick Slab (Itemsanity)": 5,
       "Mossy Cobblestone Slab (Itemsanity)": 5,
       "Shears (Itemsanity)": 5,
       "Honeycomb (Itemsanity)": 5,
       "Beehive (Itemsanity)": 5,
       "Honeycomb Block (Itemsanity)": 5,
       "Candle (Itemsanity)": 5,
       "White Candle (Itemsanity)": 5,
       "Orange Candle (Itemsanity)": 5,
       "Magenta Candle (Itemsanity)": 5,
       "Light Blue Candle (Itemsanity)": 5,
       "Yellow Candle (Itemsanity)": 5,
       "Lime Candle (Itemsanity)": 5,
       "Pink Candle (Itemsanity)": 5,
       "Gray Candle (Itemsanity)": 5,
       "Light Gray Candle (Itemsanity)": 5,
       "Cyan Candle (Itemsanity)": 5,
       "Purple Candle (Itemsanity)": 5,
       "Blue Candle (Itemsanity)": 5,
       "Brown Candle (Itemsanity)": 5,
       "Green Candle (Itemsanity)": 5,
       "Red Candle (Itemsanity)": 5
   }, lambda state: canUseShears(world, state))


   # REQUIRES SHEARS
   create_locations_and_connect(world, "CanSmeltItems", "CanCraftMiscStations", {
       "Loom (Itemsanity)": 5,
       "Cartography Table (Itemsanity)": 5,
       "Fletching Table (Itemsanity)": 5,
       "Grindstone (Itemsanity)": 5,
       "Stonecutter (Itemsanity)": 5
   }, lambda state: canAccessMiscJobsites(world, state))




   ####################################################################################################################
   # MULTIPLE CHECKS ##################################################################################################
   ####################################################################################################################


   # REQUIRES SWIMMING AND ENCHANTING
   create_locations_and_connect(world, "HasEnchanting", "HasSwimAndEnchanting", {
       "Very Very Frightening": 1,


       "Tube Coral Block (Itemsanity)": 5,
       "Brain Coral Block (Itemsanity)": 5,
       "Bubble Coral Block (Itemsanity)": 5,
       "Fire Coral Block (Itemsanity)": 5,
       "Horn Coral Block (Itemsanity)": 5,
       "Tube Coral (Itemsanity)": 5,
       "Brain Coral (Itemsanity)": 5,
       "Bubble Coral (Itemsanity)": 5,
       "Fire Coral (Itemsanity)": 5,
       "Horn Coral (Itemsanity)": 5,
       "Dead Brain Coral (Itemsanity)": 5,
       "Dead Bubble Coral (Itemsanity)": 5,
       "Dead Fire Coral (Itemsanity)": 5,
       "Dead Horn Coral (Itemsanity)": 5,
       "Dead Tube Coral (Itemsanity)": 5,
       "Tube Coral Fan (Itemsanity)": 5,
       "Brain Coral Fan (Itemsanity)": 5,
       "Bubble Coral Fan (Itemsanity)": 5,
       "Fire Coral Fan (Itemsanity)": 5,
       "Horn Coral Fan (Itemsanity)": 5,
       "Dead Tube Coral Fan (Itemsanity)": 5,
       "Dead Brain Coral Fan (Itemsanity)": 5,
       "Dead Bubble Coral Fan (Itemsanity)": 5,
       "Dead Fire Coral Fan (Itemsanity)": 5,
       "Dead Horn Coral Fan (Itemsanity)": 5
   }, lambda state: canSwim(world, state) and canEnchant(world, state))


   # REQUIRES SWIMMING AND BRUSH
   create_locations_and_connect(world, "HasBrush", "HasSwimAndBrush", {
       "Smells Interesting": 0,
       "Little Sniffs": 1,
       "Planting the Past": 1,
       "Sniffer Egg (Itemsanity)": 5
   }, lambda state: canSwim(world, state) and canUseBrush(world, state))


   # REQUIRES SWIMMING AND SHEARS
   create_locations_and_connect(world, "HasShears", "HasSwimAndShears", {
       "Seagrass (Itemsanity)": 5,
       "Black Candle (Itemsanity)": 5
   }, lambda state: canUseShears(world, state) and canSwim(world, state))


   # REQUIRES SWIMMING AND SMELTING
   create_locations_and_connect(world, "CanSmeltItems", "HasSwimAndSmelting", {
       "Black Terracotta (Itemsanity)": 5,
       "Black Glazed Terracotta (Itemsanity)": 5,
       "Dried Kelp Block (Itemsanity)": 5,
       "Dried Kelp (Itemsanity)": 5
   }, lambda state: canSmelt(world, state) and canSwim(world, state))


   # REQUIRES SWIMMING AND STONE TOOLS
   create_locations_and_connect(world, "HasStoneTools", "HasSwimAndStoneTools", {
       "Dead Tube Coral Block (Itemsanity)": 5,
       "Dead Brain Coral Block (Itemsanity)": 5,
       "Dead Bubble Coral Block (Itemsanity)": 5,
       "Dead Fire Coral Block (Itemsanity)": 5,
       "Dead Horn Coral Block (Itemsanity)": 5
   }, lambda state: canSmelt(world, state) and canSwim(world, state))


   # REQUIRES FISHING AND SMELTING
   create_locations_and_connect(world, "CanSmeltItems", "CanSmeltItemsAndHasFishing", {
       "Delicious Fish": 0
   }, lambda state: canSmelt(world, state) and canUseFishingRod(world, state))


   # REQUIRES NETHERITE NO SMITHING
   create_locations_and_connect(world, "HasDiamondTools", "NetheriteNoSmithing", {
       "Country Lode, Take Me Home": 0
   }, lambda state: canSmelt(world, state) and canAccessNether(world, state) and canUseDiamondTools(world, state))


   # REQUIRES SHEARS AND COMPACTING
   create_locations_and_connect(world, "CanSmeltItems", "HasShearsAndCompacting", {
       "Wax On": 0,
       "Wax Off": 0,


       "Waxed Block of Copper (Itemsanity)": 5,
       "Waxed Exposed Copper (Itemsanity)": 5,
       "Waxed Weathered Copper (Itemsanity)": 5,
       "Waxed Oxidized Copper (Itemsanity)": 5,
       "Waxed Cut Copper (Itemsanity)": 5,
       "Waxed Exposed Cut Copper (Itemsanity)": 5,
       "Waxed Weathered Cut Copper (Itemsanity)": 5,
       "Waxed Oxidized Cut Copper (Itemsanity)": 5,
       "Waxed Cut Copper Stairs (Itemsanity)": 5,
       "Waxed Exposed Cut Copper Stairs (Itemsanity)": 5,
       "Waxed Weathered Cut Copper Stairs (Itemsanity)": 5,
       "Waxed Oxidized Cut Copper Stairs (Itemsanity)": 5,
       "Waxed Cut Copper Slab (Itemsanity)": 5,
       "Waxed Exposed Cut Copper Slab (Itemsanity)": 5,
       "Waxed Weathered Cut Copper Slab (Itemsanity)": 5,
       "Waxed Oxidized Cut Copper Slab (Itemsanity)": 5
   }, lambda state: canUseShears(world, state) and canCompactResources(world, state))


   # REQUIRES BUCKET AND SWIM
   create_locations_and_connect(world, "HasBucket", "HasBucketAndSwim", {
       "Caves & Cliffs": 0,
       "Tactical Fishing": 0,
       "The Cutest Predator": 0,


       "Bucket of Pufferfish (Itemsanity)": 5,
       "Bucket of Salmon (Itemsanity)": 5,
       "Bucket of Cod (Itemsanity)": 5,
       "Bucket of Tropical Fish (Itemsanity)": 5,
       "Bucket of Axolotl (Itemsanity)": 5
   }, lambda state: canUseBucket(world, state) and canSwim(world, state))


   # REQUIRES SPYGLASS AND NETHER
   create_locations_and_connect(world, "HasSpyglass", "HasSpyglassNether", {
       "Is It a Balloon?": 0
   }, lambda state: canUseSpyglass(world, state) and canAccessNether(world, state))


   # REQUIRES SPYGLASS AND END
   create_locations_and_connect(world, "HasSpyglass", "HasSpyglassEnd", {
       "Is It a Plane?": 0
   }, lambda state: canUseSpyglass(world, state) and canAccessEnd(world, state))


   # REQUIRES COMPACTING AND SMELTING
   create_locations_and_connect(world, "CanSmeltItems", "CanSmeltAndCanCompact", {
       "Hired Help": 0,


       "Block of Iron (Itemsanity)": 5,
       "Block of Copper (Itemsanity)": 5,
       "Exposed Copper (Itemsanity)": 5,
       "Weathered Copper (Itemsanity)": 5,
       "Oxidized Copper (Itemsanity)": 5,
       "Cut Copper (Itemsanity)": 5,
       "Exposed Cut Copper (Itemsanity)": 5,
       "Weathered Cut Copper (Itemsanity)": 5,
       "Oxidized Cut Copper (Itemsanity)": 5,
       "Cut Copper Stairs (Itemsanity)": 5,
       "Exposed Cut Copper Stairs (Itemsanity)": 5,
       "Weathered Cut Copper Stairs (Itemsanity)": 5,
       "Oxidized Cut Copper Stairs (Itemsanity)": 5,
       "Cut Copper Slab (Itemsanity)": 5,
       "Exposed Cut Copper Slab (Itemsanity)": 5,
       "Weathered Cut Copper Slab (Itemsanity)": 5,
       "Oxidized Cut Copper Slab (Itemsanity)": 5,
       "Iron Nugget (Itemsanity)": 5,
       "Lantern (Itemsanity)": 5
   }, lambda state: canSmelt(world, state) and canCompactResources(world, state))


   # REQUIRES COMPACTING AND SMELTING AND NETHER
   create_locations_and_connect(world, "CanSmeltItems", "CanSmeltAndCanCompactAndNether", {
       "Soul Lantern (Itemsanity)": 5
   }, lambda state: canSmelt(world, state) and canCompactResources(world, state) and canAccessNether(world, state))


   # REQUIRES COMPACTING AND STONE TOOLS
   create_locations_and_connect(world, "HasStoneTools", "CanCompactAndStoneTools", {
       "Block of Coal (Itemsanity)": 5,
       "Block of Raw Iron (Itemsanity)": 5,
       "Block of Raw Copper (Itemsanity)": 5,
       "Block of Lapis Lazuli (Itemsanity)": 5
   }, lambda state: canCompactResources(world, state))


   # REQUIRES COMPACTING AND IRON TOOLS
   create_locations_and_connect(world, "HasIronTools", "CanCompactAndIronTools", {
       "Block of Raw Gold (Itemsanity)": 5,
       "Block of Diamond (Itemsanity)": 5,
       "Block of Emerald (Itemsanity)": 5,
       "Block of Redstone (Itemsanity)": 5
   }, lambda state: canCompactResources(world, state))


   # REQUIRES COMPACTING AND IRON TOOLS AND SMELTING
   create_locations_and_connect(world, "HasIronTools", "CanCompactAndIronToolsAndSmelting", {
       "Block of Gold (Itemsanity)": 5,
       "Gold Nugget (Itemsanity)": 5,
       "Glistering Melon Slice (Itemsanity)": 5,
       "Golden Carrot (Itemsanity)": 5
   }, lambda state: canCompactResources(world, state) and canSmelt(world, state) and canUseIronTools(world, state))


   # REQUIRES NETHER AND FISHING ROD
   create_locations_and_connect(world, "NetherAccess", "NetherAccessAndFishing", {
       "Warped Fungus on a Stick (Itemsanity)": 5
   }, lambda state: canAccessNether(world, state) and canUseFishingRod(world, state))


   # REQUIRES NETHER AND FISHING ROD AND CHESTS
   create_locations_and_connect(world, "NetherAccess", "NetherAccessAndFishingRodAndChests", {
       "This Boat Has Legs": 0,
       "Feels Like Home": 1
   }, lambda state: canAccessNether(world, state) and canUseFishingRod(world, state) and canAccessChests(world, state))


   # REQUIRES END AND SMELTING
   create_locations_and_connect(world, "EndAccess", "EndAccessAndSmelting", {
       "The End... Again...": 0,


       "Purpur Slab (Itemsanity)": 5,
       "Purpur Block (Itemsanity)": 5,
       "Purpur Pillar (Itemsanity)": 5,
       "Purpur Stairs (Itemsanity)": 5,
       "Popped Chorus Fruit (Itemsanity)": 5
   }, lambda state: canAccessEnd(world, state) and canSmelt(world, state))


   # REQUIRES END AND GLASS BOTTLES AND SMELTING
   create_locations_and_connect(world, "EndAccessAndSmelting", "EndAccessAndGlassBottles", {
       "You Need a Mint": 0,


       "Dragon's Breath (Itemsanity)": 5
   }, lambda state: canAccessEnd(world, state) and canSmelt(world, state) and canUseBottles(world, state))


   # REQUIRES VANILLA END GAME
   create_locations_and_connect(world, "EndAccess", "VanillaEndGame", {
       "Overkill": 0,
       "Monsters Hunted": 1,
       "Smithing with Style": 1,
       "Two by Two": 1,
       "A Balanced Diet": 1,
       "Adventuring Time": 3,
       "How Did We Get Here?": 3,


       "End Rod (Itemsanity)": 5
   }, lambda state: canAccessVanillaEndGame(world, state))


   # REQUIRES NETHER AND CHESTS
   create_locations_and_connect(world, "NetherAccess", "NetherAccessAndChests", {
       "War Pigs": 0
   }, lambda state: canAccessNether(world, state) and canAccessChests(world, state))


   # REQUIRES NETHER + DIAMOND TOOLS OR CHESTS
   create_locations_and_connect(world, "NetherAccess", "NetherAccessGetDebree", {
       "Hidden in the Depths": 0,


       "Ancient Debris (Itemsanity)": 5
   }, lambda state: canAccessNether(world, state) and (canAccessChests(world, state) or canUseDiamondTools(world, state)))


   # REQUIRES NETHER AND ENCHANTING
   create_locations_and_connect(world, "NetherAccess", "NetherAccessAndEnchanting", {
       "Crimson Nylium (Itemsanity)": 5,
       "Warped Nylium (Itemsanity)": 5,
       "Nether Gold Ore (Itemsanity)": 5,
       "Nether Quartz Ore (Itemsanity)": 5
   }, lambda state: canAccessNether(world, state) and canEnchant(world, state))


   # REQUIRES NETHER AND SMELTING
   create_locations_and_connect(world, "NetherAccess", "NetherAccessAndSmelting", {
       "Nether Brick Slab (Itemsanity)": 5,
       "Smooth Quartz Block (Itemsanity)": 5,
       "Nether Bricks (Itemsanity)": 5,
       "Cracked Nether Bricks (Itemsanity)": 5,
       "Chiseled Nether Bricks (Itemsanity)": 5,
       "Nether Brick Fence (Itemsanity)": 5,
       "Nether Brick Stairs (Itemsanity)": 5,
       "Nether Brick Wall (Itemsanity)": 5,
       "Red Nether Brick Wall (Itemsanity)": 5,
       "Smooth Quartz Stairs (Itemsanity)": 5,
       "Red Nether Brick Stairs (Itemsanity)": 5,
       "Smooth Quartz Slab (Itemsanity)": 5,
       "Red Nether Brick Slab (Itemsanity)": 5,
       "Daylight Detector (Itemsanity)": 5,
       "Red Nether Bricks (Itemsanity)": 5,
       "Nether Brick (Itemsanity)": 5,
       "Cracked Polished Blackstone Bricks (Itemsanity)": 5
   }, lambda state: canAccessNether(world, state) and canSmelt(world, state))


   # REQUIRES NETHER AND SMELTING AND IRON TOOLS
   create_locations_and_connect(world, "NetherAccessAndSmelting", "NetherAccessAndSmeltingAndIronTools", {
       "Redstone Comparator (Itemsanity)": 5,
       "Observer (Itemsanity)": 5,
       "Redstone Lamp (Itemsanity)": 5
   }, lambda state: canAccessNether(world, state) and canSmelt(world, state) and canUseIronTools(world, state))


   # REQUIRES SHEARS OR ENCHANTING
   create_locations_and_connect(world, "Menu", "ShearsOrEnchanting", {
       "Oak Leaves (Itemsanity)": 5,
       "Spruce Leaves (Itemsanity)": 5,
       "Birch Leaves (Itemsanity)": 5,
       "Jungle Leaves (Itemsanity)": 5,
       "Acacia Leaves (Itemsanity)": 5,
       "Cherry Leaves (Itemsanity)": 5,
       "Dark Oak Leaves (Itemsanity)": 5,
       "Mangrove Leaves (Itemsanity)": 5,
       "Azalea Leaves (Itemsanity)": 5,
       "Flowering Azalea Leaves (Itemsanity)": 5,
       "Cobweb (Itemsanity)": 5
   }, lambda state: canUseShears(world, state) or canEnchant(world, state))


   # REQUIRES END AND BOW
   create_locations_and_connect(world, "EndAccess", "EndAccessAndBow", {
       "Chorus Flower (Itemsanity)": 5
   }, lambda state: canAccessEnd(world, state) and canUseBow(world, state))


   # REQUIRES DIAMOND TOOLS AND EYES OF ENDER
   create_locations_and_connect(world, "HasDiamondTools", "HasDiamondToolsAndEyesOfEnder", {
       "Ender Chest (Itemsanity)": 5
   }, lambda state: canUseDiamondTools(world, state) and canGetEyesOfEnder(world, state))


   # REQUIRES SWIM OR NETHER ACCESS
   create_locations_and_connect(world, "Menu", "NetherAccessOrSwim", {
       "Magma Block (Itemsanity)": 5
   }, lambda state: canSwim(world, state) or canAccessNether(world, state))


   # REQUIRES CHESTS AND END ACCESS
   create_locations_and_connect(world, "EndAccess", "EndAccessAndChests", {
       "Shulker Box (Itemsanity)": 5,
       "White Shulker Box (Itemsanity)": 5,
       "Orange Shulker Box (Itemsanity)": 5,
       "Magenta Shulker Box (Itemsanity)": 5,
       "Light Blue Shulker Box (Itemsanity)": 5,
       "Yellow Shulker Box (Itemsanity)": 5,
       "Lime Shulker Box (Itemsanity)": 5,
       "Pink Shulker Box (Itemsanity)": 5,
       "Gray Shulker Box (Itemsanity)": 5,
       "Light Gray Shulker Box (Itemsanity)": 5,
       "Cyan Shulker Box (Itemsanity)": 5,
       "Purple Shulker Box (Itemsanity)": 5,
       "Blue Shulker Box (Itemsanity)": 5,
       "Brown Shulker Box (Itemsanity)": 5,
       "Green Shulker Box (Itemsanity)": 5,
       "Red Shulker Box (Itemsanity)": 5
   }, lambda state: canAccessChests(world, state) and canAccessEnd(world, state))


   # REQUIRES CHESTS AND END ACCESS AND SWIM
   create_locations_and_connect(world, "EndAccessAndChests", "EndAccessAndChestsAndSwim", {
       "Black Shulker Box (Itemsanity)": 5
   }, lambda state: canAccessChests(world, state) and canAccessEnd(world, state) and canSwim(world, state))


   # REQUIRES CHESTS AND SMELTING
   create_locations_and_connect(world, "CanSmeltItems", "CanSmeltItemsAndUseChests", {
       "Hopper (Itemsanity)": 5,
       "Trapped Chest (Itemsanity)": 5
   }, lambda state: canAccessChests(world, state) and canSmelt(world, state))


   # REQUIRES BOW AND IRON TOOLS
   create_locations_and_connect(world, "HasIronTools", "HasIronToolsAndBow", {
       "Dispenser (Itemsanity)": 5
   }, lambda state: canUseIronTools(world, state) and canUseBow(world, state))


   # REQUIRES MINECART AND IRON TOOLS
   create_locations_and_connect(world, "HasMinecart", "HasMinecartAndIronTools", {
       "Powered Rail (Itemsanity)": 5,
       "Detector Rail (Itemsanity)": 5,
       "Activator Rail (Itemsanity)": 5
   }, lambda state: canUseMinecart(world, state) and canUseIronTools(world, state))


   # REQUIRES MINECART AND CHESTS
   create_locations_and_connect(world, "HasMinecart", "HasMinecartAndChests", {
       "Minecart with Chest (Itemsanity)": 5,
       "Minecart with Hopper (Itemsanity)": 5
   }, lambda state: canUseMinecart(world, state) and canAccessChests(world, state))


   # REQUIRES FISHING OR SWIM
   create_locations_and_connect(world, "Menu", "HasSwimOrFishing", {
       "Raw Cod (Itemsanity)": 5,
       "Raw Salmon (Itemsanity)": 5,
       "Tropical Fish (Itemsanity)": 5,
       "Pufferfish (Itemsanity)": 5
   }, lambda state: canSwim(world, state) or canUseFishingRod(world, state))


   # REQUIRES FISHING OR SWIM + SMELTING
   create_locations_and_connect(world, "Menu", "HasSwimOrFishingAndSmelting", {
       "Cooked Cod (Itemsanity)": 5,
       "Cooked Salmon (Itemsanity)": 5
   }, lambda state: canSmelt(world, state) and (canSwim(world, state) or canUseFishingRod(world, state)))


   # REQUIRES SLEEP AND SWIM
   create_locations_and_connect(world, "HasSleep", "HasSleepAndSwim", {
       "Black Bed (Itemsanity)": 5
   }, lambda state: canSleep(world, state) and canSwim(world, state))


   # REQUIRES SLEEP AND SMELT
   create_locations_and_connect(world, "HasSleep", "HasSleepAndSmelt", {
       "Green Bed (Itemsanity)": 5
   }, lambda state: canSleep(world, state) and canSmelt(world, state))


   # REQUIRES SHEARS AND NETHER
   create_locations_and_connect(world, "NetherAccess", "NetherAccessAndShears", {
       "Nether Sprouts (Itemsanity)": 5
   }, lambda state: canAccessNether(world, state) and canUseShears(world, state))


   world.multiworld.completion_condition[world.player] = lambda state: get_goal_condition(world, state)


# Helper Methods #######################################################################################################


def create_locations_advanced(world: FabricMinecraftWorld, region_name: str, locations: dict[str, int]):
   location_list = []


   for location, type in locations.items():
       if type == 1 and world.options.exclude_hard_advancements:
           continue
       if type == 2 and world.options.exclude_exploration_advancements:
           continue
       elif type == 3 and world.options.exclude_unreasonable_advancements:
           continue
       elif type == 5 and not world.options.itemsanity:
           continue

       location_list.append(location)


   return create_locations(world, region_name, location_list)


def create_locations(world: FabricMinecraftWorld, region_name: str, locations: list[str]):
   region = Region(region_name, world.player, world.multiworld, region_name)

   for name in locations:
       location = Location(world.player, name, location_table[name], region)
       if name.endswith("(Itemsanity)"):
          world.itemsanity_locations.append(name)
       region.locations.append(location)

   world.multiworld.regions.append(region)


def connect(world, source: str, target: str, rule=None, reach: Optional[bool] = False,
           rule_to_str: Optional[str] = None, ) -> Optional[Entrance]:
   source_region = world.multiworld.get_region(source, world.player)
   target_region = world.multiworld.get_region(target, world.player)


   connection = Entrance(world.player, source + " ==> " + target, source_region)


   if rule:
       connection.access_rule = rule


   source_region.exits.append(connection)
   connection.connect(target_region)


   return connection if reach else None

def create_locations_and_connect(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None, reach: Optional[bool] = False,
           rule_to_str: Optional[str] = None, ):
   create_locations_advanced(world, new_region_name, locations)
   connect(world, region_name, new_region_name, rule)





