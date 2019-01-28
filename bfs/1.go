package main

import (
	"april/base/node"
	"fmt"
)

func main() {
	fmt.Println("vim-go")
	tree := node.NewTree1()
	bfs(tree)
}

func bfs(r *node.Node) {
	fifo := make([]*node.Node, 0)
	if r != nil {
		fifo = append(fifo, r)
	}

	for len(fifo) != 0 {
		c := fifo[len(fifo)-1]
		fifo = fifo[0 : len(fifo)-1]
		println(c.Value)
		if c.Left != nil {
			fifo = append([]*node.Node{c.Left}, fifo...)
		}
		if c.Right != nil {
			fifo = append([]*node.Node{c.Right}, fifo...)
		}
	}
}
