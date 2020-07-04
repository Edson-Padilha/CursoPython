import matplotlib.pyplot as pyplot

def jur_comp(tempo,capital,taxa):
    taxa = taxa / 100
    montante = capital * (1+ taxa) ** tempo
    return round(montante, 2)

tempo = [x for x in range(48)]