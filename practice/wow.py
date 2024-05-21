
def is_valid(s):
    # Initialize a list to keep track of open brackets
    open_brackets = []
    
    for char in s:
        if char in '({[':
            # If it's an open bracket, add it to the list
            open_brackets.append(char)
        elif char in ')}]':
            # If it's a close bracket, check if it matches the last open bracket
            if not open_brackets:
                return False
            last_open = open_brackets.pop()
            if char == ')' and last_open != '(':
                return False
            elif char == '}' and last_open != '{':
                return False
            elif char == ']' and last_open != '[':
                return False

    # If there are any open brackets left, it's not valid
    return len(open_brackets) == 0

# Test the function
s1 = "(){}[]"
print(is_valid(s1))  # Output: True

s2 = "({[})]"
print(is_valid(s2))  # Output: False

s3 = "([{}])"
print(is_valid(s3))  # Output: True

s4 = "({)}"
print(is_valid(s4))  # Output: False
