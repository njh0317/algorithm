class Solution_12954 {
    fun solution(x: Int, n: Int): LongArray {
        var answer = longArrayOf()
        var startnum: Long = x.toLong()
        for (i in 0 until n){
            answer+=startnum.toLong()
            startnum+=x.toLong()
        }
        return answer
    }
}

fun main() {
    var sol = Solution_12954()
    print(sol.solution(-4, 2).contentToString())
}