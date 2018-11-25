# DO NOT CHANGE THIS CLASS
class DiffingCell:
    def __init__(self, cost, s_char, t_char):
        self.cost = cost
        self.s_char = s_char
        self.t_char = t_char
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s,%s)"%(self.cost, self.s_char, self.t_char)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.cost) == int), "cost should be an integer"
        assert(type(self.s_char) == str), "s_char should be a string"
        assert(type(self.t_char) == str), "t_char should be a string"
        assert(len(self.s_char) == 1), "s_char should be length 1"
        assert(len(self.t_char) == 1), "t_char should be length 1"

def cost_of_next(i,j,s,t,cost):
    news = s+"-"
    newt = t+'-'
    print("Next",news[i+1],newt[j+1])
    if(news[i+1]=="-" and newt[j+1]=="-"):
        return 0
    return cost(news[i+1],newt[j+1])

# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.
def fill_cell(table, i, j, s, t, cost):
    print("+++++++++++++")

    # First cell
    if(i==0 and j==0):
        #print(0, "-", "-")
        return DiffingCell(0, "-", "-")

    # First Row
    if(j==0):
        #print(table.get(i-1,j).cost + cost(s[i-1], "-"), s[i-1] , "-")
        return DiffingCell(table.get(i-1,j).cost + cost(s[i-1], "-"), s[i-1] , "-")

    # First Column
    if(i==0):
        #print(table.get(i,j-1).cost + cost("-", t[j-1]), "-", t[j-1])
        return DiffingCell(table.get(i,j-1).cost + cost("-", t[j-1]), "-", t[j-1])

    c1 = table.get(i,j-1).cost + cost("-", t[j-1])
    c2 = table.get(i-1,j).cost + cost(s[i-1], "-")
    c3 = table.get(i-1,j-1).cost + cost(s[i-1], t[j-1])
    cases = { 
        c1: DiffingCell(c1, "-", t[j-1]), 
        c2: DiffingCell(c2, s[i-1], "-"), 
        c3: DiffingCell(c3, s[i-1], t[j-1]), 
    }
    #print(cases.get(min(c1,c2,c3)))
    return cases.get(min(c1,c2,c3))

    # print("================")
    # print("c1", s[i-1], t[j-1])
    # c1 = table.get(i-1,j-1).cost + cost(s[i-1], t[j-1])
    # print("c2", "-", t[j-1])
    # c2 = table.get(i-1,j).cost + cost("-", t[j-1])
    # print("c3", s[i-1], "-")
    # c3 = table.get(i,j-1).cost + cost(s[i-1], "-")
    # cases = { 
    #     c1: DiffingCell(c1+cost_of_next(i-1, j-1,s,t,cost), s[i-1], t[j-1]), 
    #     c2: DiffingCell(c2+cost_of_next(i-2, j-1,s,t,cost), "-", t[j-1]), 
    #     c3: DiffingCell(c3+cost_of_next(i-1, j-2,s,t,cost), s[i-1], "-"), 
    # } 
    # print(i,j,cases.get(min(c1,c2,c3)))
    # return cases.get(min(c1,c2,c3)) 

    # # s_prime = "-"+s
    # t_prime = "-"+t
    # cost = cost(s_prime[i], t_prime[j])
    # print("------")
    # print(i,j)
    # print(cost, s_prime[i], t_prime[j])
    # return DiffingCell(cost, s_prime[i], t_prime[j])


    # i1 = s[i]
    # j1 = t[j]
    # i2 = j2 = "-"
    # if(i < len(s)-1):
    #     i2 = s[i+1]
    # if(j < len(t)-1):
    #     j2 = t[j+1]
    # c11 = cost("-",j1) 
    # c12 = cost(i1,j2)
    # c21 = cost(i1,"-")
    # c22 = cost(i2,j1)
    # if((c11+c12) < (c21+c22)):
    #     print(c11, '-', j1)
    #     return DiffingCell(c11, '-', j1)
    # else:
    #     print(c21, i1, "-")
    #     return DiffingCell(c21, i1, "-")

# Input: n and m, the sizes of s and t, respectively.
# Should return a list of (i,j) tuples, the order you would like us to call fill_cell
def cell_ordering(n,m):
    cells = []
    for i in range(n+1):
        for j in range(m+1):
            cells.append((i,j))
    return cells

# Returns a size-3 tuple (cost, align_s, align_t).
# cost is an integer cost.
# align_s and align_t are strings of the same length demonstrating the alignment.
# See instructions.pdf for more information on align_s and align_t.
def diff_from_table(s, t, table):
    # YOUR CODE HERE
    return (0, "", "")

# Example usage
if __name__ == "__main__":
    # Example cost function from instructions.pdf
    def costfunc(s_char, t_char):
        if s_char == t_char: return 0
        if s_char == 'a':
            if t_char == 'b': return 5
            if t_char == 'c': return 3
            if t_char == '-': return 2
        if s_char == 'b':
            if t_char == 'a': return 1
            if t_char == 'c': return 4
            if t_char == '-': return 2
        if s_char == 'c':
            if t_char == 'a': return 5
            if t_char == 'b': return 5
            if t_char == '-': return 1
        if s_char == '-':
            if t_char == 'a': return 3
            if t_char == 'b': return 3
            if t_char == 'c': return 3

    import dynamic_programming
    s = "acb"
    t = "baa"
    D = dynamic_programming.DynamicProgramTable(len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s = s, t = t, cost=costfunc)
    (cost, align_s, align_t) = diff_from_table(s,t, D)
    print align_s
    print align_t
    print "cost was %d"%cost
