
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
        # print(f"node: {node}")
        # since we only spliting TEXT this is not necessary 
        node_type = node.text_type
        
        node_splited = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            continue
        # print(f"node_splitted: {node_splited}")

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
    # print(new_nodes)
    return new_nodes

# input_string = "This is **text** with an _italic_ word"
# node = TextNode(input_string, TextType.TEXT)
# result = split_nodes_delimiter([node], "_", TextType.ITALIC)
# print(f"split test italic: {result}")


def extract_markdown_images(text):
    #--------------------------------------------------------------------------------------
    # extract_markdown images

    # input: a string of markdown text
    # output: a list of toples 
    #         each tuples contains the alt text and the url of any markdown images 
    # example:
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

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
    regex = r"\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches


def split_nodes_image(old_nodes):
    # can't use split node function because of syntax format
    # node: (text, text_type, url)

    # nodes that will be return
    new_nodes = []
    # print(f"old_nodes: {old_nodes}")
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            # this should extract the important
            # info like links and alt_Text
            # but keep in mind that this would be a list of tuples
            # and the tuples are alt_text link pair
            image_link = extract_markdown_images(node.text)
            # print(f"image_links: {image_link}")
            if len(image_link) == 0 :
                new_nodes.append(node)
                continue 
            # print(f"info: {image_link}")

            # this for loop loop throught all pair of extracted info 
            # and will split the text around them using .split() with maxsplit
            # chatgpt suggest the use of finditer with regex
            # but i think that would be a overkill


            remaining = node.text
            # print(f"original text: {remaining}")
            # pair = (alt_text, link)
            for pair in image_link:
                # convert pair tuple to a string 
                alt_text = pair[0]
                link = pair[1]
                string_form = f"![{alt_text}]({link})"
                # print(f"string_form: {string_form}")
                sections = remaining.split(string_form, 1)
                # print(f"section: {sections}")
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, link))

                remaining = sections[1]
            # could the remaining be not empty?
            if remaining != "":
                new_nodes.append(TextNode(remaining, TextType.TEXT))
        else:
            new_nodes.append(node)

    return new_nodes

    
    
    
    # extract_markdown_images()

# print("-------print test for split------------")


# node = TextNode(
#         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
#         TextType.TEXT,
#     )
# new_nodes = split_nodes_image([node])
# print(f"new_nodes: {new_nodes}")


# this is a slightly adjusted version from split_nodes_image
def split_nodes_link(old_nodes):

    new_nodes = []

    for node in old_nodes:
        if node.text_type is TextType.TEXT:

            image_link = extract_markdown_links(node.text)
            if len(image_link) == 0 :
                new_nodes.append(node)
                continue 

            remaining = node.text
            # print(f"original text: {remaining}")
            # pair = (alt_text, link)
            for pair in image_link:
                # convert pair tuple to a string 
                alt_text = pair[0]
                link = pair[1]
                string_form = f"[{alt_text}]({link})"
                # print(f"string_form: {string_form}")
                sections = remaining.split(string_form, 1)
                # print(f"section: {sections}")
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(alt_text, TextType.LINK, link))

                remaining = sections[1]
            if remaining != "":
                new_nodes.append(TextNode(remaining, TextType.TEXT))
        else:
            new_nodes.append(node)

    return new_nodes


# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# print(new_nodes)

def text_to_textnodes(text):
    # text_nodes to return 
    text_nodes = []
    # convert input text to textnode 
    string_node = TextNode(text, TextType.TEXT)

    # using split_node_delimiter to split 3 times 

    text_nodes = (split_nodes_delimiter([string_node], "**", TextType.BOLD))
    # print(f"text_nodes_**: {text_nodes}")
    # text_nodes should be 
    # 

    text_nodes = (split_nodes_delimiter(text_nodes, "_", TextType.ITALIC))
    # print(f"text_nodes_italic: {text_nodes}")

    text_nodes = (split_nodes_delimiter(text_nodes, "`", TextType.CODE))
    # print(f"text_nodes_code: {text_nodes}")

    text_nodes = split_nodes_image(text_nodes)
    # print(f"text_nodes_image: {text_nodes}")

    text_nodes = split_nodes_link(text_nodes)
    # print(f"text_nodes_link: {text_nodes}")



    return text_nodes

print(f"debugging text_textnode:   ")
input_string = (
        "This is **text** with an _italic_ word and a `code block` and an ![obi wan image]"
        "(https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )


text_nodes = text_to_textnodes(input_string)
# for node in text_nodes:
#     print(node)






