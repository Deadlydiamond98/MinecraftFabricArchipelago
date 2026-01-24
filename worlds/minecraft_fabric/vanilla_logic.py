from __future__ import annotations

from math import floor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.minecraft_fabric import FabricMinecraftWorld

from BaseClasses import CollectionState

########################################################################################################################
# VANILLA ##############################################################################################################
########################################################################################################################

# DIFFICULTY CHECK #####################################################################################################

def getDifficultyRequirements(level: int, world: FabricMinecraftWorld, state: CollectionState):
    difficulty = world.options.randomizerDifficulty.value
    if difficulty == level:
        return (canUseIronTools(world, state) and canWearIronArmor(world, state) and canUseBow(world, state)
                and optionalRequireSprint(world, state)) and optionalRequireJump(world, state)
    return True

# OPTIONAL ABILITY CHECKS ##############################################################################################

def optionalRequireSprint(world: FabricMinecraftWorld, state: CollectionState):
    if world.options.randomize_sprint.value == 1:
        return state.has("Sprint", world.player)
    else:
        return True

def optionalRequireJump(world: FabricMinecraftWorld, state: CollectionState):
    if world.options.randomize_jump.value == 1:
        return state.has("Jump", world.player)
    else:
        return True

def canAccessChests(world: FabricMinecraftWorld, state: CollectionState):
    if world.options.randomize_chests.value == 1:
        return state.has("Chests & Barrels", world.player)
    else:
        return True

def hasOptionalGoalAbilities(world: FabricMinecraftWorld, state: CollectionState):
    return optionalRequireJump(world, state) and optionalRequireSprint(world, state)

# ABILITY CHECKS #######################################################################################################

def canSwim(world: FabricMinecraftWorld, state: CollectionState):
    if world.options.randomize_swim:
        return state.has("Swim", world.player)
    else:
        return True

def speedrunnerMode(world: FabricMinecraftWorld, state: CollectionState):
    if world.options.speedrunner_mode:
        return canSleep(world, state)
    else:
        return True

def canTrade(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Villager Trading", world.player)

def canBarter(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Piglin Bartering", world.player) and canAccessNether(world, state) and canSmelt(world, state)

def canSleep(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Sleeping", world.player)

# CRAFTING STATION CHECKS ##############################################################################################

def canSmelt(world: FabricMinecraftWorld, state: CollectionState):
    return canUseStoneTools(world, state) and state.has("Progressive Smelting", world.player)

def canSmith(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Smithing", world.player)

def canBrew(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessNether(world, state) and canUseBottles(world, state) and state.has("Brewing", world.player)

def canEnchant(world: FabricMinecraftWorld, state: CollectionState):
    return canUseDiamondTools(world, state) and state.has("Enchanting", world.player) and canCompactResources(world, state)

def canAccessMiscJobsites(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Other Crafting Stations", world.player)

# MINING TOOL CHECKS ###################################################################################################

def canUseStoneTools(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Progressive Tools", world.player)

def canUseIronTools(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Progressive Tools", world.player, 2)

def canUseDiamondTools(world: FabricMinecraftWorld, state: CollectionState):
    return canUseIronTools(world, state) and state.has("Progressive Tools", world.player, 3)

def canUseNetheriteTools(world: FabricMinecraftWorld, state: CollectionState):
    return canUseDiamondTools(world, state) and state.has("Progressive Tools", world.player, 4) and canSmith(world, state)

# ARMOR CHECKS #########################################################################################################

def canWearLeatherArmor(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Progressive Armor", world.player)

def canWearGoldArmor(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Progressive Armor", world.player, 2)

def canWearIronArmor(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Progressive Armor", world.player, 3)

def canWearDiamondArmor(world: FabricMinecraftWorld, state: CollectionState):
    return canWearIronArmor(world, state) and state.has("Progressive Armor", world.player, 4) and canUseIronTools(world, state)

def canWearNetheriteArmor(world: FabricMinecraftWorld, state: CollectionState):
    return canWearDiamondArmor(world, state) and state.has("Progressive Armor", world.player, 5) and canSmith(world, state) and canUseDiamondTools(world, state)

# OTHER TOOL CHECKS ####################################################################################################

def canUseBucket(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Bucket Recipes", world.player)

def canUseFlintAndSteel(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Flint and Steel Recipes", world.player)

def canUseMinecart(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Minecart Recipes", world.player)

def canUseBrush(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Brush Recipes", world.player)

def canUseSpyglass(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Spyglass Recipes", world.player)

def canUseShears(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Shear Recipes", world.player)

def canUseFishingRod(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Fishing Rod Recipes", world.player)

def canUseBottles(world: FabricMinecraftWorld, state: CollectionState):
    return canSmelt(world, state) and state.has("Glass Bottle Recipes", world.player)

def canUseBow(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Progressive Archery", world.player)

def canUseCrossBow(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Progressive Archery", world.player, 2) and canSmelt(world, state)

def canUseShield(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Shield Recipes", world.player) and canSmelt(world, state)

# OTHER RECIPE CHECKS ##################################################################################################

def canCompactResources(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Resource Compacting Recipes", world.player)

def canGetEyesOfEnder(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessNether(world, state) and state.has("Eye of Ender Recipes", world.player)

def canGetAndUseArmorTrims(world: FabricMinecraftWorld, state: CollectionState):
    return canSmith(world, state) and canAccessChests(world, state) and canWearLeatherArmor(world, state)

# DIMENSION CHECKS #####################################################################################################

def canAccessNether(world: FabricMinecraftWorld, state: CollectionState):
    return (((canUseDiamondTools(world, state) or canUseBucket(world, state)) and canUseFlintAndSteel(world, state))
            and getDifficultyRequirements(0, world, state))

def canAccessEnd(world: FabricMinecraftWorld, state: CollectionState):
    return canGetEyesOfEnder(world, state) and speedrunnerMode(world, state) and getDifficultyRequirements(1, world, state)

# MISC VANILLA #########################################################################################################

def canPlaceBeacon(world: FabricMinecraftWorld, state: CollectionState):
    return canGoalWither(world, state) and canSmelt(world, state) and canUseDiamondTools(world, state) and canCompactResources(world, state)

def canGetCryingObsidian(world: FabricMinecraftWorld, state: CollectionState):
    return canBarter(world, state) or canUseDiamondTools(world, state)

def canAccessVanillaEndGame(world: FabricMinecraftWorld, state: CollectionState):
    return ((canEnchant(world, state) and canBrew(world, state) and canPlaceBeacon(world, state)
            and canBeatDragonAndWither(world, state) and canUseDiamondTools(world, state))
            and canAccessChests(world, state))

# GOAL CHECKS ##########################################################################################################

def canGoalEnderDragon(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessEnd(world, state)

def canGoalWither(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessNether(world, state) and state.has("Wither Summoning", world.player) and getDifficultyRequirements(1, world, state)

def canBeatDragonAndWither(world: FabricMinecraftWorld, state: CollectionState):
    return canGoalEnderDragon(world, state) and canGoalWither(world, state)

def canCompleteRubyHunt(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Ruby", world.player, floor(world.max_ruby_count * (world.options.percentage_of_rubies_needed.value * 0.01)))

