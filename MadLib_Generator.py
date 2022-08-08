"Mustafa Al-Saeed"
"mustafa.o.alsaeed@gmail.com"

""" Mad Libs Generator
----------------------------------------
"""
loop = 1
#this means we can do it 10 times per run
while (loop < 10):
    name = input("choose a name: ")
    sport = input("choose a sport: ")
    pro= input ("choose a profession: ")
    pro1 = input ("choose a second profession: ")
    ret = input ("choose age of retiremnt: ")


    print("-------------------------------------------")
    print(name, "has been playing", sport," for 20 years")
    print("he first started as a",pro,"then he moved on to",pro1)
    print("eventually he retired at the age of:", ret)

    #adding to loop

    loop = loop +1

