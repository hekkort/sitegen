import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node, node2)
    def test_no_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("h1", "This is a header")
        self.assertNotEqual(node, node2)
    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(repr(node), "HTMLNode(p, This is a paragraph, None, None)")
    def test_repr_attrs(self):
        node = HTMLNode("p", "This is a paragraph", None, {"class": "paragraph"})
        self.assertEqual(repr(node), "HTMLNode(p, This is a paragraph, None, {'class': 'paragraph'})")

if __name__ == "__main__":
    unittest.main()
