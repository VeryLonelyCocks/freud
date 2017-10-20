from aiohttp import web
import asyncio
import os

PORT = 3000

async def main_page(request):
    """
    Web App function for processing callback
    """
    return web.Response(text='Freud is here')

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
app.router.add_get('/', main_page)
web.run_app(app, port=PORT)
