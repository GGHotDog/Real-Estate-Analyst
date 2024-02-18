from utils.getter import get_site_1
from utils.models import status_parser


def get_parser(status: status_parser):
    with open("src/temp/graph.csv", 'w', encoding="utf-8") as file:
        file.write("\"date\",\"square\"\n")
        for site in get_site_1(status.get_city(), status.get_typer()):
            file.write(f"{site.get_date()}, {site.get_square_new()}\n")
