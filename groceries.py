# groceries.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output
#begins with dashed lines, then "THERE ARE XX PRODUCTS" then dashed lines
#alphabetized
#provide max ID on the products
#Format: "+ " "name" ($XX.YY)
seq = [x['id'] for x in products]
number_prods = max(seq)
#print(len(products))
#print(number_prods)
print('-'*10)
print("THERE ARE " ,number_prods, " PRODUCTS:")
print ('-'*10)

#how to loop through and print name
for x in products:
    print(x["id"])


#remove irrelevant keys to create pared down dictionary
names = [x['name'] for x in products]
prices = [x['price'] for x in products]
formattedprices = ["($%.2f)" % x for x in prices]
arr = {key: value for key, value in zip(names, formattedprices)}
#now have items as keys, prices as values
for key in sorted(arr.keys()):
    print(" + %s %s" % (key, arr[key]))



#------------------------------------------------------------------------------------
#then, add the departments
#dashed lines, "THERE ARE XX DEPARTMENTS" dashed lines
#"+ " "Department" (X products)
#HINT: use the filter() function or the filtering 
#capabilities of a list comprehension to lookup all 
#products associated with any given department
#then use the len() function to count them

#create list of departments, then create set to remove dupes then recreate list
arr_depts = [x['department'] for x in products]
arr1 = list(set(arr_depts))
arr2 = [x.title() for x in sorted(arr1)]
number_depts = len(arr2)
#print intro to number of departments
print('-'*10)
print("THERE ARE",number_depts,"DEPARTMENTS:")
print ('-'*10)

#count number of products per department
#if len of department >1, print "products" else print "product"

drygoodspasta = list(filter(lambda z: z["department"] == "dry goods pasta", products))
drygoodspasta_num = len(drygoodspasta)
if drygoodspasta_num > 1:
    drygoodspasta_num = ('('+ str(drygoodspasta_num) + ' products' +')')
else:
    drygoodspasta_num = ('('+ str(drygoodspasta_num) + ' product' +')')

beverages = list(filter(lambda z: z["department"] == "beverages", products))
beverages_num = len(beverages)
if beverages_num > 1:
    beverages_num = ('('+ str(beverages_num) + ' products' +')')
else:
    beverages_num = ('('+ str(beverages_num) + ' product' +')')

household = list(filter(lambda z: z["department"] == "household", products))
household_num = len(household)
if household_num > 1:
    household_num = ('('+ str(household_num) + ' products' +')')
else:
    household_num = ('('+ str(household_num) + ' product' +')')

frozen = list(filter(lambda z: z["department"] == "frozen", products))
frozen_num = len(frozen)
if frozen_num > 1:
    frozen_num = ('('+ str(frozen_num) + ' products' +')')
else:
    frozen_num = ('('+ str(frozen_num) + ' product' +')')

babies = list(filter(lambda z: z["department"] == "babies", products))
babies_num = len(babies)
if babies_num > 1:
    babies_num = ('('+ str(babies_num) + ' products' +')')
else:
    babies_num = ('('+ str(babies_num) + ' product' +')')

personalcare = list(filter(lambda z: z["department"] == "personal care", products))
personalcare_num = len(personalcare)
if personalcare_num > 1:
    personalcare_num = ('('+ str(personalcare_num) + ' products' +')')
else:
    personalcare_num = ('('+ str(personalcare_num) + ' product' +')')

dairyeggs = list(filter(lambda z: z["department"] == "dairy eggs", products))
dairyeggs_num = len(dairyeggs)
if dairyeggs_num > 1:
    dairyeggs_num = ('('+ str(dairyeggs_num) + ' products' +')')
else:
    dairyeggs_num = ('('+ str(dairyeggs_num) + ' product' +')')

meatseafood = list(filter(lambda z: z["department"] == "meat seafood", products))
meatseafood_num = len(meatseafood)
if meatseafood_num > 1:
    meatseafood_num = ('('+ str(meatseafood_num) + ' products' +')')
else:
    meatseafood_num = ('('+ str(meatseafood_num) + ' product' +')')

snacks = list(filter(lambda z: z["department"] == "snacks", products))
snack_num = len(snacks)
if snack_num > 1:
    snack_num = ('('+ str(snack_num) + ' products' +')')
else:
    snacknum = ('('+ str(snack_num) + ' product' +')')

pantry = list(filter(lambda z: z["department"] == "pantry", products))
pantry_num = len(pantry)
if pantry_num > 1:
    pantry_num = ('('+ str(pantry_num) + ' products' +')')
else:
    pantry_num = ('('+ str(pantry_num) + ' product' +')')

prods = [babies_num,beverages_num,dairyeggs_num,drygoodspasta_num,frozen_num,household_num,meatseafood_num,pantry_num,personalcare_num,snack_num]
dept_prods = {key: value for key, value in zip(arr2, prods)}
print('\n'.join("   + {} {}".format(k, v) for k, v in dept_prods.items()))
