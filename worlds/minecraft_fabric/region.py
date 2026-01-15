from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from worlds.minecraft_fabric import FabricMinecraftWorld

from BaseClasses import Region, Location, CollectionState, Entrance
from worlds.minecraft_fabric.locations import location_table


########################################################################################################################
# Create Regions #######################################################################################################
########################################################################################################################

def get_goal_condition(world, state):
    # Placeholder Win Condition TODO: Make actual goal
    return canAccessEnd(world, state) and canSummonWither(world, state)


def create_regions(world: FabricMinecraftWorld):
    # Menu Region (always available)
    create_locations_hard(world, "Menu", [
        "Stone Age",
        "Voluntary Exile",
        "Monster Hunter",
        "Sneak 100",
        "It Spreads",
        "The Parrots and the Bats",
        "You've Got a Friend in Me",
        "Whatever Floats Your Goat!",
        "Best Friends Forever",
        "A Seedy Place",
        "Hero of the Village",
        "Postmortal",
        "Getting Wood",
        "Benchmarking",
        "Time to Mine!",
        "Time to Farm!",
        "Bake Bread",
        "Time to Strike!"
    ], [
        "When the Squad Hops into Town"
    ])

    create_locations(world, "DiamondTools", [
        "Ice Bucket Challenge"
    ])

    create_locations(world, "StoneToolsGet", [
        "Getting an Upgrade"
    ])

    create_locations(world, "SmeltIron", [
        "Acquire Hardware",
        "Not Today, Thank You"
    ])

    create_locations(world, "NeedsFurnace", [
        "Hot Topic"
    ])

    create_locations(world, "DiamondArmor", [
        "Cover Me with Diamonds"
    ])

    create_locations(world, "IronArmor", [
        "Suit Up"
    ])

    create_locations(world, "IronTools", [
        "Isn't It Iron Pick",
        "Diamonds!"
    ])

    create_locations_hard(world, "Swim", [
        "A Throwaway Joke",
        "Very Very Frightening",
        "Glow and Behold!",
        "Smells Interesting",
        "The Cutest Predator",
        "The Healing Power of Friendship!"
    ], [
        "Little Sniffs",
        "Planting the Past"
    ])

    create_locations(world, "Bow", [
        "Take Aim",
        "Sniper Duel",
        "Bullseye"
    ])

    create_locations(world, "CrossBow", [
        "Ol' Betsy",
        "Two Birds, One Arrow",
        "Who's the Pillager Now?",
        "Arbalistic"
    ])

    create_locations(world, "Trading", [
        "What a Deal!",
        "Star Trader"
    ])

    create_locations(world, "Enchanting", [
        "Enchanter"
    ])

    create_locations(world, "Brush", [
        "Respecting the Remnants",
        "Careful Restoration"
    ])

    create_locations(world, "GlassBottle", [
        "Sticky Situation",
        "Bee Our Guest"
    ])

    create_locations(world, "IronCompacting", [
        "Hired Help",
        "Total Beelocation"
    ])

    create_locations(world, "WaxOnOff", [
        "Wax On",
        "Wax Off"
    ])

    create_locations(world, "Bucket", [
        "Bukkit Bukkit",
        "Birthday Song",
        "Hot Stuff",
        "The Lie"
    ])

    create_locations(world, "CopperOre", [
        "Surge Protector"
    ])

    create_locations_hard(world, "Fishing", [
        "Fishy Business"
    ], [
        "A Complete Catalogue"
    ])

    create_locations(world, "FishingAndSmelt", [
        "Delicious Fish"
    ])

    create_locations(world, "RequiresNetherite", [
        "Country Lode, Take Me Home"
    ])

    create_locations(world, "NetheriteTool", [
        "Serious Dedication"
    ])

    create_locations(world, "ArmorTrim", [
        "Crafting a New Look"
    ])

    create_locations(world, "BucketAndSwim", [
        "Caves & Cliffs",
        "Tactical Fishing"
    ])

    create_locations(world, "Sleep", [
        "Sweet Dreams"
    ])

    create_locations(world, "SoundsOfMusic", [
        "Sound of Music"
    ])

    create_locations(world, "LeatherArmor", [
        "Light as a Rabbit"
    ])

    # Spy Glass ########################################################################################################
    create_locations(world, "Spyglass", [
        "Is It a Bird?"
    ])
    create_locations(world, "SpyglassNether", [
        "Is It a Balloon?"
    ])
    create_locations(world, "SpyGlassEnd", [
        "Is It a Plane?"
    ])

    # Nether ###########################################################################################################

    # Checks that Require Nether Access
    create_locations_hard(world, "NetherAccess", [
        "We Need to Go Deeper",
        "Return to Sender",
        "Those Were the Days",
        "Subspace Bubble",
        "A Terrible Fortress",
        "Uneasy Alliance",
        "War Pigs",
        "Spooky Scary Skeleton",
        "Into Fire",
        "Hot Tourist Destinations",
        "The Power of Books"
    ], [
        "With Our Powers Combined!"
    ])

    # Checks that require Bartering
    create_locations(world, "Bartering", [
        "Oh Shiny"
    ])

    # Crying Obsidian
    create_locations(world, "ObtainCryingObsidian", [
        "Who is Cutting Onions?"
    ])

    # Checks that require Nether and Fishing Rod
    create_locations(world, "RideStrider", [
        "This Boat Has Legs",
        "Feels Like Home"
    ])

    # Checks that require Smithing and Netherite Armor
    create_locations(world, "NetheriteArmor", [
        "Cover Me in Debris"
    ])

    # Respawn Anchor
    create_locations(world, "RespawnAnchor", [
        "Not Quite \"Nine\" Lives"
    ])

    # Checks that Require Wither Fight
    create_locations(world, "WitherFight", [
        "Withering Heights",
        "Bring Home the Beacon",
        "Beaconator"
    ])

    create_locations_hard(world, "Brewing", [
        "Local Brewery",
        "Zombie Doctor"
    ], [
        "A Furious Cocktail"
    ])

    create_locations_hard(world, "EndGame", [

    ], [
        "Monsters Hunted",
        "How Did We Get Here?",
        "Smithing with Style",
        "Adventuring Time",
        "Two by Two",
        "A Balanced Diet"
    ])

    # End ##############################################################################################################

    # Checks that require End Access
    create_locations(world, "EndAccess", [
        "Free the End",
        "The Next Generation",
        "Remote Getaway",
        "The City at the End of the Game",
        "Sky's the Limit",
        "Great View From Up Here",
        "Eye Spy",
        "The End?"
    ])

    # Checks that require End Acess and Bottling
    create_locations(world, "DragonBreathBottling", [
        "You Need a Mint"
    ])

    # Checks that require End and Nether Access and Smelting
    create_locations(world, "RespawnDragon", [
        "The End... Again..."
    ])

    world.multiworld.completion_condition[world.player] = lambda state: get_goal_condition(world, state)


