def sel_sort(t):
    for i in range(len(t)):
        min_index = i
        for j in range(i, len(t)):
            if t[min_index] > t[j]:
                min_index = j
        t[i], t[min_index] = t[min_index], t[i]
        
