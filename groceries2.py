import csv
products = []
csv_path = "products.csv"
with open(csv_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        row["price"] = float(row["price"])
        products.append(row)


print(products)

