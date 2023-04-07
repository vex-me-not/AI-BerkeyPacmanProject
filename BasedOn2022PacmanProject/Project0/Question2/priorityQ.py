
## ΑΜ 1115201700187
## Χαρίσης Νικόλαος

import heapq ## kanoyme import to heap apo tin lib tis python

class PQ: ## i klassi PriorityQueue, PQ gia syntomia
    def __init__(self): ## o constructor
        self.objectHeap = []
        self.size = 0

    def printQ(self): ## gia na ektyposoyme ta stoixeia tis PQ
        for entry in self.objectHeap:
            print((entry[1], entry[0]))

    def getPQSize(self): ## epistrefei to megethos tis PQ
        return self.size

    def pop(self): ## to pop
        if self.getPQSize() == 0: ## checkaroyme an exoyme adeia PQ
            print("Can't pop from an emtpy PQ")
            return None
        else:
            self.size -= 1 ## prosthesame stoixeio ara to megethos tis PQ meiothike
            return heapq.heappop(self.objectHeap)[1]

    def push(self, item, priority): ## to push
        if item != None:
            self.size += 1  ## prosthesame stoixeio ara to megethos tis PQ megalose
            heapq.heappush(self.objectHeap,(priority,item)) ## akoloytho to format apo to documentation tis heap stin ekfonisi kai gia ayto vazo prota to priority
        else:
            print("Invalid input")

    def isEmpty(self): ## elegxei an i PQ einai empty
        if self.getPQSize() == 0:
            return True
        else:
            return False

    def update(self,item,priority): ## kanei to update.
        if item != None: ## check gia sosto input
            temp = []  ## adeio heap apoy tha metaferoyme ola ta stoixeia kathos kai aytho poy mas zeiteitai gia update
            for entry in self.objectHeap: ## diatrexoyme ta stoixeia toy palioy heap
                if entry[1] != item: ## an den einai to zitoyme stoixeio, to kanoyme push opos einai
                    heapq.heappush(temp,(entry[0],entry[1]))
                else: ## an einai to zitoymeno
                    if entry[0] < priority:  ## an i nea priority einai mikroteri apo tin palia
                        heapq.heappush(temp, (entry[0], entry[1])) ## push opos itam
                    else:
                        heapq.heappush(temp, (priority, entry[1])) ## push me ti nea priority

            self.objectHeap=temp ## to heap tis PQ einai to neo heap poy molis ftiaksame
        else:
            print("Invalid Input!")


def PQSort(NumList):
    pq = PQ() ## dimioyrgoyme mia PQ
    for num in NumList: ## kai pusharoyme ola to stoixeia toy NumList se ayti
        pq.push(num,num)
    sortedList=[]
    while ( not pq.isEmpty()): ## oso i PQ den einai adeia
       sortedList.append(pq.pop()) ## kanoyme pop ta stoixeia tis kai ta vazoyme stin sorted lista
    return sortedList

print("Testing PQ and PQSort!")
q = PQ()
q.push("task1", 1)
q.push("task1", 2)
q.push("task0", 0)

q.printQ()

print("First item is : %s" % q.pop())
print("Second item is : %s" % q.pop())

print("Pushing new Items!")

q.push("task3", 3)
q.push("task4", 4)
q.push("task2", 0)

q.printQ()
print("Updating task3")
q.update("task3",1)
q.printQ()

print("New First item is : %s" % q.pop())
print("New Second item is : %s" % q.pop())

numbers = [1,3,2,34,21,7,-12,-5]
print(numbers)
sortedNumbers = PQSort(numbers)
print(sortedNumbers)


print("Done Testing!")