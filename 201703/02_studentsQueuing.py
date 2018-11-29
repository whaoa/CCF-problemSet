
'''
问题描述
　　体育老师小明要将自己班上的学生按顺序排队。他首先让学生按学号从小到大的顺序排成一排，学号小的排在前面，然后进行多次调整。一次调整小明可能让一位同学出队，向前或者向后移动一段距离后再插入队列。
　　例如，下面给出了一组移动的例子，例子中学生的人数为8人。
　　0）初始队列中学生的学号依次为1, 2, 3, 4, 5, 6, 7, 8；
　　1）第一次调整，命令为“3号同学向后移动2”，表示3号同学出队，向后移动2名同学的距离，再插入到队列中，新队列中学生的学号依次为1, 2, 4, 5, 3, 6, 7, 8；
　　2）第二次调整，命令为“8号同学向前移动3”，表示8号同学出队，向前移动3名同学的距离，再插入到队列中，新队列中学生的学号依次为1, 2, 4, 5, 8, 3, 6, 7；
　　3）第三次调整，命令为“3号同学向前移动2”，表示3号同学出队，向前移动2名同学的距离，再插入到队列中，新队列中学生的学号依次为1, 2, 4, 3, 5, 8, 6, 7。
　　小明记录了所有调整的过程，请问，最终从前向后所有学生的学号依次是多少？
　　请特别注意，上述移动过程中所涉及的号码指的是学号，而不是在队伍中的位置。在向后移动时，移动的距离不超过对应同学后面的人数，如果向后移动的距离正好等于对应同学后面的人数则该同学会移动到队列的最后面。在向前移动时，移动的距离不超过对应同学前面的人数，如果向前移动的距离正好等于对应同学前面的人数则该同学会移动到队列的最前面。
输入格式
　　输入的第一行包含一个整数n，表示学生的数量，学生的学号由1到n编号。
　　第二行包含一个整数m，表示调整的次数。
　　接下来m行，每行两个整数p, q，如果q为正，表示学号为p的同学向后移动q，如果q为负，表示学号为p的同学向前移动-q。
输出格式
　　输出一行，包含n个整数，相邻两个整数之间由一个空格分隔，表示最终从前向后所有学生的学号。
样例输入
8
3
3 2
8 -3
3 -2
样例输出
1 2 4 3 5 8 6 7
评测用例规模与约定
　　对于所有评测用例，1 ≤ n ≤ 1000，1 ≤ m ≤ 1000，所有移动均合法。
'''

n = int(input())
m = int(input())
students = list(range(1, n+1))
move = []
for i in range(m):
    read = [int(x) for x in input().split()]
    move.append(read)

for mv in move:
    index = students.index(mv[0])
    newindex = index + mv[1]
    # 前移
    if index > newindex:
        mvlist = students[newindex:index+1]
        tmp = mvlist[index - newindex]
        mvlist.insert(0, tmp)
        mvlist.pop()
        for i in mvlist:
            students[newindex] = i
            newindex += 1
    else:
        mvlist = students[index:newindex+1]
        tmp = mvlist[0]
        mvlist.append(tmp)
        mvlist.pop(0)
        for i in mvlist:
            students[index] = i
            index += 1
students = [str(s) for s in students]
print(' '.join(students))