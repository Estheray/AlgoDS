# DO NOT CHANGE THIS CLASS
class RespaceTableCell:
	def __init__(self, value, index):
		self.value = value
		self.index = index
		self.validate()

	# This function allows Python to print a representation of a RespaceTableCell
	def __repr__(self):
		return "(%s,%s)"%(str(self.value), str(self.index))

	# Ensure everything stored is the right type and size
	def validate(self):
		assert(type(self.value) == bool), "Values in the respacing table should be booleans."
		assert(self.index == None or type(self.index) == int), "Indices in the respacing table should be None or int"

# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)
def fill_cell(T, i, j, string, is_word):
	if(i==0 or j==0):
		return RespaceTableCell(True, 0)
	if(is_word(string[i-1:j]) and T.get(i,i-1).value):
		return RespaceTableCell(True, j-i+1)
	previous = T.get(i-1,j)
	if(i>j or (previous.value and previous.index>0)):
		return RespaceTableCell(previous.value, previous.index)
	return RespaceTableCell(False, 0)
				  
# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.
def cell_ordering(N):
	cells = []
	for i in range(N+1):
		for j in range(N+1):
			cells.append((i,j))
	return cells

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):
	res = ""
	current_len = 0
	i = j = len(s)
	while(current_len<len(s) and i>0 and j>0):
		cell = table.get(i,j)
		if(cell.value):
			res = " "+s[j-cell.index:j]+res
			current_len+= cell.index
			j = j-cell.index
		else:
			i=i-1
	if(current_len == len(s)):
		return res[1:]
	else:
		return None

if __name__ == "__main__":
	# Example usage.
	from dynamic_programming import DynamicProgramTable
	s = "itwasthebestoftimes"
	wordlist = ["of", "it", "the", "best", "times", "was"]
	D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
	D.fill(string=s, is_word=lambda w:w in wordlist)
	print respace_from_table(s, D)