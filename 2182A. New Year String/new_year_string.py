t = int(input())
 
for i in range(t):
    n = int(input())
    s = input()
 
    a = 10**9
    for i in range(n - 3):
        b = 0
        if s[i] != '2': b += 1
        if s[i+1] != '0': b += 1
        if s[i+2] != '2': b += 1
        if s[i+3] != '6': b += 1
        a = min(a, b)
    c = 0
    d = -1
 
    for i in range(n - 3):
        if s[i:i+4] == "2025" and d < i:
            c += 1
            d = i + 3
 
    a = min(a, c)
    print(a)
