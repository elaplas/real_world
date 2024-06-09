
"""
In this file, the A* route planner algorithm is implemented. The idea is to calculate the cost of possible paths from start point
to goal point through intermediate points. The task of A* algo is to choose the intermediate points resulting in the minimum cost. 
The algorithm will first expand the start point using all connecting neighbors and then calculating the cost of them. Afterwards the
path with minimum cost is selected, expanded and the corresponding costs are calculated and added to the previously expanded paths. 
Again the path with minimum cost is selected, expanded and the corresponding costs are calculated and added to the previously expanded paths.
This procedure is iteratively repeated till the path ending with goal and has the minimum cost is met. 

The total cost of a path "a-->c-->g",  from start point "a" to goal point "g" where we are already in the point "c": 
t(a, g) = d(a,c) + h(c,g) where d(a,c) is the true distance b/w "a" and "c" and h(c,g) the estimated distance b/w "c" and "g". The 
estimated distance should be less than the true distance to guarantee the optimal solution is found ( for more information
read the comments in the function "calc_h_cost".

Assuming that there are two possible paths from two points "a" and "b" through intermediate point "c" towards the goal point "g":
1st: "a->b->g", 2nd: "a->c->g".  If we are at the point "a", expanding from point "a"  means forming the paths "a->b" and "a->c" and
calculating the corresponding total cost for each of them: d(a,b) + h(b,g) and d(a,c) + h(c,g) where d(a,b) and d(a,c) are true distances and
h(b,g) and h(c,g) estimated distances. 

"""


def calc_euclidean_dis(p_1, p_2):
    """
    Calculates the diagonal distance b/w two 2D points: sqrt( (x1 - x2)^2 + (y1 - y2)^2 ) ) 
    Arguments:
        p_1: first 2D point
        p_2: second 2D point
    Returns:
        diagonal distance
    """
    return ( (p_1[0] - p_2[0])**2 + (p_1[1] - p_2[1])**2 )**0.5 


def calc_manhattan_dis(p_1, p_2):
    """
    Calculates the Manhattan distance b/w two 2D points: |x1 - x2| + |y1 - y2|
    Arguments:
        p_1: first 2D point
        p_2: second 2D point
    Returns:
        Manhattan distance
    """
    return abs(p_1[0] - p_2[0]) + abs(p_1[1] - p_2[1])


def calc_h_cost(p_1, p_2, method="euclidean", mu="0.9"):
    """
    Estimates the distance b/w two 2D points using of one the functions above
    Arguments:
        p_1: first 2D point
        p_2: second 2D point
        method: if "euclidean" the fucntion "calc_euclidean_dis" is called, if "manhattan" the function "calc_manhattan_dis" 
        mu: a float number to reduce the estimate distance to guarantee the optimal path is found
    Returns:
        Estimate distance/cost b/w two 2D points
    """
    
    # The function is used as a "heuristic function" to estimate the distance between two 
    # intersections/points using either "euclidean" (diagonal distacne = sqrt( (x1 - x2)^2 + (y1 - y2)^2 ) ) 
    # or "manhattan" (Mahnhattan distance = |x1 - x2| + |y1 - y2| ). For the diagonal 
    # distance the ratio "mu" can be set to "0.9" or smaller to safely get admissible estimated distance.
    # For the Manhattan distance the ratio "mu" should be set to much smaller value e.g. "0.4" to ensure 
    # the estimated distance is less than the true distance. Choose one the following options:
    #  
    # 1) Recommended choices for diagonal distance: method="euclidean" , mu=0.9
    # 2) Recommended choices for Manhattan distance: method="manhattan" , mu=0.4
    # 
    # In the following you can read more details about the "mu" parameter. 
    # "mu" should be chosen so that the estimated cost is less than the true cost b/w two points.
    # Assuming there are two possibilities reaching a goal, "g", from two points "a" and "b": 
    # 1st: "a"->"c"->"g", 2nd: "b"->"c"->"g" where "c" is an intermediate point. 
    # Lets define "h(a,g)" as the estimated cost b/w "a" and "g", "h(b,g)" as estimated cost b/w "b" and "g", 
    # "d(a,c)" as true cost b/w "a" and "c", "d(b,c)" as true cost b/w "b" and "c". Lets assume the estmaited costs
    # "h(a,g)", "h(b,g)" are less than their corresponding true costs and the estimated cost "h(a,g)" is very slightly 
    # smaller than "h(b,g)", so we will choose the first possibility "a"->"c"->"g" and expand it and calculate the
    # total cost "t(a,g)" equals "d(a,c)+h(c,g)" where "h(c,g)" is the estimated cost b/w "c" and "g". The total cost
    # "t(a,g)" is bigger than the previously estimated cost "h(a,g)" since a portion of the estimated cost "h(a,g)" is 
    # replaced with true cost "d(a,c)" in the total cost "h(a,g)". Now the total cost "t(a,g)" is most probably bigger than the
    # estimated cost "h(b,c)", so for the next choice, we will choose the second option "b"->"c"->"g" and expand it. 
    # Therefore the chance of finding the optimal path is guaranteed if the estimated cost is less than the true cost 
    # for all points. 
    #
    # Smaller values for "mu" will guarantee to find the optimal solution but increase the run-time as they lead to 
    # exploring more possibilities.
        
    if method == "euclidean":
        return calc_euclidean_dis(p_1, p_2) * mu
          
    if method == "manhattan":
        return calc_manhattan_dis(p_1, p_2) * mu
            
    
