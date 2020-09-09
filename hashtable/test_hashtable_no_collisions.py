debug = True

"""
This is the same test, but with big hash tables that are _unlikely_ to
have collisions after the 3 inserts we do.

Does not collide with DJB2 or FNV-1-64. But could collide with other hashes.
"""

import unittest
from hashtable import HashTable

class TestHashTable(unittest.TestCase):

    def assertTrueWithDebug(self, hashtable, key, val):
        return_value = hashtable.get(key)
        if debug: print(f'TEST: "{key}" : ("{val}" == "{return_value}") = {val == return_value}')
        self.assertTrue(return_value == val)

    def test_hash_table_insertion_and_retrieval(self):
        if debug: print("\ntest_hash_table_insertion_and_retrieval")
        ht = HashTable(0x10000)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")

        # return_value = ht.get("key-0")
        # self.assertTrue(return_value == "val-0")
        # return_value = ht.get("key-1")
        # self.assertTrue(return_value == "val-1")
        # return_value = ht.get("key-2")
        # self.assertTrue(return_value == "val-2")
        self.assertTrueWithDebug(ht, "key-0", "val-0")
        self.assertTrueWithDebug(ht, "key-1", "val-1")
        self.assertTrueWithDebug(ht, "key-2", "val-2")

    def test_hash_table_pution_overwrites_correctly(self):
        if debug: print("\ntest_hash_table_pution_overwrites_correctly")
        ht = HashTable(0x10000)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")

        ht.put("key-0", "new-val-0")
        ht.put("key-1", "new-val-1")
        ht.put("key-2", "new-val-2")

        # return_value = ht.get("key-0")
        # self.assertTrue(return_value == "new-val-0")
        # return_value = ht.get("key-1")
        # self.assertTrue(return_value == "new-val-1")
        # return_value = ht.get("key-2")
        # self.assertTrue(return_value == "new-val-2")
        self.assertTrueWithDebug(ht, "key-0", "new-val-0")
        self.assertTrueWithDebug(ht, "key-1", "new-val-1")
        self.assertTrueWithDebug(ht, "key-2", "new-val-2")

    def test_hash_table_removes_correctly(self):
        if debug: print("\ntest_hash_table_removes_correctly")
        ht = HashTable(0x10000)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")

        # return_value = ht.get("key-0")
        # self.assertTrue(return_value == "val-0")
        # return_value = ht.get("key-1")
        # self.assertTrue(return_value == "val-1")
        # return_value = ht.get("key-2")
        # self.assertTrue(return_value == "val-2")
        self.assertTrueWithDebug(ht, "key-0", "val-0")
        self.assertTrueWithDebug(ht, "key-1", "val-1")
        self.assertTrueWithDebug(ht, "key-2", "val-2")

        ht.delete("key-2")
        ht.delete("key-1")
        ht.delete("key-0")

        # return_value = ht.get("key-0")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-1")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-2")
        # self.assertTrue(return_value is None)
        self.assertTrueWithDebug(ht, "key-0", None)
        self.assertTrueWithDebug(ht, "key-1", None)
        self.assertTrueWithDebug(ht, "key-2", None)

if __name__ == '__main__':
    unittest.main()
