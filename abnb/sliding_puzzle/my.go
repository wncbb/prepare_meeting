package main

import (
	"fmt"
	"strings"
)

func slidingPuzzle(board [][]int) int {
	// TODO: check parameters
	if len(board) == 0 || len(board[0]) == 0 {
		return -1
	}

	row := len(board)
	col := len(board[0])

	goal := "123450"
	start := ""
	for i := 0; i < row; i = i + 1 {
		for j := 0; j < col; j = j + 1 {
			start += string(board[i][j] + '0')
		}
	}

	if start == goal {
		return 0
	}

	// 记录历史状态，如果有了直接返回
	states := map[string]struct{}{
		start: struct{}{},
	}

	steps := 0
	// bfs需要一个FIFO
	q := make([]string, 0)
	q = append(q, start)

	directions := [][]int{
		[]int{0, 1},
		[]int{0, -1},
		[]int{1, 0},
		[]int{-1, 0},
	}

	for len(q) != 0 {
		size := len(q)
		// TODO: 防止变量这比
		steps = steps + 1
		// 这里Size, 是为了方便记录step数，每一层一步
		for size > 0 {
			s := q[0]
			fmt.Printf("s: %s\n", s)
			q = q[1:]
			p := strings.Index(s, "0")
			x := p % col
			y := p / col
			for _, v := range directions {
				tx := x + v[0]
				ty := y + v[1]
				fmt.Printf("nx:%d, ny:%d\n", tx, ty)
				// TODO: x,y col,row对应好
				if tx < 0 ||
					ty < 0 ||
					tx >= col ||
					ty >= row {
					continue
				}

				// TODO: y坐标乘以列
				np := ty*col + tx
				tmpS := exchangeString(s, p, np)

				// 先做转换，转换完了看转换后的状态是否已经存在
				if _, ok := states[tmpS]; ok {
					continue
				}

				if tmpS == goal {
					return steps
				}

				states[tmpS] = struct{}{}
				q = append(q, tmpS)
				fmt.Printf("q: %#v\n", q)
				fmt.Printf("tmpS: %s\n", tmpS)
				fmt.Printf("states: %#v\n", states)
				fmt.Printf("-----------\n")
			}
			size = size - 1
		}

	}

	return -1
}

func exchangeString(s string, p1, p2 int) string {
	fmt.Printf("p1:%d, p2:%d\n", p1, p2)
	s2 := s
	s2b := []byte(s2)
	s2b[p1], s2b[p2] = s2b[p2], s2b[p1]
	return string(s2b)
}

func main() {
	// [[4,1,2],[5,0,3]]
	board := [][]int{
		[]int{4, 1, 2},
		[]int{5, 0, 3},
	}
	ret := slidingPuzzle(board)

	fmt.Printf("ret: %d\n", ret)
}
