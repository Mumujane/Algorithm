s = "abcabcbb"
for i in range(0, len(s) - 1):
    print(i)
    for j in range(i + 1, len(s)):

        print("---%d"%j)
