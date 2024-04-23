def calculate_total_price(unit_price, quantity, discount_coefficient, cashback):
    """
    Рассчитывает общую стоимость покупки с учетом скидки и кэшбэка.

    :param unit_price: Цена товара за штуку
    :param quantity: Количество товара
    :param discount_coefficient: Коэффициент снижения цены в зависимости от количества товара
    :param cashback: Значение кэшбэка
    :return: Общая стоимость покупки с учетом скидки и кэшбэка
    """
    discounted_price_per_unit = unit_price * (1 - discount_coefficient)  # Цена товара со скидкой за штуку
    total_price = discounted_price_per_unit * quantity  # Общая стоимость покупки без учета кэшбэка
    total_price_with_cashback = total_price - cashback  # Общая стоимость покупки с учетом кэшбэка
    return total_price_with_cashback


def choose_better_option(unit_price_1, unit_price_2, quantity, discount_coefficient, cashback):
    """
    Определяет, какой товар выгоднее купить.

    :param unit_price_1: Цена первого товара за штуку
    :param unit_price_2: Цена второго товара за штуку
    :param quantity: Количество товара
    :param discount_coefficient: Коэффициент снижения цены в зависимости от количества товара
    :param cashback: Значение кэшбэка
    :return: Название товара (1 или 2), который выгоднее купить
    """
    total_price_1 = calculate_total_price(unit_price_1, quantity, discount_coefficient, cashback)
    total_price_2 = calculate_total_price(unit_price_2, quantity, discount_coefficient, cashback)

    if total_price_1 < total_price_2:
        return "Товар 1"
    elif total_price_2 < total_price_1:
        return "Товар 2"
    else:
        return "Оба товара имеют одинаковую стоимость"
