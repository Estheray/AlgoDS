# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.

from hashtable_chaining import HashTable as HashTableChaining
from hashtable_linear_probing import HashTable as HashTableProbing

for (name, HashTable) in [("chaining", HashTableChaining), ("linear probing", HashTableProbing)]:
    table = HashTable()
    table.insert("example_key", "example_value")
    if table.get("example_key") != "example_value":
        print("%s hash table did not return example value"%name)
    table.remove("example_key")
    if table.size() != 0:
        print("%s hash table had non-zero size"%name)
