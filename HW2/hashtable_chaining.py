# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

# Implementation of a node in a singlely linked list.
# DO NOT EDIT THIS CLASS
class SLLNode:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def set_next(self, node):
    self.next_node = node

  def get_next(self):
    return self.next_node

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

# An implementation of a hash table that uses chaining to handle collisions.
class HashTable:
  def __init__(self, initial_size=10, load_factor=.75):
    # DO NOT EDIT THIS CONSTRUCTOR
    if (initial_size < 0) or (load_factor <= 0) or (load_factor > 1):
      raise Exception("size must be greater than zero, and load factor must be between 0 and 1")
    self.array_size = initial_size
    self.load_factor = load_factor
    self.item_count = 0
    self.array = FixedSizeArray(initial_size)

  # Inserts the `(key, value)` pair into the hash table, overwriting any value
  # previously associated with `key`.
  # Note: Neither `key` nor `value` may be None (an exception will be raised)
  def insert(self, key, value):

    try:
      if key is None or value is None:
        raise TypeError
    except TypeError:
      print('Key and/or value cannot be None!')

    ind = cs5112_hash1(key) % self.array.size
    head = self.array.get(ind)

    while head != None:

      if head.get_value()[0] == key:
        head.set_value((key, value))

      head = head.get_next()

    self.item_count += 1
    head = self.array.get(ind)
    new_node = SLLNode((key,value))

    new_node.set_next(head)
    self.array.set(ind, new_node)

    if (self.item_count / self.array.size) > self.load_factor:
      temp_arr = self.array
      self._resize_array()

      for oldhead in temp_arr:
        while oldhead != None:
          self.insert(oldhead.get_value()[0], oldhead.get_value()[1])
          oldhead = oldhead.get_next()

  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):

    try:
      if key is None:
        raise TypeError
    except TypeError:
      print('Key cannot be None!')

    ind = cs5112_hash1(key) % self.array.size
    head = self.array.get(ind)

    while head != None:
      if head.get_value()[0] == key:
        return head.get_value()[1]

      head = head.get_next()

    return None

  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):


    try:
      if key is None:
        raise TypeError
    except TypeError:
      print('Key cannot be None!')

    ind = cs5112_hash1(key) % self.array_size
    head = self.array.get(ind)
    prev = None

    while head != None:

      if head.get_value()[0] == key:
        break

      prev = head
      head = head.get_next()

    if not head:
      return None

    self.item_count -= 1

    if prev != None:
      prev.set_next(head.get_next())
    else:
      self.array.set(ind, head.get_next())

    return head.get_value()[1]

  # Returns the number of elements in the hash table.
  def size(self):
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
    # YOUR CODE HERE
    self.array = FixedSizeArray(2 * self.array.size)

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS FUNCTION
    return self.array
