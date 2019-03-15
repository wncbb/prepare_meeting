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
 *     Next *ListNode * }
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

	listLen := len(lists)
	k := listLen / 2
	for k > 0 {
		for i := 0; i <= k; i = i + 1 {
			fmt.Printf("i:%d, i+k:%d\n", i, i+k)
			if i+k >= len(lists) {
				lists[i] = merge2Lists(lists[i], nil)
			} else {
				lists[i] = merge2Lists(lists[i], lists[i+k])
				lists[i+k] = nil
			}

		}
		k = k / 2
		fmt.Printf("k:%d\n", k)
	}

	/*
		res := lists[0]

		for i := 1; i < len(lists); i = i + 1 {
			res = merge2Lists(res, lists[i])
		}
	*/

	return lists[0]
}

func getTestCase() []*ListNode {
	a1 := &ListNode{
		Val: 1,
	}
	a2 := &ListNode{
		Val: 2,
	}
	a3 := &ListNode{
		Val: 3,
	}
	a4 := &ListNode{
		Val: 4,
	}
	return []*ListNode{
		a1,
		a2,
		a3,
		a4,
	}
}

func printList(a *ListNode) {
	fmt.Printf("printList: ")
	for a != nil {
		fmt.Printf("%d, ", a.Val)
		a = a.Next
	}
	fmt.Printf("\n")
}

func main() {
	lists := getTestCase()
	rst := mergeKLists(lists[0:3])
	printList(rst)
	fmt.Println("vim-go")
}
