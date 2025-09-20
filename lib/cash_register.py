#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []
    self._last_transaction = 0.0

  def add_item(self, title, price, quantity=1):
    line_total = price * quantity
    self.total += line_total
    self.items.extend([title] * quantity)
    self._last_transaction = line_total

  def apply_discount(self):
    if self.discount and self.discount != 0:
      self.total = self.total * (100 - self.discount) / 100
      shown = int(self.total) if float(self.total).is_integer() else self.total
      print(f"After the discount, the total comes to ${shown}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self._last_transaction
    if self.total < 0:
      self.total = 0.0
    self._last_transaction = 0.0
