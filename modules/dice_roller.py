from heapq import nlargest, nsmallest
from random import randint
import re

dice_regex = re.compile(r"^(\d*)d(\d*)([hmle+-]|\.[+-])?(\d*)?$")


def bold_rolls(rolls: list, sides: int):
    bold = []
    for i in range(0, len(rolls)):
        if rolls[i] == 1:
            bold.append(f'**{rolls[i]}**')
        elif rolls[i] == sides:
            bold.append(f'**{rolls[i]}**')
        else:
            bold.append(f'{rolls[i]}')

    return str(bold).replace("\'", '')


def roll(user_input: str):
    result = dice_regex.search(user_input)

    try:
        repeats = int(result.group(1))
    except AttributeError:  # In case a non integer was passed as a repeating argument
        raise ValueError("Invalid entry")
    except ValueError:  # if Nothing was provided, default to 1
        repeats = 1
    try:
        sides = int(result.group(2))  # assign the sides of the die
    except ValueError:  # In case a non integer was passed as a repeating argument
        raise ValueError("Invalid entry")

    try:
        modifier = result.group(3)
    except ValueError:
        modifier = None
    try:
        mod_value = int(result.group(4))
    except ValueError:
        mod_value = None

    if (int(sides) or int(repeats)) < 1:
        return "Invalid Parameter."
    if int(repeats) > 500 or int(sides) > 1000:
        return "Invalid Parameter."

    if isinstance(modifier, str):  # Checking for a modifier present
        rolls = []
        for i in range(repeats):
            rolls.append(randint(1, sides))

        return moder(sides=sides, rolls=rolls, modifier=modifier, repeats=repeats, mod_value=mod_value)
    else:
        rolls = []
        for i in range(repeats):
            rolls.append(randint(1, sides))

        return bold_rolls(rolls=rolls, sides=sides), sum(rolls), repeats, sides


def moder(sides: int, rolls: list, modifier: str, mod_value: int, repeats):
    if modifier == 'e':
        temp = explode(sides=sides, rolls=rolls)
        return bold_rolls(rolls=temp, sides=sides), sum(
            temp), repeats, sides  # Return exploded dice rolls along with one that were neutral
    if modifier == 'h':  # Return highest
        temp = nlargest(mod_value, rolls)
        return bold_rolls(rolls=temp, sides=sides), sum(temp), repeats, sides
    if modifier == 'l':  # Return lowest
        temp = nsmallest(mod_value, rolls)
        return bold_rolls(rolls=temp, sides=sides), sum(temp), repeats, sides
    if modifier == '+':  # Add to sum of rolls
        return f"{bold_rolls(rolls=rolls, sides=sides)} + {mod_value}", (sum(rolls) + mod_value), repeats, sides
    if modifier == '-':  # Subtract from sum of rolls
        return f"{bold_rolls(rolls=rolls, sides=sides)} - {mod_value}", (sum(rolls) - mod_value), repeats, sides
    if modifier == '.-':  # Subtract from each roll
        for i in range(0, len(rolls)):
            rolls[i] = rolls[i] - mod_value
        return bold_rolls(rolls=rolls, sides=sides), sum(rolls), repeats, sides
    if modifier == '.+':  # Add to each roll
        for i in range(0, len(rolls)):
            rolls[i] = rolls[i] + mod_value
        return bold_rolls(rolls=rolls, sides=sides), sum(rolls), repeats, sides


# The exploding dice function
def explode(sides: int, rolls: list):
    for i in range(0, len(rolls)):
        counter = 0
        loop = True
        if rolls[i] == sides:
            while loop:
                counter += 1
                temp = randint(1, sides)
                rolls[i] += temp
                if temp != sides:
                    loop = False
    return rolls
