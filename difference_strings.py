s=input()
t=input()
result = 0
for ch in s:
    result ^= ord(ch)
for ch in t:
    result ^= ord(ch)
print(chr(result))