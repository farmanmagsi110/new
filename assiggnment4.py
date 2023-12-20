# def add_remove_duplicates(input_list):
#     result_list=[]

#     for item in input_list:
#         if item not in result_list:
#             result_list.append(item)
    
#     return result_list

# my_list={1,2,3,4,5,3,5,2}
# final_list = add_remove_duplicates(my_list)
# print(final_list)

matrix1 = [

    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [

    [9,8,7],
    [6,5,4],
    [3,2,1]
]

result_matrix = [[0,0,0] for _ in range(len(matrix1))]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

for row in result_matrix:
    print(row)