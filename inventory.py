import json
import os

# File to store products
DATA_FILE = "products.json"


def load_products():
    """Load products from file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}  # Empty dict if file doesn't exist


def save_products(products):
    """Save products to file"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)


def view_products(products):
    """Display all products"""
    if not products:
        print("\nThere are no products in inventory!")
        return

    print("\n=== CURRENT INVENTORY ===")
    print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Quantity':<10}")
    print("-" * 50)

    for product_id, product in products.items():
        print(
            f"{product_id:<5} {product['name']:<20} ${product['price']:<9.2f} {product['quantity']:<10}"
        )
    print("=" * 50)


def add_product(products):
    """Add a new product"""
    print("\n=== ADD NEW PRODUCT ===")

    # Generate new ID
    if products:
        new_id = str(max([int(pid) for pid in products.keys()]) + 1)
    else:
        new_id = "1"

    # Get product details
    name = input("Product name: ")

    # Get price with error handling
    while True:
        try:
            price = float(input("Price: $"))
            if price < 0:
                print("Price cannot be negative!")
                continue
            break
        except ValueError:
            print("Invalid price! Please enter a number.")

    # Get quantity with error handling
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative!")
                continue
            break
        except ValueError:
            print("Invalid quantity! Please enter a whole number.")

    # Add to products
    products[new_id] = {"name": name, "price": price, "quantity": quantity}

    print(f"\n✓ Product '{name}' added with ID {new_id}!")


def update_quantity(products):
    """Update product quantity"""
    if not products:
        print("\nNo products to update!")
        return
    view_products(products)  # Show products first

    product_id = input("\nEnter product ID to update: ")

    if product_id not in products:
        print("Product ID not found!")
        return

    print(f"\nCurrent quantity: {products[product_id]['quantity']}")

    while True:
        try:
            new_quantity = int(input("New quantity: "))
            if new_quantity < 0:
                print("Quantity cannot be negative!")
                continue
            break
        except ValueError:
            print("Invalid quantity! Please enter a whole number.")

    products[product_id]["quantity"] = new_quantity
    print(f"\n✓ Quantity updated to {new_quantity}!")


def show_menu():
    """Display the main menu"""
    print("\n=== INVENTORY TRACKER ===")
    print("1. View all products")
    print("2. Add new product")
    print("3. Update product quantity")
    print("4. Delete product")
    print("5. Exit")
    print("=" * 25)


def get_valid_choice(min_val, max_val):
    """Get a valid integer choice from user"""
    while True:
        try:
            choice = int(input(f"\nEnter your choice ({min_val}-{max_val}): "))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"❌ Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def main():
    """Main program loop"""
    products = load_products()  # Load products at start

    while True:
        show_menu()
        choice = get_valid_choice(1, 5)  # Won't return until valid!

        # handle valid choices
        if choice == 1:
            view_products(products)
        elif choice == 2:
            add_product(products)
        elif choice == 3:
            update_quantity(products)
        elif choice == 4:
            print("Delete product - coming soon!")
        elif choice == 5:
            save_products(products)
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
