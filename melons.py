"""Classes for melon orders."""

class AbstractMelonOrder():
    """Abstract melon order"""

    def __init__(self, species, qty, order_type, tax):
        """Initialize attributes"""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False      



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        
        if self.species == "Christmas melon":
            base_price = base_price * 1.5
            
        total = (1 + self.tax) * self.qty * base_price

        if self.species == "International" and self.qty < 10: 
            total += 3 

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    class GovernmentMelonOrder(AbstractMelonOrder):
        """Government is buying melons"""

        def __init__(self, species, qty):
            super().__init__(species, qty, "government", 0.0)
            self.passed_inspection = False 

        def mark_inspection(self, passed):
            """Record wheter the melon order has passed inspection"""
            self.passed_inspection = passed
        