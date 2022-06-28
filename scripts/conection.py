#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():

    drone = System(mavsdk_server_address="localhost", port=50051) 
    await drone.connect()

    print("Waiting for the conexion")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Dron conected")
            break

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
