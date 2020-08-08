#! /usr/bin/ python
#coding=utf-8

def yield_test():
    print('this is a yield  test!!!')
    yield 56
    print('hello world !!!')
    yield 5
    print('this is end')
    yield 'h'

def main():

    result = yield_test()
    
    next(yield_test())
    next(yield_test())
    next(result)
    next(result)

def bubble_sort(ori_list):
    sorted_list = ori_list
    for i in range(len(ori_list)):
        for j in range(i, len(ori_list)):
            if sorted_list[i] > sorted_list[j]:
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[j]
                sorted_list[j] = temp
    return sorted_list

if __name__ == "__main__":
    # print('before run !!!')
    # main()
    ori_list = [4, 3, 1, 6, 9, 10]
    sort_list = bubble_sort(ori_list)
    # for i in range(len(ori_list)):
    #     ori_list[i] = 1
    print('ori_list:', ori_list)
    print(sort_list)