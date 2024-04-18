def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data,mode='r')
    s=f.read()
    l=[]
    for i in s:
        if i.isdigit():
            l.append(i)
    
    f=open(data,mode='r')
    s=f.read()
    lst=[]
    for i in s:
        if i.isalpha():
            lst.append(i)
    return [len(l),len(lst)]
print(main('data\data05.txt'))
# Read data from file