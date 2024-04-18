def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data,mode='r')
    s=f.read()
    l=[]
    for i in s:
        if i.isdigit():
            l.append(int(i))
    return sum(l)
print(main('data\data07.txt'))
    
# Read data from file