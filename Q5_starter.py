import numpy as np

class Node:
    """
        A node class for A* Pathfinding
        parent is parent of the current Node
        position is current position of the Node in the maze
        g is cost from start to current Node
        h is heuristic based estimated cost for current Node to end Node
        f is total cost of present node i.e. :  f = g + h
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position

#This function return the path of the search
def return_path(current_node,maze):
    path = []
    no_rows, no_columns = np.shape(maze)
    # here we create the initialized result maze with -1 in every position
    result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    # Return reversed path as we need to show from start to end path
    path = path[::-1]
    start_value = 0
    # we update the path of start to end found by A-star serch with every step incremented by 1
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    return result


def search(maze, cost, start, end):
    """
        Returns a list of tuples as a path from the given start to the given end in the given maze
        :param maze:
        :param cost
        :param start:
        :param end:
        :return:
    """

    # Create start and end node with initized values for g, h and f

    # Initialize both yet_to_visit and visited list
    # in this list we will put all node that are yet_to_visit for exploration. 
    # From here we will find the lowest cost node to expand next

    # in this list we will put all node those already explored so that we don't explore it again

    
    # Add the start node


    # Adding a stop condition. This is to avoid any infinite loop and stop 
    # execution after some reasonable number of steps


    # what squares do we search . serarch movement is left-right-top-bottom 
    #(4 movements) from every positon


    """
        1) We first get the current node by comparing all f cost and selecting the lowest cost node for further expansion
        2) Check max iteration reached or not . Set a message and stop execution
        3) Remove the selected node from yet_to_visit list and add this node to visited list
        4) Perofmr Goal test and return the path else perform below steps
        5) For selected node find out all children (use move to find children)
            a) get the current postion for the selected node (this becomes parent node for the children)
            b) check if a valid position exist (boundary will make few nodes invalid)
            c) if any node is a wall then ignore that
            d) add to valid children node list for the selected parent
            
            For all the children node
                a) if child in visited list then ignore it and try next node
                b) calculate child node g, h and f values
                c) if child in yet_to_visit list then ignore it
                d) else move the child to yet_to_visit list
    """
    #find maze has got how many rows and columns 

    
    # Loop until you find the end
    
        
        # Every time any node is referred from yet_to_visit list, counter of limit operation incremented


        
        # Get the current node

                
        # if we hit this point return the path such as it may be no solution or 
        # computation cost is too high


        # Pop current node out off yet_to_visit list, add to visited list


        # test if goal is reached or not, if yes then return the path


        # Generate children from all adjacent squares



            # Get node position
            
            # Make sure within range (check if within maze boundary)
            
            # Make sure walkable terrain
            

            # Create new node


            # Append

        # Loop through children

            
            # Child is on the visited list (search entire visited list)


            # Create the f, g, and h values


            ## Heuristic costs calculated here, this is using eucledian distance


            # Child is already in the yet_to_visit list and g cost is already lower


            # Add the child to the yet_to_visit list
    pass


if __name__ == '__main__':

    maze = [[0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    
    start = [0, 0] # starting position
    end = [4,5] # ending position
    cost = 1 # cost per movement

    path = search(maze,cost, start, end)
    print(path)

    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in path]))