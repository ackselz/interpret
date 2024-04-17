import asyncio
import websockets
import socket

# HOST_NAME = socket.gethostbyname(socket.gethostname())
HOST_NAME = '0.0.0.0'
PORT = 8001

# Set to store connected clients
connected_clients = set()

async def broadcast_message(message):
    """
    Broadcast a message to all connected clients.
    """
    for client in connected_clients:
        await client.send(message)

async def handle_client(websocket, path):
    """
    Handle a new client connection.
    """
    connected_clients.add(websocket)
    print('client connected')
    try:
        async for message in websocket:
            # Broadcast the received message to all other clients
            if message == 'ping':
                await websocket.send('pong')
            else:
                print('received: ', message)
                await broadcast_message(message)
    except websockets.ConnectionClosedOK:
        # Client disconnected, remove from the set
        print('client disconnected')
        connected_clients.remove(websocket)
    except websockets.ConnectionClosedError:
        print('client connection timeout')
        connected_clients.remove(websocket)


async def main():
    """
    Start the WebSocket server and listen for incoming connections.
    """
    async with websockets.serve(handle_client, HOST_NAME, PORT, ping_timeout=float('inf'), ping_interval=10):
        print(f"WebSocket server started on {HOST_NAME}:{PORT}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
