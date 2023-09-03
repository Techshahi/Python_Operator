x=["apple","banana"]
y=["apple","banana"]
z=x
#is operator:return true if both variables are same object,variable name are same

print(x is z) #return true because variable name are same
print(x is y) #return false because x is not same variable as y ,even if they have same content(variable name different)
print(x==y)#return true because x and y both have same content/same value

#is not operator:return true if both variables are not same object/same value

print(x is not z)#return false because x and z both are same variable but not same value
print(x is not y)#return true because x and y both are same value
print(x!=y)#return false because x and y both have different variable