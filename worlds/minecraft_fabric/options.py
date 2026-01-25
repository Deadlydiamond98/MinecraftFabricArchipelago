from dataclasses import dataclass

from Options import PerGameCommonOptions, Choice, Range, ItemSet, OptionSet, OptionGroup, Toggle


########################################################################################################################
# GOAL CONDITION #######################################################################################################
########################################################################################################################

class GoalCondition(Choice):
    """
    Your Goal Condition for your game

    ender_dragon - Goal when the Ender Dragon is defeated
    wither - Goal when the Wither is defeated
    both_bosses - Goal when the Ender Dragon and Wither is defeated
    advancements_only - Goal when you collect a certain amount of Advancements
    ruby_hunt - Goal when a certain amount of rubies are collected (McGuffin hunt)
    """
    option_ender_dragon = 0
    option_wither = 1
    option_both_bosses = 2
    option_advancements_only = 3
    option_ruby_hunt = 4
    default = 0

class RandomizerDifficulty(Choice):
    """
    This determines where the placement of some items should be! The Items that will be effected by this setting are...
    Progressive Weapons (x2), Progressive Armor (x3), Progressive Archery (x1), Jump, and Sprint

    easy - These Items will appear before the player can access the Nether
    normal - These Items will appear before beating the Wither or End Access
    hard - Makes it so that these items can appear anywhere, potentially even outside your goal!
    """
    option_easy = 0
    option_normal = 1
    option_hard = 2
    default = 1

class AdvancementsRequiredToGoal(Range):
    """
    Determines the number of advancements needed in order to beat the game! These Advancements are required for goaling
    in addition to your regular goal. If this is set to zero, no advancements will be required to goal.

    If fewer available advancements exist than this number, the number of available advancements will be used instead.
    """
    display_name = "Advancements to Goal"
    range_start = 0
    range_end = 1000
    default = 50

class ExcludeUnreasonableAdvancements(Toggle):
    """
    Makes it so extremely hard Advancements (such as "How Did We Get Here?" or "Adventuring Time")
    will not have checks
    """
    display_name = "Exclude Unreasonable Advancements"
    default = True

class ExcludeHardAdvancements(Toggle):
    """
    Makes it so hard Advancements (such as "Cover Me in Debris" or "A Complete Catalogue")
    will not have checks
    """
    display_name = "Exclude Hard Advancements"
    default = True

class ExcludeExplorationAdvancements(Toggle):
    """
    Makes it so Advancements that require a lot of exploration (such as "Sound of Music" or "Whatever Floats Your Goat!")
    will not have checks
    """
    display_name = "Exclude Exploration Locations"
    default = False

class SpeedRunnerMode(Toggle):
    """
    Makes it so Beds are a required check for defeating the Ender Dragon
    """
    display_name = "Speedrunner Mode"
    default = True

class TotalRubiesInGame(Range):
    """
    Maximum possible number of Rubies that will be in the item pool

    If fewer available locations exist in the pool than this number, the number of available locations will be used instead.

    Required Percentage of Rubies will be calculated based off of that number.

    (Only Takes Effect when going for the Ruby Hunt Goal)
    """
    display_name = "Total Rubies In Game"
    range_start = 1
    range_end = 500
    default = 16

class RubyPercentageNeeded(Range):
    """
    The Percentage of Rubies that need to be collected to Goal for Ruby Hunt.
    (Only Takes Effect when going for the Ruby Hunt Goal)
    """
    display_name = "Ruby Percentage Needed"
    range_start = 1
    range_end = 100
    default = 100

class KeepInventory(Toggle):
    """
    Prevents you from dropping your items when you die!
    """
    display_name = "Keep Inventory"
    default = True

class Itemsanity(Toggle):
    """
    Enables "Itemsanity" which causes items obtainable in Survival to be checks

    (Not All Items become Itemsanity Checks, for the list of items without checks, click the link)
    (https://docs.google.com/document/d/1igxLuOAG1fHOQkJi1UyKVB2nz2pa8gu4DX2h61NtWic/edit?tab=t.0)
    """
    display_name = "Itemsanity"
    default = False

