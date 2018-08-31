import random
import time

secrets = random.SystemRandom()


def randint(a, b):
    return secrets.randint(a, b)


def randcode(length):
    a = secrets.randint(0, 9)
    for i in range(length - 1):
        a += secrets.randint(9, int(i ** 9 + 9)) % 9
    return a


def randchoice(seq):
    return secrets.choice(seq)


def sleep(milliseconds):
    seconds = milliseconds / 1000
    return time.sleep(seconds)


def sign(x):
    return 1 - (x <= 0)


def clamp(val, _min, _max):
    return min(max(_min, val), _max)
