# By aniketmondal1210, contest: Codeforces Round 971 (Div. 4), problem: (A) Minimize!, Accepted, #, Copy
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    print(abs(a-b))

'''
→Judgement Protocol
Test: #1, time: 46 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3
1 2
3 10
5 5
Output
1
7
0
Answer
1
7
0
Checker Log
ok 3 number(s): "1 7 0"
Test: #2, time: 61 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
55
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
2 2
2 3
2 4
2 5
2 6
2 7
2 8
2 9
2 10
3 3
3 4
3 5
3 6
3 7
3 8
3 9
3 10
4 4
4 5
4 6
4 7
4 8
4 9
4 10
5 5
5 6
5 7
5 8
5 9
5 10
6 6
6 7
6 8
6 9
6 10
7 7
7 8
7 9
7 10
8 8
8 9
8 10
9 9
9 10
10 10
Output
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
0
1
2
3
4
5
6
7
0
1
2
3
4
5
6
0
1
2
3
4
5
0
1
2
3
4
0
1
2
3
0
1
2
0
1
0
Answer
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
0
1
2
3
4
5
6
7
0
1
2
3
4
5
6
0
1
2
3
4
5
0
1
2
3
4
0
1
2
3
0
1
2
0
1
0
Checker Log
ok 55 numbers
'''
