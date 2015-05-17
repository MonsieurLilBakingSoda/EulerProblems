# Euler Problem 12: # The sequence of triangle numbers is generated by adding the natural numbers.# So the 7th triangle number would be 1+2+3+4+5+6+7=28. The first ten terms
# would be:
#       1,3,6,10,21,28,36,45,55,...
# Let us list the factors of the first seven triangle numbers:
#       1: 1
#       3: 1,2
#       6: 1,2,3,6
#       10: 1,2,5,10
#       15: 1,3,5,15
#       21: 1,3,7,21
#       28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five
# divisors.

# What is the value of the first triangle number to have over five hundred
# divisors?

# Initial thoughts: If we can find how the number of divisors grows with
# increasing triangle number (NOT a monotone function) we can just
# find where tri(x)=500 (or higher) and calculate that triangle number only.
# Otherwise the brute force method would be to (memoiz-ingly,
# calculate each next triangle number, then run a subfunction to find it's
# divisors.

# Better thoughts (after thinking a while and realizing that generating the
# next triangular number off of the last (even when memoized) is wayyy to
# slow to get to a number that has 500 unique factors to it:
# - The smallest number with 500 unique factors is intuitively
# (1)(2)(3)...(500) = 500! = some ridiculously large number 
# - Another fact that we may utilize is that we have a closed form
# expression to generate the nth Triangular number:
#       T(n) = (n(n+1))/2
# Furthermore we can take the inverse of this equation to check if any given
# number is Triangular:
#       T = n(n+1)/2
#       2T = n(n+1)
#       2T = n^2+n
# Complete the square:
#       2T+1/4 = n^2+n+1/4
#       2T+1/4 = (n+1/2)^2
# This isn't that neat, let's go back to the line
#       2T+1/4 = n^2+n+1/4
# Multiplying through by 4:
#       8T+1 = 4n^2+4n+1
#       8T+1 = (2n+1)^2
# Note that this provides a valid check given any integer as to whether
# it's a triangular number or not, just multiply that number by 8 and add 1
# then check if that number is a perfect square (square root is an int) and
# that the square root is odd (2n+1). Note that in the solution I
# implemented below I just check for n an integer... easier than two checks

# knowing this let's first start at math.factorial(500) and check every
# number until we find a perfect square. (I'm still wary)

import math as M

def triangleNumWithOverNFactors(n):
    index = 2
    tNum = 3
    while numDivisors(tNum) <= n:
        print "The", index, "triangle number", tNum, "has", numDivisors(tNum), "divisors"
        index += 1
        tNum += index
    answer = tNum
    print "The first triangle number with more than", n, "factors is",answer



def numDivisors(num):
    sqrt = num**.5
    divisor = 2
    counter = 1
    while divisor < sqrt:
        if num % divisor == 0:
            counter += 1
        divisor += 1
    return counter

def triangularNumWithOverNFactors2(n):
    while isTriangularNumber(number) == False:
        number += 1
    print "The first triangular number with over", n, " unique factors is", number
    return number

def isTriangularNumber(num):
    if ((8*num+1)**.5-1)/2 % 1 == 0:
        print "This is the", ((8*num+1)**.5-1)/2, "triangular number"
    return True


if __name__ == "__main__":
    import sys
    numDivisors
    triangleNumWithOverNFactors(int(sys.argv[1]))
