import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf = LeafNode('p', 'Hello, World!')
        self.assertEqual(leaf.to_html(), '<p >Hello, World!</p>')
        
    def test_props_to_html(self):
        leaf = LeafNode('p', 'Hello, World!', {'class': 'my-class', 'id': 'my-id'})
        self.assertEqual(leaf.props_to_html(), 'class="my-class" id="my-id"')
        
    def test_repr(self):
        leaf = LeafNode('p', 'Hello, World!', {'class': 'my-class', 'id': 'my-id'})
        self.assertEqual(repr(leaf), 'LeafNode(p, Hello, World!, {\'class\': \'my-class\', \'id\': \'my-id\'})')

    def test_eq(self):
        leaf = LeafNode('p', 'Hello, World!', {'class': 'my-class', 'id': 'my-id'}) 
        leaf2 = LeafNode('p', 'Hello, World!', {'class': 'my-class', 'id': 'my-id'})
        self.assertEqual(leaf, leaf2)
        
    def test_no_eq(self):
        leaf = LeafNode('p', 'Hello, World!', {'class': 'my-class', 'id': 'my-id'}) 
        leaf2 = LeafNode('h1', 'Hello, World!', {'class': 'my-class', 'id': 'my-id'})
        self.assertNotEqual(leaf, leaf2)

if __name__ == "__main__":
    unittest.main()