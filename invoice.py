class Car:
    REGULAR = 0
    NEW_MODEL = 1

    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, arg):
        self._price_code = arg

    def get_title(self):
        return self._title


class Rental:
    def __init__(self, car, days_rented):
        self._car = car
        self._days_rented = days_rented

    def get_days_rented(self):
        return self._days_rented

    def get_car(self):
        return self._car


class Customer:
    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, rental):
        self._rentals.append(rental)

    def get_name(self):
        return self._name

    def invoice(self):
        total_amount = 0.0
        frequent_renter_points = 0
        result = f"Rental Record for {self.get_name()}\n"

        for rental in self._rentals:
            this_amount = 0.0

            # Determine amounts for each line
            if rental.get_car().get_price_code() == Car.REGULAR:
                this_amount += 5000 + rental.get_days_rented() * 9500
                if rental.get_days_rented() > 5:
                    this_amount -= (rental.get_days_rented() - 2) * 10000
            elif rental.get_car().get_price_code() == Car.NEW_MODEL:
                this_amount += 9000 + rental.get_days_rented() * 15000
                if rental.get_days_rented() > 3:
                    this_amount -= (rental.get_days_rented() - 2) * 10000

            # Add frequent renter points
            frequent_renter_points += 1

            # Add bonus for a two-day new release rental
            if rental.get_car().get_price_code() == Car.NEW_MODEL and rental.get_days_rented() > 1:
                frequent_renter_points += 1

            # Show figures for this rental
            result += f"\t{rental.get_car().get_title()}\t{this_amount / 100:.1f}\n"
            total_amount += this_amount

        # Add footer lines
        result += f"Amount owed is {total_amount / 100:.1f}\n"
        result += f"You earned {frequent_renter_points} frequent renter points\n"

        return result


# Examples of usage:
car1 = Car("Car 1", Car.REGULAR)
car2 = Car("Car 2", Car.NEW_MODEL)

rental1 = Rental(car1, 3)
rental2 = Rental(car2, 2)

customer = Customer("John Doe")
customer.add_rental(rental1)
customer.add_rental(rental2)

print(customer.invoice())
