package main

import "fmt"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * @param headA: the first list
 * @param headB: the second list
 * @return: a ListNode
 */
func getIntersectionNode(headA *ListNode, headB *ListNode) *ListNode {
	// write your code here
	if headA == nil || headB == nil {
		return nil
	}

	aLen := getListLen(headA)
	bLen := getListLen(headB)
	if aLen > bLen {
		headA, headB = headB, headA
		aLen, bLen = bLen, aLen
	}

	diff := bLen - aLen
	for i := 0; i < diff; i = i + 1 {
		headB = headB.Next
	}

	for headA != nil && headB != nil {
		if headA == headB {
			return headA
		}
		headA = headA.Next
		headB = headB.Next
	}
	return nil
}

func getListLen(head *ListNode) int {
	ret := 0
	for head != nil {
		ret = ret + 1
		head = head.Next
	}
	return ret
}

func main() {
	a1 := &ListNode{Val: 1}
	a2 := &ListNode{Val: 2}
	a3 := &ListNode{Val: 3}
	a4 := &ListNode{Val: 4}
	a5 := &ListNode{Val: 5}
	a1.Next = a2
	a2.Next = a4
	a4.Next = a5
	a3.Next = a4
	fmt.Printf("rst: %#v\n", getIntersectionNode(a1, a3))
	fmt.Printf("rst: %#v\n", getIntersectionNode(nil, nil))
}
