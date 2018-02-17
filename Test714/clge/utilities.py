import random
import time

secrets = random.SystemRandom()

def randint(a, b):
    return secrets.randint(a, b)


def randcode(length):
    a = secrets.randint(0, 9)
    for i in range(length - 1):
        b = i
        a += secrets.randbelow(0, 9)
    return a


def randchoice(seq):
    return secrets.choice(seq)


def sleep(milliseconds):
    seconds = milliseconds / 1000
    return time.sleep(seconds)
