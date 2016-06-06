#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '
image_list_path="/Users/foresummer/git/show_query_result/app/static/imagelist.txt"
image_folder_path="/static/"

def just_for_fun(query):
    result = []
    result += ['woman']
    f=open(image_list_path, 'r')
    list=[]
    for line in f:
        img=line[0:-1]
        list.append(img)
    for i in range(10):
    	result += [image_folder_path + list[i]]
    return result
