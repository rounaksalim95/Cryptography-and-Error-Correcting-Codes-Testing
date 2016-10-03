# This is the example from our notes
A = matrix(GF(3),[[2,1,0,1,2],[1,1,1,2,1],[1,2,0,2,1],[2,1,0,2,1]])
print (ParityCheckMatrix2(A) == ParityCheckMatrix1(A), ParityCheckMatrix2(A))

# An example I pulled from the book. This returns the exact answer as given by the book
C2 = matrix(GF(2),[[0,0,0],[0,1,1],[1,0,1],[1,1,0]])
GeneratorMatrix1(C2)

# However this returns a slightly different answer than the given one
# Might be that my code is wrong
GeneratorMatrix2(C2)
