import pandas as pd
import numpy as np
#data/recipes.csv
df = pd.read_csv('data/recipes.csv', index_col=0)

def get_recipes(inputs):
    for list_ingreds, list_title, list_instructions in zip(df['ingredients'].tolist(), df.index.tolist(), df['instructions'].tolist()):
        split_ingreds = str(list_ingreds)
        split_ingreds = split_ingreds.split()
        if all(x in split_ingreds for x in inputs):
            print ('\nThe title of the dish is: ')
            print (list_title)
    
            print(f'\nThe List of ingredients for {list_title} are: ')
            print (list_ingreds)
            
            print (f'\nThe instructions to cook {list_title} are: ')
            print (list_instructions)
            print('-'*50)
            
        else:
            continue

available = ['Apple', 'Chicken']
get_recipes(inputs = available)