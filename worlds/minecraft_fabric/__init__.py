import math
from typing import Mapping, Any

from BaseClasses import ItemClassification, Item
from worlds.AutoWorld import World
from worlds.minecraft_fabric.items import item_table, useful_index, traps_index, bl_progression_index
from worlds.minecraft_fabric.locations import location_table
from worlds.minecraft_fabric.options import FMCOptions
from worlds.minecraft_fabric.region import create_regions


class FabricMinecraftWorld(World):
    game = "Minecraft Fabric"
    options_dataclass = FMCOptions
    options: FMCOptions
    topology_present = True

    item_name_to_id = {
        item.name: item.item_id for item in item_table
    }

    location_name_to_id = location_table

    max_ruby_count = 0


    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

    def create_regions(self):
        create_regions(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        # from Utils import visualize_regions
        # state = self.multiworld.get_all_state()
        # state.update_reachable_regions(self.player)
        #
        # reachable_regions = state.reachable_regions[self.player]
        # unreachable_regions: set[Region] = set()  # type: ignore
        # for regionb in self.multiworld.regions:
        #     if regionb not in reachable_regions:
        #         unreachable_regions.add(regionb)
        #
        # visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml", show_entrance_names=True,
        #                   regions_to_highlight=unreachable_regions)

        advancements = 0

        for name in self.multiworld.get_locations():
            if not name.name.endswith("(Itemsanity)"):
                advancements += 1

        return {
            # Base
            "goal_condition": self.options.goal_condition.value,
            # Advancements Needed to Goal
            "advancements_to_goal": min(advancements, self.options.advancements_required_for_goal.value),
            "exclude_hard": self.options.exclude_hard_advancements.value,
            "exclude_exploration": self.options.exclude_exploration_advancements.value,
            "exclude_unreasonable": self.options.exclude_unreasonable_advancements.value,
            # Rubies
            "rubies_to_goal": self.options.percentage_of_rubies_needed.value,
            "total_rubies": self.max_ruby_count,
            "deathlink": self.options.deathlink_enabled.value,
            # Other Options
            "keep_inventory": self.options.keep_inventory.value,
            "randomize_swim": self.options.randomize_swim.value,
            "randomize_sprint": self.options.randomize_sprint.value,
            "randomize_jump": self.options.randomize_jump.value,
            "randomize_chests": self.options.randomize_chests.value
        }

    def create_item(self, name: str) -> "Item":
        return Item(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_items(self):
        total_items = len(self.multiworld.get_unfilled_locations(self.player))

        # Progression Items ############################################################################################

        if self.options.randomize_swim:
            total_items = self.add_to_pool(1, total_items)
        if self.options.randomize_sprint:
            total_items = self.add_to_pool(2, total_items)
        if self.options.randomize_jump:
            total_items = self.add_to_pool(3, total_items)
        if self.options.randomize_chests:
            total_items = self.add_to_pool(4, total_items)

        progressive_index = 5

        # Progressive Tools
        total_items = self.add_multiple_to_pool(progressive_index, 4, total_items)
        # Progressive Weapons
        total_items = self.add_multiple_to_pool(progressive_index + 1, 4, total_items)
        # Progressive Smelting
        total_items = self.add_multiple_to_pool(progressive_index + 2, 2, total_items)
        # Progressive Armor
        total_items = self.add_multiple_to_pool(progressive_index + 3, 5, total_items)
        # Progressive Archery
        total_items = self.add_multiple_to_pool(progressive_index + 4, 2, total_items)

        # Single Check Progressive Items
        for i in range(bl_progression_index + 1, useful_index + 1):
            total_items = self.add_to_pool(i, total_items)

        # Ruby Hunt Items
        if self.options.goal_condition.value == 4:
            self.max_ruby_count = min(self.options.total_rubies.value, total_items)
            total_items = self.add_multiple_to_pool(0, self.max_ruby_count, total_items)


        # Trap Items ###################################################################################################
        trap_weights = []
        trap_weights += self.add_trap_weight(traps_index + 1, self.options.reverse_controls_trap_weight)
        trap_weights += self.add_trap_weight(traps_index + 2, self.options.inverted_mouse_trap_weight)
        trap_weights += self.add_trap_weight(traps_index + 3, self.options.ice_trap_weight)
        trap_weights += self.add_trap_weight(traps_index + 4, self.options.random_effect_trap_weight)
        trap_weights += self.add_trap_weight(traps_index + 5, self.options.stun_trap_weight)
        trap_weights += self.add_trap_weight(traps_index + 6, self.options.tnt_trap_weight)
        trap_weights += self.add_trap_weight(traps_index + 7, self.options.teleport_trap_weight)
        trap_weights += self.add_trap_weight(traps_index + 8, self.options.bee_trap_weight)
        trap_weights += self.add_trap_weight(traps_index + 9, self.options.literature_trap_weight)
        trap_count = 0 if (len(trap_weights) == 0) else math.ceil(
            total_items * (self.options.trap_fill_percentage.value / 100.0))

        for i in range(trap_count):
            trap_item = self.random.choice(trap_weights)
            self.multiworld.itempool.append(Item(trap_item.name, trap_item.item_type, trap_item.item_id, self.player))
            total_items -= 1

        # Filler Items #####################################################################################################
        while total_items > 0:
            total_items = self.add_to_pool(self.random.randint(useful_index + 1, traps_index), total_items)

    def add_multiple_to_pool(self, index: int, count: int, total_items: int):
        for i in range(count):
            total_items = self.add_to_pool(index, total_items)
        return total_items

    def add_to_pool(self, index: int, total_items: int):
        self.multiworld.itempool.append(
            Item(item_table[index].name, item_table[index].item_type, item_table[index].item_id, self.player)
        )
        total_items -= 1
        return total_items

    def add_trap_weight(self, index, weight):
        return [item_table[index]] * weight