### Part Three -- your code goes here. 
a = input("input numbers seperated by spaces: ")#
b = list(map(int, a.split()))
b.sort()
b.remove(1)
b.extend([7,8])
print(b)