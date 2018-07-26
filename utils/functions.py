import random


def get_ticket():
    ticket = ''
    s = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for x in range(100):
        ticket += random.choice(s)
    return ticket
















