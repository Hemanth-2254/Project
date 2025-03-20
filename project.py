# Initialize dictionaries for the library and student records
library = {}  # Dictionary to store book names as keys and their counts as values
students = {}  # Dictionary to store student details and issued books

# Display books in the library
def display_books():
    # Print the available books and their respective counts
    print("\nAvailable Books:")
    for book, count in library.items():  # Iterate over the library dictionary
        print(f"{book} - Copies: {count}")  # Display each book with the count

# Add books to the library
def add_books(book_name, copies):
    # Add the specified number of copies of a book to the library
    library[book_name] = library.get(book_name, 0) + copies  # Update book count
    print(f"\n'{book_name}' has been added with {copies} copies.")  # Confirmation message

# Import the datetime module to capture issue/return timestamps
from datetime import datetime

# Issue a book to a student
def issue_book(book_name, student_name, student_no):
    # Check if the book is available in the library
    if library.get(book_name, 0) > 0:
        library[book_name] -= 1  # Reduce the book count by 1
        student_key = (student_name, student_no)  # Create a unique key for the student
        issue_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Record current date and time
        # Add the book and issue timestamp to the student's records
        students[student_key] = students.get(student_key, []) + [(book_name, issue_datetime)]
        print(f"\nYou have issued '{book_name}' to {student_name} (ID: {student_no}). Enjoy reading!")  # Confirmation
    else:
        # If the book is not available, display an error message
        print(f"\nSorry, '{book_name}' is currently not available.")

# Return a book to the library
def return_book(book_name, student_name, student_no):
    student_key = (student_name, student_no)  # Identify the student using their unique key
    if student_key in students:  # Check if the student is registered
        # Loop through the books issued to the student
        for record in students[student_key]:
            if record[0] == book_name:  # Check if the student has the specified book
                students[student_key].remove(record)  # Remove the book entry
                library[book_name] += 1  # Increase the book count in the library
                print(f"\nThank you, {student_name} (ID: {student_no}), for returning '{book_name}'.")  # Confirmation
                break
        else:
            # If the book was not issued to the student, display an error message
            print(f"\nError: '{book_name}' was not issued to {student_name} (ID: {student_no}).")
        # Remove the student from the records if they have no books left
        if not students[student_key]:
            del students[student_key]
    else:
        # If the student is not registered, display an error message
        print(f"\nError: Student {student_name} (ID: {student_no}) not found.")

# Display registered students and their issued books
def display_students():
    print("\nRegistered Students and Issued Books:")
    if not students:  # Check if there are any student records
        print("No student found.")  # Display a message if no students are found
    else:
        # Iterate over the student records and display their issued books
        for (student_name, student_no), books in students.items():
            if books:
                # Create a string representation of issued books and their timestamps
                books_list = ', '.join([f"{book} (Issued: {datetime_issued})" for book, datetime_issued in books])
            else:
                books_list = 'No books issued'
            print(f"{student_name} (ID: {student_no}): {books_list}")  # Display the student's details

# Main menu to interact with the library system
def main():
    while True:  # Infinite loop for continuous interaction until exited
        # Display menu options
        print("\n-- Library Menu --")
        print("1. View all books")
        print("2. Add a book")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. View all students")
        print("6. Exit")
        # Accept user input for menu selection
        choice = input("Enter your choice: ")
        
        if choice == "1":  # Option to view all books
            display_books()
        elif choice == "2":  # Option to add a book to the library
            book_name = input("Enter the book name: ")
            copies = int(input("Enter the number of copies: "))  # Ensure copies is an integer
            add_books(book_name, copies)
        elif choice == "3":  # Option to issue a book to a student
            book_name = input("Enter the book name to issue: ")
            student_name = input("Enter the student's name: ")
            student_no = int(input("Enter the student number: "))  # Ensure student_no is an integer
            issue_book(book_name, student_name, student_no)
        elif choice == "4":  # Option to return a book
            book_name = input("Enter the book name to return: ")
            student_name = input("Enter the student's name: ")
            student_no = int(input("Enter the student number: "))
            return_book(book_name, student_name, student_no)
        elif choice == "5":  # Option to view all students and their issued books
            display_students()
        elif choice == "6":  # Option to exit the system
            print("Thank you for using the Library service. Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("\nInvalid choice. Please try again.")

# Run the main function to start the program
main()