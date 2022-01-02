class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                 child.print_tree()

def build_tree():
    root = TreeNode("Do action")

    punish = TreeNode("punish")
    accept = TreeNode("accept")
    root.add_child(punish)
    root.add_child(accept)

    punish.add_child(TreeNode("retaliate"))
    punish.add_child(TreeNode("nothing"))

    root.print_tree()
    print("ho")

if __name__ == '__main__':
    build_tree()