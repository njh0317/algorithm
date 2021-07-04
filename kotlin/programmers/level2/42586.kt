import java.util.*

class Solution_42586 {
    lateinit var queue: Queue<Int>
    fun calculate_day(nowprog: Int, speed: Int): Int{ //작업이 완료될 때 까지 날 수를 계산
        val lastprogress = 100-nowprog
        when {
            lastprogress%speed == 0 -> return lastprogress/speed
            else -> return lastprogress/speed+1
        }
    }
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer = intArrayOf()
        queue = LinkedList()
        progresses.forEachIndexed { index, i ->
            queue.add(calculate_day(i, speeds[index]))
        }

        while(queue.peek() != null){
            val first_num = queue.poll()
            var cnt = 1
            while(queue.peek()!= null && first_num>=queue.peek()){
                queue.poll()
                cnt+=1
            }
            answer+=cnt

        }


        return answer
    }
}

fun main() {
    val sol = Solution_42586()
    val progresses = intArrayOf(95, 90, 99, 99, 80, 99)
    val speeds = intArrayOf(1, 1, 1, 1, 1, 1)

    print(sol.solution(progresses,speeds).contentToString())
}