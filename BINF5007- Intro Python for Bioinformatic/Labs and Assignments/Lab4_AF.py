def compliment(DNA_seq:str)->str:
    """
    return a type string given a sequence of DNA (DNA_seq).
    Gives the compliment of DNA_seq\n
    DNA_seq argument must be string type\n
    function assumes the following:\n 
        -DNA_seq only contains nucleotide bases A,T,G and C
        -len(DNA_seq) > 0 (string argument is not empty)
    """
    DNA_seq=DNA_seq.replace("A","t")
    DNA_seq=DNA_seq.replace("C","g")
    DNA_seq=DNA_seq.replace("T","a")
    DNA_seq=DNA_seq.replace("G","c")
    return DNA_seq.upper()
def reverse(DNA_seq:str)->str:
    """
    return a type string (DNA_seq_rev) given a sequence of DNA (DNA_seq).
    Gives the reverse order of DNA_seq\n
    DNA_seq argument must be string type\n
    function assumes the following:\n 
        -len(DNA_seq) > 0 (string argument is not empty)
    """
    DNA_seq_rev=""
    for base in range(1,len(DNA_seq)+1):
        DNA_seq_rev+=DNA_seq[-base]
    return DNA_seq_rev
def compliment_strand(DNA_seq:str)->str:
    """
    return a type string (REV_seq) given a sequence of DNA (DNA_seq).
    Gives the reverse compliment of DNA_seq in 5' to 3' orientation\n
    DNA_seq argument must be string type\n
    function assumes the following:\n 
        -DNA_seq is in 5' to 3' orientation\n
        -DNA_seq is the forward sequence\n
        -len(DNA_seq) > 0 (string argument is not empty)
    """
    REV_seq = compliment(reverse(DNA_seq))
    return REV_seq
def findIndex(source_seq:str,search_seq:str)->int:
    """
    return a type bool (match) given a pattern (search_seq) and a given sequence of DNA (source sequence).
    findIndex will determine if the following search_seq is found in the source sequence, if found then
    return is index, else return -1\n
    Search sequence and source sequence arguments must be string type\n
    function assumes the following:\n 
        -'x' is A,C,T or G\n
        -source sequence is in 5' to 3' orientation\n
        -source sequence is the forward sequence\n
        -len(source sequence) > 0 and len(search_seq) > 0(string arguments are not empty)
    """
    match = False
    index = -1
    for source_index, source_base in enumerate(source_seq):
        #print(source_base , search_seq[0], match)
        if(source_base == search_seq[0]):
            for search_index, search_base in enumerate(search_seq):
                if (search_index+source_index>=len(source_seq)):
                    match = False
                    break
                if (search_base==source_seq[source_index+search_index]):
                    match = True
                elif (search_base=='x'):
                    match = True
                else :
                    match = False
                    break
        if(match):
            break
    return(source_index)
def findMatch(source_seq:str,search_seq:str)->bool:
    """
    return a type bool (match) given a pattern (search_seq) and a given sequence of DNA (source sequence).
    findMatch will determine if the following search_seq is found in the source sequence, if found then
    return is True, else return is False\n
    Search sequence and source sequence arguments must be string type\n
    function assumes the following:\n 
        -'x' is A,C,T or G\n
        -source sequence is in 5' to 3' orientation\n
        -source sequence is the forward sequence\n
        -len(source sequence) > 0 and len(search_seq) > 0(string arguments are not empty)
    """
    match = False
    for source_index, source_base in enumerate(source_seq):
        #print(source_base , search_seq[0], match)
        if(source_base == search_seq[0]):
            for search_index, search_base in enumerate(search_seq):
                if (search_index+source_index>=len(source_seq)):
                    match = False
                    break
                if (search_base==source_seq[source_index+search_index]):
                    match = True
                elif (search_base=='x'):
                    match = True
                else :
                    match = False
                    break
        if(match):
            break
    return(match)
def findPattern(source_seq:str,search_seq:str)->None:
    """
    prints a statment determining whether the pattern (search sequence) is found in a given sequence of DNA (source sequence)
    in either the forward or reverse (compliment).
    if search sequence is found in source sequence than it will give the index that search sequence was found in source
    sequence.\n
    Search sequence and source sequence arguments must be string type\n
    function assumes the following:\n 
        -'x' is A,C,T or G\n
        -source sequence is in 5' to 3' orientation\n
        -source sequence is the forward sequence\n
        -len(source sequence) > 0 and len(search_seq) > 0(string arguments are not empty)
    """
    if (findMatch(source_seq,search_seq)):
        index = findIndex(source_seq,search_seq)
        print(search_seq+" was found at index ["+str(index)+"] in the sequence: "+source_seq)
    elif (findMatch(compliment_strand(source_seq),search_seq)):
        index = findIndex(compliment_strand(source_seq),search_seq)
        print(search_seq+" was found at index ["+str(index)+"] in complimentary sequence: "+compliment_strand(source_seq)+" (original sequence -> "+source_seq+")")
    else :
        print(search_seq+" was not found in the sequence or it's complimentary: "+source_seq)

testcase1="TATAxxxATGxxxT" #strand read 5' to 3' containing the TATAxxxATGxxxT pattern
testcase2="AxxxCATxxxTATA" #strand read 5' to 3' containing the TATAxxxATGxxxT pattern in the complimentary strand
testcase3="ACTTAGTGATAAxx" #strand read 5' to 3' that doesn't contian TATAxxxATGxxxT or in the complimentary strand

findPattern(testcase1,"TATAxxxATGxxxT") 
findPattern(testcase2,"TATAxxxATGxxxT")
findPattern(testcase3,"TATAxxxATGxxxT")
