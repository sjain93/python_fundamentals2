def speed(dist, min):
    secs = min*60
    speed = dist/secs
    return speed

person1 = 'person 1'
person2 = 'person 2'
person3 = 'person 3'

speed1 = 0
speed2 = 0
speed3 = 0

contestants = [person1, person2, person3]
speeds = [speed1, speed2, speed3]

for i in range(len(contestants)):
    athlete = contestants[i]
    print("How far did {} run (in metres)?".format(athlete))
    arg1 = int(input())
    print("How long (in minutes) did {} take to run {} metres?".format(athlete, arg1))
    arg2 = int(input())
    speeds[i] = speed(arg1, arg2)

if speeds[2] > speeds[1] and speeds[2] > speeds[0]:
  print("Person 3 was the fastest at {} m/s".format(speeds[2]))
elif speeds[1] > speeds[2] and speeds[1] > speeds[0]:
  print("Person 2 was the fastest at {} m/s".format(speeds[1]))
elif speeds[0] > speeds[2] and speeds[0] > speeds[1]:
  print("Person 1 was the fastest at {} m/s".format(speeds[0]))
elif speeds[0] == speeds[1] and speeds[1] == speeds[2]:
  print("Everyone tied at {} m/s".format(speeds[0]))

print("Well done everyone!")
