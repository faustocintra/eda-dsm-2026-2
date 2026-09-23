def fmt_tempo(segundos) -> str:
    """Formata o valor em segundos retornado por time.perf_counter()
       adequando-o para a leitura e interpetação por seres humanos

    Args:
        segundos (int): o valor em segundos a ser formatado

    Returns:
        string: o valor em minutos, segundos, milissegundos ou
        microssegundos, ajustado conforme escala, formatado como
        texto
    """
    if segundos < 0.001:
        return f"{segundos * 1_000_000:.2f} µs"
    if segundos < 1:
        return f"{segundos * 1_000:.2f} ms"
    if segundos < 60:
        return f"{segundos:.2f} s"

    minutos, segundos = divmod(segundos, 60)
    return f"{int(minutos)} min {segundos:.2f} s"

def fmt_memoria(inicial : float, final: float, pico : float):
    """Formata os valores de medição de memória de tracemalloc()
           adequando-os para a leitura e interpetação por seres humanos
    
        Args:
            inicial (float): memória ocupada ao início da medição
            final (float): memória ocupada ao final da medição
            pico (float): máximo de memória ocupada durante a medição
    
        Returns:
            (string, string): tupla com valores formatados, representando
                o pico de memória adicional causado pela execução mensurada
                e a memória adicional ocupada ao final da execução mensurada
        """
    mib : int = 1024 ** 2
    pico_fmtd : str = f"{(pico - inicial) / mib:.2f} MiB"
    adic_fmtd : str = f"{(final - inicial) / mib:.2f} MiB"

    return pico_fmtd, adic_fmtd
