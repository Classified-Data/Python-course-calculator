total = 100

complited = int(input('Please enter the number of assignments completed: '))

worth = 0
grades = 0


while complited > 0:

    complited = complited - 1
    percentage = float(input('Enter the % worth of assignment: '))
    mark = float(input('Enter the recieved mark (on a 0-100 scale): '))
    worth += percentage
    grades += mark * percentage

print ('')

ca1 = grades / total
ca4 = grades / worth
print ('Your current standing % total is at: ' + str(ca4))

ca2 = 100 - worth
print ('Remaining marks available to obtain: ' + str(ca2))

ca3 = worth - ca1
print ('Your % dropped: ' + str(ca3))


g3 = ((45 - ca1) / ca2) * 100
print ('Do get a 3, You need: ' + str(g3) + '%')
g4 = ((50 - ca1) / ca2) * 100
print ('Do get a 4, You need: ' + str(g4) + '%')
g5 = ((65 - ca1) / ca2) * 100
print ('Do get a 5, You need: ' + str(g5) + '%')
g6 = ((75 - ca1) / ca2) * 100
print ('Do get a 6, You need: ' + str(g6) + '%')
g7 = ((85 - ca1) / ca2) * 100
print ('Do get a 7, You need: ' + str(g7) + '%')
