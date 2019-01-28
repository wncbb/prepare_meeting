package main

import "fmt"

func hammingDistance(x int, y int) int {
	xorRes := x ^ y
	res := 0
	var i uint
	for i = 0; i < 64; i++ {
		if (xorRes & (1 << i)) > 0 {
			res++
		}
	}
	return res
}

func main() {
	fmt.Printf("%+v\n", hammingDistance(2, 4))
}
