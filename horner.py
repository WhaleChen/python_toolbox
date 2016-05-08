# Horner's algorithm

def horner(x, a_vector):
    '''
    # test x=0 
    >>> horner(0,[1,2,3])
    3
    >>> horner(1,[1,2,3])
    6
    >>> horner(0.5, [1,2,3])
    4.25
    '''
    if not len(a_vector):
        pass
    else:
        for i in range(len(a_vector)):
            if i ==0:
                a = a_vector[0]
            else:
                a = a*x + a_vector[i]
        return a


if __name__ =="__main__":
    import doctest
    doctest.testmod()
