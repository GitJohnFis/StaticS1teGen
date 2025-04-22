from textnode import TextNode, TextType

def main():
    node = TextNode("Hello, World!", TextType.LINK, "https://example.com")
    print(node)


 
main()   