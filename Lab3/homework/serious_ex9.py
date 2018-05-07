def get_even_list(list):
    new_list = []
    for i in list:
        if (i % 2 == 0):
            new_list.append(i)
    return new_list

if __name__ == "__main__":
    list = [1,4,5,-1,10]
    newlist = get_even_list(list)
    print(newlist)
