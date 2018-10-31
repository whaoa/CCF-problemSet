
'''
问题描述
　　涛涛最近要负责图书馆的管理工作，需要记录下每天读者的到访情况。每位读者有一个编号，每条记录用读者的编号来表示。给出读者的来访记录，请问每一条记录中的读者是第几次出现。
输入格式
　　输入的第一行包含一个整数n，表示涛涛的记录条数。
　　第二行包含n个整数，依次表示涛涛的记录中每位读者的编号。
输出格式
　　输出一行，包含n个整数，由空格分隔，依次表示每条记录中的读者编号是第几次出现。
样例输入
5
1 2 1 1 3
样例输出
1 1 2 3 1
评测用例规模与约定
　　1≤n≤1,000，读者的编号为不超过n的正整数。
'''

n = int(input())
pid = [int(x) for x in input().split()]
pidInfo = list(set(pid))
dic = {}
result = []
for i in range(len(pidInfo)):
    dic[pidInfo[i]] = pid.count(pidInfo[i])
for i in range(n-1, -1 , -1):
    result.append(dic[pid[i]])
    dic[pid[i]] -= 1
result.reverse()
for i in range(n):
    print(result[i], end=' ')