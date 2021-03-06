debug = False

import unittest

from hashtable import HashTable


class TestHashTable(unittest.TestCase):

    def assertTrueWithDebug(self, hashtable, key, val):
        return_value = hashtable.get(key)
        if debug: print(f'TEST: "{key}" : ("{val}" == "{return_value}") = {val == return_value}')
        self.assertTrue(return_value == val)

    def test_hash_table_insertion_and_retrieval(self):
        if debug: print("\ntest_hash_table_insertion_and_retrieval")
        ht = HashTable(8)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        # return_value = ht.get("key-0")
        # self.assertTrue(return_value == "val-0")
        # return_value = ht.get("key-1")
        # self.assertTrue(return_value == "val-1")
        # return_value = ht.get("key-2")
        # self.assertTrue(return_value == "val-2")
        # return_value = ht.get("key-3")
        # self.assertTrue(return_value == "val-3")
        # return_value = ht.get("key-4")
        # self.assertTrue(return_value == "val-4")
        # return_value = ht.get("key-5")
        # self.assertTrue(return_value == "val-5")
        # return_value = ht.get("key-6")
        # self.assertTrue(return_value == "val-6")
        # return_value = ht.get("key-7")
        # self.assertTrue(return_value == "val-7")
        # return_value = ht.get("key-8")
        # self.assertTrue(return_value == "val-8")
        # return_value = ht.get("key-9")
        # self.assertTrue(return_value == "val-9")
        self.assertTrueWithDebug(ht, "key-0", "val-0")
        self.assertTrueWithDebug(ht, "key-1", "val-1")
        self.assertTrueWithDebug(ht, "key-2", "val-2")
        self.assertTrueWithDebug(ht, "key-3", "val-3")
        self.assertTrueWithDebug(ht, "key-4", "val-4")
        self.assertTrueWithDebug(ht, "key-5", "val-5")
        self.assertTrueWithDebug(ht, "key-6", "val-6")
        self.assertTrueWithDebug(ht, "key-7", "val-7")
        self.assertTrueWithDebug(ht, "key-8", "val-8")
        self.assertTrueWithDebug(ht, "key-9", "val-9")

    def test_hash_table_pution_overwrites_correctly(self):
        if debug: print("\ntest_hash_table_pution_overwrites_correctly")
        ht = HashTable(8)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        ht.put("key-0", "new-val-0")
        ht.put("key-1", "new-val-1")
        ht.put("key-2", "new-val-2")
        ht.put("key-3", "new-val-3")
        ht.put("key-4", "new-val-4")
        ht.put("key-5", "new-val-5")
        ht.put("key-6", "new-val-6")
        ht.put("key-7", "new-val-7")
        ht.put("key-8", "new-val-8")
        ht.put("key-9", "new-val-9")

        # return_value = ht.get("key-0")
        # self.assertTrue(return_value == "new-val-0")
        # return_value = ht.get("key-1")
        # self.assertTrue(return_value == "new-val-1")
        # return_value = ht.get("key-2")
        # self.assertTrue(return_value == "new-val-2")
        # return_value = ht.get("key-3")
        # self.assertTrue(return_value == "new-val-3")
        # return_value = ht.get("key-4")
        # self.assertTrue(return_value == "new-val-4")
        # return_value = ht.get("key-5")
        # self.assertTrue(return_value == "new-val-5")
        # return_value = ht.get("key-6")
        # self.assertTrue(return_value == "new-val-6")
        # return_value = ht.get("key-7")
        # self.assertTrue(return_value == "new-val-7")
        # return_value = ht.get("key-8")
        # self.assertTrue(return_value == "new-val-8")
        # return_value = ht.get("key-9")
        # self.assertTrue(return_value == "new-val-9")
        self.assertTrueWithDebug(ht, "key-0", "new-val-0")
        self.assertTrueWithDebug(ht, "key-1", "new-val-1")
        self.assertTrueWithDebug(ht, "key-2", "new-val-2")
        self.assertTrueWithDebug(ht, "key-3", "new-val-3")
        self.assertTrueWithDebug(ht, "key-4", "new-val-4")
        self.assertTrueWithDebug(ht, "key-5", "new-val-5")
        self.assertTrueWithDebug(ht, "key-6", "new-val-6")
        self.assertTrueWithDebug(ht, "key-7", "new-val-7")
        self.assertTrueWithDebug(ht, "key-8", "new-val-8")
        self.assertTrueWithDebug(ht, "key-9", "new-val-9")

    def test_hash_table_removes_correctly(self):
        if debug: print("\ntest_hash_table_removes_correctly")
        ht = HashTable(8)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        # return_value = ht.get("key-0")
        # self.assertTrue(return_value == "val-0")
        # return_value = ht.get("key-1")
        # self.assertTrue(return_value == "val-1")
        # return_value = ht.get("key-2")
        # self.assertTrue(return_value == "val-2")
        # return_value = ht.get("key-3")
        # self.assertTrue(return_value == "val-3")
        # return_value = ht.get("key-4")
        # self.assertTrue(return_value == "val-4")
        # return_value = ht.get("key-5")
        # self.assertTrue(return_value == "val-5")
        # return_value = ht.get("key-6")
        # self.assertTrue(return_value == "val-6")
        # return_value = ht.get("key-7")
        # self.assertTrue(return_value == "val-7")
        # return_value = ht.get("key-8")
        # self.assertTrue(return_value == "val-8")
        # return_value = ht.get("key-9")
        # self.assertTrue(return_value == "val-9")
        self.assertTrueWithDebug(ht, "key-0", "val-0")
        self.assertTrueWithDebug(ht, "key-1", "val-1")
        self.assertTrueWithDebug(ht, "key-2", "val-2")
        self.assertTrueWithDebug(ht, "key-3", "val-3")
        self.assertTrueWithDebug(ht, "key-4", "val-4")
        self.assertTrueWithDebug(ht, "key-5", "val-5")
        self.assertTrueWithDebug(ht, "key-6", "val-6")
        self.assertTrueWithDebug(ht, "key-7", "val-7")
        self.assertTrueWithDebug(ht, "key-8", "val-8")
        self.assertTrueWithDebug(ht, "key-9", "val-9")

        ht.delete("key-9")
        ht.delete("key-8")
        ht.delete("key-7")
        ht.delete("key-6")
        ht.delete("key-5")
        ht.delete("key-4")
        ht.delete("key-3")
        ht.delete("key-2")
        ht.delete("key-1")
        ht.delete("key-0")

        # return_value = ht.get("key-0")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-1")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-2")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-3")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-4")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-5")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-6")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-7")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-8")
        # self.assertTrue(return_value is None)
        # return_value = ht.get("key-9")
        # self.assertTrue(return_value is None)
        self.assertTrueWithDebug(ht, "key-0", None)
        self.assertTrueWithDebug(ht, "key-1", None)
        self.assertTrueWithDebug(ht, "key-2", None)
        self.assertTrueWithDebug(ht, "key-3", None)
        self.assertTrueWithDebug(ht, "key-4", None)
        self.assertTrueWithDebug(ht, "key-5", None)
        self.assertTrueWithDebug(ht, "key-6", None)
        self.assertTrueWithDebug(ht, "key-7", None)
        self.assertTrueWithDebug(ht, "key-8", None)
        self.assertTrueWithDebug(ht, "key-9", None)

    def test_hash_table_resize(self):
        if debug: print("\ntest_hash_table_resize")
        ht = HashTable(8)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        if debug:
            print(f'Container size: {ht.get_num_slots()}, Values: 10')
            print(f"\n{ht}")

        if debug:
            print("\nTesting auto_resize up")
            ht.auto_resize()
            print(f'Final size: {ht.get_num_slots()}')
            print(f"\n{ht}")

        ht.resize(1024)
        self.assertTrue(ht.get_num_slots() == 1024)
        if debug:
            print(f"\nManually resized to {ht.get_num_slots()} slots")

        # return_value = ht.get("key-0")
        # self.assertTrue(return_value == "val-0")
        # return_value = ht.get("key-1")
        # self.assertTrue(return_value == "val-1")
        # return_value = ht.get("key-2")
        # self.assertTrue(return_value == "val-2")
        # return_value = ht.get("key-3")
        # self.assertTrue(return_value == "val-3")
        # return_value = ht.get("key-4")
        # self.assertTrue(return_value == "val-4")
        # return_value = ht.get("key-5")
        # self.assertTrue(return_value == "val-5")
        # return_value = ht.get("key-6")
        # self.assertTrue(return_value == "val-6")
        # return_value = ht.get("key-7")
        # self.assertTrue(return_value == "val-7")
        # return_value = ht.get("key-8")
        # self.assertTrue(return_value == "val-8")
        # return_value = ht.get("key-9")
        # self.assertTrue(return_value == "val-9")
        self.assertTrueWithDebug(ht, "key-0", "val-0")
        self.assertTrueWithDebug(ht, "key-1", "val-1")
        self.assertTrueWithDebug(ht, "key-2", "val-2")
        self.assertTrueWithDebug(ht, "key-3", "val-3")
        self.assertTrueWithDebug(ht, "key-4", "val-4")
        self.assertTrueWithDebug(ht, "key-5", "val-5")
        self.assertTrueWithDebug(ht, "key-6", "val-6")
        self.assertTrueWithDebug(ht, "key-7", "val-7")
        self.assertTrueWithDebug(ht, "key-8", "val-8")
        self.assertTrueWithDebug(ht, "key-9", "val-9")


        if debug:
            print("\nTesting auto_resize down")
            ht.auto_resize()
            print(f'Final size: {ht.get_num_slots()}')
            print(f"\n{ht}")


if __name__ == '__main__':
    unittest.main()
