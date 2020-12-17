'''
Karl Zodda
The code to input user names'''


def names():
    #names = input('Please enter in unique names seperated by commas:')
    names = 'Charles,John,Karl,Mike'
    people_to_pick = list(names.split(','))
    people_tobe_picked = people_to_pick.copy()
    return people_to_pick, people_tobe_picked
