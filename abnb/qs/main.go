package main

import "fmt"

func t(s []int, l, r int) {
	if l < r {
		m := partition(s, l, r)
		t(s, l, m-1)
		t(s, m+1, r)
	}
}

func partition(s []int, l, r int) int {
	i := l - 1
	p := s[r]
	for j := l; j < r; j = j + 1 {
		if s[j] <= p {
			i = i + 1
			s[j], s[i] = s[i], s[j]
		}
	}
	i = i + 1
	s[r], s[i] = s[i], s[r]
	return i
}

func main() {
	s := []int{0, 2, 1, 6, 9, 4, 7, 5}
	t(s, 0, len(s)-1)
	fmt.Printf("%#v\n", s)
	fmt.Println("vim-go")
}
