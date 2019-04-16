package main

import "fmt"

type StreamJudger struct {
	curNum int
}

func (s *StreamJudger) DividedByThree(cur int) bool {
	s.curNum = (s.curNum*2 + cur) % 3
	return s.curNum == 0
}

func NewStreamJudger() *StreamJudger {
	return &StreamJudger{
		curNum: 0,
	}
}

func main() {
	s := NewStreamJudger()
	curList := []int{1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1}
	num := 0
	for _, v := range curList {
		num = num*2 + v
		fmt.Printf("num:%d, cur: %v\n", num, s.DividedByThree(v))
	}
}
