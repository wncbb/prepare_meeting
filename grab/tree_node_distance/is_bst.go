package main

import "fmt"

func getMaxInt(a int, s ...int) int {
	for _, v := range s {
		if v > a {
			a = v
		}
	}
	return a
}

type Node struct {
	Val     int
	Left    *Node
	Right   *Node
	Visited bool
}

func NewNode(val int) *Node {
	return &Node{
		Val: val,
	}
}

func getDepth(r *Node) int {
	if r == nil {
		return 0
	}
	return 1 + getMaxInt(getDepth(r.Left), getDepth(r.Right))
}

func isBalance(r *Node) bool {
	if r == nil {
		return true
	}
	leftDepth := getDepth(r.Left)
	rightDepth := getDepth(r.Right)
	diffDepth := leftDepth - rightDepth
	if diffDepth < 0 {
		diffDepth *= -1
	}
	return diffDepth < 2 && isBalance(r.Left) && isBalance(r.Right)
}

func main() {
	n0 := NewNode(0)
	n1 := NewNode(1)
	n2 := NewNode(2)
	n3 := NewNode(3)
	n4 := NewNode(4)
	// n5 := NewNode(5)
	// n6 := NewNode(6)
	n7 := NewNode(7)

	n0.Left = n1
	n0.Right = n2
	n1.Left = n3
	n1.Right = n4
	// n2.Left = n5
	// n2.Right = n6
	n3.Left = n7

	fmt.Printf("is balance: %+v\n", isBalance(n0))
}
