import click


@click.command()
@click.argument("number", type=float)
# @click.option(
#     "-n",
#     "--number",
#     default=1,
#     help="Number you want to square.",
#     show_default=True,  # show default in help
# )
def square(number):
    """Calculate the square of the input number"""
    print(f"The square of {number} is equal to {number**2}")


if __name__ == "__main__":
    square()
