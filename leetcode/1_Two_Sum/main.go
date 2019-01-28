package main

import "fmt"

func qs(s []int, l, r int) {
	if l < r {
		m := partition(s, l, r)
		qs(s, l, m-1)
		qs(s, m+1, r)
	}
}

func partition(s []int, l, r int) int {
	i := l - 1
	pivot := s[r]
	j := l
	for ; j < r; j++ {
		if s[j] <= pivot {
			i = i + 1
			s[i], s[j] = s[j], s[i]
		}
	}

	i = i + 1
	s[i], s[r] = s[r], s[i]
	return i
}

func twoSum(nums []int, target int) []int {
	qs(nums, 0, len(nums)-1)
	l := 0
	r := len(nums) - 1
	for l < r {
		curSum := nums[l] + nums[r]
		if curSum == target {
			return []int{nums[l], nums[r]}
		} else if curSum > target {
			r--
		} else {
			l++
		}
	}
	return []int{}
}

func main() {
	a := []int{1, 8, 9, 3, 5, 7, 4, 6, 0, 2}
	res := twoSum(a, 12)
	fmt.Printf("res:%+v\n", res)
}
