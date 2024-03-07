import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def testEq(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a", props=props)
    
        self.assertEqual(node.propsToHTML(), ' href="https://www.google.com" target="_blank"')

    # def testNotEq(self):
    #     node = HTMLNode("Yo", "old")
    #     node2 = HTMLNode("Yoyo", "bold")

    #     self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()