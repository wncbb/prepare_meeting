package main

import "fmt"

func combinationSum(candidates []int, target int) [][]int {
	res := make([][]int, 0)

	for k, v := range candidates {
		if target-v > 0 {
			tmp := combinationSum(candidates[k:], target-v)
			for _, vv := range tmp {
				res = append(res, append(vv, v))
			}
		} else if target-v == 0 {
			res = append(res, []int{v})
		}
	}
	return res
}

func main() {
	a := []int{2, 3, 5}
	target := 8
	res := combinationSum(a, target)
	for _, v := range res {
		fmt.Printf("res: %+v\n", v)
	}
}
