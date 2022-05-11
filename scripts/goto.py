#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():
    
    drone = System(mavsdk_server_address="localhost", port=50051)
    await drone.connect()

    print("Esperando la conexion del dron")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Dron conectado!")
            break
    print("Esperando la posicion global del dron")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            print("Posicion global estimada OK")
            break

    #print("Fetching amsl altitude at home location....")
    async for terrain_info in drone.telemetry.home():
        absolute_altitude = terrain_info.absolute_altitude_m
        break

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(1)
    # To fly drone 20m above the ground plane
    flying_alt = absolute_altitude + 3.0
    # goto_location() takes Absolute MSL altitude
    await drone.action.goto_location(40.333141, -3.766982, flying_alt, 10)

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
