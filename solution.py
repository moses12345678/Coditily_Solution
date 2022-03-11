def solution(A,K):
    if K==0:
        return A
    if len(A)==0:
        return []
    lt = [] # rotation list init a 0
    while K>0:
        j = A[-1]
        lt[0] = j # assigne last element of A to lt
        gr = lt[0]+A[0:-1]
        A= gr
        lt =[]
        K-=1
    return gr