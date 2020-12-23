# class Human:
#     def __init__(self, n, o):
#         self.name = n
#         self.occupation = o
#
#     def what_do(self):
#         if self.occupation == 'tennis':
#             print (self.name, "plays tennis")
#         elif self.occupation == 'actor':
#             print (self.name, "stars in movies")
#
#
# class jew(Human):
#     def isjew(self):
#         print (self.name, 'is a jew')
#
# def create_class():
#     tom = Human('tom cruise', 'actor')
#     tom.what_do()
#     haim = jew('haim', 'actor')
#     haim.isjew()
#     haim.what_do()

class TreeNode:
    def __init__(self, data, position):
        self.data = data
        self.children = []
        self.parent = None
        self.position = position

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, what, level):
        output = ""
        if ((what == 'name') or (what == 'both')):
            output = output + self.data + " "
        if ((what == 'position') or (what == 'both')):
            output = output + "(" +self.position + ")"

        spaces = " "*self.get_level()*4
        prefix = spaces + "|___" if self.parent else ""
        print(prefix, output)
        if self.children:
            for child in self.children:
                if self.get_level() < level:
                    child.print_tree(what, level)

def create_class():
    root = TreeNode("Nilpol", "CEO")


    Chinmay = TreeNode("Chinmay", "CTO")
    Vishwa = TreeNode("Vishwa", "Infrastructure Head")
    Vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    Vishwa.add_child(TreeNode("Abhijit", "App Manager"))
    Aamir = TreeNode("Aamir", "Application head")
    Chinmay.add_child(Vishwa)
    Chinmay.add_child(Aamir)

    Gels = TreeNode("Gels", "HR head")
    Gels.add_child(TreeNode("Peter", "Recruitment Manager"))
    Gels.add_child(TreeNode("Waqas", "Policy Manager"))


    root.add_child(Chinmay)
    root.add_child(Gels)

    return root

if __name__ == '__main__':
    root = create_class()
    #choice = input("Enter choice: name, position or both ")
    root.print_tree("both", 5)
