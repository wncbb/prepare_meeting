package main

import (
	"fmt"
	"strings"
)

/*
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
*/

func fullJustify(words []string, maxWidth int) []string {
	// TODO: parameters

	// badness[i][j] means words[i]与words[j]在同一行的badness
	badness := make([][]int, len(words))
	for i := 0; i < len(words); i = i + 1 {
		badness[i] = make([]int, len(words))
	}

	for i := 0; i < len(words); i = i + 1 {
		badness[i][i] = maxWidth - len(words[i])
		for j := i + 1; j < len(words); j = j + 1 {
			badness[i][j] = badness[i][j-1] - 1 - len(words[j])
		}
	}

	for _, v := range badness {
		fmt.Printf("%+v\n", v)
	}

	// cost[i]:=badness[i][j-1]+cost[j] | j=i+1 to len(words)-1
	cost := make([]int, len(words))
	parent := make([]int, len(words))
	for i := len(words) - 1; i >= 0; i = i - 1 {
		// cost[i]默认是从i到最后一个单词，在同一行
		cost[i] = badness[i][len(words)-1]
		parent[i] = len(words)
		// 必须从后往前来
		for j := len(words) - 1; j > i; j = j - 1 {
			// TODO: 是badness[i][j-1]
			// if badness[i][j] < 0 {
			if badness[i][j-1] < 0 {

				continue
			}
			if cost[i] < 0 || cost[i] > (badness[i][j-1]+cost[j]) {
				cost[i] = badness[i][j-1] + cost[j]
				parent[i] = j
			}
		}
	}
	fmt.Printf("cost:%#v\n", cost)
	fmt.Printf("parent: %#v\n", parent)

	ret := getLines(parent, words, maxWidth)
	for _, v := range ret {
		fmt.Printf("%s|\n", v)
	}

	return []string{}
}

func getLines(parent []int, words []string, maxWidth int) []string {
	ret := make([]string, 0)
	i := 0
	for {
		j := parent[i]
		if j >= len(words) {
			ret = append(ret, getLine(words[i:j], maxWidth, true))
			break
		} else {
			ret = append(ret, getLine(words[i:j], maxWidth, false))
		}
		i = j
	}
	return ret
}

func getSpaces(n int) string {
	ret := ""
	for i := 0; i < n; i = i + 1 {
		ret = ret + " "
	}
	return ret
}

func getLine(words []string, maxWidth int, isLast bool) string {
	ret := ""
	if isLast || len(words) == 1 {
		ret += strings.Join(words, " ")
	} else {
		nonSpaceLen := 0
		for _, v := range words {
			nonSpaceLen += len(v)
		}
		intervalSpaceNum := (maxWidth - nonSpaceLen) / (len(words) - 1)
		moreSpaceNum := (maxWidth - nonSpaceLen) % (len(words) - 1)
		for i := 0; i < len(words)-1; i = i + 1 {
			ret = ret + words[i] + getSpaces(intervalSpaceNum)
			if moreSpaceNum > 0 {
				ret = ret + " "
				moreSpaceNum = moreSpaceNum - 1
			}
		}
		ret = ret + words[len(words)-1]
	}

	ret += getSpaces(maxWidth - len(ret))
	return ret
}

func main() {
	fmt.Println("vim-go")
	words := []string{"This", "is", "an", "example", "of", "text", "justification."}
	maxWidth := 16
	fullJustify(words, maxWidth)
}
