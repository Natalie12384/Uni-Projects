##############
# QUESTION 1 #
##############

class Edge:
    def __init__(self, capacity, start, end, res, edge):
        """
       		Function description: initialises and characterizes an Edge instance based on parameter inputs. 
               This represents an network graph edge. 
       		Input: 
       			None
       		Output: 
                integer value.
       		Time complexity: O(1)
       		Time complexity analysis: The function is all variable assignments, which are all O(1) time. 
       		Space complexity: O(1)
       		Space complexity analysis: the total memory required does not grow with input size, since 
               all except self.edge is an integer, while self.edge is an reference variable. 
               Thus, O(1)
       		
       	"""
        self.capacity = capacity
        self.flow = 0
        self.start = start
        self.end = end
        self.res = res
        self.edge = edge

    

    def get_residual(self):
        """
       		Function description: Calculates the residual capcity value and returns the integer result.
       		Input: 
       			None
       		Output: 
                integer value.
       		Time complexity: O(1)
       		Time complexity analysis: only a single integer arithmetic calculation operation is done, regardless of input. 
       		Space complexity: O(1)
       		Space complexity analysis: No extra aux space was initialised.
       		
       	"""
        return self.capacity - self.flow

    #delete
    def __repr__(self):
        return f'({self.flow}/{self.capacity}, {self.start}->{self.end})'

def ford_fulkerson(network, s, t):
    """
   		Function description: This function returns the max flow of an given network from node s to t. 
   		Input: 
   			network: Adjacency list of lists of Edge objects, representing an network graph
   			s: integer value that represent source node
            t: integer value that represent sink node
   		Output: 
            integer value, represents max_flow of network.
   		Time complexity: O((V+E)*Max_flow), where E is the number of edges in network array and Max_flow is max number of 
           possible augment paths found, V is the size of network Array
   		Time complexity analysis:              
               Each loop interation intialises an V sized array, visited, which takes O(V) time. 
               Each dfs_augment call in the loop takes O(E) time to find an augment path. The max number of while loop iterations is Max_flow, if it adds 1 unit per loop
   		Space complexity: 
               O(V), were V is the size of the network array
   		Space complexity analysis: 
               The variable visited is initialised and reassigned to a V sized array of False values over the duration of the while loop.
   		
   	"""
    max_flow = 0
    augment = 1
    while augment>0:
        visited= [False]*len(network)
        augment = dfs_augment(s,t ,float('inf'), network, visited)
        max_flow += augment
    return max_flow


def dfs_augment(u, t , bottleneck, network, visited):
    """
   		Function description: This function returns the max flow of an given network from node s to t. 
   		Input: 
   			network: Adjacency list of lists of Edge objects, representing an network graph
   			bottleneck: integer value, represents augment path flow
            u: integer value that represent starting node
            t: integer value that represent sink node
            visited: Array list of Boolean values. 
   		Output: 
            integer value, represents augment flow of network.
   		Time complexity: O(E), where E is the number of edges in network array.
   		Time complexity analysis:              
               The for loop iterates until u equals t. This can take up to E
               number of iterations or recursive calls.
   		Space complexity: 
               O(1)
   		Space complexity analysis: 
               No extra space was initialised. This function is in place.
   		
   	"""
    if u == t:
        return bottleneck
    augment = 0
    visited[u] = True
    for e in network[u]:
        v = e.end
        if not e.res:
            if not visited[v] and e.get_residual()>0:
                augment = dfs_augment(e.end, t, min(bottleneck, e.get_residual()), network, visited)
        elif e.res:
            if not visited[v] and e.capacity >0:
                augment = dfs_augment(e.end, t, min(bottleneck, e.capacity), network, visited)
        if augment > 0:
            if e.res:
                e.capacity -= augment
                e.edge.flow -= augment
            else:
                e.flow +=augment
                e.edge.capacity = e.flow   
            return augment
    return 0
    
