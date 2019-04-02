package main

import (
	"fmt"
	"net"
)

var right = "6451"

func getMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func cowsAndBulls(guess string) (int, int) {
	cows := 0
	bulls := 0
	rightLookup := make(map[byte]int, 4)
	guessLookup := make(map[byte]int, 4)
	for i := 0; i < len(guess); i = i + 1 {
		if guess[i] == right[i] {
			cows += 1
		} else {
			if _, ok := rightLookup[right[i]]; !ok {
				rightLookup[right[i]] = 0
			}
			if _, ok := guessLookup[guess[i]]; !ok {
				guessLookup[guess[i]] = 0
			}
			rightLookup[right[i]] += 1
			guessLookup[guess[i]] += 1
		}
	}
	for rightCh, rightNum := range rightLookup {
		if guessNum, ok := guessLookup[rightCh]; ok {
			bulls = bulls + getMin(rightNum, guessNum)
		}
	}
	fmt.Printf("guess:%s, cows:%d, bulls:%d\n", guess, cows, bulls)
	return cows, bulls
}

func connHandler(c net.Conn) {
	if c == nil {
		return
	}
	readBuf := make([]byte, 4096)
	for {
		_, _ = c.Read(readBuf)
		r1, r2 := cowsAndBulls(string(readBuf[:4]))
		if r1 == 4 {
			break
		}
		wirteStr := fmt.Sprintf("%d %d", r1, r2)
		c.Write([]byte(wirteStr))
		fmt.Printf("read: %s\n", string(readBuf[:4]))
	}
	fmt.Printf("Connection from %v closed. \n", c.RemoteAddr())
}
func main() {
	server, err := net.Listen("tcp", ":1208")
	if err != nil {
		fmt.Printf("Fail to start server, %s\n", err)
	}
	fmt.Println("Server Started ...")
	for {
		conn, err := server.Accept()
		if err != nil {
			fmt.Printf("Fail to connect, %s\n", err)
			break
		}
		go connHandler(conn)
	}
}
