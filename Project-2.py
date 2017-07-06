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
              "When you want to let the Marauder's Map show you people's trace, you should say __1__.",
              "And when you finished your spying, you should say __2__."]

qusOfCharms = ["You took your wand out and said __1__ .",
               "In the darkness, you said __2__ and the wand was lit up.",
               "So you pointed it with your wand, saying __3__ and suddenly it floated up in the air. It was a flying broom.",
               "All of a sudden, you heard someone saying a curse at you in the darkness, so you shouted __4__ and the curse was rebound.",
               "The person fell down on the floor, so you approached him and accessed his mind by saying __5__ .",
               "So you said __6__ to summon your broom", "and said __7__ to extinguish the light on the wand."]
qusOfRunes = ["fehu","raido","hagalaz","teiwaz","sowilo","laguz","wealth, cattle","ride, journey","hail (the precipitation)","the god Tyr","Sun","water, lake"]
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
blanksNum = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__"]
blanksAlp = ['__A__', '__B__', '__C__', '__D__']
charmsStr = "Alohomora,Lumos,Wingardium Leviosa,Protegos,Legilimens,Accio Firebolt,Nox"
runesStr = "B,A,D,C,A,B"
dadaStr = "Petrificus Totalus,Expelliarmus,Riddikulus,Expecto Patronus,Avada Kedavra,Stupefy"
astronomyStr = "earth,Greeks,Polaris,moon"
bonusList = ["I solemnly swear that I am up to no good.", "Mischief managed."]

print "Ordinary Wizarding Level"
print "Caution"
print "This test is protected by Anti - Cheating Spell"

print"Please Choose Subject"


def subChoose():
    print "1, Carms"
    print "2, Runes"
    print "3, Defence Against Dark Arts"
    print "4, Astronomy"
    print "5, Bonus"

def word_in_pos(word, blanks):
    for pos in blanks:
        if pos in word:
            return pos
    return None

def play_game(ml_string, ansList, subList, i):
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

# charmsList's order must be in accord with the correct answer.
def ansJudge(ansList, ml_string, blanksList, i):
    ansInput = raw_input('Please fill in the first blank: ')
    i = 0

    while i < len(ansList)-1:
        if ansInput == ansList[i]:
            print "Great! " + play_game(ml_string, blanksList, ansList, i)
            i += 1
            ansInput = raw_input('Please enter your answer for the next blank: ')
        else:
            print "Good try! Try it again."
            ansInput = raw_input('Please enter your answer again: ')

    while i == len(ansList)-1:
        if ansInput == ansList[i]:
           print "Great! " + play_game(ml_string, blanksList, ansList, i)
           print "You have past this test!"
           break
        else:
            print "Nice try, but please try again."
            ansInput = raw_input('Please enter your answer again: ')

while True:
    subChoose()
    subject = input()

    if subject == 1:
        print "Fill in the blanks with the appropriate charms."
        print textOfCharms
        print charmsStr
        charmsList = charmsStr.split(',')
        print "Hint: Notice the uppercase and lowercase!"
        ansJudge(charmsList, qusOfCharms, blanksNum, 0)
        break
    elif subject == 2:
        print "Please choose the correct explanation for the Runes."
        print textOfRunes
        print runesStr
        runesList = runesStr.split(',')
        print "Hint: The letter of answer should be uppercase!"
        ansJudge(runesList)
        break
    elif subject == 3:
        print "Which charm is the sentence explain for?"
        print textOfDADA
        print dadaStr
        dadaList = dadaStr.split(',')
        print "Hint: Notice the uppercase and lowercase!"
        ansJudge(dadaList)
        break
    elif subject == 4:
        print "Fill in the blanks."
        print textOfAstronomy
        print astronomyStr
        print "Hint: Notice the uppercase and lowercase!"
        astronomyList = astronomyStr.split(',')
        print astronomyList
        ansJudge(astronomyList, qusOfAstromony, blanksAlp, 0)
        break
    elif subject == 5:
        print textOfBonus[0]
        print textOfBonus[1]
        print textOfBonus[2]
        print textOfBonus[3]
        print "Hint: Don't forget the period in your answer!"
        ansJudge(bonusList)
        break
    else:
        print "Wrong input, please input again."
