package main

/**
 * @param board: the given board
 * @return:  the least number of moves required so that the state of the board is solved
 */

import (
	"fmt"
	"strings"
)

func slidingPuzzle(board [][]int) int {
	// write your code here
	if len(board) == 0 || len(board[0]) == 0 {
		return -1
	}
	row := len(board)
	col := len(board[0])

	goal := "123450"
	start := ""

	// 按行整成字符串，好记录状态，以及是否到达过当前状态
	for i := 0; i < row; i = i + 1 {
		for j := 0; j < col; j = j + 1 {
			start += string(board[i][j] + '0')
		}
	}
	if start == goal {
		return 0
	}

	dirs := getDirections()
	fmt.Printf("dirs: %+v\n", dirs)
	// 记录已经到达过的状态（节点）
	visited := map[string]struct{}{
		start: struct{}{},
	}

	steps := 0
	// BFS 层级遍历，需要一个FIFO队列
	q := make([]string, 0)
	q = append(q, start)

	for len(q) != 0 {
		steps += 1
		size := len(q)
		for size > 0 {
			s := q[0]
			q = q[1:]
			p := strings.Index(s, "0")
			x := p % col
			y := p / col
			// 0跟相邻的四个方向上的数字交换
			for _, v := range dirs {
				tx := x + v[0]
				ty := y + v[1]
				if tx < 0 ||
					ty < 0 ||
					tx >= col ||
					ty >= row {
					continue
				}
				pp := ty*col + tx
				fmt.Printf("tx:%d, ty:%d, pp:%d\n", tx, ty, pp)
				t := exchangeString(s, p, pp)
				// 到达过的状态不需要了
				if _, ok := visited[t]; ok {
					continue
				}
				if t == goal {
					return steps
				}
				visited[t] = struct{}{}
				q = append(q, t)
				fmt.Printf("q:%#v\n", q)
			}
			size = size - 1
		}
	}
	return -1

}

func exchangeString(s string, p, pp int) string {
	s1 := s
	a1 := []byte(s1)
	a1[p], a1[pp] = a1[pp], a1[p]
	return string(a1)
}

func getDirections() [][]int {
	return [][]int{
		[]int{1, 0},
		[]int{-1, 0},
		[]int{0, 1},
		[]int{0, -1},
	}
}

func main() {
	board := [][]int{
		[]int{1, 2, 3},
		[]int{4, 0, 5},
	}
	ret := slidingPuzzle(board)

	fmt.Printf("ret: %d\n", ret)
}
