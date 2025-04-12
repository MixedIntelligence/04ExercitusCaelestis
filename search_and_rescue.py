import time

class Drone:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.status = "idle"

    def deploy(self, disaster_zone):
        """Deploy the drone to a disaster zone."""
        self.status = "deployed"
        self.location = disaster_zone
        print(f"Drone {self.id} deployed to {disaster_zone}")

    def perform_search_and_rescue(self):
        """Perform search and rescue operations."""
        if self.status == "deployed":
            print(f"Drone {self.id} is performing search and rescue.")
            time.sleep(2)
            print(f"Drone {self.id} completed search and rescue.")
        else:
            print(f"Drone {self.id} is not deployed.")

# Example usage
if __name__ == "__main__":
    drone1 = Drone(id=1, location="base")
    drone1.deploy("Zone A")
    drone1.perform_search_and_rescue()
