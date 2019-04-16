# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Arti','pooja','Rohan','Parth']
# for person in people:
#     print(person)
for person in people:
    if person == 'Rohan':
        continue
    print(person)

for i in range(0,10):
    print(i)
# While loops execute a set of statements as long as a condition is true.
count =0
while count<=6:
    print(count)
    count +=1