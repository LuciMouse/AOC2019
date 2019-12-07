from aocd import data

test_str="COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
test2_str="COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN"

def orbit_map_counter(orbit_list):
    """
    takes the list of orbits and returns the total number of orbits
    :param orbit_list: list of orbit relationships
    :return: total number of orbits
    """
    #node are in the format (node_name,curr_count,[child nodes])
    root=("COM",0)
    mapped=add_node(root,orbit_list)
    count=orbit_counter(mapped)
    return count
    print("foo")

def add_node(node, orbit_list):
    """
    looks through the orbit list and finds the next node(s)
    :param node: current node to search for
    :param orbit_list: list of nodes that need to be added
    :param count: count of all orbits up to this point
    :return: (tuple of map and count)
    """
    object=node[0]
    curr_count=node[1]
    next_nodes=[orbit for orbit in orbit_list if orbit[0]==object]
    if len(next_nodes)==0:#no further nodes
        return(object,curr_count,[])
    else:
        return(object,curr_count,[add_node((new_node[1],curr_count+1),orbit_list) for new_node in next_nodes])
    print ("foo")

def orbit_counter(node):
    """
    given a mapped orbit, counts the cumulative sum of all orbits
    :param node: node under consideration
    :return:
    """
    if len(node[2])==0:#no further nodes
        return node[1]
    else:#has child nodes
        return node[1]+sum([orbit_counter(new_node) for new_node in node[2]])

def transfer_calc(orbit_list,pos_1,pos_2):
    """
    calculates number of transfers needed to go from position 1 to position2
    :param orbit_list: list of orbits
    :return: min number of transfers needed
    """
    root = ("COM", 0)
    mapped_orbits = add_node(root, orbit_list)

    #map path back to COM for both pos_1 and pos_2
    pos_1_path=pathmapper(orbit_list,pos_1)
    pos_2_path = pathmapper(orbit_list, pos_2)

    common_nodes=[node for node in pos_1_path if node in pos_2_path]
    farthest_node = common_nodes[len(common_nodes)-1]
    pos_1_dist_to_common=node_dist(pos_1_path,farthest_node, pos_1)
    pos_2_dist_to_common=node_dist(pos_2_path,farthest_node,pos_2)
    return pos_1_dist_to_common+pos_2_dist_to_common-2
    print("done")

def pathmapper(orbit_list,object):
    """
    creates path from COM to target
    :param target: target node
    :return: string of interviening nodes
    """
    prev_node=[orbit for orbit in orbit_list if orbit[1]==object]
    if prev_node[0][0]=="COM":#this is the origin node
        return ["COM",object]
    else:
        return pathmapper(orbit_list,prev_node[0][0])+[object]

def node_dist(path,node_1, node_2):
      """
      Calculates distance between node1 and node2
      :param path: list of nodes in order
      :param node_1:
      :param node_2:
      :return: distance between two nodes
      """
      index_1=path.index(node_1)
      index_2=path.index(node_2)
      distance = abs(index_1-index_2)
      return distance
if __name__=="__main__":
    test_ls=test2_str.split("\n")
    #split_ls=[x.split(")") for x in test_ls]
    #orbit_map_counter(split_ls)

    data_ls=data.split("\n")
    split_ls=[x.split(")") for x in data_ls]
    #count=orbit_map_counter(split_ls)

    distance=transfer_calc(split_ls,"YOU","SAN")
    print("foo")