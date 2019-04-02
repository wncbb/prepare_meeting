package main

import (
	"fmt"
	"net"
	"strconv"
)

func sameSlice(s []int) bool {
	cur := s[0]
	for i := 1; i < len(s); i = i + 1 {
		if cur != s[i] {
			return false
		}
	}
	return true
}

func getMaxIdx(s []int) int {
	if sameSlice(s) {
		return 5
	}
	res := 0
	for i := 1; i < len(s); i = i + 1 {
		if s[i] > s[res] {
			res = i
		}
	}
	return res
}

func getRight(s []string, rs []int) string {
	c1 := getMaxIdx(rs[0:5])
	c2 := getMaxIdx(rs[5:10])
	c3 := getMaxIdx(rs[10:15])
	c4 := getMaxIdx(rs[15:20])
	return fmt.Sprintf("%d%d%d%d", c1+1, c2+1, c3+1, c4+1)
}

func getCases() []string {
	res := make([]string, 0, 24)
	for i := 0; i < 4; i = i + 1 {
		for j := 0; j < 5; j = j + 1 {
			tmpStr := ""
			for tmp := 0; tmp < i; tmp = tmp + 1 {
				tmpStr += "1"
			}
			tmpStr += strconv.FormatInt(int64(j+1), 10)
			for tmp := len(tmpStr); tmp < 4; tmp = tmp + 1 {
				tmpStr += "1"
			}
			res = append(res, tmpStr)
		}
	}

	return res
}

func connHandler(c net.Conn) {
	defer c.Close()
	// reader := bufio.NewReader(os.Stdin)

	cases := getCases()
	buf := make([]byte, 1024)
	rs := make([]int, 0)
	for _, v := range cases {
		c.Write([]byte(v))
		_, err := c.Read(buf)
		r1 := int(buf[0] - '0')
		r2 := int(buf[2] - '0')
		if r1 == 4 {
			fmt.Printf("right str: %s\n", v)
			return
		}
		if err != nil {
			fmt.Printf("Fail to read data, %s\n", err)
			break
		}
		rs = append(rs, r1)
		fmt.Printf("rst guess:%s, r1:%d, r2:%d\n", v, r1, r2)
	}
	rst := getRight(cases, rs)
	fmt.Printf("right str: %s\n", rst)
}
func main() {
	conn, err := net.Dial("tcp", "localhost:1208")
	if err != nil {
		fmt.Printf("Fail to connect, %s\n", err)
		return
	}
	connHandler(conn)
	// cases := getCases()
	// for _, v := range cases {
	// 	fmt.Printf("v:%s\n", v)
	// }
}
