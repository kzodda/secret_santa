'''
Code to create a secret santa generator
Karl Zodda

Notes-
I want there to be a feature where the person in charge types in names.
Then anonymously people go through and select people. You should have to enter your name so that you cannot choose yourself. You should be able to pass on two people or if there are only two- you cannot pass. 
'''

#people = input('Hello please add a list of names seperated by commas:')
people = 'Jack,John,Karl,Martha,Ella,Mike,John'
## Creates a string. Need to split on commas for it to work
lst_people = list(people.split(','))
## Now it is a list of people that can be used. 

## I am going to copy the list so there are two lists. One for the people who need to pick and the other for people who need to be picked. 
people_tobe_picked = lst_people.copy()
print('This is the people who need to pick', lst_people)
print('This is people to be picked', people_tobe_picked)
