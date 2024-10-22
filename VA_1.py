"""
Solutions to module VA 1
Student: 
Mail:
"""
import sys
import time
from turtledemo.penrose import start

sys.setrecursionlimit(100000)
def exchange(a, coins, memo) -> int:
    """ Count possible way to exchange a with the coins in coins. Use memoization"""
    if memo is None:
       memo = {}
    if a == 0:
       return 1
    if a < 0 or len(coins) == 0:
       return 0
    if (a, len(coins)) in memo:
       return memo[(a,len(coins))]

    result = exchange(a, coins[1:], memo) + exchange(a - coins[0], coins, memo)

    memo[(a,len(coins))] = result
    return result





def zippa(l1: list, l2: list) -> list: 
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    if not l1:
        return l2[:]
    if not l2:
        return l1[:]
    return [l1[0],l2[0]] + zippa(l1[1:],l2[1:])





def main():
    print('\nCode that demonstates my implementations\n')
    coins = [1, 5, 10, 50, 100]
    test_values = [1000,2000,10000]
    for a in test_values:
        memo = {}
        start_time = time.perf_counter()
        ways = exchange(a, coins, memo)
        end_time = time.perf_counter()
        print(f"number of ways to exchange {a} Euros:{exchange(a, coins, memo)}")
        print(f"time taken for a = {a} : {end_time-start_time:.4f} seconds")

    l1 = ['a','b','c']
    l2 = [1, 2, 3, 4]
    print(f"zipped list:{zippa(l1, l2)}")

if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 1

What time did it take to calculate large sums such as 1000 and 2000? 
time taken for a = 1000 : 0.0030 seconds
time taken for a = 2000 : 0.0049 seconds
What happens if you try to calculate e.g. 10000?
time taken for a = 10000 : 0.0266 seconds 
the time taken for large sums like 10000 was significantly longer.
"""
