package main

import (
	"fmt"
)

func parent(i int) int {
	return (i - 1) / 2
}

func left(i int) int {
	return i*2 + 1
}

func right(i int) int {
	return i*2 + 2
}

func maxHeapify(a []int, i int) {
	l := left(i)
	r := right(i)
	largestIdx := i
	if l < len(a) && a[l] > a[i] {
		largestIdx = l
	}
	if r < len(a) && a[r] > a[largestIdx] {
		largestIdx = r
	}

	if largestIdx != i {
		a[i], a[largestIdx] = a[largestIdx], a[i]
		maxHeapify(a, largestIdx)
	}
}

func buildMaxHeap(a []int) {
	for i := len(a) / 2; i >= 0; i-- {
		maxHeapify(a, i)
	}
}

func heapSort(a []int) {
	buildMaxHeap(a)
	for i := len(a) - 1; i > 0; i = i - 1 {
		a[0], a[i] = a[i], a[0]
		maxHeapify(a[:i], 0)
	}
}

func main() {
	a := []int{3, 8, 4, 6, 1, 9, 0, 5, 7, 2}
	buildMaxHeap(a)
	for _, v := range a {
		println(v)
	}
	heapSort(a)
	fmt.Printf("sorted rst: %#v\n", a)

}
