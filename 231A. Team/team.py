# By aniketmondal1210, contest: Codeforces Round 143 (Div. 2), problem: (A) Team, Accepted, #, Copy
t = int(input())
d = 0
for i in range(t):
    a, b, c = map(int, input().split())
    if (a+b+c) >= 2:
        d += 1
print(d)

'''
→Judgement Protocol
Test: #1, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
3
1 1 0
1 1 1
1 0 0
Output
2
Answer
2
Checker Log
ok answer is 2
Test: #2, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
1 0 0
0 1 1
Output
1
Answer
1
Checker Log
ok answer is 1
Test: #3, time: 186 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
1 0 0
Output
0
Answer
0
Checker Log
ok answer is 0
Test: #4, time: 124 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
1 0 0
1 1 1
Output
1
Answer
1
Checker Log
ok answer is 1
Test: #5, time: 154 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
5
1 0 0
0 1 0
1 1 1
0 0 1
0 0 0
Output
1
Answer
1
Checker Log
ok answer is 1
Test: #6, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
10
0 1 0
0 1 0
1 1 0
1 0 0
0 0 1
0 1 1
1 1 1
1 1 0
0 0 0
0 0 0
Output
4
Answer
4
Checker Log
ok answer is 4
Test: #7, time: 92 ms., memory: 12 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
15
0 1 0
1 0 0
1 1 0
1 1 1
0 1 0
0 0 1
1 0 1
1 0 1
1 0 1
0 0 0
1 1 1
1 1 0
0 1 1
1 1 0
1 1 1
Output
10
Answer
10
Checker Log
ok answer is 10
Test: #8, time: 92 ms., memory: 24 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
50
0 0 0
0 1 1
1 1 1
0 1 0
1 0 1
1 1 1
0 0 1
1 0 0
1 1 0
1 0 1
0 1 0
0 0 1
1 1 0
0 1 0
1 1 0
0 0 0
1 1 1
1 0 1
0 0 1
1 1 0
1 1 1
0 1 1
1 1 0
0 0 0
0 0 0
1 1 1
0 0 0
1 1 1
0 1 1
0 0 1
0 0 0
0 0 0
1 1 0
1 1 0
1 0 1
1 0 0
1 0 1
1 0 1
0 1 1
1 1 0
1 1 0
0 1 0
1 0 1
0 0 0
0 0 0
0 0 0
0 0 1
1 1 1
0 1 1
1 0 1
Output
29
Answer
29
Checker Log
ok answer is 29
Test: #9, time: 124 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
100
1 0 0
0 1 0
1 0 1
0 0 0
1 1 1
1 0 0
0 0 1
0 1 0
1 0 0
1 0 0
0 1 0
1 1 0
1 0 1
1 0 0
0 1 0
0 1 1
0 1 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
1 1 0
0 0 0
0 0 1
0 0 1
0 1 0
0 1 1
1 1 0
1 1 0
1 0 0
1 0 1
1 1 0
1 0 1
1 1 0
0 1 0
1 1 1
0 1 0
0 1 1
0 0 1
1 0 0
0 0 0
0 0 1
0 0 1
0 0 0
1 1 0
0 1 1
0 0 1
0 1 0
1 0 1
1 0 0
1 0 0
0 0 0
1 0 1
0 1 0
1 1 0
0 1 1
1 0 0
1 1 0
0 1 0
1 0 0
0 1 1
0 1 1
0 0 0
1 0 0
0 0 1
0 1 1
1 1 0
0 1 1
0 0 1
1 1 0
1 0 0
1 ...
Output
44
Answer
44
Checker Log
ok answer is 44
Test: #10, time: 92 ms., memory: 8 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
200
1 1 1
1 1 1
0 0 0
1 1 0
0 0 1
1 0 0
0 1 1
0 0 0
1 0 1
1 0 1
0 1 0
0 0 0
0 1 1
1 1 0
1 0 0
1 1 0
1 0 1
1 0 0
1 0 0
0 1 0
1 0 0
0 1 0
1 1 0
0 0 0
0 0 1
1 1 0
1 0 0
0 1 0
0 1 0
0 0 0
0 0 0
0 1 1
1 1 1
1 1 0
1 1 1
1 1 1
0 0 1
1 0 1
0 1 1
0 1 1
1 1 0
0 1 0
1 1 1
0 1 0
0 1 1
1 0 0
0 0 0
1 0 0
1 1 0
1 0 0
1 1 1
0 0 1
0 1 0
1 0 1
0 0 1
0 1 1
0 0 1
1 0 0
1 0 0
1 0 1
0 1 1
0 1 0
1 0 1
1 1 1
0 0 1
0 0 0
0 0 1
0 1 1
1 0 1
1 1 1
0 0 0
0 0 1
1 ...
Output
103
Answer
103
Checker Log
ok answer is 103
Test: #11, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
300
1 0 1
0 0 1
1 1 0
1 0 1
0 0 0
0 0 0
0 0 0
1 0 1
0 0 0
1 0 0
0 1 0
1 0 1
0 1 1
0 0 1
1 1 1
1 0 0
0 0 0
0 1 0
1 0 0
1 0 1
0 1 0
1 0 1
0 1 0
1 0 0
0 0 1
1 0 0
1 1 1
0 1 1
1 0 0
1 0 1
1 1 1
0 0 0
1 1 0
1 0 0
1 1 0
0 0 1
0 1 0
0 0 0
1 0 1
1 0 0
0 0 1
1 0 1
1 1 0
0 0 0
1 1 0
1 1 1
0 1 0
0 1 1
0 0 1
0 1 1
1 0 1
1 1 1
0 0 1
1 0 1
1 0 1
0 1 0
1 1 0
0 0 0
1 1 1
1 0 0
0 1 0
1 0 1
0 0 1
1 1 1
0 1 1
1 0 1
0 1 0
0 1 0
0 0 1
1 0 0
1 0 1
0 0 0
1 ...
Output
153
Answer
153
Checker Log
ok answer is 153
Test: #12, time: 122 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
400
0 0 1
1 0 0
0 1 1
0 0 0
0 0 1
0 0 0
0 1 0
1 1 0
1 1 0
1 0 1
1 0 0
0 1 0
1 1 1
0 1 1
0 1 1
0 1 1
1 1 0
1 1 0
1 0 0
1 1 1
1 1 0
0 0 0
0 1 0
1 0 0
0 0 1
0 0 0
0 1 1
0 1 0
0 0 0
0 1 0
0 1 1
1 0 0
0 0 0
0 0 0
1 1 1
1 0 0
1 1 1
1 1 0
0 0 1
1 1 0
1 0 1
1 1 1
0 1 1
1 1 1
1 0 0
1 0 1
0 0 1
1 1 0
0 1 1
1 1 0
0 1 0
1 0 0
0 1 1
1 0 1
0 1 1
1 0 1
1 0 0
0 0 0
0 1 1
1 0 1
1 1 1
1 0 0
0 1 0
1 1 1
1 0 0
1 0 0
0 0 0
1 0 1
1 1 0
1 1 0
0 1 0
1 1 0
1 ...
Output
202
Answer
202
Checker Log
ok answer is 202
Test: #13, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
500
0 1 0
0 1 1
0 0 0
1 1 0
1 0 0
0 0 0
0 0 1
1 0 0
0 1 1
1 0 0
1 0 0
0 0 0
0 0 0
1 1 1
0 0 1
1 1 0
0 1 1
0 0 1
0 1 0
1 0 0
0 0 1
0 1 0
1 0 0
0 1 0
1 0 1
0 1 1
0 0 1
0 1 1
1 1 1
0 0 0
0 1 1
1 1 0
0 0 1
0 1 1
1 1 0
1 0 1
1 0 1
1 0 1
0 0 1
0 1 1
0 1 1
0 1 0
1 0 0
1 0 1
1 1 1
1 1 0
0 1 1
0 0 0
1 1 1
0 0 0
0 0 0
0 0 1
0 0 0
1 0 1
1 1 1
1 0 0
0 0 0
1 1 1
0 0 1
0 0 0
1 1 0
0 0 1
1 0 0
0 1 1
0 0 1
0 1 1
1 0 1
1 0 0
0 1 0
0 1 1
1 1 1
1 1 1
1 ...
Output
248
Answer
248
Checker Log
ok answer is 248
Test: #14, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
600
0 0 0
0 1 0
1 1 0
0 1 1
1 0 1
1 1 1
0 1 1
1 1 1
1 0 0
0 0 1
1 0 0
1 0 1
0 0 0
1 0 0
1 1 0
0 0 0
1 0 0
1 0 1
0 1 0
1 1 0
0 0 1
1 0 1
1 0 0
0 1 0
1 0 1
1 0 1
1 1 0
0 1 0
0 1 1
1 0 1
1 0 1
1 0 1
0 0 0
1 0 1
1 1 1
0 1 0
0 1 0
0 0 0
1 1 0
0 0 0
0 0 0
0 0 1
0 0 1
0 0 1
1 0 1
0 0 0
0 0 0
1 0 1
0 0 0
1 0 1
0 1 1
1 1 1
1 1 0
1 0 1
0 0 0
0 0 1
0 1 1
1 1 1
0 1 0
0 0 1
0 0 0
0 0 0
0 0 0
0 1 1
0 1 1
0 1 0
1 1 0
0 0 1
1 0 0
0 0 0
0 0 1
1 1 0
0 ...
Output
279
Answer
279
Checker Log
ok answer is 279
Test: #15, time: 154 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
700
0 1 1
1 1 1
0 1 1
1 0 0
0 1 0
1 1 1
0 0 0
0 0 1
0 0 1
0 0 0
1 0 0
0 1 0
1 0 0
0 1 0
1 0 0
0 1 1
0 0 1
0 1 1
1 1 0
0 1 1
1 0 1
0 0 0
1 0 0
1 1 0
1 0 1
0 0 1
1 0 0
1 1 1
1 0 1
0 1 0
0 0 1
0 1 1
0 0 1
1 1 0
1 1 0
1 1 1
0 0 0
1 1 0
0 1 0
0 1 0
1 0 0
1 1 1
1 1 1
0 1 0
1 1 0
0 1 1
0 1 0
0 1 0
0 1 0
0 1 0
0 0 1
1 0 0
1 0 1
1 0 1
1 0 0
0 0 0
1 0 1
0 1 1
0 0 0
0 0 0
1 0 1
1 1 0
1 1 1
1 0 1
1 0 0
0 1 1
1 0 0
1 1 1
0 0 0
1 1 0
0 1 0
0 1 1
0 ...
Output
352
Answer
352
Checker Log
ok answer is 352
Test: #16, time: 122 ms., memory: 16 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
800
0 0 1
0 0 1
1 0 0
1 1 0
0 1 1
1 1 1
0 1 0
0 1 0
1 1 1
0 0 1
1 0 0
1 1 1
1 0 0
0 0 1
0 0 0
1 1 0
1 1 1
1 1 1
1 1 0
0 0 0
0 1 1
0 1 0
0 0 0
1 1 0
1 0 1
0 1 0
0 0 0
1 1 0
1 0 1
1 1 1
1 1 0
0 0 0
0 0 0
1 0 0
1 1 1
0 0 1
1 0 1
0 1 1
0 1 0
1 0 1
0 1 0
1 0 0
1 1 0
0 0 0
0 0 0
0 0 1
0 0 1
1 1 1
1 1 0
1 1 1
0 1 0
0 0 1
1 1 1
1 0 1
1 1 0
1 1 0
1 1 0
0 1 1
0 1 1
1 1 0
1 0 0
1 1 1
0 1 1
1 0 1
1 1 0
1 1 0
1 1 1
1 1 0
1 1 1
1 0 1
1 1 1
0 1 0
0 ...
Output
383
Answer
383
Checker Log
ok answer is 383
Test: #17, time: 154 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
900
0 1 0
1 0 0
0 0 1
0 1 1
0 1 0
0 1 1
0 0 1
0 0 0
1 1 0
0 0 0
1 0 0
0 0 1
0 1 0
1 0 1
0 1 1
0 0 0
1 1 0
0 0 0
1 1 0
0 1 0
1 1 1
1 0 1
0 0 0
0 0 1
1 0 1
1 0 0
0 1 1
1 1 1
0 0 1
0 0 1
0 1 0
1 0 0
0 0 1
0 0 0
1 1 0
1 0 0
1 1 0
1 0 0
1 0 0
1 1 1
1 1 0
0 0 1
0 1 1
1 1 1
0 1 1
0 1 0
0 1 1
0 0 1
0 0 1
0 0 1
0 0 0
0 1 1
1 0 0
1 0 1
0 0 1
0 1 1
0 1 0
1 0 1
0 0 1
1 1 1
0 1 1
1 1 0
1 0 1
1 0 1
0 1 1
1 1 1
1 0 1
0 1 1
0 1 1
1 1 1
0 0 1
1 0 1
0 ...
Output
473
Answer
473
Checker Log
ok answer is 473
Test: #18, time: 122 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1000
0 1 0
0 1 0
0 1 1
1 1 1
0 1 0
1 1 1
0 0 0
0 0 1
1 1 1
0 0 0
1 1 0
1 1 1
0 1 1
0 0 1
0 0 0
0 0 0
0 1 0
0 1 0
1 0 0
0 0 0
1 0 1
1 1 0
1 0 0
1 0 0
1 0 1
1 1 0
1 1 1
1 1 1
0 0 0
0 0 0
0 1 0
1 0 0
1 1 1
1 0 0
1 0 1
1 1 1
0 1 1
1 1 1
0 0 1
1 0 1
0 1 0
0 1 1
1 0 1
1 1 1
1 0 0
1 0 1
0 0 0
1 1 0
1 0 1
1 0 0
1 1 1
1 0 0
1 0 0
0 1 1
0 1 1
1 0 1
0 1 0
1 0 1
1 1 0
1 1 0
0 1 1
0 1 1
0 1 1
0 1 0
0 0 0
0 0 0
0 1 0
0 1 0
1 0 0
1 1 0
0 1 0
1 0 1
0...
Output
491
Answer
491
Checker Log
ok answer is 491
Test: #19, time: 122 ms., memory: 16 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
1 1 1
Output
1
Answer
1
Checker Log
ok answer is 1
Test: #20, time: 92 ms., memory: 12 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
8
0 0 0
0 0 1
0 0 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
Output
4
Answer
4
Checker Log
ok answer is 4
Test: #21, time: 154 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
16
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
Output
16
Answer
16
Checker Log
ok answer is 16
'''
