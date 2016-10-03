# This is the example from our notes
A = matrix(GF(3),[[2,1,0,1,2],[1,1,1,2,1],[1,2,0,2,1],[2,1,0,2,1]])
print (ParityCheckMatrix2(A) == ParityCheckMatrix1(A), ParityCheckMatrix2(A))

# An example I pulled from the book. This returns the exact answer as given by the book
C2 = matrix(GF(2),[[0,0,0],[0,1,1],[1,0,1],[1,1,0]])
GeneratorMatrix1(C2)

# This returns the answer in a different order than the previous command
GeneratorMatrix2(C2)

# Another example from book
# My code returns a G.M. in standard form for this one
C1 = matrix(GF(2),[[1,1,1,1,1,1,1,],[1,0,0,0,1,0,1],[1,1,0,0,0,1,0],[0,1,1,0,0,0,1]])
GeneratorMatrix1(C1)

# This one is returned as-is
GeneratorMatrix2(C1)


"""
We should probably handle empty matrix and wrong matrix (right?)
We should also handle matrices that are not created properly: for example, a binary matrix that is not created as a binary matrix.
We can do this by remaking it.
Any other idea?
"""
