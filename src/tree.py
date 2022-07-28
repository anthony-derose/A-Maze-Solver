class Node:
    def __init__(self, parent, position, gPosition, alg):
        self.parent = parent
        self.row = position[0]
        self.col = position[1]
        self.g = 1000000  # cost to get to this node from the starting point
        self.h = self.manhattan(gPosition)  # heuristic:= manhattan distance
        self.f = self.g+self.h
        self.search = 0
        self.visible = 0
        self.alg = alg  # true means large g, false means little g

    def __cmp__(self, other):  # for putting nodes into the heap
        return cmp(self.f, other.f)

    # def __lt__(self, other): ## for large g
       # if self.f == other.f:
        # return ((self.g>other.g))
        # else:
        # return (self.f<other.f)

    def __lt__(self, other):  # Tie breaking large and small G
        if self.alg == True:  # large G case
            if self.f == other.f:
                return ((self.g > other.g))
            else:
                return (self.f < other.f)
        else:  # small G case
            if self.f == other.f:
                return ((self.g < other.g))
            else:
                return (self.f < other.f)

    # gives the manhattan distance from current node to the goal node
    def manhattan(self, gPosition):
        x1 = self.row
        y1 = self.col
        x2 = gPosition[0]
        y2 = gPosition[1]
        distance = abs(x1-x2)+abs(y1-y2)
        return distance  # h(n)


# infinity represented as 1,000,000


# function to calculate f(n) = g(n) + h(n)
if __name__ == "__main__":
    print(manhattan())
