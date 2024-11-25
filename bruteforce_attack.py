import time

# Recursive function to generate combinations for brute force
def generate_combinations(characters, length, prefix, target_password):
    if length == 0:
        if prefix == target_password:
            return prefix
    else:
        for c in characters:
            result = generate_combinations(characters, length - 1, prefix + c, target_password)
            if result:
                return result
    return None

# Brute Force Attack
def brute_force_crack(target_password):
    start_time = time.time()
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_length = 6  # Maximum password length to try

    for length in range(1, max_length + 1):
        cracked_password = generate_combinations(characters, length, "", target_password)
        if cracked_password:
            elapsed_time = time.time() - start_time
            print(f"Time Taken: {elapsed_time:.2f} seconds")
            return cracked_password
    return None

# Main function
if __name__ == "__main__":
    target_password = "abc123"  # You can change this for testing

    print("Brute Force Attack:")
    cracked_password = brute_force_crack(target_password)

    if cracked_password:
        print(f"Cracked Password: {cracked_password}")
    else:
        print("Failed to crack password.")
