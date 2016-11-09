import asyncio
from aiohttp import web

async def hello_world(request):
    print(request.url)
    return web.Response(text="hello world")

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
app.router.add_get('/', hello_world)
