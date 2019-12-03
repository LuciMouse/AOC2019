
TEST_1="R8,U5,L5,D3\nU7,R6,D4,L4"
TEST_2="R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
TEST_3="R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

def node_tracker(path_ls):
    """
    Takes a path list (of form "R75, D30") and returns a list of the co-ordinates of all the nodes the path touches.  Path starts at 0,0
    :param path_ls: list of path instrucstions as direction-distance pairs
    :return: a list of co-ordinates
    """
    curr_node=(0,0)
    node_list=[curr_node]#all paths start at the origin

    for instruction in path_ls:
        direction = instruction[0]
        distance = int(instruction[1:])

        #interpret direction and create distance number of nodes in that direction
        for n in range(0, distance):
            if direction=="R":
                new_node=(curr_node[0]+1,curr_node[1])
            elif direction=="U":
                new_node=(curr_node[0],curr_node[1]+1)
            elif direction=="L":
                new_node=(curr_node[0]-1,curr_node[1])
            elif direction=="D":
                new_node=(curr_node[0],curr_node[1]-1)
            else:
                print("bad direction")
                break
            node_list.append(new_node)
            curr_node=new_node
    return node_list
    print("done")

def intersection_finder(pair_ls):
    """
    given a pair of path lists (that describe a path), returns the manhattan distance to the intersection point of the paths that is closest to the origin
    :param pair_ls: list of a pair of path lists
    :return: list of all nodes where the two paths intersect
    """
    path_1_ls=pair_ls[0]
    path_2_ls=pair_ls[1]

    #find the nodes in each path
    path_1_node_ls=node_tracker(path_1_ls)
    path_2_node_ls=node_tracker(path_2_ls)

    #find nodes in common between both lists
    set_2=set(path_2_node_ls)
    common_nodes=[node for node in path_1_node_ls if node in set_2]

    #drop (0,0) node
    common_nodes.remove((0,0))

    return (common_nodes,path_1_node_ls,path_2_node_ls)

    print("done")

def string_to_pair_list(path_string):
    """
    takes a path string and converts it into  pair of lists
    :param path_string: single string to split up
    :return: list of a pair of path strings
    """
    pair_ls = path_string.split("\n")  # split into pair of strings
    pair_split_ls = []
    for sub_list in pair_ls:  # split each sublist along commas
        pair_split_ls.append(sub_list.split(","))
    return pair_split_ls

def shortest_distance(path_string):
    """
    takes a path string, splits it up, and finds the intersection closest to the origin
    :param path_string: single string describing two paths
    :return: shortest distance
    """
    split_ls=string_to_pair_list(path_string)
    nodes_tuple=intersection_finder(split_ls)
    common_nodes=nodes_tuple[0]
    # calculate distance to first node (or I'd have to set min distance to an arbitrary large number
    curr_node = common_nodes[0]
    x_dist = abs(curr_node[0])
    y_dist = abs(curr_node[1])
    total_dist = x_dist + y_dist
    common_nodes.remove(curr_node)
    min_distance = total_dist  # this is now the value to beat

    # look at all other intersections and see if they're closer
    for curr_node in common_nodes:
        x_dist = abs(curr_node[0])
        y_dist = abs(curr_node[1])
        total_dist = x_dist + y_dist

        if total_dist < min_distance:
            min_distance = total_dist

    return min_distance

def fewest_steps(path_string):
    """
        takes a path string, splits it up, and finds the intersection requiring the fewest steps
        :param path_string: single string describing two paths
        :return: fewest steps
        """
    split_ls = string_to_pair_list(path_string)
    nodes_tuple = intersection_finder(split_ls)
    common_nodes = nodes_tuple[0]
    path1_nodes = nodes_tuple[1]
    path2_nodes = nodes_tuple[2]

    # calculate distance to first node (or I'd have to set min distance to an arbitrary large number
    curr_node = common_nodes[0]
    path1_dist = path1_nodes.index(curr_node)
    path2_dist = path2_nodes.index(curr_node)
    total_dist = path1_dist + path2_dist
    common_nodes.remove(curr_node)
    min_distance = total_dist  # this is now the value to beat

    # look at all other intersections and see if they're closer
    for curr_node in common_nodes:
        path1_dist = path1_nodes.index(curr_node)
        path2_dist = path2_nodes.index(curr_node)
        total_dist = path1_dist + path2_dist

        if total_dist < min_distance:
            min_distance = total_dist

    return min_distance

if __name__=="__main__":
    #part1

    #tests


    #test node_tracker
    """test_a=node_tracker(["R8","U5","L5","D3"])
    test_b=node_tracker(test1_pair_split_ls[0])"""

    #test shortest distance
    #shortest_distance(TEST_1)#should be 6
    #shortest_distance(TEST_2) # should be 159
    #shortest_distance(TEST_3) #should be 135

    #actual data
    with open("Day3_input.txt","r")as input_file:
        input_str=input_file.read()
    """distance=shortest_distance(input_str)
    print(distance)"""

    #part2

    #tests
    """fewest_steps(TEST_1)#should be 30
    fewest_steps(TEST_2)  # should be 610
    fewest_steps(TEST_3)  # should be 410"""

    #actual
    steps=fewest_steps(input_str)
    print(steps)

    print("done")