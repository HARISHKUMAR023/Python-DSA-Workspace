s = "abcabcbb"
char_index = {}
max_len = 0
sa = 0

for e in range(len(s)):
    if s[e] in char_index and char_index[s[e]] >= sa:
        sa = char_index[s[e]] + 1
    char_index[s[e]] = e
    max_len = max(max_len, e - sa + 1)

print(max_len)
