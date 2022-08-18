import string
import random
from typing import List  # add support for type hints in functions/methods
from abc import ABC, abstractmethod

# Example of using a Strategy Design Pattern.  This design pattern creates an interface which is used to perform
# different strategies.  Using abstract classes is a common method in OOP to enforce behavior with each new
# strategy class created from a parent class.


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class TicketOrderingStrategy(ABC):
    """Use Abstract Base Classes to define a set of classes that create different ordering strategies for the tickets.
    Inheriting from the ABC class and using the abstractmethod decorator enforces the implementation of the
    create_ordering method for each subsequent child class of TicketOrderingStrategy"""
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOorderingStrategy(TicketOrderingStrategy):
    """Child class of TicketOrderingStrategy that will take a list and return a list of elements in the same order."""
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()


class FILOorderingStrategy(TicketOrderingStrategy):
    """Child class of TicketOrderingStrategy that will take a list and return a list of elements in reverse order."""
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy.copy()


class RandomOrderingStrategy(TicketOrderingStrategy):
    """Child class of TicketOrderingStrategy that will take a list and return a list of elements in random order."""
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy

# To create a new strategy, simply define a new child class of TicketOrderingStrategy
class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    """Child class of TicketOrderingStrategy that will take a list and return an empty list."""
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return []



class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))


    # this the kind of behavior we want to improve with strategy design patterns.
    # Selecting a way to process each ticket results in a long if/elif/else sequence.
    # Instead, we can create an abstract class which defines the strategy to use
    # and call that in the process_tickets method instead.
    # def process_tickets(self, processing_strategy: str = "fifo"):
    #     # if it's empty don't do anything
    #     if len(self.tickets) == 0:
    #         print("There are no tickets to process. Well done!")
    #         return
    #
    #     if processing_strategy == "fifo":
    #         for ticket in self.tickets:
    #             self.process_ticket(ticket)
    #     elif processing_strategy == "filo":
    #         for ticket in reversed(self.tickets):
    #             self.process_ticket(ticket)
    #     elif processing_strategy == "random":
    #         list_copy = self.tickets.copy()
    #         random.shuffle(list_copy)
    #         for ticket in list_copy:
    #             self.process_ticket(ticket)

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        # Create the ordered list
        ticket_list = processing_strategy.create_ordering(self.tickets)  # Use TicketOrderingStrategy object to return abstract
        for ticket in ticket_list:
            self.process_ticket(ticket)

        # if it's empty don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

    def process_ticket(self, ticket: SupportTicket):
        print("===========================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue {ticket.issue}")
        print("===========================")

# Create the application
app = CustomerSupport()

# Register a few tickets
app.create_ticket("John Smith", "My comptuer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# Process the tickets
# app.process_tickets("filo")  # this will no longer work when using abstract classes to define strategy
# Change ticket ordering by selecting a different child class from TicketOrderingStrategy
app.process_tickets(FILOorderingStrategy())
