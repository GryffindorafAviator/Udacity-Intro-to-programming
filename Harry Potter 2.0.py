# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 19:32:06 2017
@author: flash_pilot
"""

import random

textOfCharms = """
You were standing in front of an ancient house.
The house was empty and the door was locked.
You took your wand out and said __1__. 
As you finished your spell, the door opened.
In the darkness, you said __2__ and the wand was lit up.
You saw something on the floor ahead, but you couldn't identify what it was. 
So you pointed it with your wand, saying __3__, and suddenly it floated up in the air.
It was a flying broom.
All of a sudden, you heard someone saying a curse at you in the darkness, 
so you shouted __4__, and the curse was rebound.
The person fell down on the floor, so you approached him and accessed his mind by saying __5__.
You realized he was a Death Eater and fighting him would be a losing game.
So you said __6__ to summon your broom and said __7__ to extinguish the light on the wand.
You mounted your broom and left.
"""

textOfRunes = """
1,fehu
A, aurochs, water, slag   B, wealth, cattle C, the god Thor, giant  D, one of the Asir (gods)
2,raido
A, ride, journey  B, ulcer (or kenaz "torch")  C, gift  D, joy
3,hagalaz
A, year, good year, harvest  B, need  C, ice  D, hail (the precipitation)
4,teiwaz
A, yew-tree  B, unclear, possibly "elk"  C, the god Tyr  D, meaning unclear, perhaps "pear-tree"
5,sowilo
A, sun  B, birch  C, horse  D, man
6,laguz
A, the god Yngvi B, water, lake C, heritage, estate, possession  D, day 
"""

textOfDADA = """
1, Makes the person or animal can't move like a stone.
2, Remove wand from your opponent.
3, A charm used to defeat Boggart.
4, A charm used to defeat Dementor.
5, Unforgivable curse, kill others.
6, Knock out others. 
"""

textOfAstronomy = """
In ancient times, many people believed the __A__ was a flat disc. 
Well over 2,000 years ago, the ancient Greek philosophers were able to put forward two good arguments proving that it was not. 
Direct observations of heavenly bodies were the basis of both these arguments. 
First, the __B__ knew that during eclipses of the __D__ the __A__ was between the sun and the __D__, 
and they saw that during these eclipses, the earth's shadow on the __D__ was always round, 
they realized that this could be true only if the __A__ was spherical. 
If the __A__ was a flat disc, then its shadow during eclipses would not be a perfect circle, it would be stretched out into a long ellipse. 
The second argument was based on what the __B__ saw during their travels. 
They noticed that the North Star, or __C__, appeared lower in the sky when they traveled south, in the more northerly regions, 
the North Star appeared to them to be much higher in the sky. 
By the way, it was also from this difference in the apparent position of the North Star that the __B__ first calculated 
the approximate distance around the circumference of the __A__, a figure recorded in ancient documents says 400.000 stadia, 
that's the plural of the word stadium. 
Today, it's not known exactly what length one stadium represents, 
but let's say it was about 200 meters, the length of many athletic stadiums. 
This would make the Greek's estimate about twice the figure accepted today, 
a very good estimate for those writing so long before even the first telescope was invented.
"""

textOfBonus = ["Bonus", "Do you know how to use the Marauder's Map?",
              "When you want to let the Marauder's Map show you people's trace, you should say: __1__.",
              "And when you finished your spying, you should say: __2__."]

qusOfCharms = ["You took your wand out and said __1__ .",
               "In the darkness, you said __2__ and the wand was lit up.",
               "So you pointed it with your wand, saying __3__ and suddenly it floated up in the air. It was a flying broom.",
               "All of a sudden, you heard someone saying a curse at you in the darkness, so you shouted __4__ and the curse was rebound.",
               "The person fell down on the floor, so you approached him and accessed his mind by saying __5__ .",
               "So you said __6__ to summon your broom", "and said __7__ to extinguish the light on the wand."]

qusOfRunes = ["fehu","raido","hagalaz","teiwaz","sowilo","laguz"]

qusOfDADA = ["makes the person or animal can't move like a stone",
             "removes wand from your opponent",
             "used to defeat Boggart",
             "used to defeat Dementor",
             "is an unforgivable curse, used to kill others",
             "knocks out others"]

qusOfAstromony = ["In ancient times, many people believed the __A__ was a flat disc.",
                  "The second argument was based on what the __B__ saw during their travels.",
                  """They noticed that the North Star, or __C__ , appeared lower in the sky when they traveled south, in the more northerly regions, 
                the North Star appeared to them to be much higher in the sky.""",
                  "The earth's shadow on the __D__ was always round."]

qusOfBonus = [textOfBonus[2], textOfBonus[3]]

blanksNum = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__"]

blanksRunes = ['wealth, cattle', 'ride, journey', 'hail (the precipitation)', 'the god Tyr', 'sun', 'water, lake']

blanksAlp = ['__A__', '__B__', '__C__', '__D__']

blanksBonus = ['__1__', '__2__']

charmsStr = "Alohomora,Lumos,Wingardium Leviosa,Protegos,Legilimens,Accio Firebolt,Nox"

runesStr = "B,A,D,C,A,B"

dadaStr = "Petrificus Totalus,Expelliarmus,Riddikulus,Expecto Patronus,Avada Kedavra,Stupefy"

astronomyStr = "earth,Greeks,Polaris,moon"

bonusList = ["I solemnly swear that I am up to no good.", "Mischief managed."]

def subChoose():
    """Choose your test subject."""

    print "Please Choose Subject:\n\n1, Carms\n2, Runes\n3, Defence Against Dark Arts\n4, Astronomy\n5, Bonus"

def randomOutput(ml_string):
    """Print out the answer list in a random order."""

    ml_stringList = ml_string.split(',')
    lenMl = len(ml_stringList)
    randSample = random.sample(ml_stringList, lenMl)
    randList = ','.join(randSample)
    return randList

def word_in_pos(word, blanks):
    """Used to find the blank in the string."""

    for pos in blanks:
        if pos in word:
            return pos
    return None

def play_game(ml_string, ansList, subList, i):
    """Used to replace the blank with the answer."""

    ml_stringList = ml_string[i].split()
    replaced = []
    for word in ml_stringList:
        replacement = word_in_pos(word, ansList)
        if replacement != None:
            replaced.append(subList[i])
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

def ansJudge(ansList, ml_string, blanksList, i):
    """Judge the answer of fill in the blank question."""

    ansInput = raw_input('Please fill in the first blank: ')
    i = 0

    while i < len(ansList) - 1:
        if ansInput == ansList[i]:
            print "Great! " + play_game(ml_string, blanksList, ansList, i)
            i += 1
            ansInput = raw_input('Please enter your answer for the next blank: ')
        else:
            print "Nice try, but please try it again."
            ansInput = raw_input('Please enter your answer again: ')

    while i == len(ansList) - 1:
        if ansInput == ansList[i]:
           print "Great! " + play_game(ml_string, blanksList, ansList, i) + "\nYou have past this test!"
           break
        else:
            print "Nice try, but please try again."
            ansInput = raw_input('Please enter your answer again: ')

def ansJudgeRunes(ml_string, qusList, ansList, i):
    """Judge the answer in choice question of Runes."""

    ansInput = raw_input('Please fill in the first blank: ')
    ml_stringList = ml_string.split(',')
    i = 0

    while i < len(ml_stringList) - 1:
        if ansInput == ml_stringList[i]:
            print"Great! The meaning of " + qusList[i] + " is: " + ansList[i]
            i += 1
            ansInput = raw_input('Please enter your answer for the next blank: ')
        else:
            print "Nice try, but please try it again."
            ansInput = raw_input('Please enter your answer again: ')

    while i == len(ml_stringList) - 1:
        if ansInput == ml_stringList[i]:
            print"Great! The meaning of " + qusList[i] + " is: " + ansList[i] + "\nYou have past this test!"
            break
        else:
            print "Nice try, but please try again."
            ansInput = raw_input('Please enter your answer again: ')

def ansJudgeDada(ml_string, qusList, i):
    """Judge the answer in choice question of DADA."""

    ansInput = raw_input('Please fill in the first blank: ')
    ml_stringList = ml_string.split(',')
    i = 0

    while i < len(ml_stringList) - 1:
        if ansInput == ml_stringList[i]:
            print"Great! The charm " + qusList[i] + " is " + ml_stringList[i] + '.'
            i += 1
            ansInput = raw_input('Please enter your answer for the next blank: ')
        else:
            print "Nice try, but please try it again."
            ansInput = raw_input('Please enter your answer again: ')

    while i == len(ml_stringList) - 1:
        if ansInput == ml_stringList[i]:
            print"Great! The charm " + qusList[i] + " is " + ml_stringList[i] + '.' +"\nYou have past this test!"
            break
        else:
            print "Nice try, but please try again."
            ansInput = raw_input('Please enter your answer again: ')

def toDoOrNotToDo(i):
    """To determine whether you have finished all the tests."""
    print '\nDo you want to finish the rest of the test?'
    choice = raw_input('Please enter Y or N.')
    print ''
    return choice

def congratulations():
    print 'Congratulations! You have finished all the tests!'

def althoughITHinkItisNonesenseJusttoSatisfytheRequire():
    print """
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
    #                 Ordinary Wizarding Level                 #
    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
    
    ######                   Caution                       #####
    
    ###  This test is protected by Anti - Cheating Spell     ###
    """

althoughITHinkItisNonesenseJusttoSatisfytheRequire()

i = 0 # First to use i to denote the times of iteration is very common in programing no matter in C++, Java or other languages,
      # and to change i into other expression means I need to change every i in the following parts,
      #and that means a lot of scrutiny and big potential of mistakes,
      #but the whole codes is running normal already.
      #So take the reason the reviewer gave and the consequences it may caused I will not to change the name i.

while True:
    subChoose()
    subject = int(raw_input())

    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

    if subject == one:
        if i == 5:
            congratulations()
            break
        else:
            print '\nFill in the blanks with the appropriate charms.\n' + textOfCharms + '\nYou may choose your answer from the following list:\n' + randomOutput(
                charmsStr)
            charmsList = charmsStr.split(',')
            print '\nHint: Notice the uppercase and lowercase!\n'
            ansJudge(charmsList, qusOfCharms, blanksNum, 0)
            print ''
            if toDoOrNotToDo(i) == 'Y':
                i += 1
                print ''
                continue
            else:
                print '\nSee you!\n'
                break

    elif subject == two:
        if i == 5:
            congratulations()
            break
        else:
            print '\nPlease choose the correct explanation for the Runes.\n' + textOfRunes
            runesList = runesStr.split(',')
            print '\nHint: Notice the uppercase and lowercase!\n'
            ansJudgeRunes(runesStr, qusOfRunes, blanksRunes, 0)
            print ''
            if toDoOrNotToDo(i) == 'Y':
                i += 1
                print ''
                continue
            else:
                print '\nSee you!\n'
                break

    elif subject == three:
        if i == 5:
            congratulations()
            break
        else:
            print '\nWhich charm is the sentence explain for?\n' + textOfDADA
            print '\nYou may choose your answer from the following list:\n'
            print randomOutput(dadaStr)
            dadaList = dadaStr.split(',')
            print '\nHint: Notice the uppercase and lowercase!\n'
            ansJudgeDada(dadaStr, qusOfDADA, 0)
            print ''
            if toDoOrNotToDo(i) == 'Y':
                i += 1
                print ''
                continue
            else:
                print '\nSee you!\n'
                break

    elif subject == four:
        if i == 5:
            congratulations()
            break
        else:
            print '\nFill in the blanks.\n' + textOfAstronomy
            print '\nYou may choose your answer from the following list:\n'
            print randomOutput(astronomyStr)
            print '\nHint: Notice the uppercase and lowercase!\n'
            astronomyList = astronomyStr.split(',')
            ansJudge(astronomyList, qusOfAstromony, blanksAlp, 0)
            print ''

            astronomyList = astronomyStr.split(',')
            ansJudge(astronomyList, qusOfAstromony, blanksAlp, 0)
            print ''
            if toDoOrNotToDo(i) == 'Y':
                i += 1
                print ''
                continue
            else:
                print '\nSee you!\n'
                break

    elif subject == five:
        if i == 5:
            congratulations()
            break
        else:
            print ''
            print textOfBonus[0]
            print textOfBonus[1]
            print textOfBonus[2]
            print textOfBonus[3]
            print '\nHint: Notice the uppercase and lowercase!\n'
            ansJudge(bonusList, qusOfBonus, blanksBonus, 0)
            print ''
            if toDoOrNotToDo(i) == 'Y':
                i += 1
                print ''
                continue
            else:
                print '\nSee you!\n'
                break

    else:
        print "Wrong input, please input again."
