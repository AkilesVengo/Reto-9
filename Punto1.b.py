n_gallinas = int(input("Ingrese la cantidad de gallinas: "))
m_gallos = int(input("Ingrese la cantidad de gallos: "))
k_pollitos = int(input("Ingrese la cantidad de pollitos: "))
cantidad_carne_aves = lambda n_gallinas, m_gallos, k_pollitos: (n_gallinas * 6) + (m_gallos * 7) + (k_pollitos * 1)

cantidad_carne = cantidad_carne_aves(n_gallinas, m_gallos, k_pollitos)

print("La cantidad de carne de aves es:", cantidad_carne, "kilos.")