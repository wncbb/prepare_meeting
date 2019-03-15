package main

import "fmt"

func getKey(key1, key2 byte) string {
	keyA := string(key1)
	keyB := string(key2)
	return keyA + keyB
}

func buildPyramidByBlock(bottom string, top string, options map[string]map[string]bool) bool {
	if len(bottom) == 2 && len(top) == 1 {
		return true
	}
	if len(bottom)-1 == len(top) {
		return buildPyramidByBlock(top, "", options)
	}
	// 该解法只要考虑当前在处理的两块底座砖就行了
	option := options[getKey(bottom[len(top)], bottom[len(top)+1])]
	// 找出所有当前两块底砖能往上搭的砖
	for block := range option {
		// 开始处理下两块砖
		if buildPyramidByBlock(bottom, top+block, options) {
			return true
		}
	}
	return false
}

func pyramidTransition(bottom string, allowed []string) bool {
	options := map[string]map[string]bool{}
	for _, tuple := range allowed {
		key := getKey(tuple[0], tuple[1])
		if _, ok := options[key]; !ok {
			options[key] = map[string]bool{}
		}
		options[key][string(tuple[2])] = true
	}
	return buildPyramidByBlock(bottom, "", options)
}

func main() {
	/*
		Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
	*/
	fmt.Println("vim-go")
	bottom := "XYZ"
	allowed := []string{
		"XYD",
		"YZE",
		"DEA",
		"FFF",
	}
	rst := pyramidTransition(bottom, allowed)
	fmt.Printf("pyramidTransition: %+v\n", rst)
}
