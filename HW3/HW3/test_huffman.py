from huffman import HuffmanTree

# This helper function takes a binary tree, and encodes it a string,
# using parentheses. For example, this tree:
#                .
#               / \
#              /   \
#             /\    Z
#            /  \
#           A    B
#
# Is parenthesized as ((AB)Z).

def BinaryTreeToString(root):
  if root.symbol is not None: return root.symbol
  else: return "(%s%s)"%(BinaryTreeToString(root.left), BinaryTreeToString(root.right))

if __name__ == "__main__":
  f = open("testcases_huffman.txt", 'r')
  num_tests = 0
  for l in f.readlines():
    l = l.strip()
    (testname, symbols, weights, tree, encode_input, encode_output, decode_input, decode_output) = l.split(";")
    decode_output = None if decode_output == '!' else decode_output
    symbols = symbols.split(",")
    weights = [int(w) for w in weights.split(",")]
    try:
      h = HuffmanTree(list(zip(symbols, weights)))
      assert(BinaryTreeToString(h.root) == tree)
      assert(h.encode(encode_input) == encode_output)
      assert(h.decode(decode_input) == decode_output)
    except:
      print("Failed test %s"%testname)
      break
    num_tests += 1
  print("Ran %d tests"%num_tests)
  f.close()
