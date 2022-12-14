def sq(n):
    for i in range(n):
        for j in range(n):
            if n==i*i+j*j:
                return True
    return False
    
a=int(input())
c=sq(a)
print(c)