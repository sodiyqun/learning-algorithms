# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 14:48:15 2022

@author: sodiyqun
"""

## N factorial calculation algorithm
"""N factorial is the product of numbers from 1 to N. 
For example, if N = 5: 
5 factorial is equal to 1 * 2 * 3 * 4 * 5 = 120."""

# 1. start
# 2. create var. N, factorial, i
# 3. give value one to factorial and i: factorial = 1, i = 1
# 4. get value for N
# 5. repeat process below untill i = N+1:
#       factorial = factoiral * i
#       i = i + 1
# 6. return value factorial
# 7. stop


def faktorial(N):
    i=1
    fakt=1
    while i!=N+1:
        fakt = fakt*i
        i += 1
    return fakt