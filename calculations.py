"""

SUM = X * (1 + %)**n
где
SUM — конечная сумма;
X — начальная сумма;
% — процентная ставка, процентов годовых /100;
n — количество периодов, лет (месяцев, кварталов).

"""


def compound_interest(initial_amount, percentage, period):
    total = initial_amount * (1 + percentage) ** period
    return total


print(compound_interest(10000, 10, 1))

"""

SUM = X * (1 + %)**n
где
SUM — конечная сумма;
X — начальная сумма;
% — процентная ставка, процентов годовых /100;
n — количество периодов, лет (месяцев, кварталов).

"""


def compound_interest_replenish(initial_amount, percentage, period):
    total = initial_amount * (1 + percentage) ** period
    return total


print(compound_interest_replenish(10000, 9.5, 1))
