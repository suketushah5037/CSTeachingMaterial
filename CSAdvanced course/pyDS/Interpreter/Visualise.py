"""Visualise the tree"""
#install graphviz from here
#download from http://www.graphviz.org/Download_windows.php and install
#run http://www.graphviz.org/Download_windows.php

#command to run
#C:\Program Files (x86)\Graphviz2.38\bin>dot -Tpng -o "C:\Users\Gowri\Desktop\CS_classes\MaterialRepo\CSTeachingMaterial\CSAdvanced course\pyDS\tokenizer\parsetree.png" "C:\Users\Gowri\Desktop\CS_classes\MaterialRepo\CSTeachingMaterial\CSAdvanced course\pyDS\tokenizer\parsetree.dot"

#Not Required since we are using the GraphViz executable
#pip install graphviz on the command prompt


#To provide the text for graphviz to generate a graph from
import textwrap
import Token

#generating ast graph
#bfs tree uses a queue and dfs uses a stack

class Visualise:
    def __init__(self, parser):
        self.dot_header = [textwrap.dedent("""\
                digraph astgraph {
                  node [shape=circle, fontsize=12, fontname="Courier", height=.1];
                  ranksep=.3;
                  edge [arrowsize=.5]
                """)]
        #Manipulate the ncount and dot_body
        self.ncount = 1
        self.dot_body = []
        self.parser = parser
        #constant
        self.dot_footer = ['}']


    def gendot(self):
        print("--------------------------Building the AST-------------------------------")
        tree = self.parser.expr()
        print("--------------------------Building the AST-------------------------------")
        print("\n\n\n\n\n")
        self.visitast(tree)
        
        return ''.join(self.dot_header + self.dot_body  + self.dot_footer)


    """Ever needed helper function. DFS pre and post order traversal mixed"""
    def visitast(self, tree):
        #numeric and leaf node
        if((tree.left == None) and (tree.right == None)):
            s = '  node{} [label="{}"]\n'.format(self.ncount, tree.opvalue)
            self.dot_body.append(s)
            tree._num = self.ncount
            self.ncount += 1
            print(tree.opvalue)
            return
        elif(tree.opvalue == Token.EOF):
             return
        #binop node
        else:
            s = '  node{} [label="{}"]\n'.format(self.ncount, tree.opvalue)
            print(tree.opvalue)
            self.dot_body.append(s)
            tree._num = self.ncount
            self.ncount = self.ncount+ 1
            self.visitast(tree.left)
            self.visitast(tree.right)

            for child_node in (tree.left, tree.right):
                s = '  node{} -> node{}\n'.format(tree._num, child_node._num)
                self.dot_body.append(s)

