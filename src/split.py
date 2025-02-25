from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    node_list = []

    for o in old_nodes:
        lst = o.text.split(delimiter)
        for index, item in enumerate(lst):
            if index % 2 == 0:
                node_list.append(TextNode(item, o.text_type))
            else:
                node_list.append(TextNode(item, text_type))

    return node_list
    



node = TextNode("This is text with a `code block` word", TextType.NORMAL)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
print(new_nodes)

