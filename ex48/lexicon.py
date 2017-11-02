def scan(string_input):

    words = string_input.split()
    sentance = []

    for word in words:
        token, word = classify(word)
        sentance.append((token, word))
    return sentance

def classify(WORD):

    directions = [ 'north', 'south', 'east', 'west', 'down',
                   'up', 'left', 'right', 'back']
    verbs = ['go', 'stop', 'kill', 'eat']
    stops = ['the', 'in', 'of', 'from', 'at', 'it']
    nouns = ['door', 'bear', 'princess', 'cabinet']

    if WORD in directions:
        TOKEN = 'direction'
    elif WORD in verbs:
        TOKEN = 'verb'
    elif WORD in stops:
        TOKEN = 'stop'
    elif WORD in nouns:
        TOKEN = 'noun'
    elif convert_number(WORD) != None:
        TOKEN = 'number'
        WORD = convert_number(WORD)
    else:
        TOKEN = 'error'

    return(TOKEN,WORD)


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
