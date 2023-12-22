import numpy as np
import matplotlib.pyplot as plt


class Color:
    """
    Абстрактний клас з константами кольорів для зручності
    """
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    END = '\033[0m'


def y_null(y0, u, t, gamma):
    """
    Рівняння руху для початковою швидеості v = 0
    :param y0: початкова висота, з якої падає тіло
    :param u: гранична швидкість тіла
    :param t: час
    :param gamma: коефіцієнт, дорівнює m/k - маса тіла
    на коефіцієнт лобового опору
    :return: функція y(t)
    """
    return y0 - u * t + u / gamma * (1 - np.exp(-gamma * t))


def y_not_null(y0, u, v0, t, gamma):
    """
    Рівняння руху для початковою швидеості v = v0
    :param y0: початкова висота, з якої падає тіло
    :param u: гранична швидкість тіла
    :param v0: початкова швидкість, з якої падає тіло
    :param t: час
    :param gamma: коефіцієнт, дорівнює m/k - маса тіла
    на коефіцієнт лобового опору
    :return: функція y(t)
    """
    return y0 - u * t + (u - v0) / gamma * (1 - np.exp(-gamma * t))


def planets() -> float:
    """
    Метод виводить доступні планети, супутники чи зірки
    та дає користувачеві вибрати потрібне небесне тіло.
    :return: прискорення вільного падіння тіла
    """
    planets_list = {
        "Земля": 9.81,
        "Місяць": 1.62,
        "Венера": 8.88,
        "Юпітер": 24.79,
        "Уран": 8.86,
        "Сонце": 273.1,
        "Меркурій": 3.7,
        "Марс": 3.86,
        "Сатурн": 10.44,
        "Нептун": 11.09
    }
    for planet in planets_list.keys():
        print(Color.GREEN + "{:<8}".format(planet) + Color.END, end='\t')
    planet = ''
    while planet not in planets_list:
        planet = input("\nВведіть назву планети, на якій проходить падіння: ")
        if planet not in planets_list:
            print('Такої планети у списку немає!')
    g = planets_list[planet]
    return g


def shapes() -> float:
    """
    Метод виводить доступні форму тіла
    та дає користувачеві вибрати потрібну.
    :return: коефіцієнт лобового опору тіла
    """
    shapes_list = {
        "Сфера": 0.47,
        "Півсфера": 0.38,
        "Диск": 1.15,
        "Конус": 0.5,
        "Куб": 1.05,
        "Циліндр": 0.82,
        "Крапля": 0.04
    }
    for shape in shapes_list.keys():
        print(Color.CYAN + "{:<8}".format(shape) + Color.END, end='\t')
    shape = ''
    while shape not in shapes_list:
        shape = input("\nВведіть назву форми тіла: ")
        if shape not in shapes_list:
            print('Такої форми у списку немає!')
    k = shapes_list[shape]
    return k


if __name__ == '__main__':
    v1_0 = float(input("Введіть початкову швидкість для першого графіку: "))
    v2_0 = float(input("Введіть початкову швидкість для другого графіку: "))
    y0 = float(input("Введіть початкову висоту, з якої падає тіло (м): "))
    g = planets()
    m = float(input("Введіть масу тіла (кг): "))
    k = shapes()
    t_max = float(input("Введіть тривалість часу падіння (с): "))
    t = np.linspace(0, t_max, 100)
    gamma = k / m
    u = g / gamma
    if v1_0 == 0:
        y1 = y_null(y0, u, t, gamma)
        min1 = y_null(y0, u, t_max, gamma)
    else:
        y1 = y_not_null(y0, u, v1_0, t, gamma)
        min1 = y_not_null(y0, u, v1_0, t_max, gamma)
    if v2_0 == 0:
        y2 = y_null(y0, u, t, gamma)
        min2 = y_null(y0, u, t_max, gamma)
    else:
        y2 = y_not_null(y0, u, v2_0, t, gamma)
        min2 = y_not_null(y0, u, v2_0, t_max, gamma)

    fig, ax = plt.subplots()
    ax.plot(t, y1, 'powderblue', label="Початкова швидкість " + r"$\upsilon$" + f" = {v1_0} " + r"$\frac{м}{с}$")
    ax.plot(t, y2, 'lightcoral', label="Початкова швидкість " + r"$\upsilon$" + f" = {v2_0} " + r"$\frac{м}{с}$")
    ax.legend()
    ax.set_xlabel('Час t (c)', fontsize=18)
    ax.set_ylabel('Відстань падіння y (м)', fontsize=18)
    if min1 <= 0 or min2 <= 0:
        ax.set_ylim(0)
    plt.show()
