class Solution_42889 {
    fun solution(N: Int, stages: IntArray): IntArray {
        var answer = intArrayOf()
        var fail = mutableListOf<Pair<Int, Double>>()

        for(i in 1..N){
            val top = stages.count { it == i }.toDouble()
            val down = stages.filter { it >= i }.count().toDouble()
            if(down == 0.toDouble()) fail.add(Pair(i, 0.toDouble()))
            else fail.add(Pair(i, (top/down)))
        }
        fail.sortWith(compareBy({(-1)*it.second}, {it.first}))
        fail.forEach{
            answer+=it.first
        }

        return answer
    }
}


fun main() {
    var N = 5
    var stages = intArrayOf(2, 1, 2, 6, 2, 4, 3, 3)
    val sol = Solution_42889()
    print(sol.solution(N, stages).contentToString())
}