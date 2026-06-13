class Solution:
    def climbStairs(self, n: int) -> int:
        store={1:1,2:2}
        def f(x):
            if x in store:
                return store[x]
            else:
                store[x]=f(x-1)+f(x-2)
            return store[x]
        return f(n)
    