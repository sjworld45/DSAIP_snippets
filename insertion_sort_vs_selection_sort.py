from selection_sort import sel_sort
from insertion_sort import insert_sort
from time import time
import random

def time_sort(func, num, shuffle = False):
    data = list(range(num))
    if shuffle:
        random.shuffle(data)
    else:
        while True:
            i = random.choice(range(num))
            j = random.choice(range(num))
            if i!=j:
                break
        data[i], data[j] = data[j], data[i]
    start = time()
    func(data)
    end = time()
    return end-start

array_size = 10**5
print(f'Array Size: {array_size}')
print('Time Comparision on partially sorted arrays')
print('Insertion Sort', time_sort(insert_sort, array_size))
print('Selection sort',time_sort(sel_sort, array_size))

print('Time Comparision on completely unsorted arrays')
print('Insertion Sort', time_sort(insert_sort, array_size, True))
print('Selection sort',time_sort(sel_sort, array_size, True))
        
