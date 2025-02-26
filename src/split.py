from textnode import TextType, TextNode
import re

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
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
        
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(node):
    text_list = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
    images_dict = {}
    
    for image_text, url in extract_markdown_images(node.text):
        images_dict[image_text] = url
    
    # Create a set of URLs to check against
    urls = set(images_dict.values())
    
    text_list = list(filter(None, text_list))
    final_list = []
    for element in text_list:
        if element in images_dict:
            final_list.append(TextNode(element, TextType.IMAGES, images_dict[element]))
        elif element not in urls:
            final_list.append(TextNode(element, TextType.NORMAL))

    return final_list

def split_nodes_link(node):
    text_list = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
    links_dict = {}
    
    for link_text, url in extract_markdown_links(node.text):
        links_dict[link_text] = url
    
    # Create a set of URLs to check against
    urls = set(links_dict.values())
    
    text_list = list(filter(None, text_list))
    final_list = []
    for element in text_list:
        if element in links_dict:
            final_list.append(TextNode(element, TextType.LINKS, links_dict[element]))
        elif element not in urls:
            final_list.append(TextNode(element, TextType.NORMAL))
    return final_list

def text_to_textnodes(text):
    node = TextNode(text, TextType.NORMAL)
    return split_nodes_link(node)

text = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", 
                TextType.NORMAL)

image = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.NORMAL,
    )

website = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.NORMAL,
)


print(split_nodes_link(text))
print(split_nodes_image(text))