from dataclasses import dataclass, field

@dataclass
class Vaga:
    nome: str
    skills: list = field(default_factory=list)


