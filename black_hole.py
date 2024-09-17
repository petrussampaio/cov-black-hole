import math

# Constantes Físicas
G = 6.67430e-11  # Constante gravitacional em m^3 kg^-1 s^-2
c = 2.998e8  # Velocidade da luz em m/s

class BuracoNegro:
    def __init__(self, massa):
        if massa <= 0:
            raise ValueError("A massa deve ser maior que zero.")
        self.massa = massa  # Massa em kg
    
    def raio_schwarzschild(self):
        """Calcula o raio de Schwarzschild com base na massa do buraco negro."""
        return 2 * G * self.massa / c ** 2
    
    def densidade(self):
        """Calcula a densidade dentro do horizonte de eventos, assumindo a forma esférica."""
        r_s = self.raio_schwarzschild()
        volume = (4/3) * math.pi * r_s**3
        return self.massa / volume
    
    def velocidade_escape(self):
        """Calcula a velocidade de escape no horizonte de eventos (igual à velocidade da luz)."""
        r_s = self.raio_schwarzschild()
        return math.sqrt(2 * G * self.massa / r_s)
