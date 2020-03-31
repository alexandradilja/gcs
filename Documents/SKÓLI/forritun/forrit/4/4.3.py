#chessboard squares 8*8=64
grain = 0
for i in range(64):
    grain += 2**i
print(grain)