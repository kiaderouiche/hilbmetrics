"""

Hilbert projective metric (Basic conding !)
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
from sympy.geometry import Point, Line
from sympy.geometry import convexHull

x, y = symbols('x, y', positive=True)
p, q = symbols('p, q', positive=True)

def check_collinear(x, y, p, q):
  """
  Checking collinearity of points
  """
  pass

def birapport_calculs():
  """ 
  Birapport
  """
  pass

def d_c(x, y):
  """
  Hilbert metric
  """  
 
              
