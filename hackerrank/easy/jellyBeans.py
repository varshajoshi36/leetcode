'''
Animesh has  empty candy jars, numbered from  to , with infinite capacity. He performs  operations. Each operation is described by  integers, , , and . Here,  and  are indices of the jars, and  is the number of candies to be added inside each jar whose index lies between  and  (both inclusive). Can you tell the average number of candies after  operations?

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

jars, no_ip = raw_input().split()
jars, no_ip = int(jars), int(no_ip)

inputs = []
for i in range(no_ip):
        list1 = raw_input().split()
        list1 = map(int, list1)
        inputs += [list1]
        
candies = 0

for ip in inputs:
    candies += (ip[1] - ip[0] + 1) * ip[2]
    
print candies/jars
