def maximum_subarray_sum(A, B, C):
    max_sum = 0
    current_sum = 0
    start_index = 0
    
    for end_index in range(A):
        current_sum += C[end_index]
        
        while current_sum > B:
            current_sum -= C[start_index]
            start_index += 1
        
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum

# Get input from the user
A = int(input())
B = int(input())
C = []
input_str = input("Enter the elements of array C separated by space: ")
input_list = input_str.split()
for i in range(len(input_list)):
    C.append(int(input_list[i]))

output = maximum_subarray_sum(A, B, C)
print(output)
