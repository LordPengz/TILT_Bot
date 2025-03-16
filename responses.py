from random import choice, randint


def get_response(user_input: str) -> str:   #this will take the users string input and return it as a string
    lowered: str = user_input.lower() #Python is case-sensitive, so any user input will be processed in lower case

    #Below will be all the responses for user messages

    if lowered == '':
        return "Nothing to say?"
    elif 'hello' in lowered:
        return "Hello there!"
    else:
        return "Repeat that?" #This will output if the user message is outside the specified prompt