package main

import (
	"fmt"
)

func getLookup(allowed []string) map[string][]string {
	ret := make(map[string][]string)
	for _, v := range allowed {
		if _, ok := ret[v[0:2]]; !ok {
			ret[v[0:2]] = make([]string, 0)
		}
		ret[v[0:2]] = append(ret[v[0:2]], v[2:3])
	}

	return ret
}

func build(bottom string, top string, lookup map[string][]string) bool {
	if len(bottom) == 2 && len(top) == 1 {
		return true
	}
	// 条件是bottom的长度比top多1
	if len(bottom) == len(top)+1 {
		// ERROR
		// if len(bottom) == len(top)-1 {
		return build(top, "", lookup)
	}
	//  3 2
	// 1 2 3
	// base是取bottom的俩位置的字符，必须是单个
	base := bottom[len(top):len(top)+1] + bottom[len(top)+1:len(top)+2]
	// ERROR:
	// base := bottom[len(top):len(top)+1] + bottom[len(top)+1:]

	nextOps, ok := lookup[base]
	if !ok {
		return false
	}

	for _, v := range nextOps {
		tmpRst := build(bottom, top+v, lookup)
		if tmpRst {
			return true
		}
	}

	return false
}

func pyramidTransition(bottom string, allowed []string) bool {
	lookup := getLookup(allowed)
	return build(bottom, "", lookup)
}

func main() {
	bottom := "XYZ"
	allowed := []string{
		"XYD",
		"YZE",
		"DEA",
		"FFF",
	}
	fmt.Printf("rst:%#v\n", pyramidTransition(bottom, allowed))
}
