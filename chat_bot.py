#Importing the necessary libraries
import re

# Define a function to perform the mathematical operation
def math_operation(op, a, b):
    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        if (a,b == 0,0):
            print("0 is invalid")
        else: 
            return a / b
    else:
        return None

# Define a function to handle the user input and perform the operations
def chat_bot():
    print("Bot: Hi! I'm a basic calculator. How can I assist you today?")

    while True:
        user_input = input("User: ")
        user_input = user_input.lower()

        # Check if the user wants to exit the program
        if user_input == "exit":
            print("Bot: Goodbye!")
            break

        # Check if the user wants to perform a mathematical operation
        if re.search(r"\b(add|subtract|multiply|divide)\b", user_input):
            op = re.search(r"\b(add|subtract|multiply|divide)\b", user_input).group()
            print(f"Bot: You chose {op}. What is the first operand?")
            # Getting Input from the user
            a = float(input("User: "))
            print("Bot: What is the second operand?")
            b = float(input("User: "))
            result = math_operation(op, a, b)
            if result is not None:
                print(f"Bot: The result of {op}ing {a} and {b} is {result}")
            else:
                print("Bot: I'm sorry, I didn't understand that. Please try again.")
        # Check if the user wants to see the list of available operations
        elif re.search(r"\b(list|show)\b", user_input):
            print("Bot: Available operations are: Addition, Subtraction, Multiplication, Division")
        # Handling small talk with the user
        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            print("Bot: Hello! How can I help you today?")
        elif re.search(r"\b(thank you|thanks)\b", user_input):
            print("Bot: You're welcome!")
        else:
            print("Bot: I'm sorry, I didn't understand that. Please try again.")

# Calling the function
if __name__ == "__main__":
    chat_bot()
