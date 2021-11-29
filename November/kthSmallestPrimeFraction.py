# _*_ coding = utf-8 _*_
# created by czq on 2021/11/29


# 题目786：
#
# 给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 素数  组成，且其中所有整数互不相同。
#
# 对于每对满足 0 < i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。
#
# 那么第 k 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == arr[j] 。


# 题解1：
# 思路：这个题目是典型的topk问题，可以使用堆解决，对于浮点数的问题，我们可以换一种角度思考，arr[i1] * arr[j0] < arr[j1] * arr[i0]就等价于大小的关系
# 但是要对heapq进行改造，使得堆支持[arr[i], arr[j]]的相关规则


def kthSmallestPrimeFraction(self, arr, k: int):
    def heappush(heap, item):
        """Push item onto heap, maintaining the heap invariant."""
        heap.append(item)
        _siftdown(heap, 0, len(heap) - 1)

    def _siftdown(heap, startpos, pos):
        newitem = heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if newitem[0] * parent[1] > parent[0] * newitem[1]:
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = newitem

    def heappop(heap):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            _siftup(heap, 0)
            return returnitem
        return lastelt

    def _siftup(heap, pos):
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2 * pos + 1  # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not heap[childpos][0] * heap[rightpos][1] > heap[rightpos][0] * heap[childpos][1]:
                childpos = rightpos
            # Move the smaller child up.
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2 * pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        heap[pos] = newitem
        _siftdown(heap, startpos, pos)

    n = len(arr)
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            if len(ans) == k:
                if arr[i] * ans[0][1] < arr[j] * ans[0][0]:
                    heappop(ans)
                    heappush(ans, [arr[i], arr[j]])
            else:
                heappush(ans, [arr[i], arr[j]])
    return ans[0]
