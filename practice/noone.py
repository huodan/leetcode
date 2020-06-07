# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name：     noone
Description :
Author :       danhuo
date：          2020/6/7
-------------------------------------------------
Change Activity:
2020/6/7: ...
-------------------------------------------------
"""

H = 100
N = 10
h_list = [95,96,97,98,99,101,102,103,104,105]
expect = [99,101,98,102,97,103,96,105,95,105]

# first = input("请输入H N")
# second = input("请输入N个height 以空格分割")
#
# H,N = first.split(" ")
# h_list = second.split(" ")
# h_list = [int(i) for i in h_list]
# H = int(H)
# N = int(N)
# print(H)
# print(N)
# print(h_list)



from operator import attrgetter

class Student:
        def __init__(self, height, height_diff_abs):
                self.height = height
                self.height_diff_abs = height_diff_abs
        def __repr__(self):
                return repr((self.height, self.height_diff_abs))


h_diff_abs_list = [abs(H - h) for h in h_list]
# print(h_list)
# print(h_diff_abs_list)
student_objects = [Student(h_list[i], h_diff_abs_list[i]) for i in range(len(h_list))]
sorted_res =  sorted(student_objects, key=attrgetter('height_diff_abs', 'height'))   # 两级排序
ret = [str(item.height) for item in sorted_res]
print(ret)

print(" ".join(ret))


