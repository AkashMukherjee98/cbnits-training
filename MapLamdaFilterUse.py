'''
squares = list(map(lambda n: n ** 2, range(1, 15, 3))) #1 4 5 7 13 from 1 to 10 i=i+3
print("Squares of no from 1 to 10 gapping of 2digits",squares)
num=squares
res=list(filter(lambda x: x%2==0, num))
print("Filter Ans: ",res)

'''
company=['Cbnits','TCS','BT','Infosys']

#Map takes all objects in a list and allows you to apply a function to it
#Map allows true and false both
#Filters takes all objects in a list and runs that through a function to create 
#a new list with all objects that returns true in that function. 
 
def placement(company):
    return company == 'Infosys'
offer=list(map(placement,company))
offer2=list(filter(placement,company))
print("Map: ",offer)
print("Filter: ",offer2)