class Solution_42840 {
    fun solution(answers: IntArray): IntArray {
        var answer = intArrayOf()
        var answer_num = intArrayOf(0, 0, 0)
        var persons = arrayOf(intArrayOf(1, 2, 3, 4, 5), intArrayOf(2, 1, 2, 3, 2, 4, 2, 5), intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5))
        for(i in 0 until answers.size){
            persons.forEachIndexed { index, person ->
                if(answers[i] == person[i%person.size]) {
                    answer_num[index]+=1
                }
            }
        }
        answer_num.forEachIndexed { index, i ->
            if(i == answer_num.max()){
                answer+=(index+1)
            }
        }
        return answer
    }
}

fun main() {
    var arr = intArrayOf(1,3,2,4,2)
    var sol = Solution_42840()
    print(sol.solution(arr).contentToString())
}