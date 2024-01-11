from random import choice, randint



def get_response(user_input:str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'speak to me please...'
    elif 'hello' in lowered:
        return 'Hey shawty'
    elif 'how are you' in lowered:
        return 'Feeling horrible'
    elif '!roll' in lowered:
        return f'Rolled {randint(1,6)}' # will send a random number
    else:
        return choice(['I don\'t understand ;-;',
                      'I am not sure what you\'re saying...',
                      ]) # will pick between these two dialogues if it doesn't understand


