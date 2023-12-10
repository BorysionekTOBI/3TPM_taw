'''
pętle i list comprehension
'''

#lista1 = [2,4,6,8]
#print(lista1[1:3])


#for i in lista1:
 #   print(i)
    

#for i in range(1,len(lista1)-1,1):
#    print(f"{i} - {lista1[i]}")



lista=[]
n=int(input("Podaj ile ma być elementów: "))
for i in range(n):
    lista.append(int(input(f"Podaj kolejny element {i+1}: ")))

print(lista)