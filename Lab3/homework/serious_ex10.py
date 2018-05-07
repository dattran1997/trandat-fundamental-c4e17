from serious_ex9 import get_even_list

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]): #dùng set để so sánh kí tự trong mảng giống nhau không kể trình tự
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
