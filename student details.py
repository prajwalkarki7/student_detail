student_dict = {}

def main():
    while True:
        choice = int(input("Enter the choice you want to choose:\n 1. Add\n 2. Display\n 3. Search\n 4. Delete\n 5. Update\n 6. Exit\n"))
        if choice == 1:
            add_details()
        elif choice == 2:
            display_details()
        elif choice == 3:
            search_details()
        elif choice == 4:
            delete_details()
        elif choice == 5:
            update_details()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Incorrect choice")

def add_details():
    num = input("Enter roll number: ")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    student_dict[num] = {"name": name, "phone": phone, "email": email}
    print("Details added successfully")

def display_details():
    if not student_dict:
        print("\nNo records to display.")
    else:
        print("\nRecords:")
        for num, details in student_dict.items():
            print(f"Roll Number: {num}")
            print(f"  Name: {details['name']}")
            print(f"  Phone: {details['phone']}")
            print(f"  Email: {details['email']}")
            print("-" * 30)

def search_details():
    x = input("Enter the roll number you want to search: ")
    if x in student_dict:
        print("\nDetails are:")
        print(f"Roll Number: {x}")
        print(f"  Name: {student_dict[x]['name']}")
        print(f"  Phone: {student_dict[x]['phone']}")
        print(f"  Email: {student_dict[x]['email']}")
    else:
        print("\nNo record found with that roll number.")

def delete_details():
    y = input("Enter the roll number you want to delete: ")
    if y in student_dict:
        student_dict.pop(y)
        print("Deleted successfully")
    else:
        print("\nNo record found with that roll number.")

def update_details():
    roll = input("Enter the roll number you want to update: ")
    if roll in student_dict:
        name = input("Enter your new name: ")
        phone = input("Enter your new phone number: ")
        email = input("Enter your new email: ")
        student_dict[roll] = {"name": name, "phone": phone, "email": email}
        print("\nDetails updated successfully!")
    else:
        print("\nNo record found with that roll number.")

main()
