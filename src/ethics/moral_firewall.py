class MoralFirewall:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        """Add an ethical rule to the firewall."""
        self.rules.append(rule)

    def evaluate_action(self, action):
        """Evaluate an action against the moral rules."""
        for rule in self.rules:
            if not rule(action):
                return False
        return True

# Example rules
def no_lethal_force(action):
    return action.get("type") != "lethal"

def prioritize_human_life(action):
    return action.get("target") != "human"

# Example usage
if __name__ == "__main__":
    firewall = MoralFirewall()
    firewall.add_rule(no_lethal_force)
    firewall.add_rule(prioritize_human_life)

    action = {"type": "non-lethal", "target": "structure"}
    print("Action allowed:", firewall.evaluate_action(action))
