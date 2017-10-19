import Interpreter
#File name
#Maintain the same class name and file name including the casing
import Parser
import Lexer
import Visualise

###########################################Parser call happening here#######################################
def main():
    print("ability to produce tokens")
    lexer = Lexer.Lexer("1*(2+3)/2")
    myparser = Parser.Parser(lexer)
    print("Uses tokens to build an AST and evalutating the math expression using the tree")
    interpreter = Interpreter.Interpreter(myparser)
    mathexprvalue = interpreter.interpret()
    print("calculated value = ", mathexprvalue) 
    print("--------------------------Evaluated the expression using the AST-------------------------------")
    print("\n\n\n\n\n")

    print("Generating the tree visually")
    print("Copy the output into a .dot file and run the following command")
    print("My bin - C:\Program Files (x86)\Graphviz2.38\bin>")
    print("Provide full path for the .dot and .png files")
    print("dot -Tpng -o parsetree.png parsetree.dot")

    #Generate the objects again - None goes to my parser
    lexer = Lexer.Lexer("1*(2+3)/2")
    myparser = Parser.Parser(lexer)
    visualizer = Visualise.Visualise(myparser)
    print("printing ast tree by traversing depth first using pre and post order traversals")
    content = visualizer.gendotdfs()
    print(content)


    #Generate the objects again - None goes to my parser
    lexer = Lexer.Lexer("1*(2+3)/2")
    myparser = Parser.Parser(lexer)
    visualizer = Visualise.Visualise(myparser)
    print("printing ast tree by traversing breadth first without recursion")
    content = visualizer.gendotbfs()
    print(content)
    
if __name__ == '__main__':
    main()
###########################################Parser call happening here#######################################
