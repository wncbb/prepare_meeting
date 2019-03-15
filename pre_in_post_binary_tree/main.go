package main

import (
	"april/base/node"
	"fmt"
)

type Operation struct {
	// 1:exec_now, 2:visit_children
	Typ  int
	Node *node.Node
}

func traverse(r *node.Node) {
	stack := make([]*Operation, 0)

	if r == nil {
		return
	}

	stack = append(stack, &Operation{
		Typ:  2,
		Node: r,
	})

	for len(stack) != 0 {
		op := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		switch op.Typ {
		case 1:
			fmt.Printf("%d\n", op.Node.Value)
		case 2:
			if op.Node.Right != nil {
				stack = append(stack, &Operation{
					Typ:  2,
					Node: op.Node.Right,
				})
			}
			stack = append(stack, &Operation{
				Typ:  1,
				Node: op.Node,
			})
			if op.Node.Left != nil {
				stack = append(stack, &Operation{
					Typ:  2,
					Node: op.Node.Left,
				})
			}
		}
	}
}

func main() {
	tree := node.NewTree1()

	traverse(tree)
}
