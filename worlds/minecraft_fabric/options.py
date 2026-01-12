from dataclasses import dataclass

from Options import PerGameCommonOptions, Choice, Range, ItemSet


# TRAP STUFF ###########################################################################################################

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

# class EnabledMods(ItemSet):
#     """List Compatible Mods here to include their checks in the game"""
#     display_name = "Mods"
#     rich_text_doc = True

@dataclass
class FMCOptions(PerGameCommonOptions):
    trap_fill_percentage: TrapFillPercentage
    reverseControlsTrapWeight: ReverseControlsTrapWeight
    invertedMouseTrapWeight: InvertedMouseTrapWeight
    iceTrapWeight: IceTrapWeight
    randomEffectTrapWeight: RandomEffectTrapWeight
    stunTrapWeight: StunTrapWeight
    tntTrapWeight: TNTTrapWeight
    teleportTrapWeight: TeleportTrapWeight
    beeTrapWeight: BeeTrapWeight
    literatureTrapWeight: LiteratureTrapWeight

