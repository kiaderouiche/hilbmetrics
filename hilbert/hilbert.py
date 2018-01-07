"""

Hilbert projective metric
=========================

- boundary of Ω
- order of the points p,x, q, y
- || || Real norm

              ||py|| ||xq||         
d(x,y) = ln( ---------------- )
              ||px|| ||yq||

"""

from sympy import symbols
from sympy import log

x, y = symbols('x, y')
p, q = symbols('p, q')

def d(x, y):
  pass 
              
