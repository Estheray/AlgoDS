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
    if(news[i+1]=="-" and newt[j+1]=="-"):
        return 0
    return cost(news[i+1],newt[j+1])

# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.
def fill_cell(table, i, j, s, t, cost):
    #print("==================")

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

    ctop = table.get(i,j-1).cost + cost("-", t[j-1])
    cleft = table.get(i-1,j).cost + cost(s[i-1], "-")
    cdiag = table.get(i-1,j-1).cost + cost(s[i-1], t[j-1])
    cases = { 
        ctop: DiffingCell(ctop, "-", t[j-1]),
        cleft: DiffingCell(cleft, s[i-1], "-"),
        cdiag: DiffingCell(cdiag, s[i-1], t[j-1]),
    }
    #print(cases.get(min(ctop,cleft,cdiag)))
    return cases.get(min(ctop,cleft,cdiag))

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
    print("++++++++++++++")
    cost = table.get(len(s),len(t)).cost
    i = len(s)
    j = len(t)
    align_s = ''
    align_t = ''
    cell = table.get(i, j)
    print(cell)
    align_s = cell.s_char + align_s
    align_t = cell.t_char + align_t
    if(cell.s_char != '-'):
        s = s[:-1]
    if(cell.t_char != '-'):
        t = t[:-1]
    while(True):
        ctop = table.get(i, j-1)
        cleft = table.get(i-1, j)
        cdiag = table.get(i-1, j-1)
        minimum = (float("inf"), None)
        print("000000000000000000")
        print(ctop)
        print(cleft)
        print(cdiag)
        if(len(s) == 0):
            s = '-'*len(t)
        if(len(t) == 0):
            t = '-'*len(s)
        print(s,t)
        if((ctop.s_char == s[-1] or ctop.s_char == '-') and 
            (ctop.t_char == t[-1] or ctop.t_char == '-')):
            if(ctop.cost < minimum[0]):
                minimum = (ctop.cost, (i, j-1))
        if((cleft.s_char == s[-1] or cleft.s_char == '-') and 
            (cleft.t_char == t[-1] or cleft.t_char == '-')):
            if(cleft.cost < minimum[0]):
                minimum = (cleft.cost, (i-1, j))
        if((cdiag.s_char == s[-1] or cdiag.s_char == '-') and 
            (cdiag.t_char == t[-1] or cdiag.t_char == '-')):
            if(cdiag.cost < minimum[0]):
                minimum = (cdiag.cost, (i-1, j-1))
        (i,j) = minimum[1]
        cell = table.get(i, j)
        print(cell)
        align_s = cell.s_char + align_s
        align_t = cell.t_char + align_t
        print(align_s, align_t)
        if(cell.s_char != '-'):
            s = s[:-1]
        if(cell.t_char != '-'):
            t = t[:-1]
        if((i==1 and j==0) or (i==0 and j==1)):
            break

    print("++++++++++++++")
    return (cost, align_s, align_t)

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
