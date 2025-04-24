import os
import sys

# This script is designed to test multiple data structure implementations for loading usernames
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bloom_filter.bloom_filter import BloomFilter
from prefix_trees.trie import Trie  
from b_plus_trees.b_plus_tree import BPlusTree
from redis_hashmap.redis_hm import RedisHashMap
import redis

import time
from utils.csv_utils import load_csv_data
from utils.common_functions import run_common_tests, load_usernames



def test_bloom_filter(usernames):
    size = 1000000
    hash_count = 5
    bloom_filter = load_usernames(BloomFilter(size, hash_count), usernames)
    
    if bloom_filter:
        run_common_tests(bloom_filter, usernames, {'lookup': lambda ds, key: ds.check(key)})


def test_trie(usernames):
    trie = load_usernames(Trie(), usernames)
    if trie:
        run_common_tests(trie, usernames, {'lookup': lambda ds, key: ds.search(key)})


def test_b_plus_tree(usernames):
    b_plus_tree = load_usernames(BPlusTree(3), usernames)
    if b_plus_tree:
        run_common_tests(b_plus_tree, usernames, {'lookup': lambda ds, key: ds.search(key)})


def test_redis(usernames):
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    redis_client.flushdb()  # Clear the Redis database before loading usernames
    redis_ds = load_usernames(RedisHashMap(redis_client), usernames)
    
    if redis_ds:
        run_common_tests(redis_ds, usernames,
                         {'lookup': lambda ds, key: ds.search(key) is not None})


def main():
    csv_file = 'data/usernames.csv'
    usernames = load_csv_data(csv_file)

    print("\nTesting Bloom Filter...")
    test_bloom_filter(usernames)

    print("\nTesting Trie...")
    test_trie(usernames)

    print("\nTesting B+ Tree...")
    test_b_plus_tree(usernames)

    print("\nTesting Redis...")
    test_redis(usernames)


if __name__ == "__main__":
    main()