def calc_total_cost(intersections, path, goal):
    """
    Calculates the total cost of a path
    Arguments:
        intersections: list of 2D points
        path: a list of node names/ids e.g. [1,2,3,..]
        goal: goal name/id
    Returns:
        estimated total cost of a path
    """
    path_cost = 0
    for i in range(len(path)-1):
        p_1 = intersections[path[i]]
        p_2 = intersections[path[i+1]]
        path_cost += calc_euclidean_dis(p_1, p_2)
    
    frontier = path[-1]
    h_cost = calc_h_cost(intersections[frontier], intersections[goal], "euclidean", 0.85)
    
    return h_cost + path_cost
        
# Node to be used in a min heap (helper type)     
class Node:
    def __init__(self, arg_path = [], arg_cost= float('inf')):
        self.path = arg_path
        self.cost = arg_cost

# Custome impl of min heap where the nodes/elements are ordered based on their path cost 
class MinHeap:
    def __init__(self):
        self._data = [None for _ in range(100)]
        self._next = 0
        self._size = 0
        
        
    def push(self, node):
        
        if self._next >= len(self._data):
            self.__resize()
        
        # Put new element in the most right empty spot
        self._data[self._next] = node
        
        # Heapify up
        cur_i = self._next
        while cur_i > 0:
            parent_i = self.__getParent(cur_i)
            if self._data[cur_i].cost < self._data[parent_i].cost:
                tmp=self._data[parent_i]
                self._data[parent_i] = self._data[cur_i]
                self._data[cur_i] = tmp
                cur_i = parent_i
            else:
                break
            
        # Increment next
        self._next += 1
        self._size += 1
            
    def pop(self):
        if not self._size:
            return None
        
        # Put the value of the most right element into the root position
        deleted_node = self._data[0]
        self._data[0] = self._data[self._size-1]
        self._data[self._size-1] = None
        
        # Heapify down
        cur_i = 0
        while cur_i < len(self._data):
            
            left_i = self.__getLeftChild(cur_i)
            right_i = self.__getRightChild(cur_i)
            child_i = left_i
            
            # Take the smaller element as child
            if left_i != -1 and right_i != -1:
                if self._data[left_i] and self._data[right_i]:
                    if self._data[right_i].cost < self._data[left_i].cost:
                        child_i = right_i
                        
            # If current child index out of range         
            if child_i == -1:
                break
            
            # If the value of current child index is "None"
            if not self._data[child_i]:
                break
            
            # If child is smaller than parent, swap them otherwise break the loop
            if self._data[child_i].cost < self._data[cur_i].cost:
                tmp = self._data[child_i]
                self._data[child_i] = self._data[cur_i]
                self._data[cur_i] = tmp
                cur_i = child_i
            else:
                break
          
        # Decrement next
        self._next -= 1
        self._size -= 1
        
        return deleted_node
    
    
    def getSize(self):
        return self._size
    
    
    def __resize(self):
        tmp = [None for _ in range(len(self._data)*2)]
        for i in range(len(self._data)):
            tmp[i] = self._data[i]
        self._data = tmp
                
 
    def __getLeftChild(self, i):
        
        left_i = i*2 + 1 
        if left_i < len(self._data):
            return left_i
        else:
            return -1
    
    def __getRightChild(self, i):
        right_i = i*2 + 2
        if right_i < len(self._data):
            return right_i
        else:
            return -1
    
    def __getParent(self, i):
        return i // 2

    
def shortest_path(M,start,goal):
    """
    Calculates the shortest path b/w a start point and an ending point
    Arguments:
        M: map
        start: starting point
        goal: ending point
    Returns:
        shortest path
    """
    
    print("shortest path called")

    # The idea is to use a min heap and do the following iteratively 
    # until a path consisting of "goal" and has minimum cost is met:
    # Pop the top element, form new paths from it and calculate the corresponding
    # costs of new paths and then put them back into the min heap. 
    
    min_heap = MinHeap()
    start_path = []
    start_path.append(start)
    start_cost = calc_total_cost(M.intersections, start_path, goal)
    min_heap.push(Node(start_path, start_cost))

    popped_node = None
    
    while min_heap.getSize():
        
        popped_node = min_heap.pop()
        frontier = popped_node.path[-1]
        neighbours = M.roads[frontier]
        
        for neighbour in neighbours:
            if neighbour in popped_node.path:
                continue
                
            new_path = []    
            for i in range(len(popped_node.path)):
                new_path.append(popped_node.path[i])
            new_path.append(neighbour)
            new_cost = calc_total_cost(M.intersections, new_path, goal)
            min_heap.push(Node(new_path, new_cost))                
        
        if popped_node.path[-1] == goal:
            break
            
    if popped_node:         
        return popped_node.path
    else:
        return []