filename = r'C:\Users\Saksham\Desktop\comp_sci\dsaip\try.txt'
f = open(filename, 'r', encoding = ('UTF8'))
for i in f.readlines():
    print(float(i))