def case_counter(text):
    # Initialize counters for uppercase and lowercase letters
    uppercase_count = 0
    lowercase_count = 0
    
    # Iterate through each character in the string
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1
    
    # Print the results
    print("Uppercase letters:", uppercase_count)
    print("Lowercase letters:", lowercase_count)

# Example usage:
text_example = "Hello World! 123"
case_counter(text_example)

