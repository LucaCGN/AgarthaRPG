from modules.general.dice_roller import roll_dice  # Assumes the path to dice_roller.py

def roll_stats():
    """
    Rolls 6D4 six times, drops the lowest value from each roll, and sums the remaining values.
    
    Returns:
        list: A list of six numbers representing the rolled stats.
    """
    rolled_stats = []
    for _ in range(6):
        # Roll 4D6
        result = roll_dice({'d6': 4})
        
        # Drop the lowest value and sum the rest
        rolls = result['d6']
        rolls.remove(min(rolls))
        stat_value = sum(rolls)
        
        rolled_stats.append(stat_value)
        
    return rolled_stats

def assign_stats(rolled_stats):
    """
    Allows the user to assign rolled stats to character attributes.
    
    Parameters:
        rolled_stats (list): A list of six numbers representing the rolled stats.
        
    Returns:
        dict: A dictionary mapping attributes to their assigned stats.
    """
    attributes = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    assigned_stats = {}
    
    for attr in attributes:
        # Removed ui.display_message() lines since the interaction has moved to the UI layer
        pass  # Placeholder; actual logic has been moved to UI
    
    return assigned_stats  # Note: This is now handled in the UI layer, so the function will return an empty dictionary
