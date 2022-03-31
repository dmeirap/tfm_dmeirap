CONECTAR LA BATERIA Y LA PIXHAWK A LA JETSON XAVIER

--- TERMINAL 1 ---

~/catkin_ws/src/tfm/real/launch
sudo chmod 777 /dev/ttyUSB0
roslaunch real_planner.launch 


--- TERMINAL 2 ---

cd ~/.local/lib/python3.6/site-packages/mavsdk/bin 
./mavsdk_server -p 50051 serial:///dev/ttyUSB0  


--- TERMINAL 3 ---
python3 mision.py 
