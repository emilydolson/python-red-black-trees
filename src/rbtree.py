# Implementing Red-Black Tree in Python
# Adapted from https://www.programiz.com/dsa/red-black-tree

import sys
from typing import TypeVar


T = TypeVar('T', bound='Node')


# Node creation
class Node():
    next_id = 0

    def __init__(self: T, item: int) -> None:
        self.id = Node.next_id
        Node.next_id += 1
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
        self.value = None

    def __eq__(self: T, other: T) -> bool:
        return self.id == other.id

    def __repr__(self: T) -> str:
        return "ID: " + str(self.id) + " Value: " + str(self.item)

    def get_color(self: T) -> str:
        return "black" if self.color == 0 else "red"

    def set_color(self: T, color: str) -> None:
        if color == "black":
            self.color = 0
        elif color == "red":
            self.color = 1
        else:
            raise Exception("Unknown color")

    def is_red(self: T) -> bool:
        return self.color == 1

    def is_black(self: T) -> bool:
        return self.color == 0

    def is_null(self: T) -> bool:
        return self.id == -1

    def depth(self: T) -> int:
        return 0 if self.parent is None else self.parent.depth() + 1


T = TypeVar('T', bound='RedBlackTree')


class RedBlackTree():
    def __init__(self: T) -> None:
        self.TNULL = Node(0)
        self.TNULL.id = -1
        self.TNULL.set_color("black")
        self.root = self.TNULL
        self.size = 0

    # Preorder
    def pre_order_helper(self: T, node: Node) -> None:
        if not node.is_null():
            sys.stdout.write(str(node.item) + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Inorder
    def in_order_helper(self: T, node: Node) -> None:
        if not node.is_null():
            self.in_order_helper(node.left)
            sys.stdout.write(str(node.item) + " ")
            self.in_order_helper(node.right)

    # Postorder
    def post_order_helper(self: T, node: Node) -> None:
        if not node.is_null():
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(str(node.item) + " ")

    # Search the tree
    def search_tree_helper(self: T, node: Node, key: int) -> Node:
        if node.is_null() or key == node.item:
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Balancing the tree after deletion
    def delete_fix(self: T, x: Node) -> None:
        while x != self.root and x.is_black():
            if x == x.parent.left:
                s = x.parent.right
                if s.is_red():
                    s.set_color("black")
                    x.parent.set_color("red")
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.is_black() and s.right.is_black():
                    s.set_color("red")
                    x = x.parent
                else:
                    if s.right.is_black():
                        s.left.set_color("black")
                        s.set_color("red")
                        self.right_rotate(s)
                        s = x.parent.right

                    s.set_color(x.parent.get_color())
                    x.parent.set_color("black")
                    s.right.set_color("black")
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.is_red():
                    s.set_color("black")
                    x.parent.set_color("red")
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.is_black() and s.right.is_black():
                    s.set_color("red")
                    x = x.parent
                else:
                    if s.left.is_black():
                        s.right.set_color("black")
                        s.set_color("red")
                        self.left_rotate(s)
                        s = x.parent.left

                    s.set_color(x.parent.get_color())
                    x.parent.set_color("black")
                    s.left.set_color("black")
                    self.right_rotate(x.parent)
                    x = self.root
        x.set_color("black")

    def __rb_transplant(self: T, u: Node, v: Node) -> None:
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node_helper(self: T, node: Node, key: int) -> None:
        z = self.TNULL
        while not node.is_null():
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z.is_null():
            # print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.get_color()
        if z.left.is_null():
            # If no left child, just scoot the right subtree up
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right.is_null()):
            # If no right child, just scoot the left subtree up
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.get_color()
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.set_color(z.get_color())
        if y_original_color == "black":
            self.delete_fix(x)

        self.size -= 1

    # Balance the tree after insertion
    def fix_insert(self: T, k: Node) -> None:
        while k.parent.is_red():
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.is_red():
                    u.set_color("black")
                    k.parent.set_color("black")
                    k.parent.parent.set_color("red")
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.set_color("black")
                    k.parent.parent.set_color("red")
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.is_red():
                    u.set_color("black")
                    k.parent.set_color("black")
                    k.parent.parent.set_color("red")
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.set_color("black")
                    k.parent.parent.set_color("red")
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.set_color("black")

    # Printing the tree
    def __print_helper(self: T, node: Node, indent: str, last: bool) -> None:
        if not node.is_null():
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----  ")
                indent += "     "
            else:
                sys.stdout.write("L----   ")
                indent += "|    "

            s_color = "RED" if node.is_red() else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def preorder(self: T) -> None:
        self.pre_order_helper(self.root)

    def inorder(self: T) -> None:
        self.in_order_helper(self.root)

    def postorder(self: T) -> None:
        self.post_order_helper(self.root)

    def search(self: T, k: int) -> Node:
        return self.search_tree_helper(self.root, k)

    def minimum(self: T, node: Node = None) -> Node:
        if node is None:
            node = self.root
        if node.is_null():
            return self.TNULL
        while not node.left.is_null():
            node = node.left
        return node

    def maximum(self: T, node: Node = None) -> Node:
        if node is None:
            node = self.root
        if node.is_null():
            return self.TNULL
        while not node.right.is_null():
            node = node.right
        return node

    def successor(self: T, x: Node) -> Node:
        if not x.right.is_null():
            return self.minimum(x.right)

        y = x.parent
        while not y.is_null() and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self: T,  x: Node) -> Node:
        if (not x.left.is_null()):
            return self.maximum(x.left)

        y = x.parent
        while not y.is_null() and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self: T, x: Node) -> None:
        y = x.right
        x.right = y.left
        if not y.left.is_null():
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self: T, x: Node) -> None:
        y = x.left
        x.left = y.right
        if not y.right.is_null():
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self: T, key: int) -> None:
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.set_color("red")

        y = None
        x = self.root

        while not x.is_null():
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        self.size += 1

        if node.parent is None:
            node.set_color("black")
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def get_root(self: T) -> Node:
        return self.root

    def delete(self: T, item: int) -> None:
        self.delete_node_helper(self.root, item)

    def print_tree(self: T) -> None:
        self.__print_helper(self.root, "", True)

    def __getitem__(self: T, key: int) -> int:
        return self.search(key).value

    def __setitem__(self: T, key: int, value: int) -> None:
        self.search(key).value = value
