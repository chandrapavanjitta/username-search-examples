class RedisHashMap:
    def __init__(self, redis_client):
        self.redis_client = redis_client
        self.redis_client.flushdb()  # Clear all data in Redis

    def insert(self, usernames):
        """
        add usernames into a Redis hash map
        """

        with self.redis_client.pipeline() as pipe:
            for username in usernames:
                pipe.hset('usernames', username, username)
            pipe.execute()

    def search(self, username):
        """
        Retrieve user data from Redis hash map
        """
        data = self.redis_client.hget('usernames', username)
        if data:
            return data
        else:
            return None

    def count(self):
        """
        Count the total number of usernames in the Redis hash map.
        """
        return self.redis_client.hlen('usernames')
