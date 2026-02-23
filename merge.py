# A -> Arreglo
# p -> indice inicio
# q -> indice mitad
# r -> indice fin

# async nos indica que esto es una corutina
async def merge(A, p, q, r):
    # Tamaño del subarreglo izquierdo
    nL = q - p + 1 

    # Tamaño del subarreglo derecho
    nR = r - q

    # Subarreglo izquiero copiando desde p hasta q
    L = A[p:q + 1]

    # Subarreglo derecho copiando desde q+1 hasta r
    R = A[q+1:r+1]

    i = 0 # i recorrera L
    j = 0 # j recorrera R
    k = p # k recorrera A

    # mientras haya elementos en L y R
    while i < nL and j < nR:
        # Si el elemento izquierdo es menor
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else: # Si el elemento derecho es menor
            A[k] = R[j]
            j += 1
    
    # Si quedan elementos en L
    while i < nL
        # Copiamos lo que quede en L
        A[k] = L[i]
        i += 1
        k += 1
    
    # Si quedan elementos en R
    while i < nR
        # Copiamos lo que quede en R
        A[k] = R[i]
        j += 1
        k += 1