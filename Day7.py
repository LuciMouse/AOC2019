from aocd import data
import itertools

test1_str="3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
"""test2_str="3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
test3_str="3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
"""
test4_str="3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
test5_str="3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
def intcode(list, input_ls):
    """
    interprets the list as intcode
    :param list: intial list
    :input_ls:list of input values.  Each to be used once
    :return: list after program has run
    """
    curr_index=0
    print("Initial List: {}\n".format(list))
    output_ls=[]
    mem=list.copy()
    output=None
    while output!="end":
        result=intcode_interpreter(mem,curr_index,input_ls)
        print("The list is now: {}\n".format(mem))
        mem=result[0]
        curr_index=result[1]
        input_ls=result[2]
        output=result[3]
        if (output!="end") and (output is not None):
            output_ls=output_ls+[output]
    return output_ls[0]



def intcode_interpreter(list,curr_index,input_ls):
    """
    Interprets a single command of intcode
    :param mem: memory string
    :param curr_index: pointer to current index
    :param input: input value
    :return: tuple of result_memory,new_index,input_ls,output
    """
    curr_opcode_value = list[curr_index]
    curr_opcode = curr_opcode_value % 100  # value of 1s digit
    curr_opcode_value = curr_opcode_value // 100  # rest of the value

    if curr_opcode==99:#terminate
        print("The instruction is: {}".format(list[curr_index]))
        return (list,curr_index,input_ls,"end")
    elif curr_opcode in [1,2]:
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
            return (list,curr_index + instruction_length,input_ls,None)
        elif curr_opcode==2:#multiplication
            result=value_1*value_2
            list[result_position] = result
            print("The instruction is: {}".format(list[curr_index:curr_index + 4]))
            return (list, curr_index + instruction_length, input_ls, None)
    elif curr_opcode in [3,4]:
        if curr_opcode_value % 10 == 1:  # immediate mode
            result_position = curr_index + 1
        elif curr_opcode_value % 10 == 0:  # position mode
            position = curr_index + 1
            result_position = list[position]
        instruction_length = 2
        if curr_opcode==3:#input
            print("The instruction is: {}".format(list[curr_index:curr_index + 2]))
            input=input_ls[0]
            list[result_position]=input
            print("input is {}".format(input))
            return (list, curr_index + instruction_length, input_ls[1:], None)
        elif curr_opcode==4:#output
            print("The instruction is: {}".format(list[curr_index:curr_index + 2]))
            output=list[result_position]
            print("output is {}".format(output))
            return (list, curr_index + instruction_length, input_ls, output)
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
                return (list, curr_index, input_ls, None)
            else:
                curr_index=curr_index+3
                return (list, curr_index, input_ls, None)
        elif curr_opcode==6:
            print("The instruction is: {}".format(list[curr_index:curr_index + 2]))
            if value_1==0:
                curr_index=value_2
                return (list, curr_index, input_ls, None)
            else:
                curr_index=curr_index+3
                return (list, curr_index, input_ls, None)
        elif curr_opcode==7:
            print("The instruction is: {}".format(list[curr_index:curr_index + 4]))
            result_position = list[curr_index + 3]
            if value_1<value_2:
                list[result_position]=1
                return (list, curr_index+4, input_ls, None)
            else:
                list[result_position]=0
                return (list, curr_index + 4, input_ls, None)
        elif curr_opcode==8:
            print("The instruction is: {}".format(list[curr_index:curr_index + 4]))
            result_position = list[curr_index + 3]
            if value_1 == value_2:
                list[result_position] = 1
                return (list, curr_index + 4, input_ls, None)
            else:
                list[result_position] = 0
                return (list, curr_index + 4, input_ls, None)
    else:#something other than 1-8, or 99
        print("Bad Input")



def amplification_circuit(list,phase_setting):
    """
    takes a phase setting and runs through the amplifiers
    :param phase_setting:sequence of settings
    :return:output signal
    """
    last_output=0
    for amplifier in range(0,5):
        last_output=intcode(list.copy(),[phase_setting[amplifier],last_output])
        print("done amplifier {}\n".format(amplifier))
    return(last_output)
    print("done circ")

