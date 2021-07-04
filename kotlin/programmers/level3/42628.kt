import java.util.*

class Solution_42628 {
    fun solution(operations: Array<String>): IntArray {
        var answer = intArrayOf(0, 0)

        val maxQueue = PriorityQueue<Int>(Collections.reverseOrder())
        val minQueue = PriorityQueue<Int>()

        operations.forEach {
            val op = it.split(" ")
            when(op[0])
            {
                "I" -> { //insert
                    maxQueue.add(op[1].toInt())
                    minQueue.add(op[1].toInt())
                }
                "D" -> run {//delete
                    if(maxQueue.isEmpty()) return@run
                    when(op[1]){
                        "1" -> {
                            val maxnum = maxQueue.poll()
                            minQueue.remove(maxnum)
                        }
                        "-1" -> {
                            val minnum = minQueue.poll()
                            maxQueue.remove(minnum)
                        }
                    }
                }
            }

        }

        if(!maxQueue.isEmpty()) answer = intArrayOf(maxQueue.peek(), minQueue.peek())
        return answer
    }
}

fun main() {
    val sol = Solution_42628()
    print(sol.solution(arrayOf("I 7","I 5","I -5","D -1")).contentToString())

    //print(sol.solution(arrayOf("I 16","D 1")).contentToString())
}