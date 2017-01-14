'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

def reconstructQueue(people):
	people_ordered = [people[0]]
	for person in people[1:]:
		max_people_before = person[1]
		height = person[0]
		no_greater = 0
		insert_index = 0
		index = 0
		for index in range(len(people_ordered)):
			if people_ordered[index][0] >= height and no_greater < max_people_before:
				no_greater += 1
			if (no_greater < max_people_before and people_ordered[index][0] >= height) or (people_ordered[index][0] < height and people_ordered[index][1] > insert_index):
				insert_index += 1
		people_ordered.insert(insert_index + 1, person)
		'''while no_greater < max_people_before and index < len(people_ordered):
			if people_ordered[index][0] >= height:
				no_greater += 1

			index += 1
		people_ordered.insert(index - 1, person)'''

	return people_ordered

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#people = []
print reconstructQueue(people)
