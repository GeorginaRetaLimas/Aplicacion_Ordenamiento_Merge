import asyncio
from merge import merge

# A -> Arreglo
# p -> indice inicio
# r -> indice fin

async def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2

        # Creamos las tareas concurrentes
        tarea1 = asyncio.create_task(merge_sort(A, p, q))
        tarea2 = asyncio.create_task(merge_sort(A, q+1, r))

        # Esperamos a que ambas terminen
        await tarea1
        await tarea2

        # Ejecutar merge normalmente
        await merge (A, p, q, r)
