'''
Given an array A of size N having distinct elements,
the task is to find the next greater element for each element of the array in order of their appearance in the array.
If no such element exists, output -1
'''


def next_larger_element(array):
    stack = []
    stack.append(array[0])
    for i in range(1, len(array)):
        next_e = array[i]

        if len(stack) == 0:
            stack.append(next_e)
        while len(stack) > 0:
            if stack[0] < next_e:
                print(str(stack.pop()) + ' ->> ' + str(next_e))
            else: break
        stack.append(next_e)

    while len(stack) > 0:
        print(str(stack.pop()) + ' ->> ' + str(-1))
    print('')
    return


next_larger_element([4,25,2,26])

next_larger_element([3,-1,-3,-5])