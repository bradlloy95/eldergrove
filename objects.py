class Region:
    def __init__(self, name, direction, description):
        self.name = name
        self.direction = direction
        self.description = description

    def __repr__(self):
        return f"{self.name} ({self.direction})\n" f"{self.description}"

    def __repr__(self):
        return f"{self.name} ({self.direction})\n" f"{self.description}"


# regions
frostviel_peaks = Region(
    "Frostviel Peaks",
    "Northen Region",
    "A harsh, icy mountain range, home to secluded tribes and ancient secrets buried beneath the ice.",
)

eldergrove = Region(
    "Eldergrove",
    "Eastern Region",
    "An enchanted, mystical forest where nature is alive with magic, and the trees seem to shift and change.",
)

ashen_dunes = Region(
    "Ashen Dunes",
    "Southern Region",
    "A barren desert filled with ancient ruins, forgotten temples, and dangerous nomadic tribes.",
)

verdantia_fields = Region(
    " Verdantia Fields",
    "Western Region",
    "A fertile land of rivers, villages, and rolling hills, rich in history and culture.",
)
print(ashen_dunes)
