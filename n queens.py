class Back:
    def nqueen(self, n: int):
        col = set()
        posDig = set()
        negDig = set()
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDig or (r - c) in negDig:
                    continue

                col.add(c)
                posDig.add(r + c)
                negDig.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDig.remove(r + c)
                negDig.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res


# Create an instance of Back and call nqueen
f = Back()
solutions = f.nqueen(4)
for solution in solutions:
    for row in solution:
        print(row)
    print()
