package main

import "fmt"

/**
 * @param heights: a list of integers
 * @return: a integer
 */

func getMaxInt(a int, s ...int) int {
	max := a
	for _, v := range s {
		if max < v {
			max = v
		}
	}
	return max
}

func getMinInt(a int, s ...int) int {
	min := a
	for _, v := range s {
		if min > v {
			min = v
		}
	}
	return min
}

func trapRainWater(heights []int) int {
	// write your code here
	if len(heights) <= 2 {
		return 0
	}
	left := make([]int, len(heights))
	right := make([]int, len(heights))
	left[0] = 0
	for i := 1; i < len(heights); i = i + 1 {
		left[i] = getMaxInt(left[i-1], heights[i-1])
	}
	right[len(heights)-1] = 0
	for i := len(heights) - 2; i >= 0; i = i - 1 {
		fmt.Printf("right[i+1]:%d, heights[i+1]:%d\n", right[i+1], heights[i+1])
		right[i] = getMaxInt(right[i+1], heights[i+1])
	}

	fmt.Printf("left:%#v\n", left)
	fmt.Printf("right:%#v\n", right)

	ret := 0
	for i := 0; i < len(heights); i = i + 1 {
		border := getMinInt(left[i], right[i])
		curWater := border - heights[i]
		if curWater > 0 {
			ret += curWater
		}
	}
	return ret
}

func main() {
	t := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	ret := trapRainWater(t)
	println(ret)

	fmt.Println("vim-go")
}
