import random


def get_response(message: str) -> str:
    p_message = message.lower()

    #Strings

    a = ['Yes', 'No', 'Yes', 'No']

    b = ['Eshaan', 'Abeer', 'Woojin', 'Aarav', 'Kali kid', 'That one fat kid', 'Drake', 'Miss hema', 'Obama last name(96%)', 'Padia', 'Anoop', 'Yeezu', 'The PE Coaches', 'Indus', 'Miss Wilma'   ]

    #This is a template used to make new cmd's
    if p_message == '05943-template':
        return "Template"
    # Test commands
    if p_message == '!hello':
        return "Sup, nerd!, I'm *Homo erectus*. A primate bot who is just an experiment right now"

    if message == '!roll':
        return str(random.randint(1, 100))

    if p_message == '!help':
        return '`HELP COMMANDS`' \
               '     !hello - Introduction to **homo erectus**     ' \
               '!roll - Basic roll command from 1-100     ' \
               '!Yn - Yes or no command' \
               '!Gay% - Percentage of gayness' \
               '!Gays - Names gay people from a list'

    #String commands
    if message == '!Yn':
        return str(random.randint(1, 2 ))

    if message == '!yn':
        return str(random.choice(a))


    if message == '!Gay%':
        return str(random.randint(20, 100))


    if message == '!gay%':
        return str(random.randint(20, 100))

    if p_message == '!Gays':
        return str(random.choice(b))

    if p_message == '!gays':
        return str(random.choice(b))