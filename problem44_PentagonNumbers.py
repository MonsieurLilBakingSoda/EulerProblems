# Euler Problem 44:
# Pentagonal numbers are generated by the formula P_n=n(3n-1)/2. The first ten
# pentagonal numbers are:
#   1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# It can be seen that P_4+P_7=22+70=92=P_8. However, their difference,
# 70-22=48, is not pentagonal.
# Find the pair of pentagonal numbers, P_j and P_k, for which their sum and
# difference are pentagonal and D=|P_k-P_j| is minimized; what is the value of
# D?

# Solution:
#----------------------------------------------------------

# One non-analytic way to solve this is to generate a reasonable number of the
# first n pentagonal numbers, say n=100, calculate their sums and differences
# (all combinations is
# 100+99+98+...+1=\sum_{i=1}^ni=n(n+1)/2=100(101)/2\approx 5000, which is fine
# to compute twice), then check those for "pentagonality". Once we find the one
# with smallest D for n<=100 we'll need to ensure that this is indeed the
# smalled D for all P_i and P_j. This is not to hard as we can follow the above
# algorithm with a revised upper bound of where the difference between
# consecutive pentagonal numbers >= D, ie P_i+1-P_i>=D. This is simply saying
# that once you go far enough out in the series, the pentagonal numbers will
# become farther and farther apart, eventually enough so that it would not be
# possible to even have consecutive pentagonal numbers have their D less than
# the one found in the first part of the algorithm. Note that if n=100 does not
# work orginally it will have to be increased. It would be a good idea to make
# that functional/ input dependant.

# So I found the answer (according to project Euler checking it). The first
# pentagon numbers that satisfy these criteria  would require a list of around
# the first 2500 pentagon numbers to weave through the combinations. The D ends
# up being 5482660. That the distance between the 2500 and 2499 pentagonal
# numbers (last two in the list generated with that "guessed" upper bound) is
# only 7498. The difference between the 10000th and 9999th pentagonal numbers
# is only 29998 and takes about 43 second to run. My point is this, even though
# the distance between pentagonal numbers grows with n^2, it takes entirely too
# long to generate the combinations of all of those numbers until the distance
# between consecutive pent numbers is > 5482660 (still need 2 more orders of
# magnitude). The majority of the lag comes in the form of numerous very long
# list look ups. We are lucky that the answer is the first pair that satisfies
# the properties
#
# I'm yet to see an analytical solution, I'm also yet to see someone address
# this new upper bound problem rigerously like I tried to do. However I did see
# a nice boolean hashtable lookup for all the pentagonal numbers up to n. This
# would work very nicely for my solution in a formal rigerous manner as we
# could find the first pair, then generate the hashmap with ~5mil elements,
# then prove that it's the smallest D (idk if it's the only D, perhaps it is).


import time as T
import sys as S

def generateNPentagonalNums(n):
    lst=[0]*n
    for ind in range(1,n+1):
        lst[ind-1]=ind*(3*ind-1)/2
    return lst

# We'll need this function to check if the sums and differences are pentagonal
def isPentagonal(num):
    # Using a bit of arithmetic and completing the square we find that a number
    # p is pentagonal if \sqrt{(2/3)*p+(1/36)}+1/6 comes out to be a natural
    # number. Note that Wikipedia uses if (\sqrt{24x+1}+1)/6=n where n is a
    # natural number. I believe this is the same equation just simplified a bit
    # differently... we will see!... It is, factor out 1/36 in the square root
    # then simplify to get this simpler formula. We will use this formula
    # instead since it deals with more whole numbers (don't have to worry as
    # much about error propagation... we are going to define a tolerance for
    # what mod 1 means... might not want that 2/3 approximation propagating too
    # much!)
    x=(((24.0*num+1)**.5+1)/6)
    if (((24.0*num+1)**.5+1)/6)%1<.00001:
        return True
    else:
        return False

def main(n):
    st=T.time()
    lst=generateNPentagonalNums(n)
    D=S.maxint
    for i in range(0,n):
        for j in range(i+1,n):
            fst=lst[i]
            snd=lst[j]
            if isPentagonal(fst+snd) and isPentagonal(snd-fst) and snd-fst<D:
                D=snd-fst
    tt=T.time()-st
    if D<S.maxint:
        print "The smallest distance D between pentagonal numbers P_i and P_j found where P_i+P_j and P_j-P_i are also both pentagonal numbers is:", D
        print "This program took", tt, "seconds to run"
        print lst[-1],lst[n-2], lst[n-1]-lst[n-2]
    else:
        print "Try a larger first n pentagonal numbers to check combos"



if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]))

