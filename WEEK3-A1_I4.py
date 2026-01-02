import numpy as np
list = [23,25,30,1]
list1 = [10,18,30,23]
npl1= np.array(list)
npl2= np.array(list1)
print("elements in list1 : ",npl1)
print("elements in list2 : ",npl2)
print("addition of two lists(without using numpy) : ",list+list1)
print("addition of two arrays(using numpy) : ",npl1+npl2)
print("multiplication of two arrays (using numpy)", npl1*npl2)
print("average of elements array1: ",np.mean(npl1))
print("average of elements array2: ",np.mean(npl2))
print("STD of elements array1: ",np.mean(npl1))
print("STD of elements array2: ",np.mean(npl2))