"""A module to provide writing inspiration!"""

import random
import time


class Story(object):
    def __init__(self, name):
        self.name = name

    def get_genre(self):
        """Picks a random selection from a genre lsit and returns that value."""
        genre = ['MYSTERY', 'HORROR', 'ADVENTURE']
        selection = random.choice(genre)
        return selection


    def get_character(self, selection):
        """Picks a random character based on genre type argument."""
        if selection == 'MYSTERY':
            return random.choice(['THIEF', 'DETECTIVE', 'FBI AGENT'])
        elif selection == 'HORROR':
            return random.choice(['GHOST', 'VAMPIRE', 'WITCH'])
        else:
            return random.choice(['COMMANDO', 'COWBOY', 'SPACEWOMEN'])


    def get_story_content(self, character):
        """Picks a random setting and plot based on character type argument."""
        if character in ['THIEF','DETECTIVE', 'FBI AGENT']:
            setting = random.choice(['A MUSEUM AT NIGHT', 'THE HIGHSCHOOL', 'AREA 51'])
            plot = random.choice(['A PRICELESS JEWEL IS STOLEN',
                                  'THE PRINCIPAL GOES MISSING',
                                  'UNEXPLAINED PHENOMENA TAKING PLACE'])
        elif character in ['GHOST', 'VAMPIRE', 'WITCH']:
            setting = random.choice(['A CEMETARY','NEW ORLEANS','THE DEEP, DARK WOODS'])
            plot = random.choice(['SPOOKY SOUNDS BEING HEARD',
                                  'EERIE SIGHTINGS TAKING PLACE',
                                  'A DEEP CHILL BEING FELT'])
        else:
            setting = random.choice(['A JUNGLE', 'A VOLCANO', 'THE PYRAMIDS'])
            plot = random.choice(['ALIENS HAVE LANDED', 'A MASSIVE EARTHQUAKE', 'A TIDAL WAVE INBOUND'])
        return setting, plot


def calculation_text():
    """Text simulation of a computer working."""
    time.sleep(1)
    print("\t3...*** smashing binaries together ***")
    time.sleep(1)
    print("\t2...*** cleaning up the damage ***")
    time.sleep(1)
    print("\t1 - *** results generated! ***\n")
    time.sleep(1)


def roll_a_story():
    """Get user's name and create story instance."""
    print("""
Welcome to the Roll a Story creator, where a magic number generator helps you pick story elements
to craft your tale!\n""")

    name = input("What's your name, fair writer? ")
    print(f"{name}, that is a lovely name!\n")
    time.sleep(2)

    # create story instance
    story = Story(name)

    print("Let's summon the magic number generator to help you pick a genre for your story!\n")
    genre = story.get_genre()
    calculation_text()
    print(f"You've got {genre} {name}. Exciting...!\n")
    time.sleep(5)

    print("OK, lets find a good character for you...\n")
    character = story.get_character(genre)
    calculation_text()
    print(f"Oh nice! You will write about a {character}....!\n")
    time.sleep(5)

    print(f"OK {name}, we have a genre and a character! We better find out what the plot and setting is shouldn't we!\n")
    setting, plot = story.get_story_content(character)
    time.sleep(3)
    calculation_text()
    print(f"""Wow, that was intense! I think my work is complete.\nOK. This is all occurring at {setting}.
    \nAnd guess what.....?!\n""")
    time.sleep(3)
    print(f"{plot}!!!!\n")
    time.sleep(3)
    print(f"""So to summarise.....\n
You have a {character} in a {genre} story, where {plot} happens in {setting}!\n
""")
    time.sleep(3)
    roll_again(name)

def roll_again(name):
    """Cycles through the story-generation process or quit."""
    choice = input("Shall I 'Roll Another Story'? (y/N) ")
    if choice == 'y':
        print(f"OK {name}.... here we go again!\n")
        new_story = Story(name)
        genre = new_story.get_genre()
        character = new_story.get_character(genre)
        setting, plot = new_story.get_story_content(character)
        calculation_text()
        print(f"""This time you have...\n{character} in a {genre} story, where {plot} happens in {setting}!\n\n""")
        time.sleep(5)
        roll_again(name)
    else:
        print("Few....my circuits need a rest! I look forward to reading the story. Bye for now!\n")


# python's unique way to see if a file is a module for importing or to be executed
if __name__ == "__main__":
    roll_a_story()









