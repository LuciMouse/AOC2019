import pandas as pd
import numpy as np
import math

TEST_PD = pd.DataFrame([14, 1969, 100756])

def module_fuel_requirement(mass):
    """
    Takes into account the mass of the fuel
    :param mass: mass of the module
    :return: fuel requirement for the module + required fuel
    """
    cum_fuel=0 #running total of amount of fuel needed
    curr_mass=mass[0] #current mass that we are calculating fuel requirement for.  Initialize to module mass
    print("The module has mass of {}".format(mass[0]))

    while curr_mass>0:
        curr_fuel=fuel_calculator(curr_mass)#amount of fuel needed for mass under consideration
        curr_mass=curr_fuel #fuel mass becomes the mass under consideration
        if curr_fuel>0:
            print("This requires {} fuel".format(curr_fuel))
            cum_fuel = cum_fuel + curr_fuel  # add it to the running total
        else:
            print("This requires {} fuel and is handled by wishing\n".format(curr_fuel))
    #print("The module required a total of {} fuel\n".format(cum_fuel))
    return cum_fuel



def fuel_calculator(mass):
    return math.floor(mass/3)-2

if __name__=="__main__":
    #Part1

    #test
    test_results_pd=TEST_PD.apply(fuel_calculator,axis=1)
    #Actual Data
    with open("Day1_input.csv") as input_csv:
        input_pd=pd.read_csv(input_csv,header=None)
    fuels_pd=input_pd.apply(fuel_calculator,axis=1)
    total_fuel=fuels_pd.sum()
    print("The sum of fuel requirements is {}\n".format(total_fuel))

    #Part2

    #test
    test_results_pd = TEST_PD.apply(module_fuel_requirement, axis=1)

    #Actual Data
    fuels_pd = input_pd.apply(module_fuel_requirement, axis=1)
    total_fuel = fuels_pd.sum()
    print("The sum of fuel requirements (including the mass of fuel) is {}\n".format(total_fuel))

    print("all done")