package main

import (
	"fmt"
)

/*
There're 3 kinds of bus ticket.
1: ticket 1 cost 2 and can be used for a day.
2: ticket 2 cost 7 and can be used for a consecutive 7 days.
3: ticket 3 cost 25 can be used for a month. Assume month here means 30 consecutive days.

Now there's a array filled with elements.
Each element value is a date for a person to travel.
This array has already been sorted in ascending order, like {1,3,4,5,11,12,23,24,30}.
Obviously the final day is 30th and first day is 1st.
So for any given array from a person to travel, how can this person cost least ?
*/

func getMinInt(a int, s ...int) int {
	res := a
	for _, v := range s {
		if v < res {
			res = v
		}
	}
	return res
}

var day2CostLookup = map[int]int{
	1:  2,
	7:  7,
	30: 25,
}

func target(days []int) []int {
	dp := make([]int, 31, 31)

	onTravel := make([]bool, 31, 31)
	for _, v := range days {
		onTravel[v] = true
	}

	for i := 1; i <= 30; i = i + 1 {
		dp[i] = 100
	}

	dp[0] = 0

	/*
		for i := 1; i <= 30; i = i + 1 {
			if onTravel[i] {
				for lpDay, lpCost := range day2CostLookup {
					if i >= lpDay {
						fmt.Printf("lpDay:%d,lpCost:%d, dp[%d]:%d\n", lpDay, lpCost, i, dp[i])
						dp[i] = getMinInt(dp[i], dp[i-lpDay]+lpCost)
					} else {
						dp[i] = getMinInt(dp[i], dp[0]+lpCost)
					}
				}
			} else {
				dp[i] = dp[i-1]
			}
		}
	*/
	dayIdx := 0
	for i := 1; i <= 30; i = i + 1 {
		if dayIdx < len(days) && i == days[dayIdx] {
			for lpDay, lpCost := range day2CostLookup {
				if i >= lpDay {
					fmt.Printf("lpDay:%d,lpCost:%d, dp[%d]:%d\n", lpDay, lpCost, i, dp[i])
					dp[i] = getMinInt(dp[i], dp[i-lpDay]+lpCost)
				} else {
					dp[i] = getMinInt(dp[i], dp[0]+lpCost)
				}
			}
			dayIdx = dayIdx + 1
		} else {
			dp[i] = dp[i-1]
		}
	}
	return dp
}

func main() {
	var testCase []int
	var rst []int

	testCase = []int{1, 2, 3, 4, 9, 10}
	rst = target(testCase)
	fmt.Printf("testCase:%#v\nrst:%#v\n-------------\n", testCase, rst)
}
