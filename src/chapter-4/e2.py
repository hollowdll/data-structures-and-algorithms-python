from e1 import Stack

def result_ok(pairs_found):
    return f'Ok - {pairs_found}'

def result_error(pos):
    return f'Match error at position {pos}'

def check_balance(text):
    opening_brackets = '({['
    closing_brackets = ')}]'
    bracket_pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    pairs_found = 0
    mystack = Stack()

    for i, char in enumerate(text):
        if char in opening_brackets:
            mystack.push(char)
        elif char in closing_brackets:
            if not mystack or mystack.pop() != bracket_pairs[char]:
                return result_error(i)
            else:
                pairs_found += 1
    
    # Unmatched opening bracket
    if mystack._size > 0:
        return result_error(len(text) - 1)
            
    return result_ok(pairs_found)    