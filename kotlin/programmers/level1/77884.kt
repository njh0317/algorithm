class Solution_77884 {
    fun divisor_num(num: Int): Boolean {
        var cnt = 0

        for(i in 1..num){
            if(num%i == 0){
                cnt+=1
            }
        }
        when{
            cnt%2 == 0 -> return true
            else -> return false
        }

    }
    fun solution(left: Int, right: Int): Int {
        var answer: Int = 0
        for(i in left..right){
            if(divisor_num(i))
                answer+=i
            else answer+=(i*-1)
        }
        return answer
    }
}

fun main() {
    var sol = Solution_77884()
    print(sol.solution(24, 27))
}