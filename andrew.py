def dicksucking(doses, length):
    #you can only deepthroat a dick if the length of the dick is less than 5
    #or you took at least 3 doses of magic mouthwash
    if doses >= 3 or length < 5:
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
