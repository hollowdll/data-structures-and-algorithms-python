from e1 import Stack
from e2 import check_balance

def main():
    e2()

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

if __name__ == '__main__':
    main()