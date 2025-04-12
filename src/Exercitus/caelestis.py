class DefenseOrchestrator:
    THREAT_THRESHOLD = 5

    def evaluate_threat(self, emotional_state):
        """Evaluate the threat level based on emotional state and other data."""
        if emotional_state == "anxious":
            return 7  # High threat
        return 3  # Low threat

    def deploy_agent(self, agent, location):
        """Deploy an agent to a specific location."""
        print(f"Deploying {agent.id} to {location}.")
        agent.deploy(location)
