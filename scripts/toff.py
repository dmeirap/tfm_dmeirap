#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():

    drone = System(mavsdk_server_address="localhost", port=50051)
    await drone.connect()

    status_text_task = asyncio.ensure_future(print_status_text(drone))

    print("Esperando la conexion del dron...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Dron conectado!")
            break

    print("Esperando la posicion global del dron...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("Posicion global estimada OK")
            break

    print("-- Arming")
    await drone.action.arm()
    
    print("-- Taking Off")
    await drone.action.takeoff()

    await asyncio.sleep(15)

    print("-- Landing")
    await drone.action.land()

    status_text_task.cancel()

    async def print_status_text(drone)
	try:
		async for status_text in drone.telemetry.status_text():
			print(f"Status: {status_text.type}: {status_text.text}")
	except asyncio.CancelledError:
		return


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
