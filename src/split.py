from textnode import TextType, TextNode, BlockType
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

def markdown_to_blocks(markdown):

    raw_blocks = markdown.split("\n\n")

    blocks = []
    
    for block in raw_blocks:
        cleaned = block.strip()
        if cleaned:
            blocks.append(cleaned)
    
    return blocks

def block_to_block_type(markdown_block):
    block = markdown_block
    heading_pattern = r'^#{1,6} '
    if re.match(heading_pattern, block):
        return BlockType.HEADING
    code_block_pattern = r'^```[\s\S]*```$'
    if re.match(code_block_pattern, block):
        return BlockType.CODE
    quote_block_pattern = r'^>'
    if re.match(quote_block_pattern, block):
        return BlockType.QUOTE
    unordered_list_block_pattern = r'^- '
    if re.match(unordered_list_block_pattern, block):
        return BlockType.UNORDERED_LIST
    ordered_list_block_pattern = r'^1. '
    if re.match(ordered_list_block_pattern, block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    pass


heading = "# this is a heading"
code = "```this is code```"
quote = (">this is a quote"
         ">and this as well")
unordered_list = ("- unordered list"
                  "- this is another line in the unordered list")
ordered_list = ("1. this is an ordered list"
                "2. this is another line in the ordered list")
paragraph = "dit is gewoon een stukkie"

print(block_to_block_type(heading))

print(block_to_block_type(code))
print(block_to_block_type(quote))
print(block_to_block_type(unordered_list))
print(block_to_block_type(ordered_list))
print(block_to_block_type(paragraph))

'''
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



text_block = ("# This is a heading\n\n     "

"   This is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n   "

"    - This is the first list item in a list block\n"
"- This is a list item\n"
"- This is another list item\n\n\n\n\n\n\n\n\n\n   ")


print(markdown_to_blocks(text_block))
#print(text_block)
#print(split_text_block[2])
#print(text_to_textnodes(text))
'''
