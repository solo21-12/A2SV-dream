a = ['5','1','8']
a = sorted(a,key= lambda item:int(item),reverse=True)
b = list(int(item) for item in a)
print(a)
print(b)