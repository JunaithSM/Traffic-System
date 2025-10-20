# Traffic System

## Clone Repository

Make sure git is installed [git](http://git-scm.com/downloads/)
```bash
git clone https://github.com/JunaithSM/Traffic-System.git
cd Traffic-System
```
## Start the SUMO.

[Install Sumo](https://sumo.dlr.de/docs/Installing/index.html) then run this command. 
**Start SUMO**
1. Open a terminal on your computer.
2. Run SUMO in server mode on a specific port (e.g., 8813):

```bash
sumo -c osm.sumocfg --remote-port $PORT
```

* `-c` specifies your SUMO config file.
* `--remote-port` is the port where TraCI listens. You can choose any free port.
* `$PORT` replace with the port number (e.g., 8813)
* This will start SUMO and wait for TraCI connections from your Python code.
⚠️ If you want to see the GUI, use sumo-gui instead of sumo.

## Ngork 
Colab runs on a remote server, so it cannot directly connect to localhost on your PC. You need to expose your port:
We need to connect the local sumo to the web server by using `ngrok`

1. Install ngrok locally: https://ngrok.com/
2. Start an ngrok tunnel to your TraCI port:

```bash
ngrok tcp $PORT
```
* ngrok will give you a public address like 0.tcp.ngrok.io:12345.
* Note down the hostname and port (12345 in this example).

## Google Collab

In google Colab open the `TrafficSystem.ipynb`

