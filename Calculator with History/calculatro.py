HISTORY_FILE = "history.txt"

def add_to_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No history available.")
    else:
        for line in lines:
            print(line.strip())
        file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(f"{equation} = {result}\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Please use: number1 operator number2")
        return 
    
    num1, operator, num2 = float(parts[0]), parts[1], float(parts[2])

    if operator == '+':
        result = (num1) + (num2)
    elif operator == '-':
        result = (num1) - (num2)
    elif operator == '*':
        result = (num1) * (num2)
    elif operator == '/':
        if num2 != 0:
            result = (num1) / (num2)
        else:
            print("Error: Division by zero.")
            return None
    else:
        print("Invalid operator. Please use one of: +, -, *, /")
        return None

    if int(result) == result:
        result = int(result)
    print(f"Result: {result}")    


    save_to_history(user_input, result)
    return result

def main():
    print("Welcome to the Calculator with History!")
    while True:
        user_input = input("Enter calculation (e.g., 2 + 2), 'history' to view history, 'clear' to clear history, or 'exit' to quit: ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input.lower() == 'history':
            add_to_history()
        elif user_input.lower() == 'clear':
            clear_history()
        else:
            calculate(user_input)

if __name__ == "__main__":
    main() 