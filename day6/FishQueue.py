# Alex Zhu
# 12/16/21
# Advent of Code - DAY SIX

class FishQueue:
    class Node:
        def __init__(self,count) -> None:
            self.next = None
            self.count = count
        
        def __str__(self) -> str:
            return str(self.count) + " fish"

        def get_next(self):
            return self.next

        def set_next(self,next) -> None:
            self.next = next

        def get_count(self):
            return self.count

        def set_count(self,count) -> None:
            self.count = count

        def add_count(self,count) -> None:
            self.count += count

    def __init__(self,file) -> None:
        """Initializes fish queue from file. O(n)"""
        f = open(file,'r')
        initial_fish = list(map(int,f.readline().split(','))) #int list representation of input string
        counts = [0]*9

        self.front = None
        self.rear = None

        #counts up all fish, enqueues
        for x in initial_fish:
            counts[x] += 1
        for x in counts:
            self.enqueue(x)
        return

    def __str__(self) -> str:
        node = self.front
        ret_str = "FISH QUEUE: "
        i = 0

        while node:
            ret_str += "[age {0} : {1}] <- ".format(i,str(node))
            node = node.get_next()
            i += 1
        return ret_str[:-3]

    def total_fish(self) -> int:
        """Returns total amount of fish. O(1) technically since queue length is always 8"""
        node = self.front
        total = 0
        while node:
            total += node.get_count()
            node = node.get_next()
        return total

    def enqueue(self,count) -> None:
        """Adds a fish age group to the queue. O(1)"""
        if self.front:
            #at least one node in queue
            new_node = self.Node(count)
            self.rear.set_next(new_node)
            self.rear = new_node
        else:
            #empty queue case, rather than have .isEmpty(), which isn't necessary in this case
            self.front = self.Node(count)
            self.rear = self.front

    def dequeue(self) -> int:
        """Removes a fish age group from front of queue. O(1)"""
        node = self.front
        self.front = node.get_next()
        return node.get_count()

    def lifecycle(self,days) -> None:
        """Simulates lanternfish through lifecycles as per prompt. O(d) where d is days"""
        age6_node = self.front.get_next().get_next().get_next().get_next().get_next().get_next()
        for i in range(days):
            zero_fish = self.dequeue()
            age6_node = age6_node.get_next()
            age6_node.add_count(zero_fish)
            self.enqueue(zero_fish)