def assign(preferences, places):
    """
		Function description: 
            This function returns a list of lists of integers that is order via ford fulkerson algorithm outputs.
  		Approach description: 
            This function creates the network graph representation of people preferences and activities to use as an input for the ford fulkerson max flow algorithm. The algorithm outputs an max flow value and updates a given network graph to show the paths of flow.

            Assuming the capacity of each person node is 1, since there can only be one activity a person can do at a time, the flow of person X to activity Y will indicate allocation for the weekend. The updated network is to be used find which activity is each person node flowing to. 

            The max flow value is used to ensure that the people allocated matches the total reservations available. If flow matches the demand, the flow edge that is saturated from person/participant will indicate which activity the person is assigned to and added to result.
            
		Input: 
		  places: An array based list containing integer values
          preferences: An array list of lists containing integer values
		Output: 
            Array List containing lists of integers
		Time complexity: 
            O(N^3), where N is the size of preferences array
		Time complexity analysis : 
            According to constraints, the size of places(M) is at most N/2. To check if reservations match number of people and Initialising final allocation return list through for loop sized M , O(N/2).
            Therefore O(N).
            
            Calling create_graph() to create network graph is O(N*M+M+N), which can be simplified to O(N^2+2*N), the constant 2 and N can be disregarded as N^2 dominates, simplifying to O(N^2)
            
            The ford_fulkerson() call has complexity O(E*Max_flow). E, the number of edges in the network is at most 6N+N^2. Max_flow is at most N. The time complexity resulted is O((N^2+N)*N), simplified to O(N^3), since N^3 grows cubically and much larger than N^2 or any constant.
            
            The final allocation from maxed out network takes O(N*(1+M)) time, a combination of:
               ( residual to source edge + N/2 activities) * per person (N)
            Simplified to O(N^2).
            
            Final sum is O(N + 2N^2 + N^3), since N^3 grows cubically and much larger than the other N and N^2 values, then the complexity can be simplified to the dominant O(N^3).
            
		Space complexity: 
            O(N^2), where N is the size of preferences array
            
		Space complexity analysis:
            According to constraints, the size of places(M) is at most N/2. The main function initialises final_allocation array, which eventually stores O(N) elements since the sum of number of elements in sub array is N.
            
            create_graph() call creates an network, an array list of lists of Edge instances sized O(M*N + M + N), which can be simplified to O(N^2+2*N), the constant 2 and N can be disregarded as N^2 dominates over the two, simplifying to O(N^2) size
            
            ford_fulkerson() initialises an network sized array, sized at N + 3*M +2,  which can be simplified to O(N)
            
            The total aux space used is O(2*N+N^2), which can be simplified to O(N^2)		
	""" 
    total_demand = sum(places) #O(n/2)
    if  total_demand < len(preferences): 
        return  None 
    final_allocation = []
    for i in places: #O(n/2)
        final_allocation.append([])
    network = create_graph(preferences, places) #O(n^2)
    s = len(network) - 2
    t = len(network) - 1
    
    max_flow = ford_fulkerson(network, s, t)
    if (max_flow ) != total_demand:
        return None
    for i in range(len(preferences)): #O(E)
        for e in network[i]:
            if e.flow >0 :
                place_no = e.end-len(preferences)
                if place_no%3 == 0:
                    index = int(place_no/3)
                    final_allocation[index].append(i)
                elif place_no%3 == 1:
                    index = int((place_no-1)//3)
                    final_allocation[index].append(i)  
    return final_allocation

def create_graph(preferences, places): #n^2
    """
  		Function description: 
          Creates an adjacency list of Edge objects. This represents both a network and it's residual edges.
          Returns an adjacency list of Edge instances.
          
  		Approach description: 
              This function first creates an network representation of both people/participants and places.
              Each particpants and each activity is created as an individual node at O(N) time
              
              A super target node is created, which all activity nodes have an edge to, capacity is the reservation capcity.
              2 extra nodes are created per activity. each with an edge to their corresponding activity. node 1 edge has capacity 2 to indicate need for 2 leaders, while node 2 is for left over participants aimed to fufill the reservation numbers.
              
              A super source node is created to supply flow through to each person. 
              Since the supply node is only connected to the participant nodes, it can only push at most 1 flow per person, making the max flow at most the number of people. 
              
              if the preference of person A to activity A is 2, then a edge capacity of 1 is made to node 1 of activity A. if preference is 1, then edge with capacity 1 is made from person A to node 2. An edge from node 1 to node 2 is made to ensure that if there are more than 2 people with preference 2, then leftovers flow into "make up numbers" node
              
              To create the residual graph edges, each edge created will also create an edge from end to start node and is indicated as such.
  		Input: 
  		  places: An array based list containing integer values
          preferences: An array list of lists containing integer values
  		
        Output:   
          An Array adjancency list of of Edge objects 

  		Time complexity: 
          O(N*M), where N is the size of preference list and M is the size of places list
          
  		Time complexity analysis : 
          initialising an empty network takes O(N+3M+2) time, as per the size variable calculation.
          Adding edges from between preference element, each activity place and super source node takes O(M*N) time. Adding edges from check and place activity to super sink node takes O(M) time in total, initialising nodes and adding edges takes O(N+4M+2+M*N) time. The 2 and 4 are constants which can be disregarded when M and N get arbitrarily large.
          Resulting in O(N+M+M*N)
          Simplified by dominant O(M*N)

  		Space complexity: 
          O(M*N), where N is the size of preference list and M is the size of places list

  		Space complexity analysis:
          The length of the graph represents the total nodes in the network with maximum:
          O(N + super sink node + super source node + 2 check nodes * M + M)
          This can be simplified to O(N + 3M + 2). Simplified to:
            O(N+3M)
              
          The total number of edges in original graph is assigned to the graph based on design:
          source to person (N) + people to activities check (N*M) + check edges (3*M) + activites to sink (M)
          This leads to O(N+N*M+4*M) , simplified to O(N + M + M*N)
              
          To create the residual graph, a copy of all the edges with reverse direction has been made as well, resulting in the final space used is O(2*(N + M + M*N)), again can be disregarded as a constant as M and N dominate over 2
              
         Final aux space used is O(N+3M)nodes + O(N + M + M*N)edges, simplified to O(M*N) as M*N dominates

    """
    network = []
    p_len = len(preferences)
    a_len = len(places)
    size =  p_len + 3*a_len +2
    s = size - 2
    t = size - 1
    for i in range(size):
        network.append([])
        
    for i in range(p_len): #O(N)
        node = network[i]
        add_edge(network,s,i,1)
        for l in range(a_len): #O(M)
            target = p_len + l*3 -1
            if l< len(preferences[i]):
                p = preferences[i][l]           
                if p!= 0:
                    target += p 
                    add_edge(network, i,target,1)
                
    for i in range(a_len): #add check1/2 to place , place to t, check 2 to check 1
        capacity_left = places[i] - 2       
        node = p_len+3*i
        add_edge(network, node, node+2, capacity_left)      
        add_edge(network, node+1, node+2, 2)
        add_edge(network, node+1, node, capacity_left)
        add_edge(network, node+2, t, places[i])

    return network

def add_edge(network, u,v, cap):
    """
		Function description: Creates 2 Edge objects and adds them to an adjacency list. 
        One edge is an orignal directed graph edge, while the second is representative of the residual edge.
		Input: 
			network:Adjacency list of lists of Edge objects, representing an network graph
            u: integer value, representing an starting node
            v:integer value, representing an target node
            cap: integer value, representing an Edge capacity
		Output: 
            None
		Time complexity: 
            O(1)
		Time complexity analysis : 
            5 fixed operations are done regardless of input
		Space complexity: 
            O(1)
		Space complexity analysis:
            This function only uses simple variables and alters prexisting data structures
		
    """
    edge =Edge(cap,u,v, False, None)
    network[u].append(edge)
    # res
    edge_res = Edge(0,v,u, True, edge)
    network[v].append(edge_res)
    edge.edge = edge_res
    return None