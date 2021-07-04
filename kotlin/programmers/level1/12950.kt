class Solution_12950 {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        var answer = arrayOf<IntArray>()

//        arr1.forEachIndexed{ i: Int, ints: IntArray ->
//            var newarr = intArrayOf()
//            ints.forEachIndexed { j, num ->
//                newarr+=(num+arr2[i][j])
//            }
//            answer+=newarr
//        }
        answer = arr1.mapIndexed{ indexArr, ints ->
            ints.mapIndexed{ indexInts, i ->
                i + arr2[indexArr][indexInts]
            }.toIntArray()
        }.toTypedArray()
        return answer
    }
}

fun main() {
    var arr1 = arrayOf(intArrayOf(1, 2), intArrayOf(2, 3))
    var arr2 = arrayOf(intArrayOf(3, 4), intArrayOf(5, 6))

    val sol = Solution_12950()
    print(sol.solution(arr1, arr2))
}