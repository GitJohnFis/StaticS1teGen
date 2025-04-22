import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello World!", None, {"class": "greeting", "href": "https://www.google.com","target": "_blank"}
        )
         self.assertEqual(
        node.props_to_html(),
        ' class="greeting" href="https://www.google.com" target="_blank"',
        )

    def test_values(self):
        node = HTMLNode("div", "I wish I could read",
        )
         self.assertEqual(
            node.tag,
            "div",
        )
         self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "what a strange world",
            None,
            {"class": "primary"},
        )
         self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, what a strange world, children: None,{'class': 'primary'})",
        )



if __name__ == "__main__":
    unittest.main()