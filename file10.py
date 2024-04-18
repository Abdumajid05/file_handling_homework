def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data)
    a=f.readlines()
    l=[]
    for i in a:
        l.append(len(i[:-1]))
    return max(l)
print(main('data\data06.txt'))
# Read data from file