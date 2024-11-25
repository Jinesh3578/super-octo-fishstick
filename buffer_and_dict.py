import os

# Function to demonstrate buffer overflow simulation
def buffer_overflow_demo():
    buffer_size = 10
    overflow_simulated = "NO_OVERFLOW"

    print("Buffer Overflow Demo")
    user_input = input(f"Enter a string (max {buffer_size} characters): ")

    # Simulating overflow behavior by overwriting the "overflow_simulated" variable
    if len(user_input) > buffer_size:
        overflow_simulated = user_input[:buffer_size]  # Simulating truncation to prevent real overflow
        print("WARNING: Input exceeds buffer size, simulating overflow behavior!")
    else:
        overflow_simulated = user_input

    print(f"You entered: {user_input}")
    print(f"Overflow Simulated Buffer: {overflow_simulated}")


# Simulated password validation function
def validate_password(input_password, actual_password):
    return input_password == actual_password


# Function to simulate Dictionary Attack
def dictionary_attack(target_password, dictionary_file):
    if not os.path.exists(dictionary_file):
        print(f"Error: Dictionary file '{dictionary_file}' not found.")
        return False

    print("Starting Dictionary Attack...")
    with open(dictionary_file, "r") as file:
        for line in file:
            password = line.strip()  # Remove any trailing newlines or spaces
            print(f"Trying password: {password}")
            if validate_password(password, target_password):
                print(f"Password Cracked: {password}")
                return True

    print("Password not found in dictionary.")
    return False


# Main function
def main():
    # Demonstrate Buffer Overflow
    buffer_overflow_demo()

    # Dictionary Attack Simulation
    actual_password = "secure123"
    dictionary_file = "dictionary.txt"  # Ensure this file exists with sample passwords

    print("\nDictionary Attack Demo")
    if not dictionary_attack(actual_password, dictionary_file):
        print("Failed to crack the password.")


if __name__ == "__main__":
    main()
