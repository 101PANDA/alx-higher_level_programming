#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    global listed_dic
    listed_dic = list(a_dictionary.items())
    dic_len = len(listed_dic)

    listed_dic.sort()
    for x in range(0, dic_len):
        print("{}: {}".format(listed_dic[x][0], listed_dic[x][1]))
