package main

import "fmt"

func t(s []int, target int) int {
	start := 0
	end := len(s) - 1
	for start < end {
		mid := (start + end) / 2
		if s[mid] == target {
			return mid
		}
		if s[start] < s[mid] {
			if s[start] <= target && target < s[mid] {
				end = mid - 1
			} else {
				start = mid + 1
			}
		} else if s[mid] < s[end] {
			if s[mid] < target && target <= s[end] {
				start = mid + 1
			} else {
				end = mid - 1
			}
		}
	}

	return -1
}

func main() {
	s := []int{4, 5, 6, 7, 8, 9, 0, 1, 2, 3}
	rst := t(s, 9)
	fmt.Printf("%d should be 9\n", s[rst])
	fmt.Println("vim-go")
}
