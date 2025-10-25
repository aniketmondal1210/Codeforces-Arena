# By aniketmondal1210, contest: VK Cup 2012 Qualification Round 1, problem: (A) Next Round, Accepted, #, Copy
a, b = map(int, input().split())
c = list(map(int, input().split()))
count = 0
for i in c:
    if i >= c[b-1] and i > 0:
        count += 1
print(count)

'''
→Judgement Protocol
Test: #1, time: 92 ms., memory: 180 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
8 5
10 9 8 7 7 7 5 5
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #2, time: 60 ms., memory: 196 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
4 2
0 0 0 0
Output
0
Answer
0
Checker Log
ok 1 number(s): "0"
Test: #3, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
5 1
1 1 1 1 1
Output
5
Answer
5
Checker Log
ok 1 number(s): "5"
Test: #4, time: 62 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
5 5
1 1 1 1 1
Output
5
Answer
5
Checker Log
ok 1 number(s): "5"
Test: #5, time: 62 ms., memory: 16 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 1
10
Output
1
Answer
1
Checker Log
ok 1 number(s): "1"
Test: #6, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
17 14
16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
Output
14
Answer
14
Checker Log
ok 1 number(s): "14"
Test: #7, time: 124 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
5 5
3 2 1 0 0
Output
3
Answer
3
Checker Log
ok 1 number(s): "3"
Test: #8, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
8 6
10 9 8 7 7 7 5 5
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #9, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
8 7
10 9 8 7 7 7 5 5
Output
8
Answer
8
Checker Log
ok 1 number(s): "8"
Test: #10, time: 124 ms., memory: 220 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
8 4
10 9 8 7 7 7 5 5
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #11, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
8 3
10 9 8 7 7 7 5 5
Output
3
Answer
3
Checker Log
ok 1 number(s): "3"
Test: #12, time: 122 ms., memory: 248 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
8 1
10 9 8 7 7 7 5 5
Output
1
Answer
1
Checker Log
ok 1 number(s): "1"
Test: #13, time: 60 ms., memory: 12 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
8 2
10 9 8 7 7 7 5 5
Output
2
Answer
2
Checker Log
ok 1 number(s): "2"
Test: #14, time: 122 ms., memory: 236 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 1
100
Output
1
Answer
1
Checker Log
ok 1 number(s): "1"
Test: #15, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1 1
0
Output
0
Answer
0
Checker Log
ok 1 number(s): "0"
Test: #16, time: 122 ms., memory: 176 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50 25
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
Output
50
Answer
50
Checker Log
ok 1 number(s): "50"
Test: #17, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50 25
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
Output
25
Answer
25
Checker Log
ok 1 number(s): "25"
Test: #18, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50 25
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
Output
26
Answer
26
Checker Log
ok 1 number(s): "26"
Test: #19, time: 92 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50 25
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
Output
50
Answer
50
Checker Log
ok 1 number(s): "50"
Test: #20, time: 62 ms., memory: 196 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
11 5
100 99 98 97 96 95 94 93 92 91 90
Output
5
Answer
5
Checker Log
ok 1 number(s): "5"
Test: #21, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 4
100 81 70 69 64 43 34 29 15 3
Output
4
Answer
4
Checker Log
ok 1 number(s): "4"
Test: #22, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
11 6
87 71 62 52 46 46 43 35 32 25 12
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #23, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
17 12
99 88 86 82 75 75 74 65 58 52 45 30 21 16 7 2 2
Output
12
Answer
12
Checker Log
ok 1 number(s): "12"
Test: #24, time: 124 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
20 3
98 98 96 89 87 82 82 80 76 74 74 68 61 60 43 32 30 22 4 2
Output
3
Answer
3
Checker Log
ok 1 number(s): "3"
Test: #25, time: 92 ms., memory: 204 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
36 12
90 87 86 85 83 80 79 78 76 70 69 69 61 61 59 58 56 48 45 44 42 41 33 31 27 25 23 21 20 19 15 14 12 7 5 5
Output
12
Answer
12
Checker Log
ok 1 number(s): "12"
Test: #26, time: 92 ms., memory: 180 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
49 8
99 98 98 96 92 92 90 89 89 86 86 85 83 80 79 76 74 69 67 67 58 56 55 51 49 47 47 46 45 41 41 40 39 34 34 33 25 23 18 15 13 13 11 9 5 4 3 3 1
Output
9
Answer
9
Checker Log
ok 1 number(s): "9"
Test: #27, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
49 29
100 98 98 96 96 96 95 87 85 84 81 76 74 70 63 63 63 62 57 57 56 54 53 52 50 47 45 41 41 39 38 31 30 28 27 26 23 22 20 15 15 11 7 6 6 4 2 1 0
Output
29
Answer
29
Checker Log
ok 1 number(s): "29"
Test: #28, time: 124 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
49 34
99 98 96 96 93 92 90 89 88 86 85 85 82 76 73 69 66 64 63 63 60 59 57 57 56 55 54 54 51 48 47 44 42 42 40 39 38 36 33 26 24 23 19 17 17 14 12 7 4
Output
34
Answer
34
Checker Log
ok 1 number(s): "34"
Test: #29, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50 44
100 100 99 97 95 91 91 84 83 83 79 71 70 69 69 62 61 60 59 59 58 58 58 55 55 54 52 48 47 45 44 44 38 36 32 31 28 28 25 25 24 24 24 22 17 15 14 13 12 4
Output
44
Answer
44
Checker Log
ok 1 number(s): "44"
Test: #30, time: 92 ms., memory: 240 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50 13
99 95 94 94 88 87 81 79 78 76 74 72 72 69 68 67 67 67 66 63 62 61 58 57 55 55 54 51 50 50 48 48 42 41 38 35 34 32 31 30 26 24 13 13 12 6 5 4 3 3
Output
13
Answer
13
Checker Log
ok 1 number(s): "13"
Test: #31, time: 122 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50 30
100 98 96 94 91 89 88 81 81 81 81 81 76 73 72 71 70 69 66 64 61 59 59 56 52 50 49 48 43 39 36 35 34 34 31 29 27 26 24 22 16 16 15 14 14 14 9 7 4 3
Output
30
Answer
30
Checker Log
ok 1 number(s): "30"
Test: #32, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 1
10 10
Output
2
Answer
2
Checker Log
ok 1 number(s): "2"
Test: #33, time: 92 ms., memory: 264 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 2
10 10
Output
2
Answer
2
Checker Log
ok 1 number(s): "2"
Test: #34, time: 92 ms., memory: 256 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 2
10 0
Output
1
Answer
1
Checker Log
ok 1 number(s): "1"
Test: #35, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 2
10 1
Output
2
Answer
2
Checker Log
ok 1 number(s): "2"
Test: #36, time: 154 ms., memory: 260 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 1
10 0
Output
1
Answer
1
Checker Log
ok 1 number(s): "1"
Test: #37, time: 154 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2 1
10 2
Output
1
Answer
1
Checker Log
ok 1 number(s): "1"
Test: #38, time: 62 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50 13
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Output
0
Answer
0
Checker Log
ok 1 number(s): "0"
Test: #39, time: 124 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Output
0
Answer
0
Checker Log
ok 1 number(s): "0"
Test: #40, time: 92 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50 50
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Output
0
Answer
0
Checker Log
ok 1 number(s): "0"
Test: #41, time: 92 ms., memory: 172 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 1
5 5 5 3 3 3 0 0 0 0
Output
3
Answer
3
Checker Log
ok 1 number(s): "3"
Test: #42, time: 124 ms., memory: 172 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 2
5 5 5 3 3 3 0 0 0 0
Output
3
Answer
3
Checker Log
ok 1 number(s): "3"
Test: #43, time: 124 ms., memory: 240 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 3
5 5 5 3 3 3 0 0 0 0
Output
3
Answer
3
Checker Log
ok 1 number(s): "3"
Test: #44, time: 62 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 4
5 5 5 3 3 3 0 0 0 0
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #45, time: 60 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 5
5 5 5 3 3 3 0 0 0 0
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #46, time: 62 ms., memory: 232 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 6
5 5 5 3 3 3 0 0 0 0
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #47, time: 122 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 7
5 5 5 3 3 3 0 0 0 0
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #48, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 8
5 5 5 3 3 3 0 0 0 0
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #49, time: 62 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 9
5 5 5 3 3 3 0 0 0 0
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
Test: #50, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10 10
5 5 5 3 3 3 0 0 0 0
Output
6
Answer
6
Checker Log
ok 1 number(s): "6"
'''
