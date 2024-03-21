class Participant:
    def __init__(self, name, chickenwings, hamburgers, hotdogs):
        self.name = name
        self.chickenwings = chickenwings
        self.hamburgers = hamburgers
        self.hotdogs = hotdogs

    def calculate_score(self):
        return self.chickenwings * 5 + self.hamburgers * 3 + self.hotdogs * 2

    def __repr__(self):
        return f"Participant(name='{self.name}', chickenwings={self.chickenwings}, hamburgers={self.hamburgers}, hotdogs={self.hotdogs})"