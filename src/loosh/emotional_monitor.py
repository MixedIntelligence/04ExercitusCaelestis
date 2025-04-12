class EmotionalMonitor:
    def __init__(self):
        self.emotional_state = "calm"

    def get_emotional_state(self):
        """Simulate the detection of emotional states."""
        # For demonstration, we toggle between calm and anxious
        self.emotional_state = "anxious" if self.emotional_state == "calm" else "calm"
        return self.emotional_state
