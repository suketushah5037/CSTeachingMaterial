import unittest
import Board

class BoardTestCase(unittest.TestCase):
    """Test case for 'Board.py'"""

    
    def createBoardObject(self):
        self.assertTrue(isinstance(Board(), Board))

if __name__ == '__main__':
    unittest.main()
                
