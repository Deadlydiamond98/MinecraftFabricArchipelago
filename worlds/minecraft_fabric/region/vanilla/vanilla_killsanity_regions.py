from __future__ import annotations


from typing import TYPE_CHECKING, Optional

from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.vanilla_logic import *


if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld

# def create_vanilla_killsanity_regions(world: FabricMinecraftWorld):
#     pass

def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "VanillaKillsanity", new_region_name + "VanillaKillsanity", locations, rule)