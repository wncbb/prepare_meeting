package main

func main() {
	a := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	t := 2
	println(middleSearch(a, 0, len(a)-1, t))
}

func middleSearch(s []int, l, r, t int) int {
	if l <= r {
		m := (l + r) / 2
		if s[m] == t {
			return m
		} else if t < s[m] {
			return middleSearch(s, l, m-1, t)
		} else {
			return middleSearch(s, m+1, r, t)
		}
	}
	return -1
}
