import json
import os

# File to store products
DATA_FILE = "products.json"


def load_products():
    """Load products from file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}  # Empty dict if file doesn't exist


def save_products(products):
    """Save products to file"""
    with open(DATA_FILE, "w") as f:
        json.dump(products, f, indent=2)


def show_menu():
    """Display the main menu"""
    print("\n=== INVENTORY TRACKER ===")
    print("1. View all products")
    print("2. Add new product")
    print("3. Update product quantity")
    print("4. Delete product")
    print("5. Exit")
    print("=" * 25)


def main():
    """Main program loop"""
    products = load_products()  # Load products at start

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            print("View products - coming soon!")
        elif choice == "2":
            print("Add product - coming soon!")
        elif choice == "3":
            print("Update quantity - coming soon!")
        elif choice == "4":
            print("Delete product - coming soon!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()
