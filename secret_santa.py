'''
Code to create a secret santa generator
Karl Zodda

Notes-
I want there to be a feature where the person in charge types in names.
Then anonymously people go through and select people. You should have to enter your name so that you cannot choose yourself. You should be able to pass on two people or if there are only two- you cannot pass. 
'''
## Importing packages
import random

## empty dictionary holding who has what person to keep track. 
dict = {}
#people = input('Hello please add a list of names seperated by commas:')
## I created a string of people so I don't have to input names every single time I run the code
people = 'Jack,John,Karl,Martha,Ella,Mike,John'
## Splits the names by commas and puts the names into a list.
people_to_pick = list(people.split(','))
## Now it is a list of people that can be used. 

## I am going to copy the list so there are two lists. One for the people who need to pick and the other for people who need to be picked. 
## I need to do .copy() otherwise alias
people_tobe_picked = people_to_pick.copy()


while len(people_to_pick) > 0:
    name = input('Please Enter Your Name:')
    if name not in people_to_pick:
        continue
    choices = people_tobe_picked.copy()
    if name in choices:
        choices.remove(name)
    i = 0
    threshold = min(3, len(choices))
    while i < threshold:
        random_int = random.randint(0,len(choices))
        print('Here is your choice:', choices[random_int])
        if (threshold - i) > 1:
            selection = input('To skip press 0, To confirm press any other key:')
        else:
            selection = 'Required'
            ## If they don't like the selection
        if selection == '0':
                ## pop the value from the list
            choices.pop(random_int)
                ## update i so there is a count
            i += 1
            ## If selection is yes they are sticking with it
        else:
            if selection == 'Required':
                print("Can't reject, as you are out of choices\n")
            else:
                print('Choice confirmed \n')
            people_tobe_picked.remove(choices[random_int])
            people_to_pick.remove(name)
            dict[name] = choices[random_int]
            break
print("\nFollowing are the Secret Santa matches:\n")       
print(dict)
