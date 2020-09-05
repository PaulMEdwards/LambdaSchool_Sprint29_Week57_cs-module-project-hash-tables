debug = False

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

# Resize when load_factor higher than this limit
load_factor_limit = 0.75

# Hash algorithm constants
FNV_prime = 1099511628211
FNV_offset_basis = 14695981039346656037
DJB_prime = 5381
DJB_MAGIC_NUMBER = 33

class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity: int):
        if capacity < MIN_CAPACITY: capacity = MIN_CAPACITY
        self.capacity = capacity
        self.slots = [None] * capacity
        self.container = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        self.capacity = len(self.container)
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        load = 0
        for v in self.container:
            if v is not None: load += 1
        load_factor = self.capacity / load
        if debug: print(f"Load Factor: {load_factor}")
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        hash = FNV_offset_basis
        for k in key:
            hash = hash ^ ord(k)
            hash = hash * FNV_prime
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

        hash = DJB_prime
        for k in key:
            hash = (hash * DJB_MAGIC_NUMBER) + ord(k)
            # hash = ((hash << 5) + hash) + ord(k) # Equivalent implementation; faster on some older CPUs
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        i = self.hash_index(key)
        if debug: print(f"Hash Index for key '{key}' = {i}\nValue = {value}")

        self.slots[i] = key
        self.container[i] = value

        # if self.slots[i] == None:
        #     self.slots[i] = key
        #     self.container[i] = value
        # else:
        #     if self.slots[i] == key:
        #         self.container[i] = value
        #     else:



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        if self.slots[i] is not None: self.slots[i] = None
        if self.container[i] is not None: self.container[i] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        return self.container[i]


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        s = self.slots[:]
        c = self.container[:]
        self.__init__(new_capacity)
        for i in range(len(s)):
            if debug:
                print(f"i='{i}'")
                print(f"s[i]='{s[i]}'")
                print(f"c[i]='{c[i]}'")
            if s[i] is not None:
                self.put(s[i], c[i])



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(f"{i}\t{ht.get(f'line_{i}')}")

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(f"{i}\t{ht.get(f'line_{i}')}")

    print("")
