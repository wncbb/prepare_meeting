package main

func getMin(a int, s ...int) int {
	for _, v := range s {
		if v < a {
			a = v
		}
	}
	return a
}

func getMax(a int, s ...int) int {
	for _, v := range s {
		if v > a {
			a = v
		}
	}
	return a
}

func trap(height []int) int {
	if len(height) <= 2 {
		return 0
	}

	leftMost := make([]int, len(height), len(height))
	rightMost := make([]int, len(height), len(height))

	leftMost[0] = height[0]
	rightMost[len(height)-1] = height[len(height)-1]

	for i := 1; i < len(height); i++ {
		leftMost[i] = getMax(leftMost[i-1], height[i])
	}
	for i := len(height) - 2; i >= 0; i-- {
		rightMost[i] = getMax(rightMost[i+1], height[i])
	}

	// fmt.Printf("leftMost: %+v\n", leftMost)
	// fmt.Printf("rightMost: %+v\n", rightMost)

	res := 0
	for i := 0; i < len(height); i++ {
		res += getMin(leftMost[i], rightMost[i]) - height[i]
		// fmt.Printf("leftMost:%d, rightMost:%d, height:%d\n", leftMost[i], rightMost[i], height[i])
	}

	return res
}

func main() {
	println(trap([]int{0, 1, 0, 2}))
}
