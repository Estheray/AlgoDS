from boyer_moore import BoyerMooreMajority

if __name__ == "__main__":
  f = open("testcases_boyer_moore.txt", 'r')
  num_tests = 0
  for l in f.readlines():
    l = l.strip()
    (test_name, symbols, expected_guess, expected_counter) = l.split(";")
    expected_counter = int(expected_counter)
    if len(symbols) > 0: symbols = symbols.split(",")
    else: symbols = []
    try:
      bmm = BoyerMooreMajority()
      for s in symbols: bmm.add_next_element(s)
      assert(bmm.counter == expected_counter)
      if expected_counter > 0:
        assert(bmm.guess == expected_guess or (bmm.guess == None and expected_guess=='!'))
    except:
      print("Test failure: %s"%test_name)
      break
    num_tests += 1
  f.close()
print("Ran %d tests "%num_tests)
