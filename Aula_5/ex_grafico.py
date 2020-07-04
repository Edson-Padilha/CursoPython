import matplotlib.pyplot as plt

tempo = [x for x in range(100)]
#montante = capital * (1+ taxa)** tempo
montante = [round (100*(1+0.3)**t,2) for t in tempo]
tam_mont = len(montante)

if len(tempo) == tam_mont:
    plt.plot(tempo, montante)
    plt.show()
