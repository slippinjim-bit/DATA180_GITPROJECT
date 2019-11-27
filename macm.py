# macm.py

from itertools import permutations

# Returns the product of all the integers from begin to end, i.e.
# begin * (begin + 1) * (begin + 2) * ... * end
def product(begin, end):
    assert begin <= end
    return reduce(lambda x, y: x*y, xrange(begin, end+1))

# Returns the number of permutations of size r chosen from n distinct objects.
def P(n, r):
    assert 0 <= r <= n
    return 1 if r == 0 else product(n-r+1, n)

def P_test():
    assert P(0, 0) == 1
    assert P(1, 0) == 1
    assert P(1, 1) == 1
    assert P(2, 0) == 1
    assert P(2, 1) == 2
    assert P(2, 2) == 2
    assert P(3, 0) == 1
    assert P(3, 1) == 3
    assert P(3, 2) == 6
    assert P(3, 3) == 6
    print 'All P(n,r) tests passed!'

# Returns n!, i.e. 1*2*3*...*n. Note that 0!=1.
def factorial(n):
    assert n >= 0
    return P(n, n)

# shorter name for factorial
def fact(n): return factorial(n)

def factorial_test():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 1 * 2
    assert factorial(3) == 1 * 2 * 3
    assert factorial(4) == 1 * 2 * 3 * 4
    assert factorial(5) == 1 * 2 * 3 * 4 * 5
    print 'All factorial tests passed!'

# prints all n! permutations of the numbers 1 to n
# make sure n is not too big!!
def print_perms(n):
    assert n > 0
    if n > 10:
        print 'print_perms only works for 1 <= n <= 10'
        return
    items = [a for a in xrange(1, n+1)]
    for i,p in enumerate(permutations(items)):
        print '%s  %s' % (p, i+1)

# Returns the number of ways r things can be chosen from n objects, where the
# order of the r things doesn't matter.
def C(n, r):
    assert 0 <= r <= n
    return P(n, r) / factorial(r)

def C_test():
    assert C(0, 0) == 1
    assert C(1, 0) == 1
    assert C(1, 1) == 1

    assert C(2, 0) == 1
    assert C(2, 1) == 2
    assert C(2, 2) == 1

    assert C(3, 0) == 1
    assert C(3, 1) == 3
    assert C(3, 2) == 3
    assert C(3, 3) == 1

    print 'All C(n,r) tests passed!'

if __name__ == '__main__':
    P_test()
    factorial_test()
    C_test()
