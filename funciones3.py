#funcion lambda
saludarLambda = lambda nombre:print(f'hola {nombre} !')

saludarLambda('Amaia')

#funcion asincronica

import asyncio

async def saludo():
    print('Hola')
    await asyncio.sleep(4)
    print('mundo')

asyncio.run(saludo())
