class Solution_76501 {
    fun sign(flag: Boolean):Int{
        when(flag){
            true -> return 1
            false -> return -1
        }
    }
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var answer: Int = 0
        absolutes.forEachIndexed{ index, i ->
            answer+=i*(sign(signs[index]))
        }
        return answer
    }
}

fun main() {
    var absolutes = intArrayOf(4, 7, 12)
    var signs = booleanArrayOf(true, false, true)
    val sol = Solution_76501()
    print(sol.solution(absolutes, signs))
}