from aiohttp import web
import asyncio

PORT = 3000

async def vk_callback(request):
    """
    Web App function for processing callback
    """
    try:
        data = await request.json()
        print(data)
    except Exception as e:
        print("Message process error: [%s]" % e)

    return web.Response(text='Ok')

async def main_page(request):
    return web.Response(text='Shive is alive')

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
app.router.add_get('/', main_page)
app.router.add_post('/vk', vk_callback)
web.run_app(app, port=PORT)
