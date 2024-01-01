class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    @staticmethod
    def iterative_find(node, target):
        cur = node
        while cur is not None and cur.val != target:
            if target < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return cur

    @staticmethod
    def recursive_find(node, target):
        if node is None:
            return None
        if node.val == target:
            return target
        if target > node.val:
            return TreeNode.recursive_find(node.right, target)
        else:
            return TreeNode.recursive_find(node.left, target)

    @staticmethod
    def bfs(node):
        """
        BFS level order traversal
        :param node:
        :return:
        """
        if node is None:
            return []

        queue = []
        nums = []
        queue.append(node)

        while queue:
            node = queue.pop(0)
            nums.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return nums

    @staticmethod
    def dfs_inorder_helper(node, queue):
        if node is None:
            return
        TreeNode.dfs_inorder_helper(node.left, queue)
        queue.append(node.val)
        TreeNode.dfs_inorder_helper(node.right, queue)

    @staticmethod
    def dfs(node):
        """
        DFS in order traversal
        :param node:
        :return:
        """
        queue = []
        TreeNode.dfs_inorder_helper(node, queue)
        return queue


if __name__ == "__main__":
    root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(7)), TreeNode(29, TreeNode(11), TreeNode(30)))

    print(TreeNode.iterative_find(root, 29))

    print(TreeNode.iterative_find(root, 909))

    print(TreeNode.recursive_find(root, 29))

    print(TreeNode.recursive_find(root, 909))

    print(TreeNode.dfs(root))

    print(TreeNode.bfs(root))