class ItemsanityLocalFill(Range):
    """
    The Percentage of Itemsanity Checks that should only contain items from your world
    """
    display_name = "Itemsanity Local Fill"
    range_start = 0
    range_end = 100
    default = 90


########################################################################################################################
# ABILITIES ############################################################################################################
########################################################################################################################

class RandomizeSwim(Toggle):
    """
    Removes the ability to enter water, and adds a Swim Item to the pool.
    """
    display_name = "Randomize Swim"
    default = False

class RandomizeChestStorage(Toggle):
    """
    Removes the ability to craft and use chests (and similar storage containers), and adds a Chest Item to the pool.
    """
    display_name = "Randomize Chests"
    default = False

class RandomizeSprint(Toggle):
    """
    Whether your Sprint ability should or Shouldn't be Randomized
    """
    display_name = "Randomize Sprint"
    default = False

class RandomizeJump(Toggle):
    """
    Whether your Jump ability should or Shouldn't be Randomized
    """
    display_name = "Randomize Jump"
    default = False

########################################################################################################################
# TRAP STUFF ###########################################################################################################
########################################################################################################################

class TrapFillPercentage(Range):
    """
    Replace a percentage of junk items in the item pool with random traps
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0

class BaseTrapWeight(Choice):
    """
    Base Class for Trap Weights
    """
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 4
    default = 2

class ReverseControlsTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes WASD, Shift, Jump, Break, and Place to Swap for a short duration
    """
    display_name = "Reverse Controls Trap Weight"

class InvertedMouseTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes the Mouse to Invert for a short duration
    """
    display_name = "Inverted Mouse Trap Weight"

class IceTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes all blocks to become slippery for a short duration
    """
    display_name = "Ice Trap Weight"

class RandomEffectTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which applies a random Negative Status Effect
    """
    display_name = "Random Status Effect Trap Weight"

class StunTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that temporarily stops movement of the player
    """
    display_name = "Stun Trap Weight"

class TNTTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that spawns a block of lit TNT on the player's position
    """
    display_name = "TNT Trap Weight"

class TeleportTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that Teleports the player similar to Chorus Fruit
    """
    display_name = "Teleport Trap Weight"

class BeeTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that Spawns 6 angry bees near the player
    """
    display_name = "Bee Trap Weight"

class LiteratureTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that Opens Literature Pop-Ups
    """
    display_name = "Literature Trap Weight"

class Deathlink(Toggle):
    """
    Enabled Deathlink
    """
    display_name = "Deathlink"
    default = False

# class EnabledMods(OptionSet):
#     """List Compatible Mods here to include their checks in the game"""
#     display_name = "Mods"
#     rich_text_doc = True

@dataclass
class FMCOptions(PerGameCommonOptions):
    # Goal Related Options
    goal_condition: GoalCondition
    randomizerDifficulty: RandomizerDifficulty
    # Advancements
    advancements_required_for_goal: AdvancementsRequiredToGoal
    exclude_unreasonable_advancements: ExcludeUnreasonableAdvancements
    exclude_hard_advancements: ExcludeHardAdvancements
    exclude_exploration_advancements: ExcludeExplorationAdvancements
    speedrunner_mode: SpeedRunnerMode
    percentage_of_rubies_needed: RubyPercentageNeeded
    total_rubies: TotalRubiesInGame
    keep_inventory: KeepInventory
    # Itemsanity
    itemsanity: Itemsanity
    itemsanity_local_fill: ItemsanityLocalFill
    # Abilities
    randomize_swim: RandomizeSwim
    randomize_chests: RandomizeChestStorage
    randomize_sprint: RandomizeSprint
    randomize_jump: RandomizeJump
    # Traps
    trap_fill_percentage: TrapFillPercentage
    reverse_controls_trap_weight: ReverseControlsTrapWeight
    inverted_mouse_trap_weight: InvertedMouseTrapWeight
    ice_trap_weight: IceTrapWeight
    random_effect_trap_weight: RandomEffectTrapWeight
    stun_trap_weight: StunTrapWeight
    tnt_trap_weight: TNTTrapWeight
    teleport_trap_weight: TeleportTrapWeight
    bee_trap_weight: BeeTrapWeight
    literature_trap_weight: LiteratureTrapWeight
    deathlink_enabled: Deathlink

