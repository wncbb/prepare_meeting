package main

import "fmt"

type AllSortMaker struct {
	res [][]int
}

func NewAllSortMaker() *AllSortMaker {
	return &AllSortMaker{
		res: make([][]int, 0),
	}
}

func (a *AllSortMaker) work(s []int, start, end int) {
	if start >= end {
		tmp := make([]int, len(s))
		copy(tmp, s)
		a.res = append(a.res, tmp)
	} else {
		for i := start; i < end; i = i + 1 {
			s[i], s[start] = s[start], s[i]
			a.work(s, start+1, end)
		}
	}
}

func main() {
	a := NewAllSortMaker()
	s := []int{0, 1, 2, 3}
	a.work(s, 0, len(s))
	for _, v := range a.res {
		fmt.Printf("v: %#v\n", v)
	}
	fmt.Printf("len(a.res): %d\n", len(a.res))
	fmt.Println("vim-go")
}
