# coding=set()
# robotics=set()

# while True:
#     print("1. Add Student to Coding Club")
#     print("2. Add Student to Robotics Club")
#     print("3. Display Students in Coding Club")
#     print("4. Display Students in Robotics Club")
#     print("5. Find Students in Both Clubs")
#     print("6. Find Students Only in Coding Club")
#     print("7. Find Students Only in Robotics Club")
#     print("8. Display All Unique Club Members")
#     print("9. Display Total Unique Club Members")
#     print("10. Exit")

#     choice=int(input("Enter choice: "))

#     if choice==1:
#         student=input("Enter Student ID: ")
#         coding.add(student)

#     elif choice==2:
#         student=input("Enter Student ID: ")
#         robotics.add(student)

#     elif choice==3:
#         print(coding)

#     elif choice==4:
#         print(robotics)

#     elif choice==5:
#         print(coding.intersection(robotics))

#     elif choice==6:
#         print(coding.difference(robotics))

#     elif choice==7:
#         print(robotics.difference(coding))

#     elif choice==8:
#         print(coding.union(robotics))

#     elif choice==9:
#         print(len(coding.union(robotics)))

#     elif choice==10:
#         break

#     else:
#         print("Invalid Choice")



# class Solution(object):
#     def gameOfLife(self, board):
#         rows = len(board)
#         cols = len(board[0])
#         copy = [row[:] for row in board]

#         for i in range(rows):
#             for j in range(cols):
#                 live = 0

#                 for r in range(max(0, i - 1), min(rows, i + 2)):
#                     for c in range(max(0, j - 1), min(cols, j + 2)):
#                         if (r, c) != (i, j) and copy[r][c] == 1:
#                             live += 1

#                 if copy[i][j] == 1:
#                     if live < 2 or live > 3:
#                         board[i][j] = 0
#                 else:
#                     if live == 3:
#                         board[i][j] = 1


# class Solution(object):
#     def wordPattern(self, pattern, s):
#         """
#         :type pattern: str
#         :type s: str
#         :rtype: bool
#         """
#         words = s.split()
#         if len(pattern) != len(words):
#             return False

#         char_to_word = {}
#         word_to_char = {}

#         for ch, word in zip(pattern, words):
#             if ch in char_to_word and char_to_word[ch] != word:
#                 return False
#             if word in word_to_char and word_to_char[word] != ch:
#                 return False
#             char_to_word[ch] = word
#             word_to_char[word] = ch

#         return True



# class Solution(object):
#     def pathSum(self, root, targetSum):
#         """
#         :type root: Optional[TreeNode]
#         :type targetSum: int
#         :rtype: int
#         """
#         # prefix_count[s] = how many times prefix sum s appeared on the current root-to-node path
#         prefix_count = {0: 1}  # empty prefix, so paths starting at root are counted

#         def dfs(node, curr_sum):
#             if not node:
#                 return 0

#             curr_sum += node.val

#             # How many earlier prefixes make a path ending here sum to targetSum?
#             count = prefix_count.get(curr_sum - targetSum, 0)

#             # Add current prefix for the children
#             prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

#             count += dfs(node.left, curr_sum)
#             count += dfs(node.right, curr_sum)

#             # Backtrack: remove current prefix when leaving this node
#             prefix_count[curr_sum] -= 1

#             return count

#         return dfs(root, 0)

# class Solution(object):
#     def findCircleNum(self, isConnected):
#         n = len(isConnected)
#         visited = set()
#         provinces = 0

#         def dfs(city):
#             visited.add(city)

#             for neighbour in range(n):
#                 if isConnected[city][neighbour] == 1 and neighbour not in visited:
#                     dfs(neighbour)

#         for city in range(n):
#             if city not in visited:
#                 dfs(city)
#                 provinces += 1

#         return provinces

# class Solution(object):
#     def groupAnagrams(self, strs):
#         result = {}

#         for s in strs:
#             key = ''.join(sorted(s))

#             if key not in result:
#                 result[key] = []

#             result[key].append(s)

#         return list(result.values())



# class Solution(object):
#     def rightSideView(self, root):
#         if not root:
#             return []

#         queue = [root]
#         result = []

#         while queue:
#             size = len(queue)

#             for i in range(size):
#                 node = queue.pop(0)

#                 if node.left:
#                     queue.append(node.left)

