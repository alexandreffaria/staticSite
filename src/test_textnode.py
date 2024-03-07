import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Yoyo", "bold")
        node2 = TextNode("Yoyo", "bold")

        self.assertEqual(node, node2)

    def testNotEq(self):
        node = TextNode("Yo", "old")
        node2 = TextNode("Yoyo", "bold")

        self.assertNotEqual(node, node2)

    def testTextStyleNotEq(self):
        node = TextNode("Yoyo", "old")
        node2 = TextNode("Yoyo", "bold")

        self.assertNotEqual(node.text_type, node2.text_type)

    def testTextEq(self):
        node = TextNode("Yoyo", "old")
        node2 = TextNode("Yoyo", "bold")

        self.assertEqual(node.text, node2.text)



if __name__ == "__main__":
    unittest.main()