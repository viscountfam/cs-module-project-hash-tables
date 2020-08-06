"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
def sumdiff(q):

    # create a table where each elements f(x) is held
    fxtable = [f(x) for x in q]
    
    # find a way to calculate the sum of f(a) + f(b) for every element and store them in a dictionary
    # for key, value in fxtable.items():
   

    


    # find a way to calculate the sum of f(c) - f(d) for every element and them in a dictionary

    # return the keys where the two dictionaries hold the same value 
    return sumtab

print(sumdiff(q))