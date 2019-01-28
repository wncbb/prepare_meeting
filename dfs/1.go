package main

import (
	"april/base/node"
)

func main() {
	tree := node.NewTree1()
	dfs(tree)
}

func dfs(r *node.Node) {
	if r == nil {
		return
	}
	stack := make([]*node.Node, 0)
	stack = append(stack, r)
	for len(stack) != 0 {
		c := stack[len(stack)-1]
		stack = stack[0 : len(stack)-1]
		println(c.Value)
		if c.Right != nil {
			stack = append(stack, c.Right)
		}
		if c.Left != nil {
			stack = append(stack, c.Left)
		}
	}
}
