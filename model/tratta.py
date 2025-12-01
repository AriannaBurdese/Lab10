from dataclasses import dataclass
@dataclass
class Tratta:
    id_hub_origine: int
    id_hub_destinazione: int
    guadagno_medio : float

    def __str__(self):
         return f"{self.id_hub_origine, self.id_hub_destinazione, self.guadagno_medio}"

    def __repr__(self):
        return f"{self.id_hub_origine, self.id_hub_destinazione, self.guadagno_medio}"