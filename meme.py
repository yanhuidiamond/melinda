def cursedNameExorcism(name):
    blessed_name = ""
    for letter in name:
        if letter == "k":
            blessed_name+="c"
        else:
            blessed_name+=letter
    return blessed_name

def lastDigitOfPi():
    import math
    return str(math.pi)[-1]

def wheresMelinda():
    from random import random
    num = int(2**(random()*10))
    for x in range(num):
        print("Where's Melinda",end=" ")
    print(num)

def peakComedy():
    from random import randrange
    word_list = ["huskies", "fish", "friends", "food"]
    return "{} are {}, not {}".format(word_list[randrange(len(word_list))], word_list[randrange(len(word_list))], word_list[randrange(len(word_list))])

def shouldIWearScarf(name,temp):
    if name=="Melinda" and temp<85:
        return True
    return False

def willage():
    from random import randrange
    word_list = ["ill", "age", "est"]
    return "W{} V{}{}".format(word_list[randrange(len(word_list))], word_list[randrange(len(word_list))], word_list[randrange(len(word_list))])

def trueBalance():
    import random
    list1 = ["tr","ue","bal","ance"]
    list2 = ["everything","you","want","nothing","you","cant"]
    random.shuffle(list1)
    random.shuffle(list2)
    print("{}{} {}{}: {} {} {} {} {} {}".format(list1[0],list1[1],list1[2],list1[3],list2[0],list2[1],list2[2],list2[3],list2[4],list2[5]))

def guessTheNumber():
    import random
    num = random.randrange(1,1001)
    guess = 1001
    count = 0
    while num!=guess:
        try:
            guess = int(input("Guess a number between 1 and 1000    "))
            count+=1
        except:
            print("\nFuck you that's not a number, try again\n\n")
            count+=1
            continue
        if "69" in str(guess):
            print("\nNice.")
        if "420" in str(guess):
            print("\nSick nasty bro")
        if abs(guess-num)>300:
            print("\nAre you serious right now\n\n")
        elif guess<num:
            print("\nbruh its higher than that\n\n")
        elif guess>num:
            print("\nlowerrrrrrr\n\n")
        else:
            print("i dont even fuckin know")
    print("\nThat took you {} tries. Sad.".format(count))

def guess():
    while True:
        x = input("Guess:  ")
        if "69" in x or "420" in x:
            print("\nnice")
        if "42" in x:
            print("\n42 is the meaning of life, but incorrect")
        if "password" in x:
            print("\nThe password is not password")
        if "fuck" in x:
            print("\nWatch your fucking language")
        print("\nwrong")

def gatechBuildings():
    from random import shuffle
    b = ["Clough","Crosland", "North Avenue Dining", "West Village", "Student Center", "CRC"]
    shuffle(b)
    print("Welcome to Georgia Tech! Make sure you visit the newly renovated {} building, but unfortunetly the {} building is closed for construction and the {} building recently experienced a suicide attempt".format(b[0],b[1],b[2])) 

def admissions(GPA,race,gender,instate):
    chance = .4
    if instate == False:
        chance = chance/2
    if race == "w":
        chance = chance/1.2
    elif race == "a":
        chance = chance/1.5
    elif race == "b":
        chance = chance*1.5
    else:
        pass
    if gender == "f":
        chance = chance*1.5
    elif gender == "m":
        chance = chance/1.5
    else:
        pass
    if GPA > 3.8:
        chance = chance*2
    elif GPA > 3.5:
        chance = chance*1.5
    elif GPA < 3:
        chance = chance/1.5
    elif GPA < 2.7:
        chance = chance/2
    elif GPA < 2.4:
        chance = chance/4
    elif GPA < 2.1:
        chance = chance/8
    else:
        pass
    if chance > .7:
        print("High Chance")
    elif chance > .4:
        print("Moderate Chance")
    elif chance > .15:
        print("Low Chance")
    else:
        print("No Chance")
    if chance>1:
        chance = 1
    print("({}%)".format(int(chance*100)))
    
def dicksucking(succ_potion_doses, length):
    #you can only deepthroat a dick if the length of the dick is less than 5
    #or you took at least 1 dose of succ potion for each additional 2 inches
    if length-(1/2)*succ_potion_doses<5:
        deepthroat = True
    else:
        deepthroat = False
    print(deepthroat)

def nave():
    import random
    list2 = ["forks","spoons","knives"]
    list3 = ["n","a","v","e"]
    list1 = ["food","happiness","horse meat","dignity","cups","plates", "depression"]
    random.shuffle(list1)
    random.shuffle(list3)
    random.shuffle(list2)
    print("Welcome to {}{}{}{}! In the silverware container we have {} at the top, {} in the middle, and {} at the bottom. We are currently running low on {} but have plenty of {}.".format(list3[0],list3[1],list3[2],list3[3],list2[0],list2[1],list2[2],list1[0],list1[1]))


def tinder(age,gender):
    import random
    list = [-500,-50,-34,-27,0,-4,-78]
    random.shuffle(list)
    if age < 18:
        print("Jailbait!")
    if age >= 18 and gender == "female":
        print("hey, you wanna see my dick?")
    if age >= 18 and gender == "male":
        print("you have {} matches".format(list[0]))

def credithours():
    import random
    hours = random.randrange(0,600)
    if hours < 30:
        year = "a freshman by credit hours"
    elif hours >= 30 and hours < 60:
        year = "a sophomore by credit hours"
    elif hours >= 60 and hours < 90:
        year = "a junior by credit hours"
    elif hours >= 90 and hours < 120:
        year = "a senior by credit hours"
    elif hours >= 120 and hours < 400:
        year = "a super-senior"
    else:
        year = "dead"
    print("You have {} hours. This makes you {}.".format(hours, year))
    
def shouldWeGoToRecitation():
    print("no")
    print("william is much more than 10 steps ahead now")
   
def dice():
    import random
    print(random.randrange(1,7)
    print(random.randrange(1,7)

        
