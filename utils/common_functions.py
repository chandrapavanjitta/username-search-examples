import random

from redis_hashmap.redis_hm import RedisHashMap


def run_common_tests(data_structure, usernames, operations):
    print("\nRunning common tests...")

    # Test 1: Random lookups
    print("\nTest 1: Random username lookups")
    test_samples = random.sample(usernames, min(10, len(usernames)))
    for username in test_samples:
        result = operations['lookup'](data_structure, username)
        print(f"Lookup {username}: {'Found' if result else 'Not Found'}")

    # Test 2: Non-existent username
    print("\nTest 2: Search for non-existent username")
    non_existent = "nonexistentuser123"
    result = operations['lookup'](data_structure, non_existent)
    print(f"Lookup {non_existent}: {'Found' if result else 'Not Found'}")

    # Additional tests can be added here as needed.


def load_usernames(data_structure, usernames):
    """
    A common function to load usernames into any data structure.

    Args:
        data_structure: The data structure instance to load usernames into.
        usernames: A list of usernames to load.

    Returns:
        The data structure instance with usernames loaded.
    """

    if isinstance(data_structure, RedisHashMap):
        # For RedisHashMap, we need to handle large batches to avoid memory issues.
        total_usernames = len(usernames)
        batch_size = 10000
        for i in range(0, total_usernames, batch_size):
            batch = usernames[i:i + batch_size]

            data_structure.insert(batch)
    else:
        for username in usernames:
            if hasattr(data_structure, 'insert'):
                data_structure.insert(username)
            elif hasattr(data_structure, 'add'):
                data_structure.add(username)
            else:
                raise AttributeError(
                    f"The data structure {type(data_structure).__name__} does not support 'insert' or 'add' methods.")

    # Calculate the total count of usernames in the data structure
    if hasattr(data_structure, 'count'):
        count = data_structure.count()
        print(f"Total usernames loaded: {count}")
    else:
        raise AttributeError(f"The data structure {type(data_structure).__name__} does not support 'count' method.")

    return data_structure
