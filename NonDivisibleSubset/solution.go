package main

import (
	"fmt"
	"math"
)

func nonDivisibleSubset(k int32, S []int32) int32 {
	r := make([]int32, k)
	for i := 0; i < len(S); i++ {
		r[S[i]%k]++
	}
	cnt := int32(math.Min(float64(1), float64(r[0])))
	for i := int32(1); i < k/2+1; i++ {
		if i != k-i {
			cnt += int32(math.Max(float64(r[i]), float64(r[k-i])))
		}
	}
	if k%2 == 0 && r[k/2] != 0 {
		cnt++
	}
	return cnt
}

func main() {
	// arr := []int32{3, 17, 12, 9, 11, 15}
	// var k int32 = 5
	arr := []int32{1, 7, 2, 4}
	var k int32 = 3
	fmt.Println(nonDivisibleSubset(k, arr))

}
