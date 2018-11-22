
'''
问题描述
　　给定n个整数，请统计出每个整数出现的次数，按出现次数从多到少的顺序输出。
输入格式
　　输入的第一行包含一个整数n，表示给定数字的个数。
　　第二行包含n个整数，相邻的整数之间用一个空格分隔，表示所给定的整数。
输出格式
　　输出多行，每行包含两个整数，分别表示一个给定的整数和它出现的次数。按出现次数递减的顺序输出。如果两个整数出现的次数一样多，则先输出值较小的，然后输出值较大的。
样例输入
12
5 2 3 3 1 3 4 2 5 2 3 5
样例输出
3 4
2 3
5 3
1 1
4 1
评测用例规模与约定
　　1 ≤ n ≤ 1000，给出的数都是不超过1000的非负整数。
'''

n = int(input())
numbers = input().split()

setNum = list(set(numbers))
# 存结果
result = {}
# 计算出现次数
for i in setNum:
    result[i] = numbers.count(i)
# 进行两次排序，第一次按键排序，第二次按值排序并逆序
for i in sorted(sorted(result.items(), key=lambda x:int(x[0])) , key=lambda x:x[1], reverse=True):
    print(i[0] + ' ' + str(i[1]))