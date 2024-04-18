def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
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
            l.append(int(i))
    return l
print(main('data\data03.txt'))
# Read data from file
