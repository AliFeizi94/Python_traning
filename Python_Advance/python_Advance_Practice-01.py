

##################  Fanction for Identifying and listing the  divisors of the input number ############
def MyFunction(x):
    Divisor=list()
    Row=1
    while Row!=x+1 :
        if x%Row==0:
            Divisor.append(Row)
        Row +=1
    #print(Divisor)
    return Divisor
##########################################################################################################




#################  Fanction for Identifying and listing the prime divisors of the input number ###########
def  prime_number(x):
    N=2
    while N!=x+1 :
        if x%N==0 and x!=N and x!=1:
            Answer="false" #aval nist
            break
        elif x==N or x==1:
            Answer="True" # aval ast
        N +=1
    #print(x," Aval " , Answer)
    return Answer   
##########################################################################################################




################## input numbers ########################################################################
n=0
Divisor_Dectionery=dict()
while n!=10 :

   x=int(input())
   Divisor_Dectionery[x]=MyFunction(x)
   n +=1
#print(Divisor_Dectionery)
#########################################################################################################





################### loop for add only prime divisors in to divisors list of input numbers ###############
for Row in Divisor_Dectionery:
    List=Divisor_Dectionery[Row]
    #Primer_one_List=list()
    for Row in List :
        if Row==1 :
            Primer_one_List=list()
        elif prime_number(Row)=="True" :
            Primer_one_List.append(Row)
        #print(Primer_one_List)
    Divisor_Dectionery[Row]=Primer_one_List
    #print(Divisor_Dectionery)
#print(Divisor_Dectionery)
#########################################################################################################





#################### loop for counter of prime divisors of input numbers ################################
for key in Divisor_Dectionery:
    Divisor_Dectionery[key]=len(Divisor_Dectionery[key])
########################################################################################################





######### loop for Sort the dictionery of input numbers and prime divisors of input number an print it ##
sorted_Mydictionary =dict(sorted(Divisor_Dectionery.items(), key=lambda x: (x[1],x[0]) , reverse=True))
for key in sorted_Mydictionary :
    print(key ,sorted_Mydictionary[key])
    break
##########################################################################################################
   
