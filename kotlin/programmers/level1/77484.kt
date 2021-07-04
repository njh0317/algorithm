class Solution_77484 {
    fun rank(num: Int): Int{
        when(num){
            0 -> return 6
            else -> return 7-num
        }
    }
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var zero_count = lottos.count{it == 0}
        var answer_count = 0

        win_nums.forEach {
            if(lottos.contains(it)){
                answer_count+=1
            }
        }

        answer+=rank(answer_count+zero_count)
        answer+=rank(answer_count)
        return answer
    }
}



fun main() {
    val sol = Solution_77484()
    val lottos = intArrayOf(44, 1, 0, 0, 31, 25)
    val win_nums = intArrayOf(31, 10, 45, 1, 6, 19)

    println(sol.solution(lottos, win_nums).contentToString())

}
