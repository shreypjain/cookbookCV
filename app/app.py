import pandas as pd
import numpy as np

df = pd.read_csv('../data/recipes.csv')

possibilities = []
def get_recipes(inputs):
    for input_ingred in inputs:
        input_ingred = input_ingred.lower()
    for list_ingreds, list_title, list_instructions in zip(df['ingredients'].tolist(), df['title'].tolist(), df['instructions'].tolist()):
        split_ingreds = str(list_ingreds)
        split_ingreds = split_ingreds.split()
        if all(x.lower() in split_ingreds for x in inputs):
            possibilities.append(list_title)
        else:
            continue
    
    if len(possibilities) > 3:
        for poss in possibilities[:3]:
            for list_ingreds, list_title, list_instructions in zip(df['ingredients'].tolist(), df['title'].tolist(), df['instructions'].tolist()):
                if poss == list_title:
                    print ('\nThe title for this recipe is: ')
                    print (list_title)
                    print ('\nThe ingredients for this recipe are: ')
                    print (list_ingreds)
                    print ('\nThe instructions for this recipe are: ')
                    print (list_instructions)
                    print ('-'*100)
    elif len(possibilities) > 0 and len(possibilities) <= 3:
        for poss in possibilities:
            for list_ingreds, list_title, list_instructions in zip(df['ingredients'].tolist(), df['title'].tolist(), df['instructions'].tolist()):
                if poss == list_title:
                    print ('\nThe title for this recipe is: ')
                    print (list_title)
                    print ('\nThe ingredients for this recipe are: ')
                    print (list_ingreds)
                    print ('\nThe instructions for this recipe are: ')
                    print (list_instructions)
                    print ('-'*100)
    else:
        print (f'Sorry there are no recipes for {inputs}')

available = ['Water', 'Oil', 'Bread', 'Garlic']

get_recipes(inputs = available)
