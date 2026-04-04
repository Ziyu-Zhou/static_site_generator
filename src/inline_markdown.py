
# old_nodes: list of old_nodes
# delimiter:
# text_type
# return a list of nodes
from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        # if the node is not a text type we skip it
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        # this should split the node into 3 parts 
        # a node would likely be something like This is text with a `code block` word
        # and a ` delimiter turns it to 3 parts the middle one is code block
        print(f"node: {node}")
        # since we only spliting TEXT this is not necessary 
        node_type = node.text_type
        
        node_splited = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            continue
        print(f"node_splitted: {node_splited}")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                node_splited.append(TextNode(sections[i], TextType.TEXT))
            else:
                node_splited.append(TextNode(sections[i], text_type))
        new_nodes.extend(node_splited)

        # for element in node_splited:
        #     if element is '':
        #         node_splited.remove(element)
        
        # reassemble them into textnode
        # new_node = TextNode(node_splited[0], TextType.TEXT)
        # new_node1 = TextNode(node_splited[1], text_type)
        # new_node2 = TextNode(node_splited[2], TextType.TEXT)

        # # add them to new_nodes list
        # if new_node.text is not '':
        #     new_nodes.append(new_node)
        # new_nodes.append(new_node1)
        # if new_node2.text is not '':
        #     new_nodes.append(new_node2)
        # print(f"new_nodes: {new_nodes}")
    
    # end of for loop
    print(new_nodes)
    return new_nodes

print("-------print test for split------------")
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
node = TextNode("**bold** and _italic_", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)

# print(new_nodes)
print()
print()

#--------------------------------------------------------------------------------------
# extract_markdown images

# input: a string of markdown text
# output: a list of toples 
#         each tuples contains the alt text and the url of any markdown images 
# example:
# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

def extract_markdown_images(text):
    text = text
    # print(f"input text: {text}")

    # regex = r"\[([^\[]])\]\((.*?)\)"
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    # matches_link = re.findall(regex_link, text)
    # print(matches)
    return matches

def extract_markdown_links(text):
    text = text
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches
    



text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]