import time
from souls.agent import AutonomousAgent
from loosh.emotional_monitor import EmotionalMonitor
from exercitus.caelestis import DefenseOrchestrator

# Initialize components
agent = AutonomousAgent(id="Drone01", location="Base")
emotional_monitor = EmotionalMonitor()
orchestrator = DefenseOrchestrator()

def main():
    print("Initializing Exercitus Caelestis system...")

    # Step 1: Monitor emotional states using Loosh
    emotional_state = emotional_monitor.get_emotional_state()
    print(f"Current emotional state: {emotional_state}")

    # Step 2: Orchestrator evaluates the situation
    threat_level = orchestrator.evaluate_threat(emotional_state)
    print(f"Threat level detected: {threat_level}")

    # Step 3: Deploy agents via Souls if necessary
    if threat_level > orchestrator.THREAT_THRESHOLD:
        orchestrator.deploy_agent(agent, location="Disaster Zone")
        agent.perform_mission()
    else:
        print("No significant threat detected. Standby mode.")

    print("System cycle complete.")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(10)  # Repeat every 10 seconds
