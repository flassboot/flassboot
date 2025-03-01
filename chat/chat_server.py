
import asyncio
import websockets

connected_clients = set()

async def chat_handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(chat_handler, "0.0.0.0", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
