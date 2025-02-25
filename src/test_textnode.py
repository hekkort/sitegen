import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_no_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a node", TextType.NORMAL, "whatever.com")
        self.assertNotEqual(node, node2)
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, Bold, None)")
    def test_repr_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "whatever.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, Bold, whatever.com)")

if __name__ == "__main__":
    unittest.main()