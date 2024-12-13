
# InMemDB: A Thread-Safe In-Memory Key-Value Store

A redis like in-memory data store written in Python. InMemDB is a lightweight, thread-safe, in-memory key-value database with optional time-to-live (TTL) support for expiring keys.

## Features
- Singleton Pattern: Ensures a single instance of the database.
- Thread-Safety: Uses locks to handle concurrent access safely.
- TTL Support: Allows setting an expiration time for keys, which are automatically removed upon access after expiration.

## Methods
- set_value(key, value, ttl=None): Stores a key-value pair with an optional TTL (in seconds).
- get_value(key): Retrieves the value for a key. Automatically removes expired keys and returns None for them. 

## Usage
``` 
    from in_mem_db import InMemDB  
    db = InMemDB()  
    db.set_value("key1", "value1", ttl=10)  # Set key with a TTL of 10 seconds  
    print(db.get_value("key1"))            # Output: "value1"  
    time.sleep(11)  
    print(db.get_value("key1"))            # Output: None (expired)  
```

## Authors

- [theydvgaurav](https://www.github.com/theydvgaurav)

