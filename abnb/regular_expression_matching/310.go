package main

/**
 * @param s: A string
 * @param p: A string includes "." and "*"
 * @return: A boolean
 */
func isMatch(s string, p string) bool {
	// 异常处理
	if p[0] == '*' {
		return false
	}
	// write your code here
	// check params
	dp := make([][]bool, len(s)+1)
	for k, _ := range dp {
		dp[k] = make([]bool, len(p)+1)
	}

	dp[0][0] = true
	for i := 0; i < len(p); i = i + 1 {
		if p[i] == '*' {
			// should be dp[0][i], not dp[i]
			// should be dp[0][i+1]=dp[0][i-1], not dp[0][i+1]=dp[0][i]
			// 因为*抹掉自己，也抹掉前面的字符
			dp[0][i+1] = dp[0][i-1]
		}
	}

	for i := 0; i < len(s); i = i + 1 {
		for j := 0; j < len(p); j = j + 1 {
			switch p[j : j+1] {
			case "*":
				if s[i] == p[j-1] || p[j-1:j] == "." {
					dp[i+1][j+1] = dp[i][j-1] || dp[i][j+1]
				}
				dp[i+1][j+1] = dp[i+1][j+1] || dp[i][j]
			case ".":
				dp[i+1][j+1] = dp[i][j]
			default:
				// fmt.Printf("i:%d, j:%d\n", i, j)
				// should be s[i]==p[j], not s[i]==s[j]
				if s[i] == p[j] {
					dp[i+1][j+1] = dp[i][j]
				}
			}
		}
	}
	return dp[len(s)][len(p)]
}

func main() {
	s := "aab"
	p := "c*a*b"
	println(isMatch(s, p))
}
