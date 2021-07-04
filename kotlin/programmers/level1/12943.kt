class Solution_12943 {
    fun solution(num: Int): Int {
        var answer = 0
        var collatz = num.toLong()
        while(collatz!=1.toLong()){
            collatz = if (collatz % 2 == 0L) collatz / 2 else collatz * 3 + 1
            answer+=1
            if(answer>=500) return -1
        }

        return answer
    }
    

}

fun main() {
    var n = 1
    val sol = Solution_12943()
    print(sol.solution(n))
}