package main

import (
	"fmt"
	"toddtool"
)

func getHint(secret string, guess string) string {
	if len(secret) != len(guess) {
		return ""
	}
	secretLookup := make(map[string]int, len(secret))
	guessLookup := make(map[string]int, len(guess))

	bulls := 0
	cows := 0
	for i := 0; i < len(secret); i = i + 1 {
		if secret[i] == guess[i] {
			bulls += 1
		} else {
			secretLookup[secret[i:i+1]] += 1
			guessLookup[guess[i:i+1]] += 1
		}
	}
	for k, sv := range secretLookup {
		if gv, ok := guessLookup[k]; ok {
			cows += toddtool.GetMinInt(sv, gv)
		}
	}
	return fmt.Sprintf("%dA%dB", bulls, cows)
}

func main() {
	//  "1807", guess = "7810"
	secret := "1807"
	guess := "7810"
	rst := getHint(secret, guess)
	println(rst)
}
