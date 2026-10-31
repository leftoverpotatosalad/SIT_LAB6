from product import Product
from inventory import Inventory
from file_manager import save_inventory, load_inventory

inventory = Inventory()

load_inventory(inventory)

while True:
    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.display_all()

    elif choice == "6":
        print("Exiting program...")
        break

    elif choice == "2":
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Product Stock: "))

        new_product = Product(product_id, name, price, stock)
        inventory.add_product(new_product)

    elif choice == "3":
        product_id = input("Enter Product ID to update: ")

        product = inventory.search_product(product_id)

        if product is not None:
            quantity = int(input("Enter new stock quantity: "))
            product.update_stock(quantity)
        else:
            print("Product not found!")

    elif choice == "4":
        product_id = input("Enter Product ID to search: ")
        product = inventory.search_product(product_id)

        if product is not None:
            print("Product found!")
            product.display_information()
        else:
            print("Product not found!")

    elif choice == "5":
        save_inventory(inventory)

    else:
        print("Invalid choice!")