#                 if node.right:
#                     queue.append(node.right)

#                 if i == size - 1:
#                     result.append(node.val)

#         return result
# class Solution(object):
#     def goodNodes(self, root):
#         def dfs(node, maximum):
#             if node is None:
#                 return 0

#             count = 0

#             if node.val >= maximum:
#                 count = 1

#             maximum = max(maximum, node.val)

#             count += dfs(node.left, maximum)
#             count += dfs(node.right, maximum)

#             return count

#         return dfs(root, root.val)




# class Solution(object):
#     def goodNodes(self, root):
#         def dfs(node, maximum):
#             if node is None:
#                 return 0

#             count = 0

#             if node.val >= maximum:
#                 count = 1

#             maximum = max(maximum, node.val)

#             count += dfs(node.left, maximum)
#             count += dfs(node.right, maximum)

#             return count

#         return dfs(root, root.val)

# class Solution(object):
#     def goodNodes(self, root):
#         def dfs(node, maximum):
#             if node is None:
#                 return 0

#             count = 0

#             if node.val >= maximum:
#                 count = 1

#             maximum = max(maximum, node.val)

#             count += dfs(node.left, maximum)
#             count += dfs(node.right, maximum)

#             return count

#         return dfs(root, root.val)

# class Solution(object):
#     def isHappy(self, n):
#         seen = []

#         while n != 1:
#             if n in seen:
#                 return False

#             seen.append(n)
#             total = 0

#             while n > 0:
#                 digit = n % 10
#                 total = total + digit * digit
#                 n = n // 10

#             n = total

#         return True

# QNO 1:
# table salses
# =========================================================
# | Column         | Data Type                               |
# | -------------- | --------------------------------------- |
# | sale_id        | INT                                     |
# | customer_name  | VARCHAR(50)                             |
# | city           | VARCHAR(30)                             |
# | category       | VARCHAR(30)                             |
# | product        | VARCHAR(50)                             |
# | quantity       | INT                                     |
# | price          | DECIMAL(10,2)                           |
# | discount       | DECIMAL(10,2)                           |
# | sale_date      | DATE                                    |
# | payment_method | ENUM('UPI','Card','Cash','Net Banking') |
# | status         | ENUM('Completed','Pending','Cancelled') |
# | customer_type  | ENUM('New','Regular','Premium')         |
# =========================================================


# INSERT INTO sales
# (customer_name, city, category, product, quantity, price, discount, sale_date, payment_method, status, customer_type)
# VALUES
# ('Rahul','Indore','Electronics','Laptop',2,60000,5000,'2026-01-05','Card','Completed','Premium'),
# ('Priya','Bhopal','Electronics','Mobile',3,25000,3000,'2026-01-07','UPI','Completed','Regular'),
# ('Amit','Indore','Clothing','Jeans',5,2000,500,'2026-01-10','Cash','Completed','New'),
# ('Sneha','Mumbai','Beauty','Cream',8,800,400,'2026-01-12','UPI','Completed','Premium'),
# ('Rohit','Pune','Electronics','Laptop',1,55000,4000,'2026-01-15','Card','Completed','Regular'),
# ('Neha','Delhi','Clothing','Kurti',6,1800,600,'2026-01-17','UPI','Completed','Premium'),
# ('Karan','Indore','Sports','Bat',4,3500,700,'2026-01-20','Cash','Completed','Regular'),
# ('Pooja','Bhopal','Beauty','Lipstick',10,600,300,'2026-01-22','UPI','Completed','New'),
# ('Vikas','Delhi','Books','SQL Book',7,900,200,'2026-01-25','Net Banking','Completed','Regular'),
# ('Anjali','Mumbai','Electronics','Watch',3,7000,800,'2026-01-27','Card','Completed','Premium'),
# ('Saurabh','Pune','Grocery','Rice',12,900,500,'2026-02-01','UPI','Completed','Regular'),
# ('Riya','Delhi','Electronics','AC',2,45000,5000,'2026-02-03','Card','Completed','Premium'),
# ('Manish','Indore','Clothing','Shirt',6,1500,300,'2026-02-05','UPI','Completed','New'),
# ('Komal','Bhopal','Furniture','Chair',3,8000,1000,'2026-02-07','Cash','Completed','Premium'),
# ('Deepak','Mumbai','Electronics','Speaker',5,3000,500,'2026-02-12','Card','Cancelled','Regular');




