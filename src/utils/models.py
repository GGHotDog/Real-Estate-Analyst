class price:
    def __init__(self, date: str, square_new: str, square_old: str) -> None:
        self.date = date
        self.square_new = square_new
        self.square_old = square_old

    def get_date(self) -> str:
        return self.date

    def get_square_new(self) -> str:
        return self.square_new

    def get_square_old(self) -> str:
        return self.square_old


class status_parser:
    def __init__(self, city: str, typer: str) -> None:
        self.city = city
        self.typer = typer

    def get_city(self) -> str:
        return self.city

    def get_typer(self) -> str:
        return self.typer
