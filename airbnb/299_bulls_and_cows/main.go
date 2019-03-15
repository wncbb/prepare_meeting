package main

import "fmt"

func getMinInt(a int, s ...int) int {
	min := a
	for _, v := range s {
		if min > v {
			min = v
		}
	}
	return min
}

func getHint(secret string, guess string) string {
	lookupSecret := make(map[string]int)
	lookupGuess := make(map[string]int)
	cows := 0
	bulls := 0
	if len(secret) != len(guess) {
		return ""
	}
	for k, _ := range secret {
		if guess[k:k+1] == secret[k:k+1] {
			cows += 1
		} else {
			lookupSecret[secret[k:k+1]] += 1
			lookupGuess[guess[k:k+1]] += 1
		}
	}

	for k, guessNum := range lookupGuess {
		if secretNum, ok := lookupSecret[k]; ok && secretNum > 0 {
			bulls += getMinInt(guessNum, secretNum)
		}
	}
	return fmt.Sprintf("%dA%dB", cows, bulls)
}

func main() {
	//  "1807", guess = "7810"
	secret := "1807"
	guess := "7810"
	rst := getHint(secret, guess)
	println(rst)
}
