def subSeq(string):
    if len(string)==0:
        output=[]
        output.append("")
        return output
    smallstr=string[1:]
    smalloutput=subSeq(smallstr)
    output=[]
    for sub in smalloutput:
        output.append(sub)
        
    for sub in smalloutput:
        output.append(string[0]+sub)
    return output

output=subSeq("abc")
print(output)