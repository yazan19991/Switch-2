menu = {
    1: "Palindrome Check",
    2: "Lowercase Check",
    3: "Digit Check",
    4: "Length (>15) Check",
    5: "Empty Check",
    6: "Exit Program",
}


def print_menu():
    print("what you want to do:")
    for	k,v in menu.items():
        print(f"{k} - {v}")
        

def palindrome_check(user_input):
    reversed = ''
    for i in range(len(user_input)):
        reversed = f"{reversed}{user_input[-i-1]}"
    return user_input == reversed


def lowercase_check(user_input):
    return user_input.islower()

def digit_check(user_input):
    return user_input.isdigit()

def length_check(user_input):
    return len(user_input)>15

def empty_check(user_input):
    return len(user_input)==0



active = True
while active:
    print_menu()
    
    selected_operation = input("Select an operation (1-6): ")
    
    try:
        operation_num = int(selected_operation)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6\n")
        continue
    
    if operation_num == 1:
        user_input = input("Enter an input: ")
        result = palindrome_check(user_input)
        if result:
            print(f"'{user_input}' is a palindrome\n")
        else:
            print(f"'{user_input}' is not a palindrome\n")

    elif operation_num == 2:
        user_input = input("Enter an input: ")
        result = lowercase_check(user_input)
        if result:
            print(f"'{user_input}' is all lowercase\n")
        else:
            print(f"'{user_input}' is not all lowercase\n")

    elif operation_num == 3:
        user_input = input("Enter an input: ")
        result = digit_check(user_input)
        if result:
            print(f"'{user_input}' contains only digits\n")
        else:
            print(f"'{user_input}' does not contain only digits\n")

    elif operation_num == 4:
        user_input = input("Enter an input: ")
        result = length_check(user_input)
        if result:
            print(f"The length of '{user_input}' is more than 15 characters\n")
        else:
            print(f"The length of '{user_input}' is 15 or fewer characters\n")

    elif operation_num == 5:
        user_input = input("Enter an input: ")
        result = empty_check(user_input)
        if result:
            print("The input is empty\n")
        else:
            print(f"The input is not empty. It has {len(user_input)} characters\n")

    elif operation_num == 6:
        print("Exiting the program\n")
        active = False

    else:
        print("Invalid selection. Please choose between 1 and 6\n")