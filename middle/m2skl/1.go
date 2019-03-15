package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func merge2Lists(list1, list2 *ListNode) *ListNode {
	res := &ListNode{}
	cur := res
	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			cur.Next = list1
			cur = cur.Next
			list1 = list1.Next
		} else {
			cur.Next = list2
			cur = cur.Next
			list2 = list2.Next
		}
	}

	for list1 != nil {
		cur.Next = list1
		list1 = list1.Next
		cur = cur.Next
	}

	for list2 != nil {
		cur.Next = list2
		list2 = list2.Next
		cur = cur.Next
	}

	return res.Next
}

func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	} else if len(lists) == 1 {
		return lists[0]
	}

	res := lists[0]

	for i := 1; i < len(lists); i = i + 1 {
		res = merge2Lists(res, lists[i])
	}

	return res
}

func main() {
	fmt.Println("vim-go")
}
