'''
Karl Zodda

Running the final code
'''

## import files

from inputting_name import *
from secret_santa import *

def code():
    names()
    dicti = secret_santa(names()[0], names()[1])
    selection = input('If you are the creator and need to see the results press 1, otherwise press any other key:')
    if selection == '1':
        print(dicti)
    else:
        print('Goodbye')
code()
