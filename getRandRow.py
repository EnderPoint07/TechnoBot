import random

# path to file:
path_to_file = "TechnoQuotes.txt"


async def getRandomRow():
    lines = open(path_to_file).read().split('\n')
    return random.choice(lines)
