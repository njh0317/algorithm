import java.util.*

class Solution_42587 {
    lateinit var queue: Queue<Pair<Int, Int>>
    fun solution(priorities: IntArray, location: Int): Int {
        var answer = 0

        queue = LinkedList<Pair<Int, Int>>() //index, 우선순위

        priorities.forEachIndexed{ index: Int, value: Int ->
            queue.add(Pair(index, value))
        }

        while(queue.peek()!=null){
            val (index, value) = queue.poll()
            val queue_size = queue.size
            var flag = false

            for(i in 0 until queue_size){
                val (nextindex, nextvalue) = queue.poll()
                if(nextvalue>value) flag = true //더 높은 우선순위가 있으면 true로 표시
                queue.add(Pair(nextindex, nextvalue))
            }
            if(flag){//더 높은 우선순위가 있으면
                queue.add(Pair(index, value))
            }
            else{
                answer+=1
                if(index == location) break
            }

        }

        return answer
    }
}

fun main() {
    val sol = Solution_42587()
    val priorities = intArrayOf(1, 1, 9, 1, 1, 1)

    print(sol.solution(priorities, 0))
}