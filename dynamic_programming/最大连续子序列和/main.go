package main

/*
	s表示连续序列
	dp[i]表示以s[i]结尾的连续子序列和
	dp[i] = switch {
		case dp[i-1]<0:
			s[i]
		case dp[i-1]>=0:
			dp[i-1]+s[i]
	}
*/

func main() {

}
