(sentence):
    if len(sentence) == 0:
        i = len(sentence), None
        return i
    i = len(sentence), sentence[0]
    return i
