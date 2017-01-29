def  rollingString(s, operations):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for operation in operations:
            start, end, op = operation[0], operation[1], operation[2]
            if op is 'L':
                for index in range(start, end + 1):
                    replace_with_index = alphabets.index(s[index]) -1
                    s.replace(s[index], alphabets[replace_with_index])
            elif op is 'R':
                    replace_with_index = alphabets.index(s[index]) + 1
                    if replace_with_index == 27:
                        replace_with_index = 0
                    s.replace(s[index], alphabets[replace_with_index])
                    
    return s

s = abc
3
operation = [0 0 'L',
2 2 'L',
0 2 'R',]

print rollingString(s, operations)
