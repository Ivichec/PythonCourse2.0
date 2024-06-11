"""test.assert_equals(rental_car_cost(1),40)
        test.assert_equals(rental_car_cost(4),140)
        test.assert_equals(rental_car_cost(7),230)
        test.assert_equals(rental_car_cost(8),270)"""
def rental_car_cost(d):
    if 3 <= d <= 6:
        total = d * 40 -20
    elif d >= 7:
        total = d * 40 -50
    else:
        total = d * 40

    return total

print(rental_car_cost(4))