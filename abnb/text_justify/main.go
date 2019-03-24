package main

import (
	"fmt"
)

func fullJustify(words []string, maxWidth int) []string {
	cost := make([][]int, len(words))
	for i := 0; i < len(words); i = i + 1 {
		cost[i] = make([]int, len(words))
	}
	for i := 0; i < len(words); i = i + 1 {
		cost[i][i] = maxWidth - len(words[i])
		for j := i + 1; j < len(words); j = j + 1 {
			// 负数表示不可能(从单词i到单词j在同一行)
			cost[i][j] = cost[i][j-1] - len(words[j]) - 1
		}
	}

	for _, v := range cost {
		fmt.Printf("%+v\n", v)
	}

	// cost[i][j]表示第i个到第j个单词(闭区间)在一行的cost, 复数表示不可能
	/*
		for i := 0; i < len(words); i = i + 1 {
			for j := i; j < len(words); j = j + 1 {
				if cost[i][j] >= 0 {
					cost[i][j] = cost[i][j] * cost[i][j]
				}
			}
		}
	*/

	// for _, v := range cost {
	// 	fmt.Printf("%+v\n", v)
	// }

	// minCost[i]表示从第i个单词到最后，的最优解
	minCost := make([]int, len(words))
	// 表示位置
	result := make([]int, len(words))
	for i := len(words) - 1; i >= 0; i = i - 1 {
		minCost[i] = cost[i][len(words)-1]
		// 表示第len(words)的单词是最后一行，显然不存在len(words)个单词
		result[i] = len(words)
		for j := len(words) - 1; j > i; j = j - 1 {
			if cost[i][j-1] < 0 {
				continue
			}
			if minCost[i] < 0 || minCost[i] > minCost[j]+cost[i][j-1] {
				minCost[i] = minCost[j] + cost[i][j-1]
				// 在第j个单词的位置，起新的一行
				result[i] = j
			}
		}
	}
	fmt.Printf("minCost:%#v\n", minCost)
	fmt.Printf("result:%#v\n", result)

	i := 0
	j := 0
	ret := make([]string, 0)
	for {
		j = result[i]
		fmt.Printf("i:%d, j:%d\n", i, j)

		if j >= len(words) {
			ret = append(ret, getLine(words[i:j], maxWidth, true))
			break
		} else {
			ret = append(ret, getLine(words[i:j], maxWidth, false))
		}
		i = j
	}

	// for _, v := range ret {
	// 	println(v)
	// }

	return ret
}

func getSpace(num int) string {
	ret := ""
	for i := 0; i < num; i = i + 1 {
		ret = ret + " "
	}
	return ret
}

func getLine(words []string, maxWidth int, isLast bool) string {
	ret := ""
	if isLast {
		for i := 0; i < len(words)-1; i = i + 1 {
			ret += words[i] + " "
		}
		ret += words[len(words)-1]
		ret += getSpace(maxWidth - len(ret))
		return ret
	}

	avg := 0
	wordsLen := 0
	for _, v := range words {
		wordsLen += len(v)
	}
	if len(words) > 1 {
		avg = (maxWidth - wordsLen) / (len(words) - 1)
	}

	moreSpace := maxWidth - wordsLen - avg*(len(words)-1)
	// fmt.Printf("avg:%d\n", avg)
	// fmt.Printf("moreSpace:%d\n", moreSpace)
	for i := 0; i < len(words)-1; i = i + 1 {
		ret = ret + words[i]
		if moreSpace > 0 {
			ret = ret + getSpace(1+avg)
		} else {
			ret = ret + getSpace(avg)
		}
		moreSpace -= 1
	}
	ret += words[len(words)-1]

	ret += getSpace(maxWidth - len(ret))

	return ret
}

func main() {
	words := []string{"This", "is", "an", "example", "of", "text", "justification."}
	maxWidth := 16
	rst := fullJustify(words, maxWidth)
	for _, v := range rst {
		println(v)
	}
}
