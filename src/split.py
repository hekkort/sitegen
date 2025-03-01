from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    node_list = []

    for o in old_nodes:
        if o.text_type == TextType.NORMAL:
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


def split_nodes_image(old_nodes):
    result = []
    
    for node in old_nodes:
        # Only process NORMAL nodes - skip nodes of other types
        if node.text_type != TextType.NORMAL:
            result.append(node)
            continue
            
        text_list = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        images_dict = {}
        
        for image_text, url in extract_markdown_images(node.text):
            images_dict[image_text] = url
        
        # Create a set of URLs to check against
        urls = set(images_dict.values())
        
        text_list = list(filter(None, text_list))
        for element in text_list:
            if element in images_dict:
                result.append(TextNode(element, TextType.IMAGES, images_dict[element]))
            elif element not in urls:
                result.append(TextNode(element, TextType.NORMAL))
    
    return result

def split_nodes_link(old_nodes):
    result = []
    
    for node in old_nodes:
        # Only process NORMAL nodes - skip nodes of other types
        if node.text_type != TextType.NORMAL:
            result.append(node)
            continue
            
        text_list = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        links_dict = {}
        
        for link_text, url in extract_markdown_links(node.text):
            links_dict[link_text] = url
        
        # Create a set of URLs to check against
        urls = set(links_dict.values())
        
        text_list = list(filter(None, text_list))
        for element in text_list:
            if element in links_dict:
                result.append(TextNode(element, TextType.LINKS, links_dict[element]))
            elif element not in urls:
                result.append(TextNode(element, TextType.NORMAL))
    
    return result

def text_to_textnodes(text):
    
    nodes = [TextNode(text, TextType.NORMAL)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes



moretext = [TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", 
                TextType.NORMAL)]

image = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.NORMAL,
    )

website = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.NORMAL,
)

text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

print(text_to_textnodes(text))
