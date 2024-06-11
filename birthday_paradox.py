import math
n=int(input("Enter Number of Persons in the Room ? "))
x=int(input("How Many Has To Have Same Birthday ? "))
l=str(input("If Leap Year give L else N   " ))

def comb(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
def probability(n,s,a):
    product = 1
    if a > n:
        return 0.0  
    ways_to_choose_a = comb(n, a)
    prob_a_share = (1 / s) ** (a - 1)
    product = 1
    for i in range(n - a):
        product *= (s - 1 - i) / s
        total_prob = ways_to_choose_a * prob_a_share * product * (1 / s)
    return total_prob


if l=="N":
    p=probability(n,365,x)
    print("The Probability of ",x," people having same birthday in a Room of ",n," people is ", p)
else:
    p=probability(n,366,x)
    print("The Probability of ",x," people having same birthday in a Room of ",n," people is ", p)

