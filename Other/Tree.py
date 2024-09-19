class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

def buildTree(inorder: list[int], postorder: list[int]):
    print(f"{inorder} | {postorder} ")
    if len(inorder) ==0 or len(postorder) == 0:
        return None
    val = postorder[-1]
    try:
        index = inorder.index(val)
    except ValueError:
        return None
    print(f"index = {index}")
    T = TreeNode(val=val)
    T.left = buildTree(inorder[0:index],postorder[0:index])
    T.right = buildTree(inorder[index+1:],postorder[index:-1])
    return T

# print(inorder,postorder)
def levelOrder(root:TreeNode):
    if(root is None):
        return
    print(root.val)
    levelOrder(root.left)
    levelOrder(root.right)

T = buildTree(inorder,postorder)
# print(T.val)
levelOrder(T)

if __name__ == '__main__':
    pass