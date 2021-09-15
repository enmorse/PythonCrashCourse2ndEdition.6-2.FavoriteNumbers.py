# Use a dictionary to store people's favorite numbers.
# Think of five names, and use them as keys in your
# dicitonary. Think of a favorite number for each
# person, and store each as a value in your dictionary.
# Print each person's name and their favorite number.
# For more fun, poll a few friends and get some actual
# data for your program.

favorite_numbers = {
    "dad": 7,
    "mom": 16,
    "my_favorite_number": 48,
    "vincent": 17,
    'nate': 23,
}

for key, value in favorite_numbers.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value}")
