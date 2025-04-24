import csv
import random
import os
from faker import Faker
from datetime import datetime

# Initialize Faker
fake = Faker()


def generate_random_username():
    # Generate a random name
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()

    # Common prefixes and suffixes used in social media
    prefixes = ['the', 'real', 'official', 'im', 'its', 'weare', 'team', 'my', 'i', 'we']
    suffixes = ['official', 'world', 'life', 'daily', 'gram', 'tiktok', 'yt', 'tv', 'hd', 'vibes']

    # Common username patterns
    patterns = [
        # Pattern 1: First name + numbers (e.g., john123, emma456)
        lambda: first_name + ''.join(random.choices('0123456789', k=random.randint(2, 4))),

        # Pattern 2: First name + last name (e.g., johnsmith, emmawilliams)
        lambda: first_name + last_name,

        # Pattern 3: First name with underscore + last name (e.g., john_smith, emma_williams)
        lambda: first_name + '_' + last_name,

        # Pattern 4: First name + last name + numbers (e.g., johnsmith123, emmawilliams456)
        lambda: first_name + last_name + ''.join(random.choices('0123456789', k=random.randint(2, 3))),

        # Pattern 5: First initial + last name (e.g., jsmith, ewilliams)
        lambda: first_name[0] + last_name,

        # Pattern 6: First name + last initial (e.g., johns, emmaw)
        lambda: first_name + last_name[0],

        # Pattern 7: First name + last name + year (e.g., johnsmith2023, emmawilliams2024)
        lambda: first_name + last_name + str(random.randint(1990, 2024)),

        # Pattern 8: First name + last name + suffix (e.g., johnsmithofficial, emmawilliamsgram)
        lambda: first_name + last_name + random.choice(suffixes),

        # Pattern 9: First name + last name with x's (e.g., johnsmithxx, emmawilliamsxxx)
        lambda: first_name + last_name + 'x' * random.randint(2, 3),

        # Pattern 10: First name + last name with dots (e.g., john.smith, emma.williams)
        lambda: first_name + '.' + last_name,

        # Pattern 11: Use Faker's built-in username generator
        lambda: fake.user_name(),

        # Pattern 12: First name + random word + numbers
        lambda: first_name + fake.word().lower() + ''.join(random.choices('0123456789', k=random.randint(2, 3))),

        # Pattern 13: Random word + last name
        lambda: fake.word().lower() + last_name,
    ]

    return random.choice(patterns)()


def generate_usernames_csv(num_rows=100000, filename='usernames.csv'):
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    # Set the full path for the CSV file
    filepath = os.path.join('data', filename)

    print(f"Generating {num_rows} usernames...")

    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'username'])  # Header with ID column

        for i in range(1, num_rows + 1):  # Start from 1 to num_rows
            username = generate_random_username()
            writer.writerow([i, username])

    print(f"Generated {num_rows} usernames and saved to {filepath}")


if __name__ == "__main__":
    generate_usernames_csv()
