import heapq

def k_largest_elements(lst, k):
    return heapq.nlargest(k, lst)

# Example
print(k_largest_elements([3, 1, 5, 12, 2, 11], 3))
