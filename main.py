#!/usr/bin/env python3
import argparse
from random import choice, randrange

class TroupeClass:
    def __init__(self, class_name="", favored_stats=[], description="", 
                 stat_distribution={"Skill": [], "Chance": [], "Reaction": [], "Unique": [], "Brawl": [], "Tough": []}):
        self.class_name = class_name
        self.favored_stats = favored_stats
        self.description = description
        self.stat_distribution = stat_distribution

class Jester(TroupeClass):
    def __init__(self, class_name="", favored_stats=[], description="", 
                 stat_distribution={}):
        self.class_name = "Jester"
        self.favored_stats = ["Skill"]
        self.description = "Despised, deadly, and dedicated to the bit."
        self.stat_distribution = {
            "Skill": [2, 2, 3],
            "Chance": [0,1,2], 
            "Reaction": [0,1,2], 
            "Unique": [0,1,2], 
            "Brawl": [0,1,2], 
            "Tough": [1,1,2]
    }

class Hedge(TroupeClass):
    def __init__(self, class_name="", favored_stats=[], description="", 
                 stat_distribution={}):
        self.class_name = "Hedge"
        self.favored_stats = ["Chance", "Reaction"]
        self.description = "Handy, keen, and in tune with the world around you."
        self.stat_distribution = {
            "Skill": [0, 0, 1],
            "Chance": [2,2,3], 
            "Reaction": [1,2,3], 
            "Unique": [0,1,2], 
            "Brawl": [0,0,1], 
            "Tough": [1,1,2]
    }

class Ghelf(TroupeClass):
    def __init__(self, class_name="", favored_stats=[], description="", 
                 stat_distribution={}):
        self.class_name = "Ghelf"
        self.favored_stats = ["Reaction", "Unique", "Brawl"]
        self.description = "Callous, charismatic, and cruel."
        self.stat_distribution = {
            "Skill": [0, 0, 1],
            "Chance": [0,0,1], 
            "Reaction": [2,2,3], 
            "Unique": [1,2,3], 
            "Brawl": [1,2,3], 
            "Tough": [0,1,1]
    }
class Witch(TroupeClass):
    def __init__(self, class_name="", favored_stats=[], description="", 
                 stat_distribution={}):
        self.class_name = "Witch"
        self.favored_stats = ["Unique", "Chance"]
        self.description = "Mystical, knowledgable, and solitary"
        self.stat_distribution = {
            "Skill": [0, 1, 2],
            "Chance": [1,2,3], 
            "Reaction": [0,0,1], 
            "Unique": [2,2,3], 
            "Brawl": [0,1,2], 
            "Tough": [0,1,1]
    }
        
class Ogra(TroupeClass):
    def __init__(self, class_name="", favored_stats=[], description="", 
                 stat_distribution={}):
        self.class_name = "Ogra"
        self.favored_stats = ["Brawl", "Skill", "Tough"]
        self.description = "Bestial, powerful, and hungry"
        self.stat_distribution = {
            "Skill": [1, 2, 3],
            "Chance": [0,0,1], 
            "Reaction": [0,0,1], 
            "Unique": [0,0,1], 
            "Brawl": [2,2,3], 
            "Tough": [1,2,3]
    }
        
class Errant(TroupeClass):
    def __init__(self, class_name="", favored_stats=[], description="", 
                 stat_distribution={}):
        self.class_name = "Errant"
        self.favored_stats = ["Tough", "Brawl"]
        self.description = "Beaten, bruised, and spiteful"
        self.stat_distribution = {
            "Skill": [0, 0, 1],
            "Chance": [0,1,2], 
            "Reaction": [0,1,2], 
            "Unique": [0,0,1], 
            "Brawl": [1,2,3], 
            "Tough": [2,2,3]
    }


class TroupeCharacter:
    def __init__(self, job="", name="", expertise=None, equipment=None, abilities=None, principles=None):
        self.name = name
        self.job = job
        self.expertise = expertise
        self.equipment = {"weapon": [], "food": [], "junk": []}
        self.abilities = []
        self.principles = []
    def add_ability(self, ability):
        self.abilities.append(ability)
    def add_principle(self, principle):
        if (len(self.principles > 2)):
            answer = input("Adding another principle will remove one of your existing ones. Are you sure you want to continue? y/n")
            answer = answer.lower()
            if answer == "y" or answer == "yes":
                self.principles = [self.principles[1], principle]
            elif answer == "n" or answer == "no":
                print("Fair enough! You have kept your principles, which are: ")
                print("- " + self.principles[0])
                print("- " + self.principles[1])
            else:
                print("Invalid response. Please try again.")
                self.add_principle(self, principle)
        else:
            self.principles.append(principle)

new_char = TroupeCharacter()


parser = argparse.ArgumentParser(description="Troupe Character Generator")

parser.add_argument("job")
parser.add_argument("expertise")
parser.add_argument("equipment")
parser.add_argument("abilities")
parser.add_argument("name")
parser.add_argument("principles")

def set_job():
    jobs = ["jester", "hedge", "ghelf", "witch", "errant"]
    new_job = choice(jobs)
    answer = input(f"You rolled {new_job}! Would you like to keep it or roll again?")
    if "keep" in answer:
        new_char.job = new_job
    else:
        set_job()

#Step one, roll for job if not already set
set_job()

#Step two, roll ability scores
possible_scores = []
for i in range(6):
    possible_scores.append(randrange(1,6))
print("Option A: ", possible_scores)

#Step three, decide whether to keep ability scores or take 1,2,3,4,5,6
print("Option B: [1, 2, 3, 4, 5, 6]")
answer = input("Do you want A or B?")
if (answer.lower()) == "b":
    possible_scores = [1,2,3,4,5,6]

print(f"Okay! You ability scores will be selected from {possible_scores}")

#Step four, assign ability scores
print(f"Next, you need to assign your ability scores. You are a {new_char.job}, so your most important stats are")

#Step 5, roll for expertises for job type

#