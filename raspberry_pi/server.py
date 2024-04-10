# import asyncio
# import websockets
# import random

# # List of words to stream
# words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# async def broadcast_words(websocket, path):
#     """
#     Broadcast a stream of words to the connected WebSocket client.
#     """
#     try:
#         while True:
#             # Pick a random word from the list
#             word = random.choice(words)
#             # Send the word to the client
#             await websocket.send(word)
#             # Wait for a short period before sending the next word
#             await asyncio.sleep(1)
#     except websockets.ConnectionClosedOK:
#         # Client disconnected, do nothing
#         pass

# async def main():
#     """
#     Start the WebSocket server and listen for incoming connections.
#     """
#     async with websockets.serve(broadcast_words, "localhost", 8001):
#         print("WebSocket server started on localhost:8001")
#         await asyncio.Future()  # run forever

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import websockets

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
    try:
        async for message in websocket:
            # Broadcast the received message to all other clients
            await broadcast_message(message)
    except websockets.ConnectionClosedOK:
        # Client disconnected, remove from the set
        connected_clients.remove(websocket)

async def main():
    """
    Start the WebSocket server and listen for incoming connections.
    """
    async with websockets.serve(handle_client, "localhost", 8001):
        print("WebSocket server started on localhost:8001")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())