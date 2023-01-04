import product
import pytest

class TestProduct():
    def test_create(self):
        p = product.Product("MINT",250,340.80)
        assert p.name == "MINT"
        assert p.quant == 250
        assert p.price == 340.80

    def test_quant(self):
        p = product.Product("MINT",250,340.80)
        assert p.quant == 250
        p.quant = 500
        assert p.quant == 500

    def test_quant_fail(self):
        p = product.Product("MINT",250,340.80)
        assert p.quant == 250
        with pytest.raises(TypeError) as e:
            p.quant = "hello"
