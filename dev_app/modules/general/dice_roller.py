import random
from collections import defaultdict

def roll_dice(dice_config):
    """
    Rolls a set of dice based on the input configuration.
    
    Parameters:
        dice_config (dict): A dictionary specifying the type and number of dice to roll.
                            Example: {'d4': 2, 'd6': 1, 'd20': 3}
                            
    Returns:
        dict: Results for each type of die rolled, as lists.
    """
    
    results = defaultdict(list)
    
    for die, count in dice_config.items():
        sides = int(die[1:])
        for _ in range(count):
            roll_result = random.randint(1, sides)
            results[die].append(roll_result)
            
    return dict(results)