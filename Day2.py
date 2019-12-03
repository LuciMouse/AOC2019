
TEST_LISTS=[[1,9,10,3,2,3,11,0,99,30,40,50],[1,0,0,0,99],[2,3,0,3,99],[2,4,4,5,99,0],[1,1,1,4,99,5,6,0,99]]

def intcode(list):
    """
    interprets the list as intcode
    :param list: intial list
    :return: list after program has run
    """
    curr_index=0
    curr_opcode=list[curr_index]
    print("Initial List: {}\n".format(list))
    while curr_opcode !=99:
        #print("The command is: {}".format(list[curr_index:curr_index+4]))
        #process the input
        position_1=list[curr_index+1]
        value_1=list[position_1]

        postion_2=list[curr_index+2]
        value_2=list[postion_2]

        result_position=list[curr_index+3]

        if curr_opcode==1:#adding
            result=value_1+value_2
        elif curr_opcode==2:#multiplication
            result=value_1*value_2
        else:#something other than 1,2, or 99
            print("Bad Input")
            break

        list[result_position]=result
        #print("The list is now: {}\n".format(list))
        curr_index=curr_index+4
        curr_opcode = list[curr_index]
    #print("program halt\n")

def parameter_permutation(list,result):
    """
    iterates though verb/noun combinations with the intcode until it produces the desired result
    :param list: list of integers to use as memory
    :param result: the value that should be in address 0
    :return: tuple of noun, verb
    """
    noun_val_list=range(0,99)
    verb_val_list = range(0, 99)

    for curr_noun in noun_val_list:
        for curr_verb in verb_val_list:
            working_list=list.copy()#make a copy of the list to work with
            working_list[1]=curr_noun
            working_list[2]=curr_verb
            intcode(working_list)
            output=working_list[0]
            if output==result:
                return (curr_noun,curr_verb)

if __name__=="__main__":
    #testing

    #single list
    """intcode(TEST_LISTS[0])"""

    #all test lists
    """for curr_list in TEST_LISTS:
        intcode(curr_list)"""

    #real data-Part1
    with open("Day2_input.txt","r") as input_file:
        input_str=input_file.read()
    input_list=[int(N) for N in input_str.split(',')]

    """
    working_list=input_list.copy()

    working_list[1]=12
    working_list[2]=2

    intcode(working_list)
    print("value at postion 0:{}".format(input_list[0]))"""

    #part2
    answer_tuple=parameter_permutation(input_list,19690720)
    answer=100*answer_tuple[0]+answer_tuple[1]

    print("all done")