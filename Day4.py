from aocd import data

TEST_ls=[111111,223450,123789]

def password_test(number):
   """
   given a number, returns whether it follows the password rules
   :param number: number to be tested
   :return: bool
   """
   password=str(number)
   adjacent=False
   increment=True
   for i in range(len(password) - 1):
       if password[i]==password[i+1]:
           adjacent=True
       if int(password[i+1])<int(password[i]):
           increment=False

   return 1 if adjacent and increment else 0

def password_counter(min,max):
    """
    Works though given range of numbers.  If there are fewer than 3 items,
    tests each one and returns the sum of passwords found.
    Otherwise recursively calls itself with a subset of the range
    :param min: minimum number to consider
    :param max: maximum number to consider
    :return: number of passwords found within the range
    """
    if max-min==1:#two numbers are adjacent
        return sum([password_test(min),password_test(max)])
    elif max-min==2:#three numbers in range
        return sum([password_test(min),
                   password_test(max-1),
                   password_test(max)])
    else:
        mid=(max-min)//2+min
        return sum([password_counter(min,mid),
                   password_counter(mid+1,max)])


if __name__=="__main__":

    """Part 1"""
    #test
    for password in TEST_ls:
        print("{} {}".format(password,password_test(password)))
    #data
    number_range=data.split("-")
    min=int(number_range[0])
    max=int(number_range[1])

    num_pass=password_counter(min,max)
    print(num_pass)