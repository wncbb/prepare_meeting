package main

import "fmt"

func t(s, p string) bool {
	d := make([][]bool, len(s)+1)
	for k, _ := range d {
		d[k] = make([]bool, len(p)+1)
	}

	d[0][0] = true
	for j := 0; j < len(p); j = j + 1 {
		// like xx* 因为s是空字符串，因此p也必须匹配空字符串
		// *只能表示重复前面的字符0次
		// 因此只要d[0][j-1]是true, 就ok, j位置，被j+1的*干掉了
		if p[j] == '*' && d[0][j-1] {
			d[0][j+1] = true
		}
	}

	fmt.Printf("d: %#v\n", d)

	for i := 0; i < len(s); i = i + 1 {
		for j := 0; j < len(p); j = j + 1 {
			switch p[j : j+1] {
			case ".":
				d[i+1][j+1] = d[i][j]
			case "*":
				// s: 00a
				// p: 0a*
				// 对于上面这种情况要么p[1]=a重复一次，此时分为:
				// s: 00|a
				// p: 0|a*
				// d[i][j-1]为true, 那么d[i+1][j+1]为true
				// 如果p[1]=a重复>1次，此时分为:
				// s: 00|a
				// p: 0a*|
				if s[i] == p[j-1] || s[i] == '.' {
					d[i+1][j+1] = d[i+1][j+1] || d[i][j-1] || d[i][j+1]
				}
				// 重复0次
				d[i+1][j+1] = d[i+1][j+1] || d[i+1][j-1]
			default:
				if s[i] == p[j] {
					d[i+1][j+1] = d[i][j]
				}
			}
		}
	}

	return d[len(s)][len(p)]
}

func main() {
	s := "aab"
	p := "a*."

	println(t(s, p))
}
