from aocd import data
import math

def intcode(list,input):
    """
    interprets the list as intcode
    :param list: intial list
    :return: list after program has run
    """
    curr_index=0
    print("Initial List: {}\n".format(list))

    curr_opcode_value = list[curr_index]

    curr_opcode = curr_opcode_value % 100  # value of 1s digit
    curr_opcode_value = curr_opcode_value // 100  # rest of the value

    while curr_opcode !=99:
        #print("The command is: {}".format(list[curr_index:curr_index+4]))
        #process the input

        if curr_opcode in [1,2]:
            instruction_length=4
            if curr_opcode_value % 10 == 1:  # immediate mode
                value_1 = list[curr_index + 1]
            elif curr_opcode_value % 10 == 0:  # position mode
                position = list[curr_index + 1]
                value_1 = list[position]
            curr_opcode_value = curr_opcode_value // 10  # rest of the value
            if curr_opcode_value % 10 == 1:  # immediate mode
                value_2 = list[curr_index + 2]
            elif curr_opcode_value % 10 == 0:  # immediate mode
                position_2 = list[curr_index + 2]
                value_2 = list[position_2]

            result_position = list[curr_index + 3]

            if curr_opcode==1:#adding
                result=value_1+value_2
                list[result_position] = result
                print("The instruction is: {}".format(list[curr_index:curr_index+4]))
            elif curr_opcode==2:#multiplication
                result=value_1*value_2
                list[result_position] = result
                print("The instruction is: {}".format(list[curr_index:curr_index + 4]))
            curr_index = curr_index + instruction_length
        elif curr_opcode in [3,4]:
            if curr_opcode_value % 10 == 1:  # immediate mode
                result_position = curr_index + 1
            elif curr_opcode_value % 10 == 0:  # position mode
                position = curr_index + 1
                result_position = list[position]
            instruction_length = 2
            if curr_opcode==3:#input
                list[result_position]=input
                print("The instruction is: {}".format(list[curr_index:curr_index + 2]))
            elif curr_opcode==4:#output
                print("The instruction is: {}".format(list[curr_index:curr_index + 2]))
                print (list[result_position])
            curr_index = curr_index + instruction_length
        elif curr_opcode in [5,6,7,8]:
            if curr_opcode_value % 10 == 1:  # immediate mode
                value_1 = list[curr_index + 1]
            elif curr_opcode_value % 10 == 0:  # position mode
                position = list[curr_index + 1]
                value_1 = list[position]
            curr_opcode_value = curr_opcode_value // 10
            if curr_opcode_value % 10 == 1:  # immediate mode
                value_2 = list[curr_index + 2]
            elif curr_opcode_value % 10 == 0:  # position mode
                position = list[curr_index + 2]
                value_2 = list[position]

            if curr_opcode==5:
                print("The instruction is: {}".format(list[curr_index:curr_index + 2]))
                if value_1 != 0:
                    curr_index=value_2
                else:
                    curr_index=curr_index+3
            elif curr_opcode==6:
                print("The instruction is: {}".format(list[curr_index:curr_index + 2]))
                if value_1==0:
                    curr_index=value_2
                else:
                    curr_index=curr_index+3
            elif curr_opcode==7:
                print("The instruction is: {}".format(list[curr_index:curr_index + 4]))
                result_position = list[curr_index + 3]
                if value_1<value_2:
                    list[result_position]=1
                else:
                    list[result_position]=0
                curr_index=curr_index+4
            elif curr_opcode==8:
                print("The instruction is: {}".format(list[curr_index:curr_index + 4]))
                result_position = list[curr_index + 3]
                if value_1 == value_2:
                    list[result_position] = 1
                else:
                    list[result_position] = 0
                curr_index = curr_index + 4



        else:#something other than 1-8, or 99
            print("Bad Input")
            break


        print("The list is now: {}\n".format(list))
        #increment for next loop
        curr_opcode_value = list[curr_index]
        curr_opcode = curr_opcode_value % 100  # value of 1s digit
        curr_opcode_value = curr_opcode_value // 100  # rest of the value
    print("program halt\n")

if __name__=="__main__":

    #test
    test_str="1002,4,3,4,33"
    test_list=[int(N) for N in test_str.split(',')]
    #intcode(test_list,1)

    #actual code
    input_list = [int(N) for N in data.split(',')]
    #intcode(input_list,1)

    #part2:
    test1_str="3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    test1_ls=[int(N) for N in test1_str.split(',')]

    #intcode(test1_ls,10)
    intcode(input_list,5)

    print("done")