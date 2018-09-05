from collections import OrderedDict
from enum import Enum

from random_functions.dice import Roll


class Table(OrderedDict):
    def __call__(self, seed=None):
        roll = Roll(seed=seed, d=len(self.values()))
        return self[roll]


COLORS = Table({
    1: "RED",
    2: "ORANGE",
    3: "YELLOW",
    4: "GREEN",
    5: "BLUE",
    6: "INDIGO",
    7: "VIOLET",
    8: "WHITE",
    9: "BLACK",
    10: "MULTI"}
)
"""
    ALMOND = [1]
    APRICOT = [2]
    AQUAMARINE = [3]
    ASPARAGUS = [4, 5]
    BANANA = [6]
    BEAVER = [7, 8]
    BLACK = [9]
    BLUE = [10, 11]
    BLUE_GRAY = [12, 13]
    BLUE_VIOLET = [14]
    BLUSH = [15]
    BRICK_RED = [16]
    BROWN = [17, 18]
    BURNT_ORANGE = [19, 20]
    CANARY = [21]
    CARNATION_PINK = [22]
    CHESTNUT = [23, 24]
    DANDELION = [25]
    DESERT_SAND = [26]
    EGGPLANT = [27, 28]
    FERN = [29, 30]
    FUCHSIA = [31]
    GOLD = [32]
    GOLDENROD = [33]
    GRAY = [34, 35]
    GREEN = [36]
    GREEN_YELLOW = [37, 38]
    INCHWORM = [39]
    INDIGO = [40]
    JUNGLE_GREEN = [41]
    LAVENDER = [42]
    LEMON = [43]
    MAHOGANY = [44, 45]
    MAIZE = [46]
    MANGO = [47]
    MAROON = [48]
    MIDNIGHT_BLUE = [49]
    MULBERRY = [50]
    OLIVE_GREEN = [51, 52]
    ORANGE = [53]
    ORANGE_RED = [54, 55]
    ORANGE_YELLOW = [56]
    ORCHID = [57]
    PEACH = [58]
    PERIWINKLE = [59]
    PINE_GREEN = [60]
    PLUM = [61]
    RAW_UMBER = [62, 63]
    RED = [64]
    RED_ORANGE = [65]
    RED_VIOLET = [66]
    ROBIN_EGG_BLUE = [67]
    SALMON = [68]
    SCARLET = [69, 70]
    SEA_GREEN = [71]
    SILVER = [72]
    SKY_BLUE = [73]
    SUNSET_ORANGE = [74]
    TAN = [75]
    TEAL_BLUE = [76]
    TUMBLEWEED = [77]
    TURQUOISE_BLUE = [78]
    VIOLET = [79]
    VIOLET_BLUE = [80]
    VIOLET_RED = [81]
    WHITE = [82, 83]
    YELLOW = [84]
    YELLOW_ORANGE = [85]
    CLEAR = [86]
    TRANSLUCENT = [87, 88, 89, 90]  # Roll again for translucency color.
    TWO_COLORS = [91, 92, 93]  # Two colors interspersed throughout but separate. Roll two more times.
    TWO_COLOR_DROPS = [94, 95, 96]  # One primary color with interspersed drops of another color. Roll for each.
    TWO_COLORS_LAYER = [97, 98, 99]  # Two colors where one floats above the other. Roll again for each.
    TWO_COLORS_CHANGE = [00]  # Two colors that change every minute or so. Roll again for each.
"""

CONSISTENCY = Table({
    1: "BUBBLY",
    2: "CLUMPY",
    3: "FIZZY",
    4: "GASSY",
    5: "RUNNY",
    6: "THIN",
    7: "THICK",
    8: "WATERY",
    9: "ROLL_TWICE",
    10: "ROLL_TWICE",
})

"""
Roll 1d4 + 1 times, or choose a few that have some strange connection to the potion's perceived
ingredients. Some alchemists may add flavor to mask the taste. Each flavor may occur at the same
time as others or may be the initial flavor, main flavor or aftertaste. In addition, you may want to
add a general taste description such as spicy, sweet, sour, bitter, floral, etc.
"""
TASTE = Table({
    1: "Apple",
    2: "Banana",
    3: "Green Beans",
    4: "Lima Beans",
    5: "Beef",
    6: "Beef",
    7: "Beef",
    8: "Blueberry",
    9: "Cabbage",
    10: "Chicken",
    11: "Chicken",
    12: "Chicken",
    13: "Chicken",
    14: "Chives",
    15: "Chives",
    16: "Chutney",
    17: "Chutney",
    18: "Cinnamon",
    19: "Cinnamon",
    20: "Cinnamon",
    21: "Cinnamon",
    22: "Coffee",
    23: "Coffee",
    24: "Coffee",
    25: "Corn",
    26: "Cucumber",
})


