# Einfaches Koordinaten-Programm
import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distanz_zum_ursprung(self):
        """Berechnet die Distanz zum Ursprung (0, 0)"""
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):
        return f"Punkt({self.x}, {self.y})"


# Beispiel-Nutzung
if __name__ == "__main__":
    p1 = Punkt(3, 4)
    p2 = Punkt(5, 12)
    
    print(f"{p1} - Distanz zum Ursprung: {p1.distanz_zum_ursprung()}")
    print(f"{p2} - Distanz zum Ursprung: {p2.distanz_zum_ursprung()}")
