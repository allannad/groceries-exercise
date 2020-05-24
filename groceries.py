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
#print(number_prods)
print('-'*10)
print("THERE ARE " ,number_prods, " PRODUCTS")
print ('-'*10)

#remove irrelevant keys to create pared down dictionary
#rem_list = ['id', 'department', 'aisle'] 
#create new dictionary: updated_dict
#[products.pop(key) for key in rem_list] 
#products.pop('department')
#products.pop('aisle')



names = [x['name'] for x in products]

prices = [x['price'] for x in products]
formattedprices = ["($%.2f)" % x for x in prices]
arr = {key: value for key, value in zip(names, formattedprices)}

#print(arr)
#now have items as keys, prices as values
print('\n'.join("   + {} {}".format(k, v) for k, v in arr.items()))


#BELOW CODE to use return sorted names
#names = sorted(names)
#print(sorted(names))
#print(names[0])

#name_price = names.append(prices)
#print(name_price)

#arr = names
#arr2 = []
#for i in arr:
#  arr2.append(prices)
#print(arr)
#print(arr2) 




#---
#then, add the departments
#dashed lines, "THERE ARE XX DEPARTMENTS" dashed lines
#"+ " "Department" (X products)
#HINT: use the filter() function or the filtering 
#capabilities of a list comprehension to lookup all 
# #products associated with any given department
# #then use the len() function to count them

