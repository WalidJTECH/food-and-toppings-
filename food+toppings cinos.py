from typing import List, Dict, Union

class Drink:
    """Class to represent a drink with a single base and multiple flavors."""

    _valid_bases = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    _valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']

    def __init__(self) -> None:
        """Initialize a drink with no base and no flavors."""
        self._base: Union[str, None] = None
        self._flavors: set[str] = set()

    def get_base(self) -> Union[str, None]:
        return self._base

    def get_flavors(self) -> List[str]:
        return list(self._flavors)

    def get_num_flavors(self) -> int:
        return len(self._flavors)

    def add_base(self, base: str) -> None:
        if self._base is not None:
            raise ValueError("A base has already been added.")
        if base not in self._valid_bases:
            raise ValueError(f"Invalid base: {base}. Valid options: {self._valid_bases}")
        self._base = base

    def add_flavor(self, flavor: str) -> None:
        if flavor not in self._valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}. Valid options: {self._valid_flavors}")
        if flavor in self._flavors:
            raise ValueError(f"Flavor '{flavor}' has already been added.")
        self._flavors.add(flavor)

    def set_flavors(self, flavors: List[str]) -> None:
        self._flavors.clear()
        for flavor in flavors:
            self.add_flavor(flavor)


class Food:
    """Class to represent a food item with optional toppings."""

    _valid_food_items: Dict[str, float] = {
        'Hotdog': 2.30,
        'Corndog': 2.00,
        'Ice Cream': 3.00,
        'Onion Rings': 1.75,
        'French Fries': 1.50,
        'Tater Tots': 1.70,
        'Nacho Chips': 1.90
    }
    _valid_toppings: Dict[str, float] = {
        'Cherry': 0.00,
        'Whipped Cream': 0.00,
        'Caramel Sauce': 0.50,
        'Chocolate Sauce': 0.50,
        'Nacho Cheese': 0.30,
        'Chili': 0.60,
        'Bacon Bits': 0.30,
        'Ketchup': 0.00,
        'Mustard': 0.00
    }

    def __init__(self, food_item: str) -> None:
        if food_item not in self._valid_food_items:
            raise ValueError(f"Invalid food item: {food_item}.")
        self._food_item: str = food_item
        self._base_price: float = self._valid_food_items[food_item]
        self._toppings: Dict[str, float] = {}

    def get_food_type(self) -> str:
        return self._food_item

    def get_price(self) -> float:
        return self._base_price + sum(self._toppings.values())

    def add_topping(self, topping: str) -> None:
        if topping not in self._valid_toppings:
            raise ValueError(f"Invalid topping: {topping}.")
        self._toppings[topping] = self._valid_toppings[topping]

    def get_toppings(self) -> List[str]:
        return list(self._toppings.keys())

    def generate_receipt(self) -> str:
        lines = [f"{self._food_item}"]
        lines.append(f"- Base Price: ${self._base_price:.2f}")
        for topping, cost in self._toppings.items():
            lines.append(f"- {topping}: ${cost:.2f}")
        lines.append(f"Total: ${self.get_price():.2f}")
        return "\n".join(lines)


class Order:
    """Class to manage a collection of food and drink items."""

    def __init__(self) -> None:
        self._items: List[Union[Drink, Food]] = []

    def get_items(self) -> List[Union[Drink, Food]]:
        return self._items

    def get_num_items(self) -> int:
        return len(self._items)

    def get_total(self) -> float:
        total = 0.0
        for item in self._items:
            if isinstance(item, Drink):
                total += 5.00  # Fixed price per drink
            elif isinstance(item, Food):
                total += item.get_price()
        return total

    def get_receipt(self) -> str:
        if not self._items:
            return "Order is empty. Add some items!"

        receipt_lines = ["--- Order Receipt ---"]
        for idx, item in enumerate(self._items, 1):
            if isinstance(item, Drink):
                receipt_lines.append(
                    f"{idx}. Drink - Base: {item.get_base() or 'None'}, Flavors: {', '.join(item.get_flavors()) or 'None'}"
                )
            elif isinstance(item, Food):
                receipt_lines.append(f"{idx}. {item.generate_receipt()}")
        receipt_lines.append(f"Total Items: {self.get_num_items()}")
        receipt_lines.append(f"Total Cost: ${self.get_total():.2f}")
        return "\n".join(receipt_lines)

    def add_item(self, item: Union[Drink, Food]) -> None:
        if not isinstance(item, (Drink, Food)):
            raise TypeError("Invalid item. Only Drink or Food objects are allowed.")
        self._items.append(item)

    def remove_item(self, index: int) -> None:
        if index < 0 or index >= len(self._items):
            raise IndexError("Invalid index. No item removed.")
        self._items.pop(index)
