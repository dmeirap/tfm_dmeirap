#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():

    drone = System(mavsdk_server_address="localhost", port=50051)
    await drone.connect()

    print("Esperando la conexion del dron...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Dron conectado!")
            break

    print("Esperando la posicion global del dron...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            print("Posicion global estimada OK")
            break

    print("-- Arming")
    await drone.action.arm()
    
    print("-- Taking Off")
    await drone.action.takeoff()

    await asyncio.sleep(10)

    print("-- Landing")
    await drone.action.land()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
