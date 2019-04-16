package main

import "fmt"

func reverseRune(rs []rune) {
	left := 0
	right := len(rs) - 1
	for left < right {
		rs[left], rs[right] = rs[right], rs[left]
		left += 1
		right -= 1
	}
}

func reverseWords(s string) string {
	rs := []rune(s)
	reverseRune(rs)

	wordLeft := 0

	idx := -1
	for true {
		fmt.Printf("s: '%s'\n", string(rs))
		idx = idx + 1

		if idx >= len(rs) {
			break
		}

		if rs[idx] == ' ' {
			reverseRune(rs[wordLeft:idx])
			wordLeft = idx + 1
		}
	}

	reverseRune(rs[wordLeft:idx])

	return string(rs)
}

func main() {
	s := "I am a poor guy"
	fmt.Printf("reverse(s): \"%s\"\n", reverseWords(s))
}
