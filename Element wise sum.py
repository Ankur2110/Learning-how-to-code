# Elementwise Sum

# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

# Example

#     tuple1 = (1, 2, 3)
#     tuple2 = (4, 5, 6)
#     output_tuple = tuple_elementwise_sum(tuple1, tuple2)
#     print(output_tuple)  # Expected output: (5, 7, 9)


def tuple_elementwise_sum(tuple1, tuple2):
    result_list = []
    for i in range(len(tuple1)):
        variable = 0
        variable = tuple1[i]+tuple2[i]
        result_list.append(variable)
    result_tuple = tuple(result_list)
    return result_tuple