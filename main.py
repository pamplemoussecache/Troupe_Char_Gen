#!/usr/bin/env python3
import argparse
from random import choice, randrange

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
            if answer.equals("y") or answer.equals("yes"):
                self.principles = [self.principles[1], principle]
            elif answer.equals("n") or answer.equals("no"):
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
print(possible_scores)



#Step three, decide whether to keep ability scores or take 1,2,3,4,5,6

#Step four, assign ability scores

#Step 5, roll for expertises for job type

#