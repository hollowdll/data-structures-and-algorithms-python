class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'

class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0
    
    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        # return len(key) % self.size
        return sum((index+1) * ord(char) * ord(char) for index, char in enumerate(key)) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.
        
        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        current = start

        while self.slots[current]:
            current = (current + 1) % self.size
            if current == start:
                return None
            
        return current
    
    def _find_key(self, start, key):
        """
        Starting from 'start' try to find 'key'.

        Parameters:
        - 'start': Starting index
        - 'key': The key to be found

        Returns: The index position of the key or None if not found
        """
        # Start to search from the given position
        current = start

        # While current position is occupaid and it's not the key, enter the loop
        while self.slots[current] and self.slots[current].key != key:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size
            # If we reach again the given position, that means
            # a whole cycle has been completed and the key was not found
            if current == start:
                return None

        # After the loop, current points to a free position or
        # to the position with the key
        if self.slots[current]:
            return current
        else:
            return None

    def put(self, key, value):
        """
        Add or updates a key with a value in the hash table

        Parameters:
        - 'key': The key to add or update.
        - 'value': The value of the key

        Returns: None
        """
        if self.used_slots >= self.size:
            raise(MemoryError("HashTable is full"))
        
        hash = self._hash(key)
        key_index = self._find_key(hash, key)
        
        if key_index is not None:
            self.slots[key_index].value = value
        else:
            key_index = self._find_free_slot(hash)
            if key_index is not None:
                self.slots[key_index] = HashItem(key, value)
                self.used_slots += 1
            else:
                raise(MemoryError("No free slots"))
            
    def get(self, key, alternative=None):
        """
        Get the value of 'key'.

        Parameters:
        - 'key': The key to find
        - 'alternative': An alternative value if key is not found. 
                         Optional. Default value=None
        
        Returns: The value of 'key' or alternative value
        """
        index = self._find_key(self._hash(key), key)
        if index is not None:
            return self.slots[index].value
        
        return alternative
