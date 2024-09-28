def display_menu():
    print("=============================")
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("=============================")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item: str = input("▶▶ Enter item name: ")
            shopping_list.append(item)
            print(f"▶ '{item}' is added successfully to shopping list")
            pass
        elif choice == "2":
            item: str = input("▶▶ Enter item name: ")
            if item not in shopping_list:
                print(f"▶ '{item}' is missing from shopping list")
            else:
                shopping_list.remove(item)
                print(f"▶ '{item}' is removed successfully from shopping list")
            pass
        elif choice == "3":
            if len(shopping_list) == 0:
                print(f"▶ Shopping list is empty")
            else:
                print(f"▶ Shopping list items {' '.join(shopping_list)}")
                for x in range(len(shopping_list)):
                    print(f"-- {shopping_list[x]}"),
            pass
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
