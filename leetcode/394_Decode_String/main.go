package main

func dfs(s string, k *int) string {
	var ans string
	cnt := 0
	for *k < len(s) {
		println(*k)
		switch {
		case s[*k] >= '0' && s[*k] <= '9':
			cnt = cnt*10 + int(s[*k]-'0')
			*k++
		case s[*k] == '[':
			*k++
			tem := dfs(s, k)
			for i := 0; i < cnt; i++ {
				ans += tem
			}
			cnt = 0
		case s[*k] == ']':
			*k++
			return ans
		default:
			ans += s[*k : *k+1]
			*k++
		}
	}
	return ans
}

func decodeString(s string) string {
	k := 0
	return dfs(s, &k)
}

func main() {
	println(decodeString("3[a]"))
}
