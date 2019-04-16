package main

import "fmt"

func getMaxInt(a int, s ...int) int {
	res := a
	for _, v := range s {
		if v > res {
			res = v
		}
	}
	return res
}

func getBull(intList []int) (isBull bool, bullNum int) {
	allPos := [][]int{
		[]int{0, 1, 2, 3, 4},
		[]int{0, 1, 3, 2, 4},
		[]int{0, 1, 4, 2, 3},
		[]int{0, 2, 3, 1, 4},
		[]int{0, 2, 4, 1, 3},
		[]int{0, 3, 4, 1, 2},
		[]int{1, 2, 3, 0, 4},
		[]int{1, 2, 4, 0, 3},
		[]int{1, 3, 4, 0, 2},
		[]int{2, 3, 4, 0, 1},
	}

	getBullInner := func(s []int) (bool, int) {
		bullSum := 0
		for i := 0; i < 3; i = i + 1 {
			bullSum += intList[s[i]]
		}
		resIsBull := false
		resBullNum := 0
		if bullSum == 10 || bullSum == 20 || bullSum == 30 {
			resIsBull = true
			resBullNum = (s[3] + s[4]) % 10
			// 为了好比较，如果是牛牛，值是10，而不是0
			if resBullNum == 0 {
				resBullNum = 10
			}
		}
		return resIsBull, resBullNum
	}

	resIsBull := false
	resBullNum := 0
	for _, pos := range allPos {
		curIsBull, curBullNum := getBullInner(pos)
		fmt.Printf("line50 pos:%#v, isBull:%+v, bullNum:%+v\n", pos, curIsBull, curBullNum)

		if curIsBull {
			if resIsBull {
				resBullNum = getMaxInt(resBullNum, curBullNum)
			} else {
				resIsBull = curIsBull
				resBullNum = curBullNum
			}
		}
	}

	return resIsBull, resBullNum
}

func analyseCard(s string) (isBull bool, bullNum int, maxCard int) {
	intList := make([]int, 0, len(s))
	for _, ch := range s {
		curNum := 0
		if ch == 'A' {
			curNum = 1
		} else if ch == 'J' || ch == 'Q' || ch == 'K' || ch == 'T' {
			curNum = 10
		} else if ch >= '2' && ch <= '9' {
			curNum = int(ch - '0')
		}
		if curNum == 0 {
			// TODO:
			continue
		}
		intList = append(intList, curNum)
	}

	isBull, bullNum = getBull(intList)
	if !isBull {
		maxCard = getMaxInt(intList[0], intList[1:]...)
	}

	return
}

func compareCards(s1, s2 string) int {
	// TODO: check params
	s1IsBull, s1BullNum, s1MaxCard := analyseCard(s1)
	s2IsBull, s2BullNum, s2MaxCard := analyseCard(s2)

	fmt.Printf("s1 %v, %d, %d\n", s1IsBull, s1BullNum, s1MaxCard)
	fmt.Printf("s2 %v, %d, %d\n", s2IsBull, s2BullNum, s2MaxCard)

	// 为了好比较，换算成数字，是牛就加个10000
	getNum := func(isBull bool, bullNum int, maxCard int) int {
		res := 0
		if isBull {
			res = 10000 + bullNum
		} else {
			res = maxCard
		}
		return res
	}

	s1Num := getNum(s1IsBull, s1BullNum, s1MaxCard)
	s2Num := getNum(s2IsBull, s2BullNum, s2MaxCard)

	fmt.Printf("s1Num: %d\n", s1Num)
	fmt.Printf("s2Num: %d\n", s2Num)

	if s1Num > s2Num {
		return 1
	}
	if s1Num < s2Num {
		return -1
	}

	return 0
}

func main() {
	// s := "A123456789TJQK"
	s1 := "4579K"
	s2 := "AAAA2"
	rst := compareCards(s1, s2)
	fmt.Printf("rst: %d\n", rst)

	// a, b, c := analyseCard(s1)
	// fmt.Printf("%+v, %+v, %+v\n", a, b, c)
}
