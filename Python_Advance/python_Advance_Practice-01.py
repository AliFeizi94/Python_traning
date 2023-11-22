

def MyFunction(x):
    Divisor=list()
    Row=1
    while Row!=x+1 :
        if x%Row==0:
            Divisor.append(Row)
        Row +=1
    print(Divisor)
    return Divisor

n=0
Divisor_Dectionery=dict()
while n!=3 :
   x=int(input())
   Divisor_Dectionery[x]=MyFunction(x)
   n +=1

print(Divisor_Dectionery)


#sorted_Mydictionary =dict(sorted(Mydictionary.items(), key=lambda x: (x[1],x[0]) , reverse=True))



   
