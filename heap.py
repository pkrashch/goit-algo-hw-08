import heapq

def minimize_connection_cost(cable_lengths):
    """
    Finds the minimum total cost to connect all network cables.
    This is achieved by using a Min-Heap (Priority Queue) to always
    combine the two shortest available cables.

    The cost of connection is the sum of the two cable lengths.
    """
    
    # 1. Initialize the Min-Heap
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    # 2. Iteration: Combine cables until only one remains
    while len(cable_lengths) > 1:
        
        # a) Extract the two smallest cables (O(log N))
        C1 = heapq.heappop(cable_lengths)
        C2 = heapq.heappop(cable_lengths)
        
        # b) Calculate the cost of the current connection
        connection_cost = C1 + C2
        
        # c) Accumulate the cost to the total
        total_cost += connection_cost
        
        # d) Insert the new combined cable back into the heap (O(log N))
        # This new cable (connection_cost) will be considered in future steps.
        heapq.heappush(cable_lengths, connection_cost)
        
    return total_cost

# =======================================================
# TESTING AND EXECUTION
# =======================================================

if __name__ == '__main__':
    
    # Example 1: [4, 3, 2, 6] -> Min Cost: 29
    cables_1 = [4, 3, 2, 6]
    # Use .copy() to ensure the original list is not modified by heapify
    min_cost_1 = minimize_connection_cost(cables_1.copy()) 
    print(f"Cable lengths: {cables_1}")
    print(f"Minimum Connection Cost: {min_cost_1}\n")

    # Example 2: [1, 2, 3, 4, 5] -> Min Cost: 33
    cables_2 = [1, 2, 3, 4, 5]
    min_cost_2 = minimize_connection_cost(cables_2.copy())
    print(f"Cable lengths: {cables_2}")
    print(f"Minimum Connection Cost: {min_cost_2}\n")