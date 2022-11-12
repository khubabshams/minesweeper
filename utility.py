from rich.console import Console
from rich.markdown import Markdown
from termcolor import colored
from pyfiglet import Figlet
import time


class FeedbackMixin:

    def print_colored_message(self, message: str, color: str = "white",
                              attrs: list = []) -> None:
        """
        Print given a text on terminal with specific color and attributes
        """
        print(colored(message, color=color, attrs=attrs))
        time.sleep(2)

    def print_failure_message(self, error_message: str) -> None:
        """
        Print an error message on terminal
        """
        self.print_colored_message(error_message, 'red')

    def print_success_message(self, success_message: str) -> None:
        """
        Print a success message on terminal
        """
        self.print_colored_message(success_message, 'green')

    def print_on_console(self, content: str) -> None:
        """
        Using rich console to print a given content
        """
        Console().print(content, justify="center")

    def print_title(self, text: str) -> None:
        """
        Print text in shape of centered rectangles
        """
        fig = Figlet(font='rectangles', justify="center")
        self.print_colored_message(fig.renderText(text), attrs=['bold'])

    def print_from_markup(self, markup_text: str) -> None:
        """
        Print a markdown formatted text on console
        """
        self.print_on_console(Markdown(markup_text))
