def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    x=f.readline()
    a = x.split(',')
    l=[]
    for i in a:
        l.append(int(i))
    return l
print(main("data01.txt"))

# Read data from file