package main

import (
	"fmt"
)

func add(a, b int) int {
	if a < 0 || b < 0 {
		return -1
	}
	return a + b
}

func getMin(a, b int) int {
	if a < 0 && b < 0 {
		// ERROR:
		// 显然必须是都小于0
		// if a < 0 || b < 0 {
		return -1
	}
	if a < 0 {
		return b
	}
	if b < 0 {
		return a
	}
	if a < b {
		return a
	}
	return b
}

func copyMap(a map[int]int) map[int]int {
	ret := make(map[int]int, len(a))
	for k, v := range a {
		ret[k] = v
	}
	return ret
}

func findCheapestPrice(n int, flights [][]int, src int, dst int, K int) int {
	// parent := make(map[int]int, n)
	cost := make(map[int]int, n)
	for _, v := range flights {
		cost[v[0]] = -1
		cost[v[1]] = -1
	}
	cost[src] = 0

	// 1->2->3
	for i := 0; i < K+1; i = i + 1 {
		// tmpCost := copyMap(cost)
		for _, v := range flights {
			// fmt.Printf(
			// 	"src:%d, dst:%d, w:%d, oldCost:%d, newCost:%d, newMin:%d\n",
			// 	v[0], v[1], v[2], cost[v[1]], add(cost[v[0]], v[2]),
			// 	getMin(cost[v[1]], add(cost[v[0]], v[2])),
			// )
			cost[v[1]] = getMin(cost[v[1]], add(cost[v[0]], v[2]))
			// ERROR:
			// tmpCost[v[1]] = getMin(cost[v[1]], add(cost[v[0]], v[2]))
		}
		// cost = tmpCost
		// fmt.Printf("cost: %#v\n", cost)
	}

	return cost[dst]
}

/*
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
*/

/*
3
[[0,1,100],[1,2,100],[0,2,500]]
0
2
1
*/

func main() {
	n := 3
	edges := [][]int{
		[]int{0, 1, 100},
		[]int{1, 2, 100},
		[]int{0, 2, 500},
	}
	src := 0
	dst := 2
	k := 0
	rst := findCheapestPrice(n, edges, src, dst, k)
	fmt.Printf("rst: %d\n", rst)
	fmt.Println("vim-go")

	// fmt.Printf("-1 500 : %d\n", getMin(-1, 500))
}
