from itertools import permutations

def all_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Example
string = "abc"
print(all_permutations(string))
