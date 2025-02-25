from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    node_list = []

    for o in old_nodes:
        if o.text_type == TextType.TEXT:
            lst = o.text.split(delimiter)
            for index, item in enumerate(lst):
                if item.strip():
                    if index % 2 == 0:
                        node_list.append(TextNode(item, o.text_type))
                    else:
                            node_list.append(TextNode(item, text_type))
        else:
            node_list.append(o)

    return node_list
    
def extract_markdown_images(text):
    pass

