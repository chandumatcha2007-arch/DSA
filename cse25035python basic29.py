class BinaryTreeArray:​

    def __init__(self, size):​

        self.tree = [None] * size​

        self.size = size​

​

# Insert root​

    def set_root(self, data):​

        self.tree[0] = data​

# Set left child​

    def set_left(self, parent_index, data):​

        child_index = 2 * parent_index + 1​

​

        if child_index < self.size:​

            self.tree[child_index] = data​

        else:​

            print("Index out of range!")​

# Set right child​

   def set_right(self, parent_index, data):​

        child_index = 2 * parent_index + 2​

​

        if child_index < self.size:​

            self.tree[child_index] = data​

        else:​

            print("Index out of range!")​ 
