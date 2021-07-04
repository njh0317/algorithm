import java.lang.Integer.min

class Solution_77485 {
    val dc = intArrayOf(1, 0, -1, 0)
    val dr = intArrayOf(0, 1, 0, -1)
    fun solution(rows: Int, columns: Int, queries: Array<IntArray>): IntArray {
        var answer = intArrayOf()
        var arr = Array<Array<Int>>(rows){i -> Array<Int>(columns){j -> (j+1)+i*columns} }

        queries.forEach {
            var (r1, c1, r2, c2) = it
            var now = arr[r1-1][c1-1]
            var nextr = r1+dr[0]-1
            var nextc = c1+dc[0]-1
            var next = intArrayOf(nextr, nextc)
            var dir = 0
            var min_num = -1

            while(true){
                val temp = arr[next[0]][next[1]]
                arr[next[0]][next[1]] = now
                if(min_num == -1) min_num = now
                else min_num = min(min_num, now)
                now = temp
                if(next.contentEquals(intArrayOf(r1-1, c1-1)) || next.contentEquals(intArrayOf(r1-1,c2-1)) || next.contentEquals(intArrayOf(r2-1, c2-1)) || next.contentEquals(intArrayOf(r2-1, c1-1))){

                    dir+=1
                }
                if(dir == 4){
                    break
                }
                next = intArrayOf(next[0]+dr[dir], next[1]+dc[dir])
            }
            answer+=min_num
        }


        return answer
    }
}

fun main() {
    val sol = Solution_77485()
    print(sol.solution(6, 6, arrayOf(intArrayOf(2, 2, 5, 4), intArrayOf(3, 3, 6, 6), intArrayOf(5, 1, 6, 3))))
}