import pytest
from black_hole import BuracoNegro, c
import math

def test_raio_schwarzschild_massa_valida():
    """Testa se o raio de Schwarzschild é calculado corretamente para uma massa válida."""
    bn = BuracoNegro(1.989e30)  # Massa do Sol em kg
    assert math.isclose(bn.raio_schwarzschild(), 2950, rel_tol=0.01) # Tolerância de 1%

def test_densidade_valida():
    """Testa se a densidade do buraco negro é positiva e fisicamente plausível."""
    bn = BuracoNegro(1.989e30)  # Massa do Sol em kg
    assert bn.densidade() > 0  # A densidade deve ser positiva

def test_velocidade_escape():
    """Testa se a velocidade de escape no horizonte de eventos é igual à velocidade da luz."""
    bn = BuracoNegro(1.989e30)  # Massa do Sol em kg
    assert bn.velocidade_escape() == pytest.approx(c, rel=1e-3)

def test_massa_invalida():
    """Testa se o código lança exceção para massa inválida (negativa ou zero)."""
    with pytest.raises(ValueError):
        BuracoNegro(-1.0)  # Massa negativa
        
    with pytest.raises(ValueError):
        BuracoNegro(0)  # Massa zero
        
def test_massa_extremamente_grande():
    """Testa o cálculo do raio e densidade para uma massa extremamente grande (buraco negro supermassivo)."""
    bn = BuracoNegro(1e40)  # Massa muito grande
    assert bn.raio_schwarzschild() > 0
    assert bn.densidade() > 0
    assert bn.velocidade_escape() == pytest.approx(c, rel=1e-3)

def test_massa_extremamente_pequena():
    """Testa o cálculo do raio e densidade para uma massa extremamente pequena (buraco negro primordial)."""
    bn = BuracoNegro(1e10)  # Massa muito pequena
    assert bn.raio_schwarzschild() > 0
    assert bn.densidade() > 0
    assert bn.velocidade_escape() == pytest.approx(c, rel=1e-3)

