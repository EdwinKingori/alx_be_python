
shopping_list = []


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def add_item():
    item = input("Enter the item to add: ").
    shopping_list.append(item)
    print(f"{item} added successfully!")


def remove_item():
    item = input("Enter item name to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed successfully!")
    else:
        print(f"{item} not found!")


def view_list():
    for index, items in enumerate(shopping_list):
        print(f"{index}: {items}")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item(shopping_list)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_item(shopping_list)
            pass
        elif choice == '3':
            # Display the shopping list
            view_list(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
