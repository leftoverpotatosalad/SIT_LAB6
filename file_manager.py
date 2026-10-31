import json
from product import Product

def save_inventory(inventory, filename="inventory.json"):

    products_data = []

    for product in inventory.products:
        products_data.append(product.to_dict())

    with open(filename, "w") as file:
        json.dump(products_data, file, indent=4)

    print("Inventory saved successfully!")

def load_inventory(inventory, filename="inventory.json"):

    try:
        with open(filename, "r") as file:
            products_data = json.load(file)

        for data in products_data:
            product = Product(
                data["product_id"],
                data["name"],
                data["price"],
                data["stock"]
            )

            inventory.add_product(product)

        print("Inventory loaded successfully!")

    except FileNotFoundError:
        print("No saved inventory found. Starting with an empty inventory.")