class RandomPotion:
    # Tables acquired from http://inkwellideas.com/2009/11/random-potion-description-charts/
    def __init__(self,
                 color=None,
                 consistency=None,
                 taste=None,
                 smell=None,
                 flask=None):
        self.color = color
        self.consistency = consistency
        self.taste = taste
        self.smell = smell
        self.flask = flask

    @classmethod
    def random(cls, seed=None):
        return cls(color=COLORS(seed))


Roadside_Sights = Table({
    (1, 2, 3): "An abandoned cartwheel",
    (4, 5, 6): "A holy man meditating",
    (7, 8, 9): "A newly constructed traveler's waystation",
    (10, 11, 12): "A caravan of gypsies waiting for a birth",
    (13, 14, 15): "A statue of a two-headed goat",
    (16, 17, 18): "A covered well",
    (19, 20, 21): "A squashed hedgehog",
    (22, 23, 24): "A hermit's cave",
    (25, 26, 27): "A teahouse",
    (28, 29, 30): "An abandoned barn",
    (31, 32, 33): "The remnants of a campfire",
    (34, 35, 36): "A dead sheep",
    (37, 38, 39): "An old road, now overgrown and abandoned",
    (40, 41, 42): "A footpath leading away",
    (43, 44, 45): "A tumbled-down rock wall",
    (46, 47, 48): "A tree adorned in prayer flags",
    (49, 50, 51): "An oak tree split by lightning",
    (52, 53, 54): "The ruins of a croft",
    (55, 56, 57): "A standing stone",
    (58, 59, 60): "A tiny roadside tavern",
    (61, 62, 63): "An old blind woman begging for alms",
    (64, 65, 66): "A coin",
    (67, 68, 69): "Signs of a fight",
    (70, 71): "A totem depicting foxes and wolves chasing owls",
    (72, 73): "A boarded-up mineshaft",
    (74, 75): "An overgrown graveyard",
    (76, 77): "A broken, rusty halberd",
    (78, 79): "A scarecrow",
    (80, 81): "Three dead foxes strung up in a tree",
    (82, 83): "A mangy old dog",
    (84, 85): "The carcass of a giant, picked clean by vultures",
    (86, 87): "An abandoned child",
    (88, 89): "A gallows with a dead victim",
    (90, 91): "A coaching inn",
    (92, 93): "The corpse of a criminal in a hanging cage",
    (94, 95): "A road repair gang",
    (96, 97): "A pile of flagstones waiting to be laid",
    (98, 99): "A milestone",
    (100, 100): "A huge footprint"
})

Unique_City_Decorations = Table({
    (1, 2, 3): "Six-headed gargoyle fountain",
    (4, 5, 6): "Two huge feet, all that remains of a toppled statue",
    (7, 8, 9): "Iron column 20 feet high",
    (10, 11, 12): "Ancient, decaying elm tree",
    (13, 14, 15): "Large bathing pool fed by lion-faced outflows",
    (16, 17, 18): "Hot spring with a marble statue of a white dragon rising from its center",
    (19, 20, 21): "Three bronze horsemen looking west",
    (22, 23, 24): "Roadside shrine to a local saint",
    (25, 26, 27): "Bust of the local mayor",
    (28, 29, 30): "Gilded statue of the sun goddess",
    (31, 32, 33): "A stone carving of the god of magic standing over 20 feet tall",
    (34, 35, 36): "Black stone pyramid 10 feet high",
    (37, 38, 39): "Huge weathered sphinx",
    (40, 41, 42): "Line of 20 stylized stone faces",
    (43, 44, 45): "Bronze colossus of the city's patron god",
    (46, 47, 48): "Marble statue commemorating a local hero, showing him on a chariot pulled by eight white chargers",
    (49, 50, 51): "Fresco depicting a natural disaster",
    (52, 53, 54): "Three trees intertwined to create a crude throne",
    (55, 56, 57): "Golden orb on a plinth held aloft by stone rocs",
    (58, 59, 60): "Ancient, weathered statue of a mysterious woman in otherworldly garb",
    (61, 62, 63): "Stone platform jutting from the roof of the tallest building from which criminals are thrown",
    (64, 65, 66): "Small, bronze courtyard fountain",
    (67, 68, 69): "Street fountain and watering trough",
    (70, 71, 72): "Statue of a dwarf riding a griffon",
    (73, 74, 75): "Washing fountain decorated with carved oak leaves",
    (76, 77, 78): "Fountain held aloft by eight lions",
    (79, 80, 81): "Alley with 100 fountains",
    (82, 83, 84): "Fountain depicting six seahorses",
    (85, 86, 87): "Weathered dolmen",
    (88, 89, 90): "Sarcophagus carved with one-eyed crows",
    (91, 92, 93): "Stone altar",
    (94, 95, 96): "Marble statue of a scholar instructing a trio of admiring students",
    (97, 98, 99): "Retired guillotine",
    (100, 100): "Large metal copy of a holy book; a novice turns the page each day with a key"
})

