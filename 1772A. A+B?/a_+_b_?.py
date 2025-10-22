# By aniketmondal1210, contest: Codeforces Round 839 (Div. 3), problem: (A) A+B?, Accepted, #, Copy
t = int(input())
for i in range(t):
    a = input()
    b = eval(a)
    print(b)

'''
→Judgement Protocol
Test: #1, time: 31 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
4
4+2
0+0
3+7
8+9
Output
6
0
10
17
Answer
6
0
10
17
Checker Log
ok 4 number(s): "6 0 10 17"
Test: #2, time: 61 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
100
0+0
0+1
0+2
0+3
0+4
0+5
0+6
0+7
0+8
0+9
1+0
1+1
1+2
1+3
1+4
1+5
1+6
1+7
1+8
1+9
2+0
2+1
2+2
2+3
2+4
2+5
2+6
2+7
2+8
2+9
3+0
3+1
3+2
3+3
3+4
3+5
3+6
3+7
3+8
3+9
4+0
4+1
4+2
4+3
4+4
4+5
4+6
4+7
4+8
4+9
5+0
5+1
5+2
5+3
5+4
5+5
5+6
5+7
5+8
5+9
6+0
6+1
6+2
6+3
6+4
6+5
6+6
6+7
6+8
6+9
7+0
7+1
7+2
7+3
7+4
7+5
7+6
7+7
7+8
7+9
8+0
8+1
8+2
8+3
8+4
8+5
8+6
8+7
8+8
8+9
9+0
9+1
9+2
9+3
9+4
9+5
9+6
9+7
9+8
9+9
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
1
2
3
4
5
6
7
8
9
10
2
3
4
5
6
7
8
9
10
11
3
4
5
6
7
8
9
10
11
12
4
5
6
7
8
9
10
11
12
13
5
6
7
8
9
10
11
12
13
14
6
7
8
9
10
11
12
13
14
15
7
8
9
10
11
12
13
14
15
16
8
9
10
11
12
13
14
15
16
17
9
10
11
12
13
14
15
16
17
18
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
1
2
3
4
5
6
7
8
9
10
2
3
4
5
6
7
8
9
10
11
3
4
5
6
7
8
9
10
11
12
4
5
6
7
8
9
10
11
12
13
5
6
7
8
9
10
11
12
13
14
6
7
8
9
10
11
12
13
14
15
7
8
9
10
11
12
13
14
15
16
8
9
10
11
12
13
14
15
16
17
9
10
11
12
13
14
15
16
17
18
Checker Log
ok 100 numbers
Test: #3, time: 61 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
5+5
Output
10
Answer
10
Checker Log
ok 1 number(s): "10"
Test: #4, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
1+1
Output
2
Answer
2
Checker Log
ok 1 number(s): "2"
Test: #5, time: 46 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
2+2
Output
4
Answer
4
Checker Log
ok 1 number(s): "4"
Test: #6, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
5+6
Output
11
Answer
11
Checker Log
ok 1 number(s): "11"
Test: #7, time: 77 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
1+4
Output
5
Answer
5
Checker Log
ok 1 number(s): "5"
Test: #8, time: 61 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
0+0
Output
0
Answer
0
Checker Log
ok 1 number(s): "0"
Test: #9, time: 30 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
2+3
Output
5
Answer
5
Checker Log
ok 1 number(s): "5"
Test: #10, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
3+1
Output
4
Answer
4
Checker Log
ok 1 number(s): "4"
Test: #11, time: 61 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
1+2
Output
3
Answer
3
Checker Log
ok 1 number(s): "3"
Test: #12, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
5+7
Output
12
Answer
12
Checker Log
ok 1 number(s): "12"
Test: #13, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
3+5
Output
8
Answer
8
Checker Log
ok 1 number(s): "8"
Test: #14, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
1+1
1+1
Output
2
2
Answer
2
2
Checker Log
ok 2 number(s): "2 2"
Test: #15, time: 61 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
3+2
4+2
Output
5
6
Answer
5
6
Checker Log
ok 2 number(s): "5 6"
Test: #16, time: 61 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
1+0
Output
1
Answer
1
Checker Log
ok 1 number(s): "1"
Test: #17, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
1+1
1+2
Output
2
3
Answer
2
3
Checker Log
ok 2 number(s): "2 3"
Test: #18, time: 30 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
3+4
2+4
Output
7
6
Answer
7
6
Checker Log
ok 2 number(s): "7 6"
Test: #19, time: 46 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
2+2
2+2
Output
4
4
Answer
4
4
Checker Log
ok 2 number(s): "4 4"
Test: #20, time: 62 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
2+2
1+1
Output
4
2
Answer
4
2
Checker Log
ok 2 number(s): "4 2"
Test: #21, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
4+5
3+4
Output
9
7
Answer
9
7
Checker Log
ok 2 number(s): "9 7"
Test: #22, time: 62 ms., memory: 16 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
4+5
Output
9
Answer
9
Checker Log
ok 1 number(s): "9"
Test: #23, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
7
1+1
1+1
1+1
1+1
1+1
1+1
1+1
Output
2
2
2
2
2
2
2
Answer
2
2
2
2
2
2
2
Checker Log
ok 7 numbers
Test: #24, time: 62 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3
1+0
0+1
2+2
Output
1
1
4
Answer
1
1
4
Checker Log
ok 3 number(s): "1 1 4"
Test: #25, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
11
1+1
1+1
1+1
1+1
1+1
1+1
1+1
1+1
1+1
1+1
1+1
Output
2
2
2
2
2
2
2
2
2
2
2
Answer
2
2
2
2
2
2
2
2
2
2
2
Checker Log
ok 11 numbers
Test: #26, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
20
1+5
2+7
1+5
2+7
1+5
1+5
2+7
1+5
2+7
1+5
1+5
2+7
1+5
2+7
1+5
1+5
2+7
1+5
2+7
1+5
Output
6
9
6
9
6
6
9
6
9
6
6
9
6
9
6
6
9
6
9
6
Answer
6
9
6
9
6
6
9
6
9
6
6
9
6
9
6
6
9
6
9
6
Checker Log
ok 20 numbers
Test: #27, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
1+5
2+7
Output
6
9
Answer
6
9
Checker Log
ok 2 number(s): "6 9"
Test: #28, time: 46 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
3+2
Output
5
Answer
5
Checker Log
ok 1 number(s): "5"
Test: #29, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
4
4+2
0+0
3+7
1+1
Output
6
0
10
2
Answer
6
0
10
2
Checker Log
ok 4 number(s): "6 0 10 2"
'''
