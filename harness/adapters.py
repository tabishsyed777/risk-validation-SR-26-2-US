class FixtureModel:
    """Deterministic stand-in; replace with an approved inference adapter."""
    def __init__(self, name): self.name = name
    def predict(self, text):
        lowered = text.lower()
        if self.name == "challenger":
            if "vpn" in lowered: return "SOFTWARE"
            if "invoice" in lowered: return "BILLING"
        if any(x in lowered for x in ("sign in", "password", "two-factor")): return "ACCESS"
        if any(x in lowered for x in ("invoice", "charge", "credit card")): return "BILLING"
        if any(x in lowered for x in ("battery", "monitor", "keyboard")): return "HARDWARE"
        if any(x in lowered for x in ("vpn", "wi-fi", "wifi", "network")): return "NETWORK"
        return "SOFTWARE"
