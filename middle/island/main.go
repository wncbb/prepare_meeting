package main

import "fmt"

func maxAreaOfIsland(grid [][]int) int {
	ret := 0

	for i := 0; i < len(grid); i = i + 1 {
		for j := 0; j < len(grid[0]); j = j + 1 {
			tmpRst := help(i, j, grid)
			if tmpRst > ret {
				ret = tmpRst
			}
		}
	}
	return ret
}

func help(x, y int, grid [][]int) int {
	// fmt.Printf("x:%d, y:%d\n", x, y)
	if x < 0 || x >= len(grid) {
		return 0
	}
	if y < 0 || y >= len(grid[0]) {
		return 0
	}
	if grid[x][y] == 0 {
		return 0
	}

	ret := 1

	directions := [][]int{
		[]int{0, 1},
		[]int{0, -1},
		[]int{1, 0},
		[]int{-1, 0},
	}

	grid[x][y] = 0
	for _, v := range directions {
		nx := x + v[0]
		ny := y + v[1]
		ret += help(nx, ny, grid)
	}
	return ret
}

func main() {
	/*
		grid := [][]int{
			[]int{1, 0, 1},
			[]int{1, 0, 1},
			[]int{1, 1, 1},
		}
	*/
	/*
			[[0,0,1,0,0,0,0,1,0,0,0,0,0],
		 [0,0,0,0,0,0,0,1,1,1,0,0,0],
		 [0,1,1,0,1,0,0,0,0,0,0,0,0],
		 [0,1,0,0,1,1,0,0,1,0,1,0,0],
		 [0,1,0,0,1,1,0,0,1,1,1,0,0],
		 [0,0,0,0,0,0,0,0,0,0,1,0,0],
		 [0,0,0,0,0,0,0,1,1,1,0,0,0],
		 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
	*/

	grid := [][]int{
		[]int{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
		[]int{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		[]int{0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
		[]int{0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
		[]int{0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
		[]int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
		[]int{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		[]int{0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0},
	}

	println(maxAreaOfIsland(grid))
	fmt.Println("vim-go")
}