def amplification_circuit_loop(list,phase_setting):
    """
    takes a phase setting and runs through the amplifiers
    :param phase_setting:sequence of settings
    :return:output signal
    """
    #initialize dict with starting values

    amp_dict={
        "amp_A":[list.copy(),0,[phase_setting[0],0]],
        "amp_B":[list.copy(),0,[phase_setting[1]]],
        "amp_C":[list.copy(),0,[phase_setting[2]]],
        "amp_D":[list.copy(),0,[phase_setting[3]]],
        "amp_E":[list.copy(),0,[phase_setting[4]]]
    }
    amp_list=["A","B","C","D","E"]
    amp_pointer=0

    curr_amp="amp_{}".format(amp_list[amp_pointer])
    curr_mem = amp_dict[curr_amp][0]
    curr_index = amp_dict[curr_amp][1]
    curr_input_ls = amp_dict[curr_amp][2]
    print("Initial List: {}\n".format(amp_dict[curr_amp][0]))

    last_e_output=None
    output=None

    while True:


        result=intcode_interpreter(curr_mem,curr_index,curr_input_ls)
        print("The list is now: {}\n".format(result[0]))

        amp_dict[curr_amp][0]=result[0]#memory
        amp_dict[curr_amp][1]=result[1]#index
        amp_dict[curr_amp][2]=result[2]#input list

        curr_mem = amp_dict[curr_amp][0]
        curr_index = amp_dict[curr_amp][1]
        curr_input_ls = amp_dict[curr_amp][2]

        output = result[3]

        #catching output
        if (output != "end") and (output is not None):
            #append to next amp input list
            if amp_pointer<4:
                next_amp=amp_pointer+1
            else:
                next_amp=0
            amp_dict["amp_{}".format(amp_list[next_amp])][2].append(output)

            if curr_amp=="amp_E":
                last_e_output=output
        #if one of the early amplifiers end, we need to switch to the next one
        if output=="end":
            if curr_amp=="amp_E":
                break
            else:
                print("{} terminated".format(curr_amp))
                amp_pointer=amp_pointer+1
                curr_amp = "amp_{}".format(amp_list[amp_pointer])
                print("switching to {}".format(curr_amp))
                curr_mem = amp_dict[curr_amp][0]
                curr_index = amp_dict[curr_amp][1]
                curr_input_ls = amp_dict[curr_amp][2]
                print("Initial List: {}\n".format(amp_dict[curr_amp][0]))

        #switching to next amplifier because of stall
        next_inst=curr_mem[curr_index]
        if (next_inst%100==3) and (curr_input_ls==[]): #if next command is an input command and buffer is empty
            #change to next amp
            if amp_pointer<4:
                amp_pointer=amp_pointer+1
            else:#at end of list
                amp_pointer=0
            curr_amp = "amp_{}".format(amp_list[amp_pointer])
            print("switching to {}".format(curr_amp))
            curr_mem = amp_dict[curr_amp][0]
            curr_index = amp_dict[curr_amp][1]
            curr_input_ls = amp_dict[curr_amp][2]
            print("Initial List: {}\n".format(amp_dict[curr_amp][0]))


    return last_e_output
    print("done circ")

def max_signal(list):
    """
    for a given list, determines the maximum signal and the phase setting that generaes that signal
    :param list: intcode program
    :return: tuple of (max signal, generating phase sequence)
    """
    max_value=(0,[])

    for phase_setting in itertools.permutations([x for x in range(5)]):
        value=amplification_circuit(list,phase_setting)
        if value>max_value[0]:
            max_value=(value, phase_setting)
    return max_value

def max_signal_loop(list):
    """
    for a given list, determines the maximum signal and the phase setting that generaes that signal
    :param list: intcode program
    :return: tuple of (max signal, generating phase sequence)
    """
    max_value = (0, [])
    for phase_setting in itertools.permutations([x for x in range(5,10)]):
        value = amplification_circuit_loop(list, phase_setting)
        if value > max_value[0]:
            max_value = (value, phase_setting)

    return max_value

    print("done")


if __name__=="__main__":
    #test1_ls=[int(N) for N in test1_str.split(',')]
    #result=amplification_circuit(test1_ls,[4,3,2,1,0])

    #test2_ls=[int(N) for N in test2_str.split(',')]
    #result=amplification_circuit(test2_ls,[0,1,2,3,4])

    #test3_ls = [int(N) for N in test3_str.split(',')]
    #result = amplification_circuit(test3_ls, [1, 0, 4, 3, 2])

    """result_1=max_signal(test1_ls)
    result_2 = max_signal(test2_ls)
    result_3 = max_signal(test3_ls)"""

    data_ls=[int(N) for N in data.split(",")]
    #data_result=max_signal(data_ls)

    test4_ls=[int(N)for N in test4_str.split(",")]
    #result_4=amplification_circuit_loop(test4_ls,[9,8,7,6,5])

    test5_ls=[int(N) for N in test5_str.split(",")]
    #result_5=amplification_circuit_loop(test5_ls,[9,7,8,5,6])

    data_result=max_signal_loop(data_ls)
    print("done main")