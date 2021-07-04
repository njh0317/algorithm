class Solution_42842 {
    fun calculate_brown(num1: Int, num2: Int) = (num1+1)*2 + (num2+1)*2
    fun solution(brown: Int, yellow: Int): IntArray {
        var answer = intArrayOf()
        for(i in 1 .. yellow){
            val diviend = yellow
            val divisor = i
            if(diviend%divisor == 0){
                val quotient = yellow/divisor
                if(calculate_brown(quotient, divisor) == brown){
                    answer+=(quotient+2)
                    answer+=(divisor+2)
                    break
                }
            }
        }
        return answer
    }
}

fun main() {
    val sol = Solution_42842()

    print(sol.solution(24, 24).contentToString())
}