def Kadane_Algorithm(A):
     
    maximum_sum = 0
    current_sum = 0
     
    for i in range(len(A)):
        current_sum = current_sum + A[i]
        if current_sum < 0:
            current_sum = 0
         
        elif (maximum_sum < current_sum):
            maximum_sum = current_sum
             
    return maximum_sum

A = [1,-3,2,1,-1]
print ("Maximum sum of Subarray is", Kadane_Algorithm(A))