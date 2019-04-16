package main

import "fmt"

type Stack struct {
	Data []*Node
}

func NewStack() *Stack {
	return &Stack{
		Data: make([]*Node, 0),
	}
}

func (s *Stack) Push(n *Node) {
	s.Data = append(s.Data, n)
}

func (s *Stack) IsEmpty() bool {
	return len(s.Data) == 0
}

func (s *Stack) Pop() *Node {
	if s.IsEmpty() {
		return nil
	}
	res := s.Data[len(s.Data)-1]
	s.Data = s.Data[0 : len(s.Data)-1]
	return res
}

func (s *Stack) Peek() *Node {
	if s.IsEmpty() {
		return nil
	}
	return s.Data[len(s.Data)-1]
}

func printPath(p []*Node) {
	fmt.Printf("\n")
	for _, v := range p {
		fmt.Printf("%d, ", v.Val)
	}
	fmt.Printf("\n")
}

func getPath(t *Node, r *Node) []*Node {
	if t == nil || r == nil {
		return []*Node{}
	}

	stack := NewStack()
	stack.Push(r)

	for !stack.IsEmpty() {
		// printPath(stack.Data)
		curNode := stack.Peek()
		if curNode == t {
			return stack.Data
		} else {
			if curNode.Left != nil && !curNode.Left.Visited {
				stack.Push(curNode.Left)
			} else if curNode.Right != nil && !curNode.Right.Visited {
				stack.Push(curNode.Right)
			} else {
				delNode := stack.Pop()
				delNode.Visited = true
			}
		}
	}

	return stack.Data
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

func main() {
	n0 := NewNode(0)
	n1 := NewNode(1)
	n2 := NewNode(2)
	n3 := NewNode(3)
	n4 := NewNode(4)
	n5 := NewNode(5)
	n6 := NewNode(6)
	n7 := NewNode(7)

	n0.Left = n1
	n0.Right = n2
	n1.Left = n3
	n1.Right = n4
	n2.Left = n5
	n2.Right = n6
	n3.Left = n7

	/*
		path1 := getPath(n7, n0)
		for _, v := range path1 {
			fmt.Printf("path1: %d\n", v.Val)
		}

	*/
	fmt.Println("")

	path2 := getPath(n5, n0)
	for _, v := range path2 {
		fmt.Printf("path2: %d\n", v.Val)
	}

}
