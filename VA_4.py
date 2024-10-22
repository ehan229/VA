"""
Solutions to module VA 4

Student:
Mail:
"""

#!/usr/bin/env python3

from person import Person
import time
import matplotlib.pyplot as plt
"""
Write a script that gives a plot for comparison of two approaches for Fibonacci numbers
"""
"""python"""
def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)
"""numba"""
from numba import jit
@jit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)

def fib_cpp(person,n):
	return person.fib(n)

def plot_fib_performance():
	ns = list(range(20,46))
	times_py=[]
	times_numba=[]
	times_cpp=[]

	person_instance = Person(50)
	for n in ns:
		time_py, time_numba, time_cpp = test_fib_performance(n, person_instance)
		times_py.append(time_py)
		times_numba.append(time_numba)
		times_cpp.append(time_cpp)

	plt.plot(ns, times_py, label = "Python")
	plt.plot(ns, times_numba, label = "Numba")
	plt.plot(ns, times_cpp, label = "C++(Person)")
	plt.xlabel("n(Fibonacci number")
	plt.ylabel("Time(seconds)")
	plt.title("Fibonacci Performance: Python vs Numba vs C++")
	plt.legend()
	plt.savefig(f"fibonacci_performance.png")
	plt.clf()



def test_fib_performance(n, person, print_result = True):

	start = time.perf_counter()
	result_numba = fib_numba(n)
	end = time.perf_counter()
	time_numba = end - start
	print(f"result for fib_numba({n}) = {result_numba}, time taken {time_numba:.6f} seconds")

	start = time.perf_counter()
	result_cpp = fib_cpp(person, n)
	end = time.perf_counter()
	time_cpp = end - start
	print(f"result for fib_cpp({n}) = {result_cpp}, time taken {time_cpp:.6f} seconds")

	start = time.perf_counter()
	result_py = fib_py(n)
	end = time.perf_counter()
	time_py = end - start
	print(f"result for fib_py({n}) = {result_py}, time taken {time_py:.6f} seconds")



	return time_py, time_numba, time_cpp


def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())

	n = 47
	print("fib_47")
	test_fib_performance(n,f)

	print("performance plot")
	plot_fib_performance()

if __name__ == '__main__':
	main()


"""What is the result for Fibonacci with n=47? Why?
result for fib_numba(47) = 2971215073, time taken 18.911338 seconds
result for fib_cpp(47) = 2971215073, time taken 24.428465 seconds
result for fib_py(47) = 2971215073, time taken 377.064834 seconds
The result of Fibonacci 47 is 2971215073, 
C++ Python, and Numba all give the same correct result.
However, due to Numba’s JIT optimization, 
the execution time is much faster than the other two, 
while C++ offers substantial improvements over pure Python for its compiled nature
and Python performs poorly for larger n.

"""