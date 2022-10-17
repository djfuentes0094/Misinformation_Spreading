class Operators:
    def __init__(self, person1:dict, person2:dict):
        self.person1 = person1
        self.person2 = person2
    
    def opinion_interaction(self):
        for opinion in range(len(self.person1["opinions"])):
            self.person1["opinions"][opinion] = self.person2["convincing"] * self.person1["susceptibility"] * self.person2["opinions"][opinion] + self.person1["opinions"][opinion]
            # print(opinion)