def palindrome(s):
    from collections import Counter
    
    count = Counter(s)
    odd_count = sum(1 for v in count.values() if v % 2 != 0)

    return odd_count == 0

n = int(input())
s = input().strip()
length = len(s)

if length % 2 == 1:
    middle_index = length // 2
    s = s[:middle_index] + s[middle_index + 1:]

if palindrome(s):
    print("Yes")
else:
    print("No")
