'''
Code to create a secret santa generator
Karl Zodda

Notes-
I want there to be a feature where the person in charge types in names.
Then anonymously people go through and select people. You should have to enter your name so that you cannot choose yourself. You should be able to pass on two people or if there are only two- you cannot pass. 
'''
## Importing packages
import random

def secret_santa(people_to_pick, people_tobe_picked):
    ## empty dictionary holding who has what person to keep track. 
    dict = {}
    ## Now we have two lists. One to pick and one to be picked
    #While there are still people to pick
    while len(people_to_pick) > 0:
        #Enter a name
        name = input('Please Enter Your Name:')
        #If the name does not match up have them re-enter a new name
        if name not in people_to_pick:
            continue
        # Creating a new list of choices
        choices = people_tobe_picked.copy()
        ## Removing the person picking's name from choices
        if name in choices:
            choices.remove(name)
        i = 0
        threshold = min(3, len(choices))
        while i < threshold:
            random_int = random.randint(0,(len(choices)-1))
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
    return dict
