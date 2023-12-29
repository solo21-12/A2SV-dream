from collections import Counter

t = int(input())

for _ in range(t):
    nums1 = input()
    nums2 = input()
    nums3 = input()
    
    word = nums1 + nums2 + nums3
    
    count = Counter(word)
    
    for char, freq in count.items():
        if freq == 2 and 'A' <= char <= 'C':
            print(char)
