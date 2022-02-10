from rbtree import RedBlackTree, Node


def check_node_valid(bst, node):
    if node == bst.TNULL:
        assert node.color == 0
        return

    if node.color == 1:
        assert node.left.color == 0
        assert node.right.color == 0

    if node.left != bst.TNULL and node.left is not None:
        assert node.item >= node.left.item
    if node.right != bst.TNULL and node.right is not None:
        assert node.item <= node.right.item


def check_valid_recur(bst, node):
    check_node_valid(bst, node)

    if node == bst.TNULL:
        return 1

    if node.left == bst.TNULL and node.right == bst.TNULL:
        if node.color == 0:
            return 2
        else:
            return 1

    left_count = check_valid_recur(bst, node.left)
    right_count = check_valid_recur(bst, node.right)

    assert left_count == right_count

    cur_count = left_count # doesn't matter which one we choose because they're the same
    if node.color == 0:
        cur_count += 1 

    return cur_count


def check_valid(bst):
    root = bst.get_root()
    assert root.color == 0

    check_valid_recur(bst, root)


def test_insert():
    bst = RedBlackTree()
    bst.insert(55)
    assert bst.searchTree(55).item == 55
    bst.insert(40)
    assert bst.searchTree(40).item == 40    
    bst.insert(58)    
    assert bst.searchTree(58).item == 58
    bst.insert(42)
    assert bst.searchTree(42).item == 42

    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(43)
    bst.insert(44)
    bst.insert(40)
    bst.insert(-10)
    bst.insert(10)
    bst.insert(15)
    bst.insert(11)
    bst.insert(100)    
    bst.insert(101)
    bst.insert(103)
    bst.insert(106)
    bst.insert(107)
    bst.insert(109)
    bst.insert(102)

    assert bst.size == 23

    check_valid(bst)


def test_search():
    bst = RedBlackTree()
    assert bst.searchTree(60) == bst.TNULL
    bst.insert(30)
    assert bst.searchTree(30).item == 30
    

def test_delete():
    bst = RedBlackTree()
    bst.insert(78)
    assert bst.searchTree(78).item == 78
    bst.delete_node(78)
    assert bst.searchTree(78) == bst.TNULL

    bst.insert(73)
    bst.insert(48)
    bst.insert(100)    
    bst.insert(42)
    bst.insert(55)
    bst.insert(40)
    bst.insert(58)    
    bst.insert(42)
    bst.insert(55)
    bst.insert(40)
    bst.insert(58)    
    bst.insert(42)

    assert bst.size == 12

    bst.delete_node(48)
    assert bst.size == 11
    bst.delete_node(42)    
    assert bst.size == 10
    bst.delete_node(42)
    assert bst.size == 9
    assert bst.searchTree(42).item == 42
    bst.delete_node(42)
    assert bst.searchTree(42) == bst.TNULL    
    assert bst.size == 8
    bst.delete_node(100)
    assert bst.size == 7

    bst.delete_node(100)

    assert bst.size == 7
    check_valid(bst)


def test_complex_delete():
    bst = RedBlackTree()

    with open("small_input.txt") as infile:
        for line in infile:
            sline = line.split()
            # print(sline, bst.searchTree(int(sline[1])) == bst.TNULL)
            if sline[0] == "a":
                # print("add")
                bst.insert(int(sline[1]))
            else:
                # print("delete")
                bst.delete_node(int(sline[1]))
            # bst.print_tree()
            check_valid(bst)


def test_long():
    bst = RedBlackTree()

    with open("test_input.txt") as infile:
        for line in infile:
            sline = line.split()
            # print(sline, bst.searchTree(int(sline[1])) == bst.TNULL)
            if sline[0] == "a":
                # print("add")
                bst.insert(int(sline[1]))
            else:
                # print("delete")
                bst.delete_node(int(sline[1]))
            # bst.print_tree()
            check_valid(bst)


def test_dictionary():
    bst = RedBlackTree()
    bst[67] = 3
    assert bst[67] == 3


def test_get_root():
    bst = RedBlackTree()
    assert bst.get_root() == bst.TNULL
    bst.insert(3)
    assert bst.get_root().item == 3    


def test_accessors():
    bst = RedBlackTree()
    assert bst.maximum().item == float("-inf")
    assert bst.minimum().item == float("inf")

    bst.insert(55)
    bst.insert(40)
    bst.insert(58)    
    bst.insert(42)
    # bst.print_tree()

    assert bst.maximum().item == 58
    assert bst.minimum().item == 40
    assert bst.successor(bst.searchTree(42)).item == 55
    assert bst.successor(bst.searchTree(40)).item == 42
    assert bst.successor(bst.searchTree(55)).item == 58
    assert bst.predecessor(bst.searchTree(42)).item == 40
    assert bst.predecessor(bst.searchTree(55)).item == 42
    assert bst.predecessor(bst.searchTree(58)).item == 55   

    bst.insert(57) 
    assert bst.predecessor(bst.searchTree(57)).item == 55


def test_print():
    bst = RedBlackTree()    
    bst.insert(73)
    print(bst.get_root())
    bst.insert(48)
    bst.insert(100)    
    bst.insert(42)
    bst.insert(55)
    bst.insert(40)
    bst.insert(58)    
    bst.insert(42)
    bst.insert(55)
    bst.insert(40)
    bst.insert(58)    
    bst.insert(42)

    bst.print_tree()
    bst.preorder()
    bst.inorder()
    bst.postorder()


def test_elaborate_delete():
    bst = RedBlackTree()
    bst.insert(55)
    bst.insert(40)
    bst.insert(58)    
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(43)
    bst.insert(44)
    bst.insert(40)
    bst.insert(-10)
    bst.insert(10)
    bst.insert(15)
    bst.insert(11)
    bst.insert(100)    
    bst.insert(101)
    bst.insert(103)
    bst.insert(106)
    bst.insert(107)
    bst.insert(109)
    bst.insert(102)

    bst.delete_node(15)
    bst.delete_node(55)
    bst.delete_node(103)
    bst.delete_node(106)
    bst.delete_node(107)
    bst.delete_node(101)
    bst.delete_node(42)
    bst.delete_node(42)
    bst.delete_node(42)
    bst.delete_node(10)
    bst.delete_node(40)
    bst.delete_node(58)
    bst.delete_node(100)
    bst.delete_node(42)

    bst.print_tree()
    check_valid(bst)    
    # assert False


def test_duplicates():
    bst = RedBlackTree()
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)    
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)    
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)
    bst.insert(42)

    bst.delete_node(42)
    bst.delete_node(42)
    bst.delete_node(42)
    bst.delete_node(42)
    bst.delete_node(42)
    bst.delete_node(42)
    bst.delete_node(42)                        
    check_valid(bst)