Shop_Names = Table({
    (1, 2): "Jabe, Mulwithickle, and Fayeid, Tea Merchants",
    (3, 4): "Sacril's Tobacconist",
    (5, 6): "The Swordsharp Man",
    (7, 8): "Hatter's Halberds",
    (9, 10): "Whittlewood's Grocery Emporium",
    (11, 12): "J.E. Jebs and Sons, Undertakers",
    (13, 14): "Quottle and Partners, Quality Distillers and Alchemists",
    (15, 16): "Urah Quell Brewers",
    (17, 18): "H.R. Lobb and Daughter, Antiquarian Maps and Tomes",
    (19, 20): "Jogg's Butchers",
    (21, 22): "Alanna's Answers, Full Service Divination",
    (23, 24): "Peppermint Palace Pastries",
    (25, 26): "The Crow's Nest Ropes and Rigging",
    (27, 28): "Hugor's Statuary and Memoria",
    (29, 30): "Tuttle and Weft, Ladies' Quality Garments",
    (31, 32): "The Wine Warehouse",
    (33, 34): "Dor and Totter Junkyard",
    (35, 36): "Cakran, March, and Spade's Spices from Far Shores",
    (37, 38): "Dobber Cartwright's Carts, Carriages, and Coaches",
    (39, 40): "Milk and Dairy Farmers' Hall",
    (41, 42): "Elnore's Copy Shop, Skilled in Five Languages!",
    (43, 44): "The Shark Tooth Seller",
    (45, 46): "Manem's, Jewelers by Royal Appointment for 400 Years",
    (47, 48): "Yuran's Knife and Blade Sharpening Shop",
    (49, 50): "Lavender and Perfumes",
    (51, 52): "Murran's Self-Defense Academy",
    (53, 54): "Dorrie's House of Discreet Delights",
    (55, 56): "Urgin's Hair and Tooth Removal",
    (57, 58): "Warred's Perfumery and Incense Emporium",
    (59, 60): "Dokk and Gyorgi, Royal Wig Makers",
    (61, 62): "Told's Tannery and Leather Goods Warehouse",
    (63, 64): "Mother Cotter's, Seamstress",
    (65, 66): "Trackady's Curios and Components",
    (67, 68): "Artham's Runners, Linkboys, and Messenger Firm",
    (69, 70): "Hardware, Metalware, and Household Emporium",
    (71, 72): "The Sealing Wax Company",
    (73, 74): "Grig's Hourglass Bazaar",
    (75, 76): "The Flea Market",
    (77, 78): "J.M. Wortley's Healer and Chirurgery Suppliers",
    (79, 80): "Optical Objects Trading House",
    (81, 82): "P.P. Partwill's Weapons and Wares",
    (83, 84): "Purple Crescent Puppet Theater",
    (85, 86): "The Portable Ram Shop",
    (87, 88): "The Oil and Coal Barrow",
    (89, 90): "J. Hartlin's Snuff Shop",
    (91, 92): "Maps by Maurice",
    (93, 94): "Books, Tomes, and Ledgers",
    (95, 96): "Wood Paneling by Mennel Doorbry",
    (97, 98): "Gentlemen's Furnishing Entrepot",
    (99, 100): "Three-Coppers Secondhand Goods"
})

