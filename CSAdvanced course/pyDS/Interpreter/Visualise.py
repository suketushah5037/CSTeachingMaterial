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
    """Breadth first traversal, needs a queue.
    https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/
    """
    def bfs(self, tree):
        #iam reusing but ncount could have just been a local variable
        self.ncount = 1
        queue = []
        queue.append(tree)
        s = '  node{} [label="{}"]\n'.format(self.ncount, tree.opvalue)
        self.dot_body.append(s)
        #Marking the tree as visited
        tree._num = self.ncount
        #Proceeding to the next node
        self.ncount += 1
        
        while queue:
            tree = queue.pop(0)
            print("tree opvalue", tree.opvalue)

            #Neighbours in an expression tree are the tree's children
            for child_node in (tree.left, tree.right):
                 #If a leaf node, the child node is None
                 #Not handling unary operators, hence no chance that, left node is None
                 #and right node has a value, hence it is safe to break instead of continue
                 if(child_node  == None):
                     #numeric node 
                     break
                 #adds the child to the queue
                 queue.append(child_node)
                 #marks it as visited
                 child_node._num = self.ncount

                 #print("ncount and child node = ", ncount, child_node.opvalue)
                 s = '  node{} [label="{}"]\n'.format(self.ncount, child_node.opvalue)
                 self.dot_body.append(s)
                 #print("node{} -> node{} ".format( tree._num,child_node._num))
                 s = '  node{} -> node{}\n'.format(tree._num,child_node._num)
                 self.dot_body.append(s)


                 #proceed
                 self.ncount = self.ncount + 1

                 
    def gendotbfs(self):
        print("--------------------------Building the AST-------------------------------")
        tree = self.parser.expr()
        print("--------------------------Building the AST-------------------------------")
        print("\n\n\n\n\n")
        #emptying body before refilling
        self.dot_body = []
        self.bfs(tree)
        return(''.join(self.dot_header + self.dot_body + self.dot_footer))


    """Print the AST visually, using DFS"""
    def gendotdfs(self):
        print("--------------------------Building the AST-------------------------------")
        tree = self.parser.expr()
        print("--------------------------Building the AST-------------------------------")
        print("\n\n\n\n\n")
        #Emptying body before refilling
        self.dot_body = []
        self.visitast(tree)
        
        return ''.join(self.dot_header + self.dot_body  + self.dot_footer)


    """Ever needed helper function. DFS pre and post order traversal mixed"""
    def visitast(self, tree):
        #numeric and leaf node
        if((tree.left == None) and (tree.right == None)):
            s = '  node{} [label="{}"]\n'.format(self.ncount, tree.opvalue)
            self.dot_body.append(s)
            #Python let's you add member variables to the class on the fly
            tree._num = self.ncount
            self.ncount += 1
            print(tree.opvalue)
            return
        elif(tree.opvalue == Token.EOF):
             return
        #binop node
        else:
            #Pre-order traversal to maintain the node count
            s = '  node{} [label="{}"]\n'.format(self.ncount, tree.opvalue)
            print(tree.opvalue)
            self.dot_body.append(s)
            tree._num = self.ncount
            self.ncount = self.ncount+ 1
            self.visitast(tree.left)
            self.visitast(tree.right)
            #Post order traversal to traverse through the children to get the parent linkage
            #tree._num gives the parent's node count, child_node._num gives the child's node count
            for child_node in (tree.left, tree.right):
                s = '  node{} -> node{}\n'.format(tree._num, child_node._num)
                self.dot_body.append(s)

