# pagamento.py
import random
import threading
import time


def processar_pagamento_async(pedido: dict) -> threading.Thread:
    def _worker():
        # Simula latência de rede entre 0.04s (40ms) e 0.12s (120ms)
        latencia = random.uniform(0.04, 0.12)
        time.sleep(latencia)
        pedido["status"] = "APROVADO"
        pedido["tempo_s"] = round(latencia, 3)

    thread = threading.Thread(target=_worker)
    thread.start()
    return thread