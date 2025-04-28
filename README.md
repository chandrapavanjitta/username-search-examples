# Username Search Examples

This repository contains various implementations and utilities for working with username data. The primary focus is on efficient data structures and algorithms to handle username-related operations, such as searching, filtering, and detecting duplicates.

[Referenece - YT](https://www.youtube.com/watch?v=_l5Q5kKHtR8)

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Pipenv for dependency management
- Docker (if using the Redis-based implementation)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/username-search-examples.git
   cd username-search-examples
   ```

2. Install dependencies using Pipenv:
   ```bash
   pipenv install && pipenv shell
   ```

3. (Optional) Start the Redis server if using the Redis-based implementation:
   ```bash
   cd redis_hashmap
   docker-compose up
   ```

### Usage

- To generate sample usernames:
  ```bash
  python generate_usernames.py
  ```

- To test all implementations:
  ```bash
  python test_all_implementations.py
  ```

- To find duplicate usernames:
  ```bash
  python utils/find_duplicates.py
  ```


