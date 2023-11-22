

def MyFunction(x):
    Divisor=list()
    Row=1
    while Row!=x+1 :
        if x%Row==0:
            Divisor.append(Row)
        Row +=1
    print(Divisor)
    return Divisor

def  prime_number(x):
    N=2
    while N!=x+1 :
        if x%N==0 and x!=N and x!=1:
            Answer="false" #aval nist
            break
        elif x==N or x==1:
            Answer="True" # aval ast
        N +=1
    print(Answer)
    return Answer   

n=0
Divisor_Dectionery=dict()
while n!=3 :
   x=int(input())
   Divisor_Dectionery[x]=MyFunction(x)
   n +=1
print(Divisor_Dectionery)


for Row in Divisor_Dectionery:
    List=Divisor_Dectionery[Row]
    for Row in List :
        if Row!=1 and prime_number(Row)=="false" :
            List.remove(Row)

        
print(List)


#

#sorted_Mydictionary =dict(sorted(Mydictionary.items(), key=lambda x: (x[1],x[0]) , reverse=True))

   
