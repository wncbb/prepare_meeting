package tmp

/**
 * @param nums: the given array
 * @param k: the given k
 * @param t: the given t
 * @return: whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
 */
func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	// Write your code here
	if len(nums) == 0 || k < 0 || t <= 0 {
		return false
	}

	min := nums[0]
	max := nums[0]
	for i := 1; i < len(nums); i = i + 1 {
		if nums[i] > max {
			max = nums[i]
		}
		if nums[i] < min {
			min = nums[i]
		}
	}

	bucketWidth := t + 1
	bucket := make(map[int]int)
	for i := 0; i < len(nums); i = i + 1 {
		remappedNum := (nums[i] - min)
		bktIdx := remappedNum / (t + 1)
		if _, ok := bucket[bktIdx]; ok {
			return true
		}

		if bktIdx >= 1 {
			j, ok := bucket[bktIdx-1]
			if ok && getAbsInt(remappedNum-j) <= t {
				return true
			}
		}
		if bktIdx < len(nums)-1 {
			j, ok := bucket[bktIdx+1]
			if ok && getAbsInt(remappedNum-j) <= t {
				return true
			}
		}
		if len(bucket) >= k {
			laskBucketIdx := (nums[i-k] - min) / bucketWidth
			delete(bucket, laskBucketIdx)
		}
		bucket[bktIdx] = remappedNum
	}
	return false
}
