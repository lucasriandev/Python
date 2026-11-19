# test_pagamento.py
import time
import unittest
from pagamento import processar_pagamento_async


class TestPagamentoFlaky(unittest.TestCase):
    def test_deve_aprovar_pagamento_rapidamente(self):
        pedido = {"id": 101, "status": "PENDENTE"}

        # Dispara o processamento em outra thread
        processar_pagamento_async(pedido)

        # ERRO CLÁSSICO: chute de tempo fixo (80ms)
        time.sleep(0.08)

        # Se a latência sorteada foi maior que 0.08s, o status ainda será "PENDENTE"
        self.assertEqual(pedido["status"], "APROVADO")


if __name__ == "__main__":
    unittest.main()