Tavern_Traits = Table({
    (1, 2): "Only opens on public holidays",
    (3, 4): "In a former church",
    (5, 6): "In a former theater",
    (7, 8): "In a farmhouse",
    (9, 10): "In a cellar",
    (11, 12): "Partly ruined",
    (13, 14): "Stocks or gallows inside",
    (15, 16): "Magical lighting that slowly shifts hues",
    (17, 18): "",
    (19, 20): "Jogg's Butchers",
    (21, 22): "Alanna's Answers, Full Service Divination",
    (23, 24): "Peppermint Palace Pastries",
    (25, 26): "The Crow's Nest Ropes and Rigging",
    (27, 28): "Hugor's Statuary and Memoria",
    (29, 30): "Tuttle and Weft, Ladies' Quality Garments",
    (31, 32): "The Wine Warehouse",
    (33, 34): "Dor and Totter Junkyard",
    (35, 36): "Cakran, March, and Spade's Spices from Far Shores",
    (37, 38): "Dobber Cartwright's Carts, Carriages, and Coaches",
    (39, 40): "Milk and Dairy Farmers' Hall",
    (41, 42): "Elnore's Copy Shop, Skilled in Five Languages!",
    (43, 44): "The Shark Tooth Seller",
    (45, 46): "Manem's, Jewelers by Royal Appointment for 400 Years",
    (47, 48): "Yuran's Knife and Blade Sharpening Shop",
    (49, 50): "Lavender and Perfumes",
    (51, 52): "Murran's Self-Defense Academy",
    (53, 54): "Dorrie's House of Discreet Delights",
    (55, 56): "Urgin's Hair and Tooth Removal",
    (57, 58): "Warred's Perfumery and Incense Emporium",
    (59, 60): "Dokk and Gyorgi, Royal Wig Makers",
    (61, 62): "Told's Tannery and Leather Goods Warehouse",
    (63, 64): "Mother Cotter's, Seamstress",
    (65, 66): "Trackady's Curios and Components",
    (67, 68): "Artham's Runners, Linkboys, and Messenger Firm",
    (69, 70): "Hardware, Metalware, and Household Emporium",
    (71, 72): "The Sealing Wax Company",
    (73, 74): "Grig's Hourglass Bazaar",
    (75, 76): "The Flea Market",
    (77, 78): "J.M. Wortley's Healer and Chirurgery Suppliers",
    (79, 80): "Optical Objects Trading House",
    (81, 82): "P.P. Partwill's Weapons and Wares",
    (83, 84): "Purple Crescent Puppet Theater",
    (85, 86): "The Portable Ram Shop",
    (87, 88): "The Oil and Coal Barrow",
    (89, 90): "J. Hartlin's Snuff Shop",
    (91, 92): "Maps by Maurice",
    (93, 94): "Books, Tomes, and Ledgers",
    (95, 96): "Wood Paneling by Mennel Doorbry",
    (97, 98): "Gentlemen's Furnishing Entrepot",
    (99, 100): "Three-Coppers Secondhand Goods"
})

Random_Tavern_Name_Generator = Table({
    (1, 2): ("Blind", "Cat"),
    (3, 4): ("Three", "Fire"),
    (5, 6): (),
    (7, 8): (),
    (9, 10): (),
    (11, 12): (),
    (13, 14): (),
    (15, 16): (),
    (17, 18): (),
    (19, 20): (),
    (21, 22): (),
    (23, 24): (),
    (25, 26): (),
    (27, 28): (),
    (29, 30): (),
    (31, 32): (),
    (33, 34): (),
    (35, 36): (),
    (37, 38): (),
    (39, 40): (),
    (41, 42): (),
    (43, 44): (),
    (45, 46): (),
    (47, 48): (),
    (49, 50): (),
    (51, 52): (),
    (53, 54): (),
    (55, 56): (),
    (57, 58): (),
    (59, 60): (),
    (61, 62): (),
    (63, 64): (),
    (65, 66): (),
    (67, 68): (),
    (69, 70): (),
    (71, 72): (),
    (73, 74): (),
    (75, 76): (),
    (77, 78): (),
    (79, 80): (),
    (81, 82): (),
    (83, 84): (),
    (85, 86): (),
    (87, 88): (),
    (89, 90): (),
    (91, 92): (),
    (93, 94): (),
    (95, 96): (),
    (97, 98): (),
    (99, 100): ()
})
