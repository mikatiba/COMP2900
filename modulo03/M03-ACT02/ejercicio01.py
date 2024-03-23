import timeit

#enfoque 1
def search_for(number, numbers):
    for i in range(len(numbers)):
        if numbers [i] == number:
            return i
    return -1

 #enfoque 2
def search_index(number, numbers):
     try:
         return numbers.index(number) 
     except ValueError:
         return -1


numbers = list(range(1, 1001))

time_for = timeit.timeit(lambda: search_for(1000,numbers), number=10000)

print(f"Enfoque 1: {time_for}")


numbers = list(range(1, 1001))

time_genexp = timeit.timeit(lambda: search_index(1000,numbers), number=10000)

print(f"Enfoque 2: {time_index}")

