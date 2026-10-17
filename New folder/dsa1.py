
# # class Solution(object):
# #     def lowestCommonAncestor(self, root, p, q):
# #         if root is None or root == p or root == q:
# #             return root

# #         left = self.lowestCommonAncestor(root.left, p, q)
# #         right = self.lowestCommonAncestor(root.right, p, q)

# #         if left and right:
# #             return root

# #         return left if left else right
# s = "python"
# result = sort(s)
# print(result)
# s = "python"

# result = sorted(s)

# print(result)
class Solution(object):
    def pairSum(self, head):
        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        max_sum = 0
        left = 0
        right = len(values) - 1

        while left < right:
            total = values[left] + values[right]
            max_sum = max(max_sum, total)
            left += 1
            right -= 1

        return max_sum