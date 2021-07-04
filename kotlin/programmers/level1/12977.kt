class Solution_12977 {
    fun combination(answer: MutableList<List<Int>>, el: IntArray, ck: Array<Boolean>, start: Int, target: Int){
        /*
        dfs 방식으로 구성
        answer: 결과가 담김
        el : comb 할 배열
        ck : el 크기만큼의 boolean 배열
        start : 시작 인덱스
        target : comb 개수
         */
        if(target == 0){
            //target 개수만큼 구성하면 answer에 더함
            answer.addAll(listOf(el.filterIndexed { index, t ->  ck[index]}))
        }
        else{
            for(i in start until el.size){
                ck[i] = true
                combination(answer, el, ck, i+1, target-1)
                ck[i] = false
            }
        }
    }
    fun isPrime(num: Int):Boolean{
        if(num<=1) return false
        for(i in 2..num-2){
            if(num%i == 0) return false
        }
        return true
    }
    fun solution(nums: IntArray): Int {
        var answer = 0
        val comb = mutableListOf<List<Int>>()
        combination(comb, nums, Array<Boolean>(nums.size){ false }, 0, 3)
        comb.forEach{
            if(isPrime(it.sum())){
                answer+=1
            }
        }
        return answer
    }
}

fun main() {
    val sol = Solution_12977()
    val arr = intArrayOf(1, 2, 3, 4)
    print(sol.solution(arr))
}