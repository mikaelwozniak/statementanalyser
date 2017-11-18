import unittest
import os, sys
sys.path.append(os.path.abspath('../..'))
print('\n'.join(sorted(sys.path)))
from statementanalyser.utilsregex import *




class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test1(self):
        line = "Cats are smarter than dogs"
        results = utilsregex.get_match_groups(r'(.*) are (.*?) .*',line)
        print(results)
        self.assertEqual( len(results), 2)
        self.assertEqual( results[0], "Cats")
        self.assertEqual( results[1], "smarter")
 
 
if __name__ == '__main__':
    unittest.main()