# Tuples

filename = "dataset/mbox-short.txt"

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hrs = dict()

for l in handle:
    l = l.strip()
    if 'From' in l:
        if 'From:' not in l:
            l = l.split()
            for w in l:
                if ':' in w:
                    w = w[:2]
                    if w in hrs:
                        hrs[w] = hrs[w] + 1
                    else :
                        hrs[w] = 1
                        
for (k,v) in sorted(hrs.items()):
    print(k,v)