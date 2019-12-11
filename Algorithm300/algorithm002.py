# coding=utf-8

# author:chen gang
# E-mail:gang.f.chen@qq.com
# date: 2019/12/10 10:29 上午

class Solution:
    def isPerfectSquare(self, num):
        l = 0
        r = num
        while (r - l > 1):
            mid = (l + r) / 2
            if (mid * mid <= num):
                l = mid
            else:
                r = mid
        ans = l
        if (l * l < num):
            ans = r
        return ans * ans == num
#主函数
if __name__ == '__main__':
    num = 23
    print("初始值：", num)
    solution = Solution()
    print("结果：", solution.isPerfectSquare(num))
