#Import statements
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
import json

#Getting the JSON data
data = json.load(open("data.json",'r'))

#Input
def gettingUserInput():
    return input("Enter the word you want : ")
#Output
def gettingOutput(get):
    #making the input lowercase
    get = get.lower()
    if get in data:
        return data[get]
    elif get.title() in data:
        return data[get.title()]
    elif get.upper() in data:
        return data[get.upper()]
    elif len(get_close_matches(get,data.keys(),3,0.7)) > 0:
        askey = input("Did you mean "+"\n"+"1. "+get_close_matches(get,data.keys(),3,0.7)[0]+"\n"
                      +"2. "+get_close_matches(get,data.keys(),3,0.7)[1]+"\n"
                      +"3. "+get_close_matches(get,data.keys(),3,0.7)[2]+"\n"
                      +" instead ?(Type the letter in the next to the word)"
                      +"\n"+" Type 0 to return  to main")
        if askey == "1":
            return data[get_close_matches(get,data.keys(),3,0.7)[0]]
        elif askey == "2":
            return data[get_close_matches(get,data.keys(),3,0.7)[1]]
        elif askey == "3":
            return data[get_close_matches(get,data.keys(),3,0.7)[2]]
        elif askey == "0":
            main()
        else:
            print("The word " + get + " is incorrect, please check it again.")
            # Recursive Function
            main()

    else:

        print("The word " + get + " is incorrect, please check it again.")
        #Recursive Function
        main()

#Default Thread
def main():
    listobject = gettingOutput(gettingUserInput())
    if type(listobject) is list:
        for element in listobject:
            print(element)

ask = "y"

#Sentinel Check
while ((ask == "y")|(ask == "Y")):
    main()
    ask = input("\n"+"Do you want to enter more Words? (Yes - y / No - n)\n")

#Inverse Sentinel in the program
if (ask != "y"):
    print("The prgram is exiting.")