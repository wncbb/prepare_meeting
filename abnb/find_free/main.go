package main

import (
	"fmt"
	"sort"
	"toddtool"
)

type UserWork struct {
	Start int
	End   int
}

type UserWorks []*UserWork

func (u UserWorks) Len() int {
	return len(u)
}

func (u UserWorks) Swap(a, b int) {
	u[a], u[b] = u[b], u[a]
}

func (u UserWorks) Less(a, b int) bool {
	return u[a].Start < u[b].Start
}

func findFree(data [][]int) [][]int {
	u := make([]*UserWork, 0, len(data))

	for _, v := range data {
		u = append(u, &UserWork{
			Start: v[0],
			End:   v[1],
		})
	}
	sort.Sort(UserWorks(u))

	cur := u[0].End
	rst := make([][]int, 0)
	for _, v := range u {
		if v.Start <= cur {
			cur = toddtool.GetMaxInt(v.End, cur)
		} else {
			rst = append(rst, []int{cur, v.Start})
			cur = v.End
		}
	}

	return rst
}

func main() {
	data := [][]int{
		[]int{10, 20},
		[]int{15, 18},
		[]int{30, 40},
		[]int{50, 60},
		[]int{44, 55},
	}

	rst := findFree(data)
	for _, v := range rst {
		fmt.Printf("%#v\n", v)
	}
}
