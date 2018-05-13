# Writing a simulation program using queues, verify that a multi-counter queue is more efficient / productive than a singe-counter queue.

class Queue:
    MAX = 20  # queue can only hold Max-1 items( to account for rear)

    def __init__(self):
        self.queue = []
        for i in range(self.MAX):
            self.queue.append(0)
        self.front = 0  # location to delete from
        self.rear = 0  # location to insert to

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.size() == self.MAX - 1

    def size(self):
        if self.front == self.rear:  # or self.is_empty()
            return 0
        elif self.front < self.rear:
            return self.rear - self.front
        else:  # wrap around
            return self.rear + self.MAX - self.front

    def enqueue(self, data):
        if self.is_full():
            print("Cannot insert to full queue.")
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % self.MAX

    def dequeue(self):  # delete
        if self.is_empty():
            print("Cannot delete from empty queue.")
        else:
            data = self.queue[self.front]
            self.front = (self.front + 1) % self.MAX
            return data

    def peek(self):
        return self.queue[self.front]

    def display(self):
        if self.front == self.rear:
            print("Empty")
        elif self.front < self.rear:
            for i in range(self.front, self.rear):
                print(self.queue[i],end="")
        else:  # wrap around
            for i in range(self.front, self.MAX):
                print(self.queue[i],end="")
            for j in range(self.rear):
                print(self.queue,end="")


# main
q1 = Queue()
q2 = Queue()
q3 = Queue()
no1 = int(input("Enter number of people in counter 1: "))
no2 = int(input("Enter number of people in counter 2: "))
no3 = int(input("Enter number of people in counter 3: "))
time1 = int(input("Enter productivity at counter 1 in terms of seconds:"))
time2 = int(input("Enter productivity at counter 2 in terms of seconds:"))
time3 = int(input("Enter productivity at counter 3 in terms of seconds:"))

totaltime1 = 0
totaltime2 = 0
totaltime3 = 0

for i in range(0, no1):
    q1.enqueue(1)
for i in range(0, no2):
    q2.enqueue(1)
for i in range(0, no3):
    q3.enqueue(1)

while q1.is_empty() is not True:
    q1.dequeue()
    if q1.is_empty() is not True:
        totaltime1 += time1

while q2.is_empty() is not True:
    q2.dequeue()
    if q2.is_empty() is not True:
        totaltime2 += time2

while q3.is_empty() is not True:
    q3.dequeue()
    if q3.is_empty() is not True:
        totaltime3 += time3

max_time = 0
if totaltime1>max_time:
    max_time = totaltime1
if totaltime2>max_time:
    max_time = totaltime2
if totaltime3>max_time:
    max_time = totaltime3
print("Time spend for first type is: ", max_time, "s")


q4 = Queue()
no4 = no1+no2+no3
print(no4)
for i in range(0, no4):
    q4.enqueue(1)

c1time = 0
c2time = 0
c3time = 0
c1 = 0
c2 = 0
c3 = 0
timer = 0
while q4.is_empty() is not True:
    if c1 == 0:
        q4.dequeue()
        c1 = 1
        c1time = timer
    if c2 == 0:
        q4.dequeue()
        c2 = 1
        c2time = timer
    if c3 == 0:
        q4.dequeue()
        c3time = timer
        c3 = 1
    if c1 == 1 and (timer - c1time) == time1-1:
        c1 = 0
    if c2 == 1 and (timer - c2time) == time2-1:
        c2 = 0
    if c3 == 1 and (timer - c3time) == time3-1:
        c3 = 0
    timer += 1


print("Time spend for 2nd type is: ", timer-1, "s")
if timer -1 < max_time:
    print("2nd one is better")
else:
    print("both are same time")




















