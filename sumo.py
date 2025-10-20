import traci

sumoBinary = "sumo-gui"
traci.start([sumoBinary,"-c","osm.sumocfg"]);

for step in range(1000):
    traci.simulationStep();
    print("Vehicles:", traci.vehicle.getIDList())
traci.close()
