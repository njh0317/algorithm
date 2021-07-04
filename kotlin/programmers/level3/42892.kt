class Solution_42892 {
    fun solution(nodeinfo: Array<IntArray>): Array<IntArray> {
        var answer = arrayOf<IntArray>()

        val list = ArrayList<Point>()

        for(i in nodeinfo.indices){
            val info = nodeinfo[i]
            list.add(Point(info[0], info[1], i+1))
        }
        list.sort()

        val binary = Binary(Node(list[0]))

        for (i in 1 until list.size){
            binary.insert(list[i])
        }

        binary.preOrder(binary.root)
        binary.postOrder(binary.root)

        answer+=binary.preList.toIntArray()
        answer+=binary.postList.toIntArray()
        return answer
    }
}
class Node(val point: Point){
    var left: Node? = null
    var right: Node? = null
}

class Binary(val root: Node){
    val preList = ArrayList<Int>()
    val postList = ArrayList<Int>()
    fun insert(point: Point){
        find(root, point)
    }
    fun find(parent: Node, point: Point){
        if(point.x < parent.point.x){
            if(parent.left == null){
                parent.left = Node(point)
            }
            else{
                find(parent.left!!, point)
            }
        }
        else{
            if(parent.right == null){
                parent.right = Node(point)
            }
            else{
                find(parent.right!!, point)
            }
        }
    }

    fun preOrder(node: Node){
        preList.add(node.point.num)
        node.left?.let {
            preOrder(it)
        }
        node.right?.let {
            preOrder(it)
        }
    }

    fun postOrder(node: Node){
        node.left?.let {
            postOrder(it)
        }
        node.right?.let{
            postOrder(it)
        }
        postList.add(node.point.num)
    }
}
class Point(val x: Int, val y: Int, val num: Int) :Comparable<Point>
{
    override fun compareTo(other: Point): Int {
        if(this.y > other.y) return -1
        else if(this.y == other.y){
            if(this.x < other.x) return -1
        }
        return 1
    }

}
fun main() {
    val sol = Solution_42892()
    print(sol.solution(arrayOf(intArrayOf(5,3), intArrayOf(11, 5), intArrayOf(13, 3), intArrayOf(3, 5), intArrayOf(6, 1), intArrayOf(1, 3), intArrayOf(8, 6), intArrayOf(7, 2), intArrayOf(2, 2))).contentDeepToString())
}