import unittest
#To capture output from stdout, store it in a file, read a file and compare it's contents
import sys
from bingo import *

#Test cases class
class TDDInPythonExample(unittest.TestCase):
    #Test case to test the constructor
    def test_arr_len(self):
        bingo = BingoGame()
        lenarr = bingo.bingoarrlen()
        self.assertEqual(5, lenarr)
    #Test case to test the array contents filled by "bingorhyme"
    def test_arr_contents(self):
        bingo = BingoGame()
        bingo.bingorhyme()
        i = 0
        while(i<bingo.bingoarrlen()):
            #print(bingo.bingoarray(i))
            self.assertEqual('clap',bingo.bingoarray(i))
            i = i + 1
    #Test case to test what is being printed
    def testbingorhyme(self):
        bingo = BingoGame()
        bingo.bingorhyme()

        saveout =  sys.stdout
        fsock = open('out.log', 'w')
        
        sys.stdout = fsock
        bingo.printbingorhyme()
        sys.stdout =  saveout
        fsock.close()

        fsock = open('out.log' , 'r')
        filecontent = fsock.read()
        #print(filecontent)
        #print("[['clap', 'i', 'n', 'g', 'o'], ['clap', 'clap', 'n', 'g', 'o'], ['clap', 'clap', 'clap', 'g', 'o'], ['clap', 'clap', 'clap', 'clap', 'o'], ['clap', 'clap', 'clap', 'clap', 'clap']]".rstrip())
        fsock.close()
      
        self.assertEqual("[['clap', 'i', 'n', 'g', 'o'], ['clap', 'clap', 'n', 'g', 'o'], ['clap', 'clap', 'clap', 'g', 'o'], ['clap', 'clap', 'clap', 'clap', 'o'], ['clap', 'clap', 'clap', 'clap', 'clap']]".rstrip(),
                         filecontent.rstrip())
#Run the test cases
if __name__ == '__main__':
    unittest.main()
    
