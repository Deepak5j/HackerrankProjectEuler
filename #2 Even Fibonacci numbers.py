import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a, b, sm = 1, 2, 0
    
    for i in range(n):
        c = a + b
        if b%2 == 0:
            sm += b
        a = b
        b = c
        
        if c>n:
            break;

    print(sm)