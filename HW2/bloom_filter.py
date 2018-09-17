# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1
from cs5112_hash import cs5112_hash2
from cs5112_hash import cs5112_hash3

# Implementation of a basic bloom filter. Uses exactly three hash functions.
class BloomFilter:
  def __init__(self, size=10):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.size = size
    self.array = FixedSizeArray(size)
    for i in range(0, size):
      self.array.set(i, False)

  # Adds an element to the bloom filter using three hash functions.
  def add_elem(self, elem):

    h_val1 = cs5112_hash1(elem) % 10
    init_h_val2 = cs5112_hash2(elem)
    h_val2 = init_h_val2 % 10
    init_h_val3 = cs5112_hash3(elem)
    h_val3 = init_h_val3 % 10

    i = 1
    while h_val2 == h_val1 and i < len(str(init_h_val2)):
        # h_val2 = int(cs5112_hash2(elem) % (10 ** (i + 1)) / 10 ** i)
        h_val2 = init_h_val2 % (10 ** (i + 1)) // 10 ** i
        i += 1

    j = 1
    while (h_val3 == h_val1 or h_val3 == h_val2) and j < len(str(init_h_val3)):
        # h_val3 = int(cs5112_hash3(elem) % (10 ** (j + 1)) / 10 **j)
        h_val3 = init_h_val3 % (10 ** (j + 1)) // 10 ** j
        j += 1

    self.array.set(h_val1, True)
    self.array.set(h_val2, True)
    self.array.set(h_val3, True)

  # Returns False if the given element is was definitely not added to the
  # filter. Returns True if it's possible that the element was added to the
  # filter (but not necessarily certain).
  def check_membership(self, elem):

    h_val1 = cs5112_hash1(elem) % 10
    init_h_val2 = cs5112_hash2(elem)
    h_val2 = init_h_val2 % 10
    init_h_val3 = cs5112_hash3(elem)
    h_val3 = init_h_val3 % 10

    i = 1
    while h_val2 == h_val1 and i < len(str(init_h_val2)):
        # h_val2 = int(cs5112_hash2(elem) % (10 ** (i + 1)) / 10 ** i)
        h_val2 = init_h_val2 % (10 ** (i + 1)) // 10 ** i
        i += 1

    j = 1
    while (h_val3 == h_val1 or h_val3 == h_val2) and j < len(str(init_h_val3)):
        # h_val3 = int(cs5112_hash3(elem) % (10 ** (j + 1)) / 10 **j)
        h_val3 = init_h_val3 % (10 ** (j + 1)) // 10 ** j
        j += 1

    for ind in [h_val1, h_val2, h_val3]:
        if not self.array.get(ind):
            return False

    return True
