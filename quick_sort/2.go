package main

import (
	"fmt"
)

func qs(s []int, l, r, k int) {
	if l < r {
		m := partition(s, l, r)
		if m == k {
			return
		} else if m < k {
			qs(s, m+1, r, m-k)
			return
		} else if m > k {
			qs(s, l, m-1, k)
			return
		}
	}
	return
}

func partition(s []int, l, r int) int {
	pivot := s[r]
	i := l - 1
	for j := l; j < r; j = j + 1 {
		if s[j] <= pivot {
			i = i + 1
			s[i], s[j] = s[j], s[i]
		}
	}
	i = i + 1
	s[i], s[r] = s[r], s[i]
	return i
}

func main() {
	s := []int{1, 3, 0, 6, 4, 8, 7, 5, 9, 2}
	qs(s, 0, len(s)-1, 5)
	fmt.Printf("s:%#v\n", s)
}
