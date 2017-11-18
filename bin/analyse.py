import os, sys
sys.path.append(os.path.abspath('..'))
print('\n'.join(sorted(sys.path)))
from statementanalyser.utilsregex import *

line = "Mikael is 33yo and he lives in London"

results = utilsregex.get_match_groups(r'([a-zA-Z]*) .* ([0-9]*?)yo .*',line)
print("name: ",results[0]," age: ",results[1])
    
import numpy as np
import matplotlib.pyplot as plt

plt.ioff()
plt.plot(np.random.rand(10))
plt.show()