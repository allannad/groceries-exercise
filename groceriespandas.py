import pandas as pd

df = pd.read_csv("products.csv")
#assemble list of dictionaries
products = df.to_dict("records")
print(products)