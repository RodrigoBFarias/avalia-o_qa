from calculadora import calcular_desconto


def test_compra_abaixo_de_100():
    assert calcular_desconto(50, "COMUM") == 0


def test_compra_exatamente_100():
    assert calcular_desconto(100, "COMUM") == 10


def test_compra_entre_100_e_500():
    assert calcular_desconto(300, "COMUM") == 30


def test_compra_exatamente_500():
    assert calcular_desconto(500, "COMUM") == 100


def test_compra_acima_de_500():
    assert calcular_desconto(600, "COMUM") == 120


def test_vip_abaixo_de_100():
    assert calcular_desconto(50, "VIP") == 2.50


def test_vip_entre_100_e_500():
    assert calcular_desconto(300, "VIP") == 45


def test_vip_minusculo():
    assert calcular_desconto(300, "vip") == 45


def test_vip_exatamente_500():
    assert calcular_desconto(500, "VIP") == 125


def test_teto_desconto():
    assert calcular_desconto(2000, "COMUM") == 200


def test_teto_desconto_vip():
    assert calcular_desconto(2000, "VIP") == 200