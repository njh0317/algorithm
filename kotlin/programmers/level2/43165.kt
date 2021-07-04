class Solution_43165 {
    var answer = 0
    fun dfs(numbers: IntArray, sum: Int, start: Int, count: Int, target: Int){
        if(start == count){
            if(sum == target){
                answer+=1
            }
        }
        else{
            dfs(numbers, sum+numbers[start], start+1, count, target)
            dfs(numbers, sum+(-1*numbers[start]), start+1, count, target)

        }
    }
    fun solution(numbers: IntArray, target: Int): Int {

        dfs(numbers, 0, 0, numbers.size, target)

        return answer
    }
}
fun main() {
    val sol = Solution_43165()
    var numbers = intArrayOf(1, 1, 1, 1, 1)
    print(sol.solution(numbers, 3))
}