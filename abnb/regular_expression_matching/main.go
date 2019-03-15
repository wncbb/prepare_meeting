package main

import "fmt"

/*
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
*/

func isMatch(s string, p string) bool {
	sLen := len(s)
	pLen := len(p)

	// 长度是sLen+1, 索引的最大值是sLen
	dp := make([][]bool, sLen+1)
	for k := range dp {
		dp[k] = make([]bool, pLen+1)
	}

	dp[0][0] = true

	for j := 0; j < pLen; j = j + 1 {
		// fmt.Printf("TODDLINE:22 dp[0][%d]=%v\n", i-1, dp[0][i-1])
		if p[j] == '*' && dp[0][j-1] {
			dp[0][j+1] = true
		}
	}

	for i := 0; i < sLen; i = i + 1 {
		for j := 0; j < pLen; j = j + 1 {
			switch p[j] {
			// p[j]是.
			case '.':
				dp[i+1][j+1] = dp[i][j]
			// p[j]是*
			case '*':
				if p[j-1] == s[i] || p[j-1] == '.' {
					dp[i+1][j+1] = dp[i][j-1] || dp[i][j+1]
				}
				// should be dp[i+1][j-1], not dp[i][j-1]
				dp[i+1][j+1] = dp[i+1][j+1] || dp[i+1][j-1]
			// p[j]是普通字母
			default:
				if s[i] == p[j] {
					dp[i+1][j+1] = dp[i][j]
				}
			}

		}
	}
	return dp[sLen][pLen]

}

func main() {
	fmt.Println("vim-go")
}
