# By aniketmondal1210, contest: Codeforces Beta Round 47, problem: (A) Domino piling, Accepted, #, Copy
x,y = map(int,input().split())
print((x*y)//2)

'''
→Judgement Protocol
Test: #1, time: 92 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 4
Output
4
Answer
4
Checker Log
ok 1 number(s): "4"
Test: #2, time: 154 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3 3
Output
4
Answer
4
Checker Log
ok 1 number(s): "4"
Test: #3, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 5
Output
2
Answer
2
Checker Log
ok 1 number(s): "2"
Test: #4, time: 124 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 6
Output
3
Answer
3
Checker Log
ok 1 number(s): "3"
Test: #5, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 15
Output
7
Answer
7
Checker Log
ok 1 number(s): "7"
Test: #6, time: 92 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 16
Output
8
Answer
8
Checker Log
ok 1 number(s): "8"
Test: #7, time: 124 ms., memory: 12 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 5
Output
5
Answer
5
Checker Log
ok 1 number(s): "5"
Test: #8, time: 92 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 6
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #9, time: 122 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 7
Output
7
Answer
7
Checker Log
ok 1 number(s): "7"
Test: #10, time: 124 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 14
Output
14
Answer
14
Checker Log
ok 1 number(s): "14"
Test: #11, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 15
Output
15
Answer
15
Checker Log
ok 1 number(s): "15"
Test: #12, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 4
Output
2
Answer
2
Checker Log
ok 1 number(s): "2"
Test: #13, time: 124 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 16
Output
16
Answer
16
Checker Log
ok 1 number(s): "16"
Test: #14, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3 5
Output
7
Answer
7
Checker Log
ok 1 number(s): "7"
Test: #15, time: 122 ms., memory: 12 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3 6
Output
9
Answer
9
Checker Log
ok 1 number(s): "9"
Test: #16, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3 10
Output
15
Answer
15
Checker Log
ok 1 number(s): "15"
Test: #17, time: 124 ms., memory: 16 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3 14
Output
21
Answer
21
Checker Log
ok 1 number(s): "21"
Test: #18, time: 60 ms., memory: 16 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3 15
Output
22
Answer
22
Checker Log
ok 1 number(s): "22"
Test: #19, time: 62 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3 16
Output
24
Answer
24
Checker Log
ok 1 number(s): "24"
Test: #20, time: 124 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
5 7
Output
17
Answer
17
Checker Log
ok 1 number(s): "17"
Test: #21, time: 30 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
16 16
Output
128
Answer
128
Checker Log
ok 1 number(s): "128"
Test: #22, time: 92 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
15 16
Output
120
Answer
120
Checker Log
ok 1 number(s): "120"
Test: #23, time: 124 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 3
Output
3
Answer
3
Checker Log
ok 1 number(s): "3"
Test: #24, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
15 15
Output
112
Answer
112
Checker Log
ok 1 number(s): "112"
Test: #25, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
14 16
Output
112
Answer
112
Checker Log
ok 1 number(s): "112"
Test: #26, time: 122 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
11 13
Output
71
Answer
71
Checker Log
ok 1 number(s): "71"
Test: #27, time: 124 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
5 16
Output
40
Answer
40
Checker Log
ok 1 number(s): "40"
Test: #28, time: 124 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
8 15
Output
60
Answer
60
Checker Log
ok 1 number(s): "60"
Test: #29, time: 154 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 2
Output
2
Answer
2
Checker Log
ok 1 number(s): "2"
Test: #30, time: 60 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3 4
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #31, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
4 4
Output
8
Answer
8
Checker Log
ok 1 number(s): "8"
Test: #32, time: 124 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 1
Output
0
Answer
0
Checker Log
ok 1 number(s): "0"
Test: #33, time: 60 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 2
Output
1
Answer
1
Checker Log
ok 1 number(s): "1"
Test: #34, time: 122 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 3
Output
1
Answer
1
Checker Log
ok 1 number(s): "1"
Test: #35, time: 62 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
14 15
Output
105
Answer
105
Checker Log
ok 1 number(s): "105"
'''
