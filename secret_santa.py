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
people_tobe_picked = people_to_pick

## I can maybe do it with a while loop
'''
while len > 0 
Enter your name
Find which name it matches
Create a new list of people to be picked
Get rid of the person's name
while hits < 3 so they only have so many chances
Pull a random name
If they like it hit 1 and that is the person. 
If they dislike it hit 0 and it will pop that name and pull a different name.
Outside of while loop say this is the person you have
Remove that person's name from the people_tobe_picked list.
Remove the person who picked someone from the list. 
Say All Done 
'''

## Should I run it in a function and then return a value?
def picking():
    '''Creating a function that does the entire process'''
    while len(people_to_pick) > 0:
        name = input('Please Enter Your Name:')
        choices = people_tobe_picked
        choices.remove(name)
        i = 0
        while i < 3:
            random_int = random.randint(0,len(choices))
            print('Here is your choice:', choices[random_int])
            selection = input('To skip press 0, To confirm press any other key:')
            ## If they don't like the selection
            if selection == '0':
                ## pop the value from the list
                choices.pop(random_int)
                ## update i so there is a count
                i += 1
            ## If selection is yes they are sticking with it
            else:
                ## Adding 300 so the while loop becomes deactivated.
                i += 300
        ## I need to set something up that if i is greater than 3 you get assigned a 
        ## This is the part where I am at a lost. I don't want it to randomly assign a new person after a person has already been selected.
        #if selection == '0':
            
        #second_num = random.randint(0, len(choices))
        #forced
        #print(choices)
picking()