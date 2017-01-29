def  rollingString(s, operations):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for operation in operations:
            start, end, op = operation.split()
            
            if op is 'L':
                for index in range(int(start), int(end) + 1):
                    replace_with_index = alphabets.index(s[index]) - 1
                    s = s[0:index] + s[index].replace(s[index], alphabets[replace_with_index], 1) + s[index + 1:]
            elif op is 'R':
                for index in range(int(start), int(end) + 1):
                    replace_with_index = alphabets.index(s[index]) + 1
                    if replace_with_index == 26:
                        replace_with_index = 0
                    s = s[0 : index] + s[index].replace(s[index], alphabets[replace_with_index], 1) + s[index + 1:]
                    
    return s

s, operations = 'gcd', ['0 0 L', '2 2 L', '2 2 R', '1 1 R' ]
print rollingString(s, operations)
