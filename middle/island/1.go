package main

import (
	"toddtool"
)

func t(grid [][]int) int {
	d := make([][]int, len(grid))
	for k, _ := range d {
		d[k] = make([]int, len(grid[0]))
	}

	for i := 0; i < len(grid); i = i + 1 {
		for j := 0; j < len(grid[0]); j = j + 1 {
			if i == 0 || j == 0 {
				d[i][j] = grid[i][j]
			} else if grid[i][j] == 1 {
				d[i][j] = 1 + toddtool.GetMinInt(grid[i-1][j-1], grid[i][j-1], grid[i-1][j])
			}
		}
	}
	return d[len(d)-1][len(d[0])-1]
}

func main() {
	grid := [][]int{
		[]int{0, 1},
		[]int{0, 1},
	}
	println(t(grid))
}
