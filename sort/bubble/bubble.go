package main

func bubble(s []int) {
	for i := 0; i < len(s)-1; i++ {
		for j := 0; j < len(s)-i-1; j++ {
			if s[j] > s[j+1] {
				s[j], s[j+1] = s[j+1], s[j]
			}
		}
	}
}

func main() {
	a := []int{1, 9, 0, 3, 2, 6, 8, 7, 4, 5}
	bubble(a)
	for _, v := range a {
		println(v)
	}
}
