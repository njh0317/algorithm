class Solution_68935 {
    fun make_ternary(n: Int):IntArray{
        var num = n
        var ternary = intArrayOf()
        while(num>=3){
            ternary+=num%3
            num/=3
        }
        ternary+=num
        return ternary.reversedArray()
    }
    fun make_decimal(arr: IntArray): Int{
        var num = 0
        var start = 1

        arr.forEach {
            num+=(it*start)
            start*=3
        }
        return num
    }
    fun solution(n: Int): Int {
        var answer: Int = 0
        answer = make_decimal(make_ternary(n))
        return answer
    }
}

fun main() {
    val sol = Solution_68935()
    print(sol.solution(125))
}