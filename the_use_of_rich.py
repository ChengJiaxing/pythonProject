# from rich.console import Console
# console=Console()
# console.print("Hello","World!")
# console.print("Hello", "World!", style="bold red")


# from rich.console import Console
# console = Console()
#
# test_data = [
#     {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},
#     {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
#     {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
# ]
#
# def test_log():
#     enabled = False
#     context = {
#         "foo": "bar",
#     }
#     movies = ["Deadpool", "Rise of the Skywalker"]
#     console.log("Hello from", console, "!")
#     console.log(test_data, log_locals=True)
#
#
# test_log()

# from rich.console import Console
# console=Console()
# test_data=[{
#     "student":"1","year":"11","weight":"100"},{
#     "student":"2","year":"12","weight":"101"},{
#     "student":"3","year":"13","weight":"102"}]
# def test_log():
#     enabled=True
#     context={
#         "name":"message",
#     }
#     movies=["message","some messages"]
#     console.log("Hello from",console,"!")
#     console.log(test_data,log_locals=True)
# test_log()

# from rich.console import Console
# console=Console()
# console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")
# console.print(":smiley:")
# console.print(":vampire:")
# console.print(":pile_of_poo:")
# console.print(":raccoon:")


# from rich.console import Console
# from rich.table import Column, Table
#
# console = Console()
#
# table = Table(show_header=True, header_style="bold magenta")
# table.add_column("Date", style="dim", width=12)
# table.add_column("Title")
# table.add_column("Production Budget", justify="right")
# table.add_column("Box Office", justify="right")
# table.add_row(
#     "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
# )
# table.add_row(
#     "May 25, 2018",
#     "[red]Solo[/red]: A Star Wars Story",
#     "$275,000,000",
#     "$393,151,347",
# )
# table.add_row(
#     "Dec 15, 2017",
#     "Star Wars Ep. VIII: The Last Jedi",
#     "$262,000,000",
#     "[bold]$1,332,539,889[/bold]",
# )
#
# console.print(table)

# from rich.console import Console
# from rich.table import Column,Table
# console=Console()
# table=Table(show_header=True,header_style="bold magenta")
# table.add_column("name",style="dim",width=12)
# table.add_column("age",justify="left")
# table.add_column("weight",justify="mid")
# table.add_column("favorite food",justify="right")
# table.add_row("student1","12","60kg","apple")
# table.add_row("student2","13","61kg","apple")
# table.add_row("student3","14","62kg","apple")
# table.add_row("studnet4","15","63kg","apple")
# console.print(table)

# from rich.progress import track
# for step in track(range(100)):
#     do_step(step)
# from rich.console import Console
# console=Console()
# console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

# import os
# import sys
# from rich import print
# from rich.columns import Columns
# path = os.listdir(os.getcwd())
# print(Columns(path))

