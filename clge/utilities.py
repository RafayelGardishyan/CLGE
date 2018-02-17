import secrets
import time


def randint(a, b):
    return secrets.randbelow(b) + a


def randcode(length):
    a = secrets.randbelow(9)
    for i in range(length - 1):
        b = i
        a += secrets.randbelow(9)
    return a


def randchoice(List):
    return secrets.choice(List)


def sleep(miliseconds):
    seconds = miliseconds / 1000
    return time.sleep(seconds)
