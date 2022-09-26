#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        first_char = 'None'
    else:
        first_char = sentence[0:1]

    str_len = len(sentence)

    the_turple = str_len, first_char
    return the_turple
