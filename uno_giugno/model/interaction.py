from dataclasses import dataclass


@dataclass
class Interaction:
    GeneID1: str
    GeneID2: str
    Expression_Corr: float

    def __str__(self):
        return f"{self.GeneID1} <-> {self.GeneID2} | Corr.: {self.Expression_Corr}"

    def __hash__(self):
        return hash((self.GeneID1, self.GeneID2))