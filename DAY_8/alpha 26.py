# print(l)
# l=[chr(i) for i in range(97,123)]
# s="a b c d e f g h i j k l m n o p q r s t u v w x y z"
# for i in l:
#     if i not in s:
#         print(False)
#         break
# else:
#     print(True)
# d={}
# for i in s:
#     if i not in d and i.isalpha():
#         d[i]=1
# c=0
# print(d)
# for k,v in d.items():
#     c=c+v
# if c==26:
#     print(True)
# else:
#     print(False)
# i=5
# for i in range(7):
#     print(i)
#     i=i+2
#     print(i)
#     print("hi")-
# print("-")
# print(i)
# arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
# arr2 = [2, 1, 4, 3, 9, 6]
# nr=[]
# print(all(arr1))

# s = "abcdefg"
# k = 2
# f=""
# if len(s)<k:
#     f
def generate_pascals_triangle(n: int) -> list[list[int]]:
    if n == 0:
        return []
    if n == 1:
        return [[1]]

    result = [[1]]

    for row_num in range(1, n):
        new_row = [1] * (row_num + 1)
        prev_row = result[-1]

        for i in range(1, row_num):
            new_row[i] = prev_row[i - 1] + prev_row[i]

        result.append(new_row)

    return result


# Example usage
n = int(input("Enter the number of rows: "))
print(generate_pascals_triangle(n))
