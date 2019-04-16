package main

import (
	"fmt"
)

type Stack struct {
	Data []int
}

func NewStack() *Stack {
	fmt.Prit
	return &Stack{
		Data: make([]int, 0),
	}
}

func (s *Stack) Push(v int) {
	s.Data = append(s.Data, v)
}

func (s *Stack) IsEmtpy() bool {
	return len(s.Data) == 0
}

func (s *Stack) Pop() int {
	if s.IsEmtpy() {
		return -1
	}
	res := s.Data[len(s.Data)-1]
	s.Data = s.Data[:len(s.Data)-1]
	return res
}

type StackQueue struct {
	stack1 *Stack
	stack2 *Stack
}

func NewStackQueue() *StackQueue {
	return &StackQueue{
		stack1: NewStack(),
		stack2: NewStack(),
	}
}

func (s *StackQueue) IsEmpty() bool {
	return s.stack1.IsEmtpy() && s.stack2.IsEmtpy()
}

func (s *StackQueue) AppendLeft(a int) {
	s.stack1.Push(a)
}

func (s *StackQueue) PopRight() int {
	if s.IsEmpty() {
		return -1
	}
	if s.stack2.IsEmtpy() {
		for !s.stack1.IsEmtpy() {
			s.stack2.Push(s.stack1.Pop())
		}
	}
	return s.stack2.Pop()
}

func main() {
	q := NewStackQueue()
	q.AppendLeft(0)
	q.AppendLeft(1)
	q.AppendLeft(2)
	fmt.Printf("rst: %d\n", q.PopRight())
	q.AppendLeft(3)
	q.AppendLeft(4)
	fmt.Printf("rst: %d\n", q.PopRight())
	fmt.Printf("rst: %d\n", q.PopRight())
	fmt.Printf("rst: %d\n", q.PopRight())
	fmt.Printf("rst: %d\n", q.PopRight())
	q.AppendLeft(5)
	q.AppendLeft(6)
	fmt.Printf("rst: %d\n", q.PopRight())
	fmt.Printf("rst: %d\n", q.PopRight())
	fmt.Printf("rst: %d\n", q.PopRight())
	fmt.Printf("rst: %d\n", q.PopRight())

}
