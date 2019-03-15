package main

import (
	"fmt"
	"toddtool"
)

/**
 * @param A: An array of non-negative integers
 * @return: The maximum amount of money you can rob tonight
 */
func houseRobber(A []int) int64 {
	if len(A) == 0 {
		return 0
	}
	if len(A) == 1 {
		return int64(A[0])
	}
	rst := make([]int, len(A), len(A))
	rst[0] = A[0]
	rst[1] = toddtool.GetMaxInt(A[0], A[1])
	for i := 2; i < len(A); i = i + 1 {
		rst[i] = toddtool.GetMaxInt(A[i]+rst[i-2], rst[i-1])
	}
	return int64(rst[len(A)-1])
}

func main() {
	s := []int{5, 2, 1, 3}
	rst := houseRobber(s)
	fmt.Printf("rst:%d\n", rst)
	fmt.Println("vim-go")
}
