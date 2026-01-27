from __future__ import annotations


from typing import TYPE_CHECKING, Optional

from worlds.minecraft_fabric.region.regions_helper import create_locations_advanced
from worlds.minecraft_fabric.region.vanilla.vanilla_advancement_regions import create_vanilla_advancement_regions
from worlds.minecraft_fabric.region.vanilla.vanilla_itemsanity_regions import create_vanilla_itemsanity_regions
from worlds.minecraft_fabric.logic.vanilla_logic import *

if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld

# Creates all Regions in the Randomizer!
def create_regions(world: FabricMinecraftWorld):
    # Creates a Main Region for everything to branch from!
    create_locations_advanced(world, "Menu", {})
    # Vanilla Regions
    create_vanilla_advancement_regions(world)
    create_vanilla_itemsanity_regions(world)
