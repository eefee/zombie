print
people_on_left = range(0, 4)
choices = []
first = 0

##################################
class Person:
	def __init__(self, name, time_to_cross):
		self.name = name
		self.time_to_cross = time_to_cross
people = (Person("John", 1), Person("Ringo", 2), Person("Paul", 5), Person("George", 10))
###################################
def calcPeopleOnLeft(list_of_crossings):
	left = list(people_on_left)
	returning_people = []
	right = []
	for crossing in list_of_crossings:
		right.append(min(crossing))
		right.append(max(crossing))
		returning_person = min(right)
		returning_people.append(returning_person)
		right.remove(returning_person)
	left = list(crossing for crossing in left if crossing not in right)
	returning_people.pop()
	return left, returning_people

###################################
def mergeChoices(current_crossings, possible_crossings):
	merged_choices = []
	current_crossings_to_delete = list(current_crossings)
	for choice_pair in possible_crossings:
		merged_choices = list(current_crossings)
		merged_choices.append(choice_pair)
		choices.append(merged_choices)

###################################
def calcPossibleCrossings(left):
	possible_crossings = []
	for outer in range(0, len(left) - 1):
		for inner in range(outer + 1, len(left)):
			possible_crossings.append([[left[outer], left[inner]]])
	return possible_crossings

###################################
#people_who_crossed = [[0, 1], [0, 2], [0, 3]]
def calcTimeTaken(people_who_crossed):
	time_taken = 0
	left, returning_people = calcPeopleOnLeft(people_who_crossed)
	for crossing in people_who_crossed:
		time_taken += people[max(crossing)].time_to_cross
	for returning_person in returning_people:
		time_taken += people[returning_person].time_to_cross
	return time_taken


###################################
choices = calcPossibleCrossings(people_on_left)
should_break = False
crossings_to_delete = []
while True:
	choices_copy = list(choices)
	for current_crossing in choices:
		left, returning_people = calcPeopleOnLeft(current_crossing)
		if len(left) > 1: 
			new_choices = calcPossibleCrossings(left)
			new_choices = [item for sublist in new_choices for item in sublist]
			mergeChoices(current_crossing, new_choices)
			crossings_to_delete.append(current_crossing)
		else:
			should_break = True
			break
			
	if should_break == True:
		break
for crossing_to_delete in crossings_to_delete:
	choices.remove(crossing_to_delete)

total_time = 0
for choice in choices:
	total_time = calcTimeTaken(choice)
	if total_time < 18:
		solution = list(choice)
		break
left, returning_people = calcPeopleOnLeft(solution)
for index in range(0, 3):
	first_person = people[solution[index][0]].name
	second_person = people[solution[index][1]].name
	print first_person, "crossed with", second_person
	if index != 2:
		print people[returning_people[index]].name, "came back with the lantern"
	print
print "Yay we crossed, chop down the bridge!"
print "It took ", total_time, " minutes"
print
