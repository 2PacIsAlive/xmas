INSTALL_PCAPY="pip install pcapy"
CLONE_MALTRAIL="git clone https://github.com/stamparm/maltrail.git"
CHANGE_DIR="cd maltrail"
RUN_SENSOR="sudo python sensor.py"
RUN_SERVER="osascript run_server.scpt"
BACK_DIR="cd .."
OPEN_SERVER="open http://0.0.0.0:8338/ -a Google\ Chrome"
echo "\ninstalling packet capture library..."
eval $INSTALL_PCAPY
echo "\ncloning maltrail..."
eval $CLONE_MALTRAIL
eval $CHANGE_DIR
echo "\nrunning sensor..."
eval $RUN_SENSOR
echo "\nstarting server..."
eval $BACK_DIR 
eval $RUN_SERVER
echo "\nopening HTTP server..."
eval $OPEN_SERVER
