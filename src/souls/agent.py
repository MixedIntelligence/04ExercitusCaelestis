class AutonomousAgent:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.status = "idle"

    def deploy(self, location):
        """Deploy the agent to a specific location."""
        self.location = location
        self.status = "deployed"
        print(f"{self.id} deployed to {location}")

    def perform_mission(self):
        """Perform the assigned mission."""
        if self.status == "deployed":
            print(f"{self.id} is executing its mission at {self.location}.")
        else:
            print(f"{self.id} is not deployed. Cannot perform mission.")
