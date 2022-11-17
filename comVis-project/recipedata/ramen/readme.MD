# Recipe files

## important: you may not share any of the data here or make it available publicly online

Some files/directories may be empty if there's no match.

### Spoonacular
Files in the spoonacular directory with the -recip- name are recipe files
obtained from the spoonacular api (https://spoonacular.com/food-api) given
the query (e.g., 'tomato sauce') for the food item. These may include
recipes that simply have the recipe (e.g., use tomato sauce like pizza) and
are not recipes *for* that item (e.g., a recipe of how to make tomato sauce).

Each recipe is in a .json file and there is an example python notebook file 
(parserecipe.ipynb) that shows you how to parse the file. There are 
ingredients, steps, nutritional facts, etc. I retrieve a max of 500 results, 
but in most cases there are far less.

### Allrecipes

allrecipes.jsonl contains recipes that match the query scraped from
allrecipes.com. Each line is a json object so read the file one line
at a time.

These recipes came from: https://archive.org/download/recipes-en-201706

### BBC recipes
bbc.jsonl contains recipes scraped from the BBC. Each line is a json
object so read the file one line at a time.

I *believe* the recipes came from: https://github.com/mneedham/bbcgoodfood

### Openrecipes
openrecipes.jsonl contains recipes from the openrecipes dataset
https://github.com/fictivekin/openrecipes. Each line is a json
object so read the file one line at a time.

### Food.com
foodcom.csv is a csv file containing matched recipes from
https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews

### RecipeNLG
recipenlg.csv is a csv file containing matched recipes from
https://github.com/Glorf/recipenlg