# Questions===>
# # Find the total number of completed sales for each city where quantity is greater than 2. Display cities in descending order of sales count.
# mysql> select city,count(*) from employees where quantity>2 and status ='completed' group by city order by count(*) desc;
# ERROR 1146 (42S02): Table 'shop.employees' doesn't exist
# mysql> select city,count(*) from sales where quantity>2 and status ='completed' group by city order by count(*) desc;
# +--------+----------+
# | city   | count(*) |
# +--------+----------+
# | Bhopal |        3 |
# | Indore |        3 |
# | Mumbai |        2 |
# | Delhi  |        2 |
# | Pune   |        1 |
# +--------+----------+
# 5 rows in set (0.02 sec)
# Find the total quantity sold for each category where discount is greater than 300. Display highest quantity first.
# Find the total sales amount for each city for completed sales only. Display highest-selling city first.
# mysql> select category,count(*) as co from sales where discount>300 group by category order by co desc;
# +-------------+----+
# | category    | co |
# +-------------+----+
# | Electronics |  6 |
# | Clothing    |  2 |
# | Beauty      |  1 |
# | Sports      |  1 |
# | Grocery     |  1 |
# | Furniture   |  1 |
# +-------------+----+
# 6 rows in set (0.00 sec)
# # Find the average product price for each category where quantity is at least 3. Display categories by average price descending.
# mysql> select category,avg(price) as av from sales where quantity>=3 group by category order by av desc;
# +-------------+--------------+
# | category    | av           |
# +-------------+--------------+
# | Electronics | 11666.666667 |
# | Furniture   |  8000.000000 |
# | Sports      |  3500.000000 |
# | Clothing    |  1766.666667 |
# | Books       |   900.000000 |
# | Grocery     |   900.000000 |
# | Beauty      |   700.000000 |
# +-------------+--------------+
# 7 rows in set (0.02 sec)
#
# Find the number of sales for each customer type where the order amount (quantity * price) is greater than 5000. Sort by number of sales descending.
# mysql> select customer_type,count(*) as co from sales where (quantity*price) >5000 group by customer_type order by co desc;
# +---------------+----+
# | customer_type | co |
# +---------------+----+
# | Premium       |  6 |
# | Regular       |  6 |
# | New           |  3 |
# +---------------+----+
# 3 rows in set (0.00 sec)
# Find the total discount given for each city for UPI transactions. Display highest discount first.
# mysql> SELECT city, COUNT(discount) AS co
#     -> FROM sales
#     -> GROUP BY city
#     -> ORDER BY co DESC;
# +--------+----+
# | city   | co |
# +--------+----+
# | Indore |  4 |
# | Bhopal |  3 |
# | Mumbai |  3 |
# | Delhi  |  3 |
# | Pune   |  2 |
# +--------+----+
# 5 rows in set (0.00 sec) 
# # Find the total quantity sold through each payment method for completed transactions. Sort by total quantity descending.
# select payment_method,count(quantity) as qu from sales where status = "completed" group by payment_method order by qu desc; 
# mysql> select payment_method,count(quantity) as qu from sales where status = "completed" group by payment_method order by qu desc;
# +----------------+----+
# | payment_method | qu |
# +----------------+----+
# | upi            |  6 |
# | card           |  4 |
# | cash           |  3 |
# | net banking    |  1 |
# +----------------+----+
# 4 rows in set (0.00 sec)
# Find the average discount for each category where quantity is greater than 4. Display highest average discount first.
select category,avg(discount) as dis from sales where quantity>4 group by category order by dis desc;

mysql> select category,avg(discount) as dis from sales where quantity>4 group by category order by dis desc;
+-------------+------------+
| category    | dis        |
+-------------+------------+
| Grocery     | 500.000000 |
| Electronics | 500.000000 |
| Clothing    | 466.666667 |
| Beauty      | 350.000000 |
| Books       | 200.000000 |
+-------------+------------+
5 rows in set (0.00 sec)

