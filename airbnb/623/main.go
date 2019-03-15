package main

import "fmt"

func getMinInt(a int, s ...int) int {
	min := a
	for _, v := range s {
		if v < min {
			min = v
		}
	}
	return min
}

var result = make([]string, 0)

func helper(prevDp []int, w string, nodes map[string]interface{}, target string, preStr string, k int) {
	curDp := []int{prevDp[0] + 1}
	for idx, _ := range target {
		if target[idx:idx+1] == w {
			curDp = append(curDp, prevDp[idx])
		} else {
			minDis := getMinInt(prevDp[idx]+1, curDp[idx]+1, prevDp[idx+1]+1)
			curDp = append(curDp, minDis)
		}
	}
	if curDp[len(curDp)-1] <= k {
		if _, ok := nodes["#"]; ok {
			result = append(result, preStr+w)
		}
	}
	for _, nxt := range nodes {
		if v, ok := nxt.(string); !ok || v != "#" {
			helper(curDp, nxt, nodes[nxt], target, preStr+w, k)
		}
	}
}

func getKdistanceWord(wordList []string, target string, k int) []string {
	nodes := make(map[string]interface{})
	for _, word := range wordList {
		curNodes := nodes
		for idx, _ := range word {
			if _, ok := curNodes[word[idx:idx+1]]; !ok {
				curNodes[word[idx:idx+1]] = make(map[string]interface{})
			}
			curNodes = curNodes[word[idx:idx+1]].(map[string]interface{})
			if idx == len(word)-1 {
				curNodes["#"] = 1
			}
		}
	}

	for key, _ := range nodes {
		prevDp := make([]int, 0)
		for i := 0; i < len(target)+1; i = i + 1 {
			prevDp = i
		}
		helper(prevDp, key, nodes[key], target, "", k)
	}
	return result
}

func main() {
	wordList := []string{"abc", "abd", "abcd", "adc"}
	target := "ac"
	k := 1
	getKdistanceWord(wordList, target, k)

	rst := fmt.Println("vim-go")
	fmt.Printf("rst: %#v\n", rst)
}
