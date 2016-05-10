import random
 
# Definition for a  binary tree node.
# For simplification, we use binary tree to demo the algorithm.
# But any kind of trees, it should work well.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self, ind = 0):
        res = "t"*ind + str(self.val) + "n"
        if self.left == None:   res += "t"*(ind+1) + "None" + "n"
        else:                   res += self.left.__str__(ind+1)
        if self.right == None:   res += "t"*(ind+1) + "None" + "n"
        else:                   res += self.right.__str__(ind+1)
        return res
    def generateRandomBinaryTree(depth = 0):
        guess = random.randint(0,3)
        if guess == 0 or depth == 20:
            return None
        else:
            root = TreeNode(random.randint(1,100))
            root.left = TreeNode.generateRandomBinaryTree(depth+1)
            root.right = TreeNode.generateRandomBinaryTree(depth+1)
            return root
    def CountVisibleNodeRec(root, maxSoFar = None):
        if root == None:        # Empty tree
            return 0
 
        assert isinstance(root, TreeNode)
 
        if maxSoFar == None:    maxSoFar = root.val
 
        if maxSoFar <= root.val:
            return TreeNode.CountVisibleNodeRec(root.left, root.val) +
                   TreeNode.CountVisibleNodeRec(root.right, root.val) +
                   1
        else:
            return TreeNode.CountVisibleNodeRec(root.left, maxSoFar) +
                   TreeNode.CountVisibleNodeRec(root.right, maxSoFar)
    def CountVisibleNodeIte(root):
        if root == None:       # Empty tree
            return 0
        stack = [[root, root.val]]
        count = 0
        while len(stack) != 0:
            current = stack.pop()
            if current[0].val >= current[1]:
                count += 1
 
            maxSoFar = max(current[0].val, current[1])
            if current[0].left != None:
                stack.append([current[0].left, maxSoFar])
            if current[0].right != None:
                stack.append([current[0].right, maxSoFar])
        return count
 
def main():
    # Make the test case
    root = TreeNode.generateRandomBinaryTree()
 
    print "The count of visible nodes is (with recursive method):",
           TreeNode.CountVisibleNodeRec(root)
    print "The count of visible nodes is (with iterative method):",
           TreeNode.CountVisibleNodeIte(root)
 
 
if __name__ == "__main__":
    main()