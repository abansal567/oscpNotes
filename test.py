nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count=0

if nterms == 1:
    print(n1)
else:
    while count < nterms:
        nth = n1 + n2
        print(n1)
        n1 = n2
        n2 = nth
        count +=1



