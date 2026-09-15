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