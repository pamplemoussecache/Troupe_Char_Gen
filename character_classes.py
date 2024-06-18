class TroupeClass:
    def __init__(self, class_name="", favored_stats=[], description="", 
                 stat_distribution={"skill": [], "chance": [], "reaction": [], "unique": [], "brawl": [], "tough": []}):
        self.class_name = class_name
        self.favored_stats = favored_stats
        self.description = description
        self.stat_distribution = stat_distribution

class Jester(TroupeClass):
    class_name = "Jester"
    favored_stats = ["skill"]
    description = "Despised, deadly, and dedicated to the bit."
    stat_distribution = {
        "skill": [2, 2, 3],
        "chance": [0,1,2], 
        "reaction": [0,1,2], 
        "unique": [0,1,2], 
        "brawl": [0,1,2], 
        "tough": [1,1,2]
    }

class Hedge(TroupeClass):
    class_name = "Hedge"
    favored_stats = ["chance", "reaction"]
    description = "Handy, keen, and in tune with the world around you."
    stat_distribution = {
        "skill": [0, 0, 1],
        "chance": [2,2,3], 
        "reaction": [1,2,3], 
        "unique": [0,1,2], 
        "brawl": [0,0,1], 
        "tough": [1,1,2]
    }

class Ghelf(TroupeClass):
    class_name = "Ghelf"
    favored_stats = ["reaction", "unique", "brawl"]
    description = "Callous, charismatic, and cruel."
    stat_distribution = {
        "skill": [0, 0, 1],
        "chance": [0,0,1], 
        "reaction": [2,2,3], 
        "unique": [1,2,3], 
        "brawl": [1,2,3], 
        "tough": [0,1,1]
    }
class Witch(TroupeClass):
    class_name = "Witch"
    favored_stats = ["unique", "chance"]
    description = "Mystical, knowledgable, and solitary"
    stat_distribution = {
        "skill": [0, 1, 2],
        "chance": [1,2,3], 
        "reaction": [0,0,1], 
        "unique": [2,2,3], 
        "brawl": [0,1,2], 
        "tough": [0,1,1]
    }
        
class Ogra(TroupeClass):
    class_name = "Ogra"
    favored_stats = ["brawl", "skill", "tough"]
    description = "Bestial, powerful, and hungry"
    stat_distribution = {
        "skill": [1, 2, 3],
        "chance": [0,0,1], 
        "reaction": [0,0,1], 
        "unique": [0,0,1], 
        "brawl": [2,2,3], 
        "tough": [1,2,3]
    }
        
class Errant(TroupeClass):
    class_name = "Errant"
    favored_stats = ["tough", "brawl"]
    description = "Beaten, bruised, and spiteful"
    stat_distribution = {
        "skill": [0, 0, 1],
        "chance": [0,1,2], 
        "reaction": [0,1,2], 
        "unique": [0,0,1], 
        "brawl": [1,2,3], 
        "tough": [2,2,3]
    }