class Solution_68644 {

    fun solution(numbers: IntArray): IntArray {
        var answer = intArrayOf()

        for ((index, value) in numbers.withIndex()){
            for(i in index+1 until numbers.size){
                answer+=numbers[index]+numbers[i]
            }
        }
        return answer.toSet().toIntArray().sortedArray()
    }
}

fun main() {
    val sol = Solution_68644()
    val numbers = intArrayOf(5,0,2,7)

    print(sol.solution(numbers).contentToString())
}