########################################################################################################################
# Connect Entrances ####################################################################################################
########################################################################################################################

def connect_entrances(world: FabricMinecraftWorld) -> None:

    connect(world, "Menu", "FishingAndSmelt", lambda state: canSmelt(world, state) and state.has("Fishing Rod Recipes", world.player))
    connect(world, "Menu", "NeedsFurnace", lambda state: canSmelt(world, state))
    connect(world, "Menu", "RequiresNetherite", lambda state: canMakeNetherite(world, state))
    connect(world, "Menu", "Enchanting", lambda state: state.has("Enchanting", world.player))
    connect(world, "Menu", "IronArmor", lambda state: state.has("Progressive Armor", world.player, 3) and canSmelt(world, state))
    connect(world, "Menu", "DiamondArmor", lambda state: state.has("Progressive Armor", world.player, 4) and canUseIronPickaxe(world, state))
    connect(world, "Menu", "DiamondTools", lambda state: canUseDiamondPickaxe(world, state))
    connect(world, "Menu", "IronTools", lambda state: canUseIronPickaxe(world, state) and canSmelt(world, state))
    connect(world, "Menu", "SmeltIron", lambda state: canSmelt(world, state) and canUseStonePickaxe(world, state))
    connect(world, "Menu", "StoneToolsGet", lambda state: canUseStonePickaxe(world, state))
    connect(world, "Menu", "Spyglass", lambda state: canMakeCopper(world, state) and state.has("Spyglass Recipes", world.player))
    connect(world, "Menu", "SpyglassNether", lambda state: canMakeCopper(world, state) and state.has("Spyglass Recipes", world.player) and canAccessNether(world, state))
    connect(world, "Menu", "SpyGlassEnd", lambda state: canMakeCopper(world, state) and state.has("Spyglass Recipes", world.player) and canAccessEnd(world, state))
    connect(world, "Menu", "Trading", lambda state: state.has("Villager Trading", world.player))
    connect(world, "Menu", "ArmorTrim", lambda state: canSmith(world, state))
    connect(world, "Menu", "GlassBottle", lambda state: state.has("Glass Bottle Recipes", world.player))
    connect(world, "Menu", "Bow", lambda state: state.has("Progressive Archery", world.player))
    connect(world, "Menu", "CrossBow", lambda state: state.has("Progressive Archery", world.player, 2))
    connect(world, "Menu", "CopperOre", lambda state: canMakeCopper(world, state))
    connect(world, "Menu", "BucketAndSwim", lambda state: hasBucket(world, state) and hasSwim(world, state))
    connect(world, "Menu", "Brush", lambda state: hasBrush(world, state))
    connect(world, "Menu", "Sleep", lambda state: state.has("Sleeping", world.player))
    connect(world, "Menu", "Swim", lambda state: hasSwim(world, state))
    connect(world, "Menu", "IronCompacting", lambda state: canUseIronPickaxe(world, state) and canSmelt(world, state) and state.has("Resource Compacting Recipes", world.player))
    connect(world, "Menu", "SoundsOfMusic", lambda state: canSmelt(world, state) or canUseIronPickaxe(world, state))
    connect(world, "Menu", "LeatherArmor", lambda state: state.has("Progressive Armor", world.player))
    connect(world, "Menu", "Fishing", lambda state: state.has("Fishing Rod Recipes", world.player))
    connect(world, "Menu", "Bucket", lambda state: hasBucket(world, state))
    connect(world, "Menu", "WaxOnOff", lambda state: state.has("Shear Recipes", world.player) and state.has("Resource Compacting Recipes", world.player))
    connect(world, "Menu", "NetheriteTool", lambda state: canMakeNetheriteTool(world, state)and state.has("Progressive Tools", world.player, 4))
    # Nether
    connect(world, "Menu", "NetherAccess", lambda state: canAccessNether(world, state))
    connect(world, "Menu", "Bartering", lambda state: canBarter(world, state))
    connect(world, "Menu", "ObtainCryingObsidian", lambda state: canBarter(world, state) or state.has("Progressive Tools", world.player, 3))
    connect(world, "Menu", "RideStrider", lambda state: canAccessNether(world, state) and state.has("Fishing Rod Recipes", world.player))
    connect(world, "Menu", "NetheriteArmor", lambda state: canMakeNetheriteTool(world, state) and state.has("Progressive Armor", world.player, 5))
    connect(world, "Menu", "RespawnAnchor", lambda state: canGetCryingObsidian(world, state) and canAccessNether(world, state) and state.has("Sleeping", world.player))
    connect(world, "Menu", "WitherFight", lambda state: canSummonWither(world, state))
    connect(world, "Menu", "Brewing", lambda state: canBrewPotions(world, state))
    connect(world, "Menu", "EndGame", lambda state: canBrewPotions(world, state) and canSummonWither(world, state) and canAccessEnd(world, state) and hasSwim(world, state))

    # End
    connect(world, "Menu", "EndAccess", lambda state: canAccessEnd(world, state))
    connect(world, "Menu", "DragonBreathBottling", lambda state: canBottleDragonBreath(world, state))
    connect(world, "Menu", "RespawnDragon", lambda state: canRespawnEnderDragon(world, state))


