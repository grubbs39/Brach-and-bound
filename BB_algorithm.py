items = [[5,3],[4,1]]
depth = 0


class BranchBound():
    def __init__(self):
        self.max_value = 0
        self.best_taken = []
        self.local_value = 0
        self.local_taken = [0] * len(items)
        self.best_taken = self.local_taken[:]
       
    
    def branch_and_bound(self,depth):
        new_depth = depth
        if new_depth < len(items):
            #Take item
            self.local_taken[new_depth] = 1           
            new_depth += 1
            self.branch_and_bound(new_depth)
            
            # Do not take item
            new_depth = depth
            self.local_taken[new_depth] = 0
            new_depth += 1
            self.branch_and_bound(new_depth)
        else:
            self.local_value = 0
            for i,j in zip(self.local_taken,items):
                self.local_value += i*j[0]
            if self.local_value > self.max_value:
                print("ping")
                self.max_value = self.local_value
                self.best_taken = self.local_taken
            
for i in range(5):
    
    print("Here is the time for Backtracking programming:")

    bb = BranchBound()
    
    
    start = time.perf_counter()
    bb.branch_and_bound(depth)
    end = time.perf_counter()   
    
    print("BB Max value: ", bb.max_value)
    print("BB Best taken: ", bb.best_taken)
    print("Time consumed for Knapsack of Breach and Bound Algorithim: ",end - start)
