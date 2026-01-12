import math

from BaseClasses import ItemClassification, Item
from worlds.AutoWorld import World
from worlds.minecraft_fabric.items import item_table, end_index, traps_index
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


    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

    def create_regions(self):
        create_regions(self)

    def create_item(self, name: str) -> "Item":
        return Item(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_items(self):
        total_items = len(self.multiworld.get_unfilled_locations(self.player))

        # Progression Items ############################################################################################
        total_items = self.add_to_pool(0, total_items)
        total_items = self.add_to_pool(0, total_items)

        # Trap Items ###################################################################################################
        trap_weights = []
        trap_weights += self.add_trap_weight(traps_index + 1, self.options.reverseControlsTrapWeight)
        trap_weights += self.add_trap_weight(traps_index + 2, self.options.invertedMouseTrapWeight)
        trap_weights += self.add_trap_weight(traps_index + 3, self.options.iceTrapWeight)
        trap_weights += self.add_trap_weight(traps_index + 4, self.options.randomEffectTrapWeight)
        trap_weights += self.add_trap_weight(traps_index + 5, self.options.stunTrapWeight)
        trap_weights += self.add_trap_weight(traps_index + 6, self.options.tntTrapWeight)
        trap_weights += self.add_trap_weight(traps_index + 7, self.options.teleportTrapWeight)
        trap_weights += self.add_trap_weight(traps_index + 8, self.options.beeTrapWeight)
        trap_weights += self.add_trap_weight(traps_index + 9, self.options.literatureTrapWeight)
        trap_count = 0 if (len(trap_weights) == 0) else math.ceil(total_items * (self.options.trap_fill_percentage.value / 100.0))

        for i in range(trap_count):
            trap_item = self.random.choice(trap_weights)
            self.multiworld.itempool.append(Item(trap_item.name, trap_item.item_type, trap_item.item_id, self.player))
            total_items -= 1

        # Filler Items #################################################################################################
        for i in range(total_items):
            total_items = self.add_to_pool(self.random.randint(0, traps_index), total_items)


    def add_to_pool(self, index: int, total_items: int):
        self.multiworld.itempool.append(Item(item_table[index].name, item_table[index].item_type, item_table[index].item_id, self.player))
        total_items -= 1
        return total_items

    def add_trap_weight(self, index, weight):
        return [item_table[index]] * weight
