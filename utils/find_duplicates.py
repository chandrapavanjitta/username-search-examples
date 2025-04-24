from csv_utils import load_csv_data

def main():
    csv_file = 'data/usernames.csv'  # Path to the CSV file
    sample_size = None  # Set to an integer to load a sample, or None to load all data

    print("Loading usernames from CSV...")
    usernames = load_csv_data(csv_file, sample_size)

    print(f"Loaded {len(usernames)} usernames.")

    # Find duplicates using a set-based approach
    seen = set()
    duplicates = set()
    duplicates_count = 0
    for username in usernames:     
        if username in seen:
            duplicates_count += 1
            duplicates.add(username)
        else:
            seen.add(username)

    print(f"Duplicate usernames count: {duplicates_count}")

    with open('data/duplicates.txt', 'w') as file:
        for username in duplicates:
            file.write(username + '\n')

    print("Duplicate usernames have been stored in '../data/duplicates.txt'.")

if __name__ == "__main__":
    main()