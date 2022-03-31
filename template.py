import random

def genRandom_Integer(start, stop):
    return random.randint(start,stop)

def big_loop():
    first = genRandom_Integer(1,9)

#big_loop()     # test the whole big bastard loop

number = genRandom_Integer(1,3)
if number >0 and number <4:
    print("Fuck yeh")
else:
    print("Shit no")