package main

import "fmt"

/**
 * @param matrix: a matrix of 0 and 1
 * @return: an integer
 */
func getMax(a int, s ...int) int {
	max := a
	for _, v := range s {
		if max < v {
			max = v
		}
	}
	return max
}
func getMin(a int, s ...int) int {
	min := a
	for _, v := range s {
		if min > v {
			min = v
		}
	}
	return min
}
func maxSquare(matrix [][]int) int {
	if len(matrix) == 0 {
		return 0
	}
	// write your code here
	dp := make([][]int, len(matrix)+1)
	for i := 0; i < len(matrix); i = i + 1 {
		dp[i] = make([]int, len(matrix[0]))
	}

	ret := 0

	for i := 0; i < len(matrix); i = i + 1 {
		for j := 0; j < len(matrix[0]); j = j + 1 {
			if i == 0 || j == 0 {
				dp[i][j] = matrix[i][j]
			} else if matrix[i][j] == 1 {
				dp[i][j] = getMin(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
			}
			ret = getMax(ret, dp[i][j])

		}
	}

	for _, v := range dp {
		fmt.Printf("dp: %+v\n", v)
	}

	return ret * ret
}

func main() {
	matrix := [][]int{
		[]int{1, 0, 1, 0, 0},
		[]int{1, 0, 1, 1, 1},
		[]int{1, 1, 1, 1, 1},
		[]int{1, 0, 0, 1, 0},
	}
	rst := maxSquare(matrix)
	fmt.Printf("rst: %+v\n", rst)

	fmt.Println("vim-go")
}
