package node

type Node struct {
	Value int
	Left  *Node
	Right *Node
}

func NewNode(v int, left, right *Node) *Node {
	return &Node{
		Value: v,
		Left:  left,
		Right: right,
	}
}

func NewTree1() *Node {
	nodes := make([]*Node, 0, 5)
	for i := 0; i < 5; i++ {
		nodes = append(nodes, NewNode(i, nil, nil))
	}

	nodes[0].Left = nodes[1]
	nodes[0].Right = nodes[2]
	nodes[1].Right = nodes[3]
	nodes[2].Left = nodes[4]

	return nodes[0]
}
