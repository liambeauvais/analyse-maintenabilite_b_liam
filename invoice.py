from enum import Enum


class CarTypeAmount(Enum):
    REGULAR = {"initial_price": 5000, "per_day_price": 9500}
    NEW_MODEL = {"initial_price": 9000, "per_day_price": 15000}


class Car:

    def __init__(self, title, price_code: CarTypeAmount):
        self._title = title
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, arg):
        self._price_code = arg

    def get_title(self):
        return self._title


class Rental:
    def __init__(self, car: Car, days_rented: int):
        self._car = car
        self._days_rented = days_rented

    def get_days_rented(self):
        return self._days_rented

    def get_car(self):
        return self._car

    def get_rental_amount(self):
        rental_amount = 0.0
        price_codes = self._car.get_price_code()
        rental_amount += price_codes.value["initial_price"] + self.get_days_rented() * price_codes.value[
            "per_day_price"]

        if self.get_days_rented() > 3:
            rental_amount -= (self.get_days_rented() - 2) * 10000

        return rental_amount


class Invoice:
    def __init__(self, rentals: list[Rental]):
        self.renter_points = 0
        self.rentals = rentals

    def as_pdf(self):
        pass

    def as_json(self):
        pass


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

            # Add frequent renter points
            frequent_renter_points += 1

            # Add bonus for a two-day new release rental
            if rental.get_car().get_price_code() == CarTypeAmount.NEW_MODEL and rental.get_days_rented() > 1:
                frequent_renter_points += 1

            # Show figures for this rental
            result += f"\t{rental.get_car().get_title()}\t{rental.get_rental_amount() / 100:.1f}\n"
            total_amount += rental.get_rental_amount()

        # Add footer lines
        result += f"Amount owed is {total_amount / 100:.1f}\n"
        result += f"You earned {frequent_renter_points} frequent renter points\n"

        return result


# Examples of usage:
car1 = Car("Car 1", CarTypeAmount.REGULAR)
car2 = Car("Car 2", CarTypeAmount.NEW_MODEL)

rental1 = Rental(car1, 3)
rental2 = Rental(car2, 2)

customer = Customer("John Doe")
customer.add_rental(rental1)
customer.add_rental(rental2)

print(customer.invoice())
