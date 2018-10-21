# Implementation of the Boyer-Moore majority vote algorithm.
#
# Given a list of elements `l`, one would use this class in the following way
# to get the element that appears the majority of the time in the list:
#
# b = BoyerMooreMajority()
# for elem in l:
#   b.add_next_element(elem)
# return b.get_majority()
class BoyerMooreMajority:
  def __init__(self):
    self.guess = None
    self.counter = 0

  # Registers another element to be considered by the algorithm. This will
  # influence the majority element guess returned by `get_majority`.
  def add_next_element(self, element):
    assert(element is not None)
    #if counter is zero, supplant guess with incoming
    if self.counter < 1:
        self.guess = element
        self.counter = 1
    #if incoming is guess, increase bet on incoming as absolute majority
    elif self.guess == element:
        self.counter += 1
    #if incoming is other than guess, decrease bet on incoming as absolute majority
    else:
        self.counter -=1
  # Gives the best guess of which of the elements seen so far make up the
  # majority of the elements in set of elements. If a majority element exists,
  # this algorithm will report it correctly. Otherwise, there is no guarantee
  # about the output.
  def get_majority(self):
    #YOUR CODE HERE
    return self.guess
    # pass
