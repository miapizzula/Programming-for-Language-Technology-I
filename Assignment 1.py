import numbers
def find_largest(args):
    if isinstance(args,list):
        return max(args)
    if isinstance(args,numbers.Number):
        return args
    else:
        return 0

print(find_largest("ok"))

def find_largest_from_the_two(input1,input2):
        x=find_largest(input1)
        y=find_largest(input2)
        if (x>=y):
            return x
        else:
            return y

print (find_largest_from_the_two([0,1],[0,1000]))



