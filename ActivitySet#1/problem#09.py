# Lists

filename = "dataset/romeo.txt"

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    g=line.split()
    for i in g:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)