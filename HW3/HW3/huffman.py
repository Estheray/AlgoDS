# Represents a Huffman tree for use in encoding/decoding strings.
# A sample usage is as follows:
#
# h = HuffmanTree([('A', 2), ('B', 7), ('C', 1)])
# assert(h.encode('ABC') == '01100')
# assert(h.decode(h.encode('ABC')) == 'ABC')

class HuffmanTree:
  # Helper object for building the Huffman tree.
  # You may modify this constructor but the grading script rlies on the left, right, and symbol fields.
  class TreeNode:
    def __init__ (self, symbol=None, left=None, right=None, min_element=None):
      self.left = left
      self.right = right
      self.symbol = symbol
      self.min_element = min_element

  # The `symbol_list` argument should be a list of tuples `(symbol, weight)`,
  # where `symbol` is a symbol that can be encoded, and `weight` is the
  # the unnormalized probabilitiy of that symbol appearing.
  def __init__(self, symbol_list):
    assert(len(symbol_list) >= 2)
      # (place TreeNode object here)

    while len(symbol_list) > 1:
      symbol_list = sorted(symbol_list, key=lambda x: (x[1], self.get_min_element(x[0])), reverse=True)

      tmp_left = symbol_list.pop()
      left_w = tmp_left[1]

      if type(tmp_left[0]) == str:
        tmp_left = self.TreeNode(symbol=tmp_left[0], min_element=tmp_left[0])
      else:
        tmp_left = tmp_left[0]

      tmp_right = symbol_list.pop()
      right_w = tmp_right[1]

      if type(tmp_right[0]) == str:
        tmp_right = self.TreeNode(symbol=tmp_right[0], min_element=tmp_right[0])
      else:
        tmp_right = tmp_right[0]

      if left_w == right_w and tmp_right.min_element < tmp_left.min_element:
        tmp_root = self.TreeNode(left=tmp_right, right=tmp_left, min_element=min(tmp_left.min_element, tmp_right.min_element))
      else:
        tmp_root = self.TreeNode(left=tmp_left, right=tmp_right, min_element=min(tmp_left.min_element, tmp_right.min_element))

      symbol_list.append((tmp_root, left_w + right_w))

    self.root = symbol_list.pop()[0]
    self.wordict = dict()
    self.dict_builder(self.root, [])

  def get_min_element(self, element):
    if type(element) == str:
      return element
    else:
      return element.min_element

  def dict_builder(self, root, path):

    if not root.left and not root.right:
      self.wordict[root.symbol] = "".join(path)
      return

    if root.left:
      path.append('0')
      self.dict_builder(root.left, path)
      path.pop()

    if root.right:
      path.append('1')
      self.dict_builder(root.right, path)
      path.pop()

  # Encodes a string of characters into a string of bits using the
  # symbol/weight list provided.
  def encode(self, s):
    assert(s is not None)
    ans = ""
    for c in s:
      ans += self.wordict[c]

    return ans
  # Decodes a string of bits into a string of characters using the
  # symbol/weight list provided.
  def decode(self,s):
    assert(s is not None)
    ans = []
    while len(s) > 0:
      count = 0
      if not self.decode_util(self.root, s, ans, count):
        return None
      slen = len(self.wordict[ans[-1]])
      s = s[slen:]
    return "".join(ans)

  def decode_util(self, root, s, ans, count):

    if not root.left and not root.right:
      ans.append(root.symbol)
      return True

    if len(s) == 0:
      return None

    if s[0] == '0':
      return self.decode_util(root.left, s[1:], ans, count+1)
    else:
      return self.decode_util(root.right, s[1:], ans, count+1)




















