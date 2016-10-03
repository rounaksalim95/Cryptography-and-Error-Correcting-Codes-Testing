# Cryptography-and-Error-Correcting-Codes-Testing    
# Tests for PP2:
- `GeneratorMatrix1?`  
- `GeneratorMatrix2?`  
- `ParityCheckMatrix1?`
- `ParityCheckMatrix2?`
- `S = matrix(GF(3), [[2,1,0,1,2],[1,1,1,2,1],[1,2,0,2,1],[2,1,0,2,1]])`  
  - Parity check matrix should be  	
[1 1 1 0 0]  
[0 0 0 1 1]
- Messsage for exception  
# Error checking for index out of range when Algorithm doesn't work  

    `if (len(negativeRows) < len(leadingColumns)):  
        print "It appears as though this Algorithm goes out of range for this matrix"
        return`
