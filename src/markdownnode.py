
# old_nodes: list of old_nodes
# delimiter:
# text_type
# return a list of nodes
from textnode import TextType, TextNode

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

        # since we only spliting TEXT this is not necessary 
        node_type = node.text_type
        node_splited = node.text.split(delimiter)
        print(f"node_splitted: {node_splited}")
        
        # reassemble them into textnode
        new_node = TextNode(node_splited[0], TextType.TEXT)
        new_node1 = TextNode(node_splited[1], text_type)
        new_node2 = TextNode(node_splited[2], TextType.TEXT)

        # add them to new_nodes list

        new_nodes.append(new_node)
        new_nodes.append(new_node1)
        new_nodes.append(new_node2)
        # print(f"new_nodes: {new_nodes}")
    
    # end of for loop

    return new_nodes
    


        
