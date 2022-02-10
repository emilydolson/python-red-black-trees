from rbtree import RedBlackTree

def test_insert():
    bst = RedBlackTree()
    bst.insert(55)
    assert bst.searchTree(55).item == 55

def test_search():
    bst = RedBlackTree()
    assert bst.searchTree(60) == bst.TNULL
    
def test_delete():
    bst = RedBlackTree()
    bst.insert(78)
    assert bst.searchTree(78).item == 78
    bst.delete_node(78)
    assert bst.searchTree(78) == bst.TNULL