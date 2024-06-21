from invoice import CarTypeAmount, Rental, Customer, Car


def test_invoice():
    car1 = Car("Car 1", CarTypeAmount.REGULAR)
    car2 = Car("Car 2", CarTypeAmount.NEW_MODEL)

    rental1 = Rental(car1, 3)
    rental2 = Rental(car2, 2)

    customer = Customer("John Doe")
    customer.add_rental(rental1)
    customer.add_rental(rental2)

    customer_invoice = customer.invoice()
    assert customer_invoice == ("Rental Record for John Doe\n\tCar 1	335.0\n\tCar 2	390.0\nAmount owed is 725.0\nYou "
                                "earned 3 frequent renter points\n")
