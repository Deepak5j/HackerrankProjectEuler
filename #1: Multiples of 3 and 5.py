#!/bin/python3X

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1

    asum, bsum, csum = 0, 0, 0
    
    a1 = 3
    an = n - (n%3)
    n1 = an // 3
    asum = (n1 * (a1+an))//2 
    
    b1 = 5
    bn = n - (n%5) 
    n2 = bn // 5
    bsum = (n2 * (b1+bn))//2

    
    if n>=15:
        c1 = 15
        cn = n - (n%15) 
        n3 = cn // 15
        csum = (n3 * (c1+cn))//2

    
    print(int(asum+bsum-csum))
    
    
    
