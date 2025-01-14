import sys
input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()
string3 = input().rstrip()

lit = []
lit.append(string1[0])
lit.append(string2[0])
lit.append(string3[0])
if ("l" in lit) and("k" in lit) and ("p" in lit):
    print("GLOBAL")
else:
    print("PONIX")