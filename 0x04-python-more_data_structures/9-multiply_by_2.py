#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = {}
    listed_dic = list(a_dictionary.items())
    dic_len = len(listed_dic)

    for x in range(0, dic_len):
        new_dic[listed_dic[x][0]] = (listed_dic[x][1] * 2)

    return new_dic
