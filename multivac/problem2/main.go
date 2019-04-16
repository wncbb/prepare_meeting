package main

import (
	"errors"
	"fmt"
)

const INT_MAX = int(^uint(0) >> 1)

var dirs = [][]int{
	[]int{-2, 1},
	[]int{-1, 2},
	[]int{1, 2},
	[]int{2, 1},
}

func getMinInt(a int, s ...int) int {
	res := a
	for _, v := range s {
		if v < res {
			res = v
		}
	}
	return res
}

func minCost(path [][]int) (int, error) {
	if len(path) == 0 {
		return 0, errors.New("length of path should not be 0")
	}

	n := len(path[0])

	res := INT_MAX

	for i := 0; i < n; i = i + 1 {
		curRst := minCostCore(path, 0, i, 0)
		fmt.Printf("line38 curRst: %d\n", curRst)
		res = getMinInt(res, curRst)
	}

	return res, nil
}

func minCostCore(path [][]int, startRow int, startCol int, curCost int) int {
	fmt.Printf("startRow:%d, startCol:%d, curCost:%d\n", startRow, startCol, curCost)
	m := len(path)
	n := len(path[0])
	if startRow >= m || startCol >= n || startRow < 0 || startCol < 0 {
		return INT_MAX
	}
	curCost += path[startRow][startCol]
	fmt.Printf("line52 curCost: %d\n", curCost)
	if startRow == m-1 {
		fmt.Printf("line54 %d\n", curCost)
		return curCost
	}

	res := INT_MAX

	for _, dir := range dirs {
		dCol := dir[0]
		dRow := dir[1]
		nextCol := startCol + dCol
		nextRow := startRow + dRow
		res = getMinInt(res, minCostCore(path, nextRow, nextCol, curCost))
	}

	return res
}

func main() {
	path := [][]int{
		[]int{3, 0, -2, 4, 0},
		[]int{-1, 2, -2, 1, 4},
		[]int{3, 1, -2, -3, 3},
		[]int{2, -4, -3, -3, 2},
		[]int{5, 2, -2, -3, 1},
	}
	res, _ := minCost(path)
	fmt.Printf("res: %+v\n", res)
}