# Find the maximum product price for each city where the status is Completed. Sort by maximum price descending.
# Find the minimum product price for each category where discount is greater than 300. Sort by minimum price ascending.
# Find cities having more than 2 completed sales. Sort cities by completed sales count descending.
# Find categories having total quantity greater than 10. Sort by total quantity descending.
# Find cities having total sales greater than 50,000. Sort by total sales descending.
# Find customer types having average product price greater than 10,000. Sort by average price descending.
# Find categories having average discount greater than 400. Sort by average discount descending.
# Find payment methods having more than 2 completed transactions. Sort by transaction count descending.
# Find cities where the maximum product price is greater than 20,000. Sort by maximum price descending.
# Find categories where the minimum product price is less than 2,000. Sort by minimum price ascending.
# Find customer types where total discount is greater than 2,000. Sort by total discount descending.
# Find cities where average quantity per transaction is greater than 4. Sort by average quantity descending.
# Find each city’s total sales for completed UPI transactions where quantity is greater than 2. Display only cities having total sales greater than 10,000.
# Find each category’s total quantity for completed transactions where discount is greater than 300. Display only categories having total quantity greater than 5.
# Find each customer type’s average price for completed transactions where quantity >= 2. Display only customer types whose average price exceeds 10,000.
# Find each city’s total discount for UPI transactions where quantity > 3. Display cities having total discount greater than 500.
# Find each category’s total sales where payment method is UPI or Card and status is Completed. Display categories having total sales greater than 10,000.
# Find each city’s transaction count for January 2026 completed transactions. Display cities having at least 2 transactions.
# Find each category’s average sales amount where quantity >= 3 and status = Completed. Display categories whose average sales amount is greater than 5,000.
# Find each customer type’s maximum price where payment method is Card and status is Completed. Display only customer types whose maximum price exceeds 20,000.
# Find each city’s total quantity for Electronics and Clothing products where status is Completed. Display cities having total quantity greater than 5.
# Find each payment method’s total sales where status is Completed and discount is greater than 400. Display payment methods having total sales greater than 20,000.
# Find cities having more than 2 completed transactions and total sales greater than 50,000. Sort by total sales descending.
# Find categories having total quantity greater than 8 and average price greater than 2,000. Sort by total quantity descending.
# Find customer types having more than 2 transactions and total discount greater than 2,000. Sort by total discount descending.
# Find cities having average quantity greater than 3 and maximum product price greater than 20,000. Sort by average quantity descending.
# Find categories having more than 2 completed transactions and total sales greater than 20,000. Sort by total sales descending.
# Find payment methods having more than 2 completed transactions and average price greater than 10,000. Sort by average price descending.
# Find cities having total quantity greater than 8 and average discount greater than 300. Sort by total quantity descending.
# Find customer types having average price greater than 5,000 and total quantity greater than 8. Sort by total quantity descending.
# Find categories having minimum price below 2,000 and maximum price above 20,000. Sort by maximum price descending.
# Find cities having total discount greater than 1,000 and total sales greater than 30,000. Sort by total sales descending.
# Find the top 3 cities based on total sales, considering only completed transactions with quantity greater than 1 and displaying only cities having more than 1 transaction.
# Find the top 3 categories based on total quantity where discount is greater than 300 and total quantity is greater than 5.
# Find the top 3 customer types based on average sales amount where status is Completed and transaction count is greater than 1.
# Find the top 3 cities based on total discount for UPI transactions where status is Completed and total discount is greater than 500.
# Find the top 3 categories based on total sales where quantity is greater than 2, average price is greater than 1,000, and total sales exceeds 10,000.
# Find the top 3 cities based on average order value where status is Completed, total quantity is greater than 5, and transaction count is greater than 1.
# Find the second-highest city based on total sales after considering only completed transactions and cities having at least 2 transactions.
# Find the third-highest category based on total quantity where quantity is greater than 2 and total discount exceeds 500.
# Find the 2nd and 3rd highest customer types based on total sales where status is Completed and average price is greater than 5,000.
# Find the top 3 cities where:
# status is Completed
# payment method is UPI or Card
# quantity is greater than 1
# number of transactions is greater than 1
# total quantity is greater than 5
# total sales is greater than 20,000


class Solution(object):
    def maxLevelSum(self, root):
        queue = [root]
        level = 0
        max_sum = float('-inf')
        ans = 0

        while queue:
            level += 1
            total = 0

            for i in range(len(queue)):
                node = queue.pop(0)
                total += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if total > max_sum:
                max_sum = total
                ans = level

        return ans
