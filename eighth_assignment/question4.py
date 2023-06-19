class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructBinaryTree(s):
    def helper(s, start):
        # Check if there are no more characters or if it's an empty tree represented by '()'
        if start >= len(s) or s[start] == ')':
            return None, start
        
        # Find the value of the current node
        end = start
        while end < len(s) and s[end] not in ['(', ')']:
            end += 1
        val = int(s[start:end])

        # Create the current node
        node = TreeNode(val)

        # Process the left child
        if end < len(s) and s[end] == '(':
            node.left, end = helper(s, end + 1)

        # Process the right child
        if end < len(s) and s[end] == '(':
            node.right, end = helper(s, end + 1)

        return node, end + 1

    root, _ = helper(s, 0)
    return root


s = "4(2(3)(1))(6(5))"
root = constructBinaryTree(s)