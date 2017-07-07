import random

def randomOutput(ml_string):
    ml_stringList = ml_string.split()
    print ml_stringList
    lenMl = len(ml_stringList) + 1

    for i in range(1, lenMl):
        randSample = random.sample(ml_stringList, i)

        print randSample

randomOutput("H, T, E, P")
