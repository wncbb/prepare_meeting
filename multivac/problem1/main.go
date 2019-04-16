package main

import "fmt"

func getIntersectionNums(a, b []int) []int {
	if len(a) == 0 || len(b) == 0 {
		return []int{}
	}

	res := make([]int, 0)
	idxA := 0
	idxB := 0
	for idxA < len(a) && idxB < len(b) {
		if a[idxA] == b[idxB] {
			res = append(res, a[idxA])
			idxA += 1
			idxB += 1
		} else if a[idxA] < b[idxB] {
			idxA += 1
		} else {
			idxB += 1
		}
	}

	return res
}

func main() {
	a := []int{1, 3, 5, 11}
	b := []int{2, 3, 5, 11, 12}
	res := getIntersectionNums(a, b)
	fmt.Printf("res: %#v\n", res)
}
