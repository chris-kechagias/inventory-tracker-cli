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
