#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ""):
        new = (0, None)
        return new
    new = (len(sentence), sentence[0])
    return new
