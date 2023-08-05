package main

func is_safe(board [][]bool, row, col, N int) bool {

	for i := 0; i < row; i++ {
		if board[i][col] {
			return false
		}
	}

	for i, j := row-1, col-1; i >= 0 && j >= 0; i, j = i-1, j-1 {
		if board[i][j] {
			return false
		}
	}

	for i, j := row-1, col+1; i >= 0 && j < N; i, j = i-1, j+1 {
		if board[i][j] {
			return false
		}
	}

	return true
}

func SolveN_queens(board [][]bool, row, N int, outputs *[][]int) {
	if row == N {

		var output []int
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if board[i][j] {
					output = append(output, j+1)
					break
				}
			}
		}
		*outputs = append(*outputs, output)
		return
	}

	for col := 0; col < N; col++ {
		if is_safe(board, row, col, N) {

			board[row][col] = true

			SolveN_queens(board, row+1, N, outputs)

			board[row][col] = false
		}
	}
}
