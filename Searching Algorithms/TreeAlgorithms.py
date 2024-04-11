class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_left(self, new_left):
        self.left = new_left

    def set_right(self, new_right):
        self.right = new_right
    

class BinaryTree:
    def __init__(self):
        self.root = None
    

    '''
        Level Order Traversal: -> nodes are added level by level, left to right from top to bottom.
        1) If the tree is empty, the new node becomes the root of the tree.
        2) If the tree is not empty, the code uses a queue to keep track of of the nodes at the current level.
        3) The code dequeues a node from the front of the queue, and checks if it has a left child. If not, the new node
            becomes the left child of the current node.
        4) If the current node has a left child, the child is enqueued onto the queue.
        5) The code checks if the code has a right child. If not, the new node becomes the right child of the current node.
        6) If the current node has a right child, the right child is enqueued onto the queue.
        7) The process continues until the new node is inserted.
    '''
    def insert_level_order(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if not current_node.get_left():
                current_node.set_left(new_node)
                return
            else:
                queue.append(current_node.get_left())
            
            if not current_node.get_right():
                current_node.set_right(new_node)
                return
            else:
                queue.append(current_node.get_right())


    '''
        In Order Traversal: -> This method is used for constructing Binary Search Trees. order (left subtree, root, right subree)
        1) If the tree is empty, the new node becomes the root of the tree.
        2) If the tree is not empty, the current node is set to the root of the tree.
        3) The code then starts an infinite loop. 
        4) If the data to be inserted is less than the data in the current node and the current node doesn't have a left node,
            the new data becomes the left node of the current_node. But, if the current node has a left node, the current node 
            becomes the left node and the loop continues.
        5) If the data to be inserted is greater than or equal to the data in the current node and the current node doesn't have
            a right node, the new data becomes the right node of the current_node. But, if the current node has a right node, 
            the current node becomes the right node and the loop continues.
        6) The process continues until the new node is inserted.
    '''
    def insert_inorder(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        
        current_node = self.root
        while True:
            if data < current_node.get_data():
                if not current_node.get_left():
                    current_node.set_left(new_node)
                    break
                current_node = current_node.get_left()
            
            else:
                if not current_node.get_right():
                    current_node.set_right(new_node)
                    break
                current_node = current_node.get_right()
            

    '''
        Pre Order Insertion: order of visiting (root, left subtree, right subtree)
    '''
    def insert_preorder(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        
        stack = [self.root]
        while stack:
            current_node = stack.pop()
            if not current_node.get_left():
                current_node.set_left(data)
                return
            
            else:
                stack.append(current_node.get_right()) # Push right child first
                stack.append(current_node.get_left()) # Then push left child
            

    '''
        Post Order Insertion: order of visiting(left subtree, right sub tree, root)
    '''
    def insert_postorder(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        stack = [self.root]
        while stack:
            current_node = stack.pop()
            if not current_node.left:
                current_node.left = new_node
                return
            
            else:
                stack.append(current_node.left) # Push left child first
                stack.append(current_node.right) # Then push right child


    '''
        Simple Depth First Traveral - DFT uses STACK!!!
    '''
    def depth_first_traversal(self):
        result = []

        if not self.root:
            return result

        stack = [self.root]
        while stack:
            current_node = stack.pop()
            if current_node:
                result.append(current_node.get_data())
                if current_node.get_left():
                    stack.append(current_node.get_left())
                if current_node.get_right():
                    stack.append(current_node.get_right())

        return result
    

    '''
        Simple Breadth First Traversal - BFT uses QUEUE!!!
    '''
    def breadth_first_traversal(self):
        result = []
        
        if not self.root:
            return result
        
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node:
                result.append(current_node.get_data())
                if current_node.get_left():
                    queue.append(current_node.get_left())
                if current_node.get_right():
                    queue.append(current_node.get_right())

        return result