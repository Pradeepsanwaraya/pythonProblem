coding=set()
robotics=set()

while True:
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        student=input("Enter Student ID: ")
        coding.add(student)

    elif choice==2:
        student=input("Enter Student ID: ")
        robotics.add(student)

    elif choice==3:
        print(coding)

    elif choice==4:
        print(robotics)

    elif choice==5:
        print(coding.intersection(robotics))

    elif choice==6:
        print(coding.difference(robotics))

    elif choice==7:
        print(robotics.difference(coding))

    elif choice==8:
        print(coding.union(robotics))

    elif choice==9:
        print(len(coding.union(robotics)))

    elif choice==10:
        break

    else:
        print("Invalid Choice")



class Solution(object):
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])
        copy = [row[:] for row in board]

        for i in range(rows):
            for j in range(cols):
                live = 0

                for r in range(max(0, i - 1), min(rows, i + 2)):
                    for c in range(max(0, j - 1), min(cols, j + 2)):
                        if (r, c) != (i, j) and copy[r][c] == 1:
                            live += 1

                if copy[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, word in zip(pattern, words):
            if ch in char_to_word and char_to_word[ch] != word:
                return False
            if word in word_to_char and word_to_char[word] != ch:
                return False
            char_to_word[ch] = word
            word_to_char[word] = ch

        return True



class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        # prefix_count[s] = how many times prefix sum s appeared on the current root-to-node path
        prefix_count = {0: 1}  # empty prefix, so paths starting at root are counted

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val

            # How many earlier prefixes make a path ending here sum to targetSum?
            count = prefix_count.get(curr_sum - targetSum, 0)

            # Add current prefix for the children
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # Backtrack: remove current prefix when leaving this node
            prefix_count[curr_sum] -= 1

            return count

        return dfs(root, 0)

class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)

            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and neighbour not in visited:
                    dfs(neighbour)

        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces += 1

        return provinces

class Solution(object):
    def groupAnagrams(self, strs):
        result = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in result:
                result[key] = []

            result[key].append(s)

        return list(result.values())