import java.util.*

class Solution_42583 {
    lateinit var queue: Queue<Pair<Int, Int>> //weight, time
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        var answer = 0
        var truck = truck_weights.toCollection(ArrayList())
        queue = LinkedList<Pair<Int, Int>>()
        var truck_sum = 0
        while(truck.size!=0 || queue.size!=0){
            val queue_size = queue.size

            for(i in 0 until queue_size){
                val (w, time) = queue.poll()
                if(time+1!=bridge_length) queue.add(Pair(w, time+1))
                else{
                    truck_sum-=w
                }
            }

            if(truck.size!=0 && truck_sum + truck[0] <= weight){
                queue.add(Pair(truck[0], 0))
                truck_sum+=truck[0]
                truck.removeAt(0)
            }
            answer+=1
        }
        return answer
    }
}

fun main() {
    val sol = Solution_42583()
    print(sol.solution(100, 100, intArrayOf(10)))
}