from textnode import TextNode, TextType


def main():
    t = TextNode("hello", TextType.BOLD, "whatever.com")
    print(t)

if __name__ == "__main__":
    main()