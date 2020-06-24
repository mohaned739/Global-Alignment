#DNA Scoring Scheme:
#match score = 1
#mismatch score = -1
#gap penalty = -1
def ga(seq1, seq2):
    len2=len(seq2)
    len1=len(seq1)
    table_cell = [[0 for seq1 in range(len1+1)] for seq2 in range(len2+1)]

    #initialization and filling:
    for i in range (len2+1):
        table_cell[i][0]=-i
    for j in range (len1+1):
        table_cell[0][j] =-j

    for i in range(1,len2+1,1):
        for j in range(1,len1+1,1):
            if seq1[j-1] == seq2[i-1]:
                score = 1
            else :
                score =-1
            table_cell[i][j] = max(table_cell[i-1][j]-1, table_cell[i][j-1]-1,table_cell[i-1][j-1]+score)

    #score
    print(table_cell[len2][len1])

    #traceback:
    seq1_GA =""
    seq2_GA=""
    GAMatch=""
    i = len2
    j = len1
    while i > 0 and j > 0:
        up = table_cell[i-1][j]-1
        left=table_cell[i][j-1]-1
        if  seq1[j-1]!=seq2[i-1]:
            score=-1
        else :
            score=1
        diagonal = table_cell[i-1][j-1]+score
        if table_cell[i][j]==diagonal:
            seq1_GA+=seq1[j-1]
            seq2_GA+=seq2[i-1]
            if score==1:
                GAMatch+="|"
            else:
                GAMatch+=" "
            i-=1
            j-=1
        elif table_cell[i][j] == up:
            seq1_GA+="-"
            GAMatch+=" "
            seq2_GA+=seq2[i-1]
            i-=1
        else:
            seq1_GA+=seq1[j-1]
            seq2_GA+="-"
            GAMatch+=" "
            j-=1

    while (i>0):
        seq1_GA+="-"
        seq2_GA+=seq2[i-1]
        GAMatch+=" "
        i-=1
    while(j>0):
        seq1_GA+=seq1[j-1]
        seq2_GA+="-"
        GAMatch+=" "
        j-=1
        
    seq1_GA=seq1_GA[::-1]
    GAMatch=GAMatch[::-1]
    seq2_GA=seq2_GA[::-1]
    
    print (seq1_GA)
    print(GAMatch)
    print(seq2_GA)
 
# Main:
seq1 = "TTCCCTCCGCCGCCCCCCGGCCGCGGGGAGGACGTGGCCGCGCACAGGCCGGTGGAATGGGTCCAGGCCG"
seq2 = "TTCCCTCCGCCGCCCCCCGGCCGCGGGGAGGACATGGCCGCGCACAGGCCGGTGGAATGGGTCCAGGCCG"
ga(seq1, seq2)
