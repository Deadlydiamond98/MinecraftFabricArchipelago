from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.minecraft_fabric import FabricMinecraftWorld

from BaseClasses import Region, Location, CollectionState
from worlds.minecraft_fabric.locations import location_table, vanilla_start_locations


def get_goal_condition(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Apple", world.player, 2)


def create_regions(world):
    # Menu Region
    create_locations(world, "Menu", vanilla_start_locations)

    # Goal
    world.multiworld.completion_condition[world.player] = lambda state: get_goal_condition(world, state)


def create_locations(world: FabricMinecraftWorld, region_name: str, locations: list[str]):
    region = Region(region_name, world.player, world.multiworld, region_name)
    region.locations += [Location(world.player, name, location_table[name], region) for name in locations]
    world.multiworld.regions.append(region)