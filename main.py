#!/usr/bin/env python3
import argparse
from random import choice, randrange
from character_classes import *
from abilities import abilities

class TroupeCharacter:
    def __init__(self, job="", name="", expertise=None, equipment=None, abilities=None, principles=None):
        self.name = name
        self.job = job
        self.expertise = expertise
        self.equipment = {"weapon": [], "food": [], "junk": []}
        self.abilities = {
            "skill": 0, 
            "chance": 0, 
            "reaction": 0, 
            "unique": 0, 
            "brawl": 0, 
            "tough": 0
        }
        self.principles = []
    def add_ability(self, ability, value):
        self.abilities[ability] = value
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
    jobs = [Jester, Hedge, Ghelf, Witch, Errant]
    new_job = choice(jobs)
    answer = input(f"You rolled {new_job.class_name}! Would you like to keep it or roll again?")
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
print(f"Next, you need to assign your ability scores. You are a {new_char.job.class_name}, so your most important stats are {new_char.job.favored_stats}")

remaining_abilities = list(abilities.keys())

#A:1 B:1 C:3 D:4 E:6 F:2
#1:Skill 2:Chance 3:Reaction 4:Unique Brawl Tough
print(f"You need to assign values to the following abilities: {remaining_abilities}. Each ability roll converts into a different bonus value depending on the table associated with your class.")

while len(remaining_abilities) > 0:
    curr_ability = input("Which ability do you you want to assign?").lower()
    if curr_ability in remaining_abilities:
        remaining_abilities.remove(curr_ability)
        
        print(f"You're assigning the value for {curr_ability}. As a {new_char.job.class_name}, ability rolls for this ability map to bonuses as follows:")
        stat_dist = new_char.job.stat_distribution[curr_ability]
        print(f"A roll of 1-2: +{stat_dist[0]}")
        print(f"A roll of 3-5: +{stat_dist[1]}")
        print(f"A roll of 6: +{stat_dist[2]}")

        ability_roll = input(f"You have the following ability rolls available {possible_scores}. Type in the ability roll that you would like to assign to this ability.")
        ability_value = 0
        if ability_roll in possible_scores:
            if ability_value == 6:
                ability_value = stat_dist[2]
            elif ability_value >= 3:
                ability_value = stat_dist[1]
            else:
                ability_value = stat_dist[0]
            new_char.add_ability(curr_ability, ability_value)
        else:
            print(f"You've typed a number not in the array you rolled. Try again.")
            continue



#Step 5, roll for expertises for job type