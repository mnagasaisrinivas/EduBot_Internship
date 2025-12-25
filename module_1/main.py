import sys
import re
import logging
import logging.config

users_path = "user_data.txt"
log_path = "app_logs.txt"


# Loging Configurations
loging_config = {

    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
        },
    },

    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': log_path,
            'formatter': 'default',
            'level': 'INFO',
            'mode': 'a'
        },
    },

    'loggers': {
        'user_validation': {
            'handlers': ['file_handler'],
            'level': 'INFO',
            'propagate': False
        },
    }

}


# Apply the logging configuration
logging.config.dictConfig(loging_config)


# Logger Intialization
logger = logging.getLogger('user_validation')


# For Categorizing people based on their age
def categorize(age):

    age = int(age)

    if age < 18 :
        return "Underage"
    
    elif age > 18 and age < 60 :
        return "Adult"
    
    else :
        return "Senior"
    
    
# For making entry into file
def file_entry(data):

    with open(users_path, "a") as file :
        file.write(f"Name:{data[0]}, Email:{data[1]}, Age:{data[2]}, Category:{data[3]}. \n")


# For input validation
def validate(data):

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not data[0].isalpha():
            
            print("Invalid name. Only alphabets are allowed.")
            logger.error(f"Invalid name entered: {data[0]}")

            return True

    elif not re.match(email_pattern, data[1]):
            
            print("Invalid email format.")
            logger.error(f"Invalid email entered: {data[1]}")

            return True

    elif not data[2].isdigit() :
            
            print("Invalid age. Only positive numbers are allowed.")
            logger.error(f"Invalid age entered: {data[2]}")
            
            return True

    else :

        return False    


# For making a new entry
def add_entry():
    
    while True:

        command = input("\nTo Switch Mode type 'Switch' \nEnter Details Name, Mail, Age separated by ',' : ")

        if command.lower() == "switch" :
            return
        
        else :
            data = [command.strip() for command in command.split(',')]

            if validate(data):
                continue

            data.append(categorize(data[2]))
            file_entry(data)
            logger.info(f"User {data[0]} entered a valid Details")
            print("Data has been registered \n")
            print(f"""
                  User Name: {data[0]}
                  Email: {data[1]}
                  Age: {data[2]}
                  Category: {data[3]} \n""")



# For viewing the entries            
def view_entries():

    try:
        with open(users_path, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No entries found.\n")
                return
            print("Entries from file:")
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")
            print()
        return  
      
    except FileNotFoundError:
        print("File not found. No entries yet.\n")
        return



# Main Function
def main():

    while True:
        print("\nAvailable modes:")
        print("1. Enter entries")
        print("2. View entries")
        print("3. Exit")
        
        choice = input("Choose your mode (1/2/3): ").strip()

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Exiting Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()