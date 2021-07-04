package programmers_level1

class Solution_42748 {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var answer = intArrayOf()

        commands.forEach {
            val (i, j, k) = it
            val slice = array.sliceArray(i-1..j-1)
            slice.sort()
            answer+=slice[k-1]
        }

        return answer
    }
}

fun main() {
    var sol = Solution_42748()
    var array = intArrayOf(1, 5, 2, 6, 3, 7, 4)
    var commands = arrayOf(intArrayOf(2, 5, 3), intArrayOf(4, 4, 1), intArrayOf(1, 7, 3))

    print(sol.solution(array, commands).contentToString())
}