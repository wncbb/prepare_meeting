package main

/*
	V(i, j), 表示对于前i件商品，在背包承重为j的情况下，背包所能带走的最大价值
	对于第i件商品
	if wi>j {
		V(i, j)=V(i-1, j)
	}else{
		V(j, j)=Max(V(i-1, j), V(i-1, j-wj)+vj)
	}

*/

func main() {

}
