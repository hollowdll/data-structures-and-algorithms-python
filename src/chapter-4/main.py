from e1 import Stack
from e2 import check_balance
from e5 import get_pairs

def main():
    e5()

def e1():
    mystack = Stack()
    mystack.push('A')
    mystack.push('X')
    mystack.push('M')
    val = mystack.pop()
    print(val, mystack)  # M, <Stack (2 elements): [X, A]>

def e2():
    text = 'a(b)c[d]e{f}g'
    result = check_balance(text)
    print(result)   # Ok - 3

def e5():
    nums = [1,2,3,4,5,6,7,8,6,6,4,5,3]
    print(get_pairs(nums))

if __name__ == '__main__':
    main()