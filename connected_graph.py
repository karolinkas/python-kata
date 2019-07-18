class Node(object):

    """Find if two nodes in a directed graph are connected.
    Based on http://www.codewars.com/kata/53897d3187c26d42ac00040d
    For example:
    a -+-> b -> c -> e
    |
    +-> d
    a.connected_to(a) == true
    a.connected_to(b) == true
    a.connected_to(c) == true
    b.connected_to(d) == false"""

    def __init__(self, value, edges=None):
        #This is describing the Node itself
        self.value = value
        #This is describing all the connections of this Node
        self.edges = edges or []

    def connected_to(self, target):
        # TODO: check if target is defined
        #Check direct connections
        if target in self.edges:
            return True
        #Check indirect connections
        elif self.edges:
            connections = []
            for edge in self.edges:
                connected = Node.connected_to(edge, target)
                connections.append(connected)
            return any(connections)
        #Check if Node equals itself because it's theorectically connected
        elif Node.__eq__(self, target):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.value == other.value
