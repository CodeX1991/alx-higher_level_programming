#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character

    Args:
        sentence: the string to work with

    Return:
        length of the tuple if sentence is not empty with first char
        otherwise return None
    """
    if sentence == "":
        return (len(sentence), None)
    return (len(sentence), sentence[0])
