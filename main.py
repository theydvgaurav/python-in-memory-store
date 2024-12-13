import time
from datetime import datetime, timedelta
from threading import Lock


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class InMemDB(metaclass=Singleton):
    def __init__(self):
        self._data_store = {}
        self.lock = Lock()

    def _update_data_store(self, k, v):
        self._data_store[k] = v

    def _pop_key_from_data_store(self, k):
        self._data_store.pop(k, None)

    def _get_from_data_store(self, k):
        if self._data_store.get(k):
            return self._data_store.get(k)

    def get_value(self, key):
        # lazily removing key when it's being accessed
        val, ttl = self._get_from_data_store(key)
        if ttl and ttl <= datetime.now():
            self._pop_key_from_data_store(key)
            return None
        return val

    def set_value(self, key, value, ttl=None):
        self.lock.acquire()
        if ttl:
            ttl = datetime.now() + timedelta(seconds=ttl)
        self._update_data_store(key, (value, ttl))
        self.lock.release()
        return True


if __name__ == "__main__":
    db = InMemDB()
    db.set_value("Name", "Gaurav", 2)
    db.set_value("name", "Not Gaurav")
    time.sleep(2)
    print(db.get_value("Name"))
    print(db.get_value("name"))
