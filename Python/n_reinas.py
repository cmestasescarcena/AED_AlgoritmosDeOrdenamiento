def free(row, col):
        for i in range(10):
            if tablero[row][i] == 'R' or tablero[i][col] == 'R':
                return False

        if row <= col:
            c = col - row
            r = 0
        else:
            r = row - col
            c = 0
        while c < 10 and r < 10:
            if tablero[r][c] == 'R':
                return False
            r += 1
            c += 1

        if row <= col:
            r = 0
            c = col + row
            if c > 9:
                r = c - 9
                c = 7
        else:
            c = 9
            r = row - (9 - col)

        while c >= 0 and r < 10:
            if tablero[r][c] == 'R':
                return False
            r += 1
            c -= 1

        return True

def agregar_reina(n):
    
        if n < 1:
            return True

        for idx_row in range(10):
            for idx_col in range(10):
                if free(idx_row, idx_col):
                    tablero[idx_row][idx_col] = 'R'
                    if agregar_reina(n-1):
                        return True
                    else:
                        tablero[idx_row][idx_col] = '_'
        return False
tablero = []
for i in range(10):
    tablero.append(['_'] * 10)
agregar_reina(10)
for row in tablero:
    print(*row)