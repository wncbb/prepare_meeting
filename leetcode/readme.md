

#### [leetcode top 100](https://leetcode.com/problemset/top-100-liked-questions/)

#### 1. Two Sum

#### 2. Add Two Numbers

#### 3. Longest Substring Without Repeating Characters

#### 4. Median of Two Sorted Arrays
```
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	allNums := make([]int, 0, len(nums1)+len(nums2))
	i := 0
	j := 0
	for i < len(nums1) || j < len(nums2) {
		a := 0
		aIsEmpty := true
		if i < len(nums1) {
			a = nums1[i]
			aIsEmpty = false
		}

		b := 0
		bIsEmpty := true
		if j < len(nums2) {
			b = nums2[j]
			bIsEmpty = false
		}

		if aIsEmpty {
			allNums = append(allNums, b)
			j = j + 1
		} else if bIsEmpty {
			allNums = append(allNums, a)
			i = i + 1
		} else if !aIsEmpty && !bIsEmpty {
			if a > b {
				allNums = append(allNums, b)
				j = j + 1
			} else {
				allNums = append(allNums, a)
				i = i + 1
			}
		}
	}
	fmt.Printf("line40:%+v\n", allNums)
	if len(allNums) == 1 {
		return float64(allNums[0])
	}
	if len(allNums) == 2 {
		return float64(allNums[0]+allNums[1]) / 2
	}
	if len(allNums)%2 == 1 {
		return float64(allNums[len(allNums)/2])
	}
	return float64(allNums[(len(allNums)-1)/2]+allNums[(len(allNums)-1)/2+1]) / float64(2.0)}
```

#### 5. Longest Palindromic Substring
```
class Solution {
public:
    string longestPalindrome(string s) {
        string T;// Transform S to T
        for(int i=0;i<s.size();i++)
            T+="#"+s.substr(i,1);
        T.push_back('#');

        vector<int> P(T.size(),0); // Array to record longest palindrome
        int center=0,boundary=0,maxLen=0,resCenter=0;
        for(int i=1;i<T.size()-1;i++) {
            int iMirror=2*center-i; // calc mirror i = center-(i-center)
            P[i]=(boundary>i)?min(boundary-i,P[iMirror]):0; // shortcut
            while(i-1-P[i]>=0&&i+1+P[i]<=T.size()-1&&T[i+1+P[i]] == T[i-1-P[i]]) // Attempt to expand palindrome centered at i
                P[i]++;
            if(i+P[i]>boundary) { // update center and boundary
                center = i;
                boundary = i+P[i];
            }
            if(P[i]>maxLen) { // update result
                maxLen = P[i];
                resCenter = i;
            }    
        }
        return s.substr((resCenter - maxLen)/2, maxLen);
    }
};
```

#### 7. Reverse Integer
```
func reverse(x int) int {
	if x == 0 {
		return 0
	}
	sign := 1
	if x < 0 {
		sign = -1
		x = -1 * x
	}
	rst := 0
	for x > 0 {
		lastOne := x % 10
		x = x / 10
		rst = rst*10 + lastOne
		if rst > (1<<31 - 1) {
			return 0
		}
	}
	return rst * sign
}
```

#### 8. String to Integer (atoi)
```
import "strings"

func myAtoi(str string) int {
	str = strings.Trim(str, " ")

	if len(str) == 0 {
		return 0
	}

	sign := 1
	res := int64(0)
	if str[0] == '-' {
		sign = -1
		str = str[1:]
	} else if str[0] == '+' {
		str = str[1:]
	}

	strLen := 0
	for i := 0; i < len(str); i = i + 1 {
		if str[i] >= '0' && str[i] <= '9' {
			strLen += 1
		} else {
			break
		}
	}
	str = str[:strLen]

	if str == "" {
		return 0
	}

     max := int64((^uint32(0) >> 1))
     min := ^max

	for i := 0; i < len(str); i = i + 1 {
		res = res*10 + int64(str[i]-'0')
		switch sign {
		case -1:
			if -1*res < int64(min) {
				return int(min)
			}
		case 1:
			if res > int64(max) {
				return int(max)
			}
		}
	}

	return int(res) * sign
}
```

#### 10 
```
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
```

#### 39. Combination Sum
#### 42. Trapping Rain Water
#### 48. Rotate Image 
#### 394 Decode String
#### 461 Hamming Distance