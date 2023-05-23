import sys
from encrypt import AES256
from save import Saver

def main():
    # Check if the user provided a file name as an argument
    if len(sys.argv) != 2:
        print("Usage: python main.py <file>")
        exit(1)
    
    # Create a Saver object with the given file name
    file = sys.argv[1]
    saver = Saver(file)
    # Read the data from the file as a list of dictionaries
    data = saver.read()
    
    # Ask the user for a master password and create an AES256 object with it
    master_password = input("Enter master password: ")
    aes = AES256(master_password)

    while True:
        # Display a menu of options for the user
        print("Choose an option:")
        print("1. Create a new password")
        print("2. Update an existing password")
        print("3. Delete a password")
        print("4. View all passwords")
        print("5. Exit")

        option = input("> ")

        if option == "1":
            # Ask the user for an account name and a password
            account = input("Enter account name: ")
            password = input("Enter password: ")
            # Encrypt the password using the AES256 object
            encrypted_password = aes.encrypt(password)
            # Append a new dictionary with the account and password to the data list
            data.append({"account": account, "password": encrypted_password})
            # Save the updated data to the file
            saver.save(data)
            print("Password created successfully.")

        elif option == "2":
            # Ask the user for an account name
            account = input("Enter account name: ")
            # Loop through the data list to find a matching account
            for item in data:
                if item["account"] == account:
                    # Ask the user for a new password
                    password = input("Enter new password: ")
                    # Encrypt the new password using the AES256 object
                    encrypted_password = aes.encrypt(password)
                    # Update the password in the dictionary
                    item["password"] = encrypted_password
                    # Save the updated data to the file
                    saver.save(data)
                    print("Password updated successfully.")
                    break
            else:
                print("Account not found.")

        elif option == "3":
            # Ask the user for an account name
            account = input("Enter account name: ")
            # Loop through the data list to find a matching account
            for item in data:
                if item["account"] == account:
                    # Remove the dictionary from the data list
                    data.remove(item)
                    # Save the updated data to the file
                    saver.save(data)
                    print("Password deleted successfully.")
                    break
            else:
                print("Account not found.")

        elif option == "4":
            # Loop through the data list and display each account and password pair
            for item in data:
                account = item["account"]
                encrypted_password = item["password"]
                # Decrypt each password using the AES256 object before displaying it
                password = aes.decrypt(encrypted_password)
                print(f"{account}: {password}")

        elif option == "5":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()