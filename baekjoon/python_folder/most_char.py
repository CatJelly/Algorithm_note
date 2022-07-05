# https://www.acmicpc.net/problem/1371

import sys

sentence = sys.stdin.read()

count = [0] * 26

for s in sentence:
    if s.islower():
        count[ord(s) - 97] += 1

for i in range(len(count)):
    if count[i] == max(count):
        print(chr(97 + i), end='')