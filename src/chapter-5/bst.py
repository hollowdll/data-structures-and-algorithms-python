# Binary search tree

class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'

class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """
        # Let's use a couple of pointers to traverse the tree
        # following BST rules and find the parent of the node
        # to be inserted
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node variable is parent node or None if Tree is empty
        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                # If tree is empty, just make the new node the root node
                self._root_node = new_node
            else:
                # If tree is not empty and parent_node is None,
                # probably is an error.
                raise(ValueError)
        elif new_node.data < parent_node.data:
            # If value of new node is smaller than parent's, add new node to its left
            parent_node._left_child = new_node
        else:
            # If value of new node is bigger than parent's, add new node to its right
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        
        current_node = self._root_node
        while current_node:
            if data == current_node.data:
                return current_node
            
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        return None
    
    def find_minimum(self):
        """
        Returns the node containing the minimum value of the tree
        """
        
        current_node = self._root_node
        while current_node:
            if current_node._left_child is None:
                return current_node
            
            current_node = current_node._left_child

        return None

    def find_maximum(self):
        """
        Returns the node containing the maximum value of the tree
        """
        
        current_node = self._root_node
        while current_node:
            if current_node._right_child is None:
                return current_node
            
            current_node = current_node._right_child

        return None
    
    def _detach_node(self, node):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        An error will be raised otherwise.
        """
        
        if node._left_child and node._right_child:
            raise(ValueError('Node has two children'))
        
        parent = node._parent
        if node._left_child:
            child = node._left_child
        else:
            child = node._right_child

        if not parent and not child:
            self._root_node = None
            return None
        
        if parent:
            if parent._left_child == node:
                parent._left_child = child
            elif parent._right_child == node:
                parent._right_child = child

        if child:
            if not parent:
                self._root_node = child
            child._parent = parent

    def delete_node(self, data):
        """
        Delete the node containing the data.

        The algorithm is based on this: https://en.wikipedia.org/wiki/Binary_search_tree#Deletion

        Parameters:
        - 'data': The data to be found.
        """
        node_to_remove = self._find(data)
        if not node_to_remove:
            return
        
        if not node_to_remove._left_child:
            self.__shift_nodes(node_to_remove, node_to_remove._right_child)
        elif not node_to_remove._right_child:
            self.__shift_nodes(node_to_remove, node_to_remove._left_child)
        else:
            successor = self.__bst_successor(node_to_remove)
            if successor._parent != node_to_remove:
                self.__shift_nodes(successor, successor._right_child)
                successor._right_child = node_to_remove._right_child
                successor._right_child._parent = successor

            self.__shift_nodes(node_to_remove, successor)
            successor._left_child = node_to_remove._left_child
            successor._left_child._parent = successor
    
    def __shift_nodes(self, node, right_node):
        """
        Shifts nodes in the BST.
        """
        if not node._parent:
            self._root_node = right_node
        elif node == node._parent._left_child:
            node._parent._left_child = right_node
        else:
            node._parent._right_child = right_node

        if right_node:
            right_node._parent = node._parent

    def __bst_successor(self, node):
        """
        Finds the successor node of a node.
        """
        current = node._right_child
        while current and current._left_child:
            current = current._left_child

        return current
    
    def __bst_successor_full(self, node):
        if node._right_child:
            current = node._right_child
            while current._left_child:
                current = current._left_child

            return current
        
        # if node doesn't have right child
        parent = node._parent
        current = node
        while parent and current == parent._right_child:
            current = parent
            parent = parent._parent

        return parent
