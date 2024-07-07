pattern ="aaa"
s = "aa aa aa "
def wordPattern() :
        my = {}
        p = s.split()
        c = 0
        for i, j in zip(pattern, s.split()):
            if i not in my:
                if j not in my.values():
                    my[i] = j

        for i in pattern:
            if len(pattern) != len(s.split()):
                print(len(pattern),len(s.split()))
                return  False
            if i not in my:
                return False
            if my[i] != p[c]:
                return False
            c += 1
        return True

print(wordPattern())