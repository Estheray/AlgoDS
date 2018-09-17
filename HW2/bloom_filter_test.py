# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.

from bloom_filter import BloomFilter

bfilter = BloomFilter()
bfilter.add_elem("example_elem")
if not bfilter.check_membership("example_elem"):
  print("bloom filter did not return True for added element ")
