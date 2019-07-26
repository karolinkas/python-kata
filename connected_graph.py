class Node(object):

    def __init__(self, value, edges=None):
        #This is describing the Node itself
        self.value = value
        #This is describing all the connections of this Node
        self.edges = edges or []

    def connected_to(self, target):
        #Create a dictionary to store all nodes/stops we have already
        #been to avoid going through one stop twice
        beenThere = {}

        if target is None:
            print("error");
        #Check direct connections
        if target in self.edges:
            beenThere[vars(target)['value']] = True;
            return True
        #Check indirect connections
        elif self.edges:
            connections = []
            for edge in self.edges:
                currentEdgeValue = vars(edge)['value']
                #Check if edges allow any further connections and if you have already been there
                targetConnected = Node.connected_to(edge, target) and not beenThere.get(currentEdgeValue, False)
                connections = targetConnected
                connections.append(connections)
            return any(connections)
        #Check if Node equals itself because it's theorectically connected
        elif Node.__eq__(self, target):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.value == other.value
