package programmers_level1

class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var relost = lost.toCollection(ArrayList())
        var rereserve = reserve.toCollection(ArrayList())
        var answer = 0
        var check = Array(n+1){i->true}

        for(i in 1..n){
            if(relost.contains(i) && !rereserve.contains(i)) {
                check[i] = false
            }
            else if(relost.contains(i) && rereserve.contains(i)){
                rereserve.remove(i)
            }
        }

        for(i in 1..n){
            if(!check[i]){
                if(i!=1 && rereserve.contains(i-1)){
                    check[i] = true
                    rereserve.remove(i-1)
                    answer+=1
                }
                else if(i!=n && rereserve.contains(i+1)){
                    check[i] = true
                    rereserve.remove(i+1)
                    answer+=1
                }
            }
            else{
                answer+=1
            }

        }
        check[0] = false

        return answer
    }

}
fun main(){
    var sol = Solution()
    val arr1 = intArrayOf(2,4)
    val arr2 = intArrayOf(1,3,5)

    var result = sol.solution(5, arr1, arr2)
    print(result)
}