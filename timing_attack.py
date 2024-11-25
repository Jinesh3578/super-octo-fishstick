import time
# Simulated target password

target_password = "abc123"

print(f"Target Password Length: {len(target_password)}")

# Simulated vulnerable `strcmp` function

def strcmp(a, b):

    """Simulates a string comparison with a timing leak."""

    for i in range(len(a)):
        if i >= len(b) or a[i] != b[i]:
            return False
        time.sleep(0.02)  # Simulated timing leak per correct character
    return len(a) == len(b)

# Measure execution time for a single comparison

def measure_time(function, target, candidate, trials=5):

    """Measures the average execution time over multiple trials."""

    total_time = 0
    for _ in range(trials):
        start = time.perf_counter()
        function(target, candidate)
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / trials

# Perform timing attack

def timing_attack():

    """Executes the timing attack to infer the target password."""
    candidate = ""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    print("\nStarting Timing Attack...\n")

    for position in range(len(target_password)):
        best_char = None
        max_time = 0
        for char in characters:
            # Test a candidate with the current guess

            test_candidate = candidate + char
            elapsed_time = measure_time(strcmp, target_password, test_candidate)

            # Update best character based on timing

            if elapsed_time > max_time:
                max_time = elapsed_time
                best_char = char

        # Verify the guessed character by comparing explicitly

        if best_char and strcmp(candidate + best_char, target_password[:len(candidate) + 1]):
            candidate += best_char
            print(f"Current Guess: {candidate} | Time: {max_time:.6f} seconds")
        else:
            print("Error in guess, retrying current position...")
            position -= 1  # Retry the same position if the guess fails
    return candidate

# Main Function

if __name__ == "__main__":
    guessed_password = timing_attack()
    print(f"\nGuessed Password: {guessed_password}")

    if guessed_password == target_password:
        print("Success: The password was cracked!")
    else:
        print("Failure: Could not crack the password.")