# Conditions ###########################################################################################################

# Generic Conditions

def canUseStonePickaxe(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Progressive Tools", world.player, 1)

def canUseIronPickaxe(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Progressive Tools", world.player, 2)

def canUseDiamondPickaxe(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Progressive Tools", world.player, 3)

def canSmelt(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Progressive Smelting", world.player, 1)

def canSmith(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Smithing", world.player)

def canBrewPotions(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessNether(world, state) and check_for_items(world, state, ["Brewing", "Glass Bottle Recipes"])

def canMakeCopper(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Progressive Tools", world.player, 1)

def hasBucket(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Bucket Recipes", world.player) and canSmelt(world, state) and canUseStonePickaxe(world, state)

def hasBrush(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Brush Recipes", world.player) and canSmelt(world, state) and canUseStonePickaxe(world, state)

def hasSwim(world: FabricMinecraftWorld, state: CollectionState):
    if world.options.randomize_swim:
        return state.has("Swim", world.player)
    else:
        return True

# Nether Conditions

def canAccessNether(world: FabricMinecraftWorld, state: CollectionState):
    return (canUseDiamondPickaxe(world, state) or hasBucket(world, state)) and state.has("Flint and Steel Recipes", world.player)

def canBarter(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessNether(world, state) and state.has("Piglin Bartering", world.player)

def canGetCryingObsidian(world: FabricMinecraftWorld, state: CollectionState):
    return canBarter(world, state) or state.has("Progressive Tools", world.player, 3)

def canMakeNetherite(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessNether(world, state) and canUseDiamondPickaxe(world, state)

def canMakeNetheriteTool(world: FabricMinecraftWorld, state: CollectionState):
    return canMakeNetherite(world, state) and canSmith(world, state)

def canSummonWither(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessNether(world, state) and state.has("Wither Summoning", world.player)

def canUseBeacon(world: FabricMinecraftWorld, state: CollectionState):
    return canSummonWither(world, state)

# End Conditions

def canAccessEnd(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Eye of Ender Recipes", world.player) and canAccessNether(world, state)

def canBottleDragonBreath(world: FabricMinecraftWorld, state: CollectionState):
    return canRespawnEnderDragon(world, state) and state.has("Glass Bottle Recipes", world.player)

def canRespawnEnderDragon(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessEnd(world, state) and canAccessNether(world, state) and state.has("Progressive Smelting", world.player)

# Helper Methods #######################################################################################################

def create_locations_hard(world: FabricMinecraftWorld, region_name: str, locations: list[str], hard_locations: list[str]):
    if world.options.exclude_hard_advancements:
        return create_locations(world, region_name, locations)
    else:
        locations += hard_locations
        return create_locations(world, region_name, locations)

def create_locations(world: FabricMinecraftWorld, region_name: str, locations: list[str]):
    region = Region(region_name, world.player, world.multiworld, region_name)
    region.locations += [Location(world.player, name, location_table[name], region) for name in locations]
    world.multiworld.regions.append(region)

def check_for_items(world: FabricMinecraftWorld, state: CollectionState, items: list[str]):
    bl = True
    for item in items:
        if not state.has(item, world.player):
            bl = False
    return bl


def connect(world, source: str, target: str, rule=None, reach: Optional[bool] = False,
            rule_to_str: Optional[str] = None, ) -> Optional[Entrance]:
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    connection = Entrance(world.player, source + " -> " + target, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    return connection if reach else None