"""Command-line interface."""

import click
# @click.command()
# @click.version_option()
def main() -> None:
    """Warehouse Ddd."""
    from warehouse_ddd_alexandra.flask_app import create_app
    
    app = create_app()
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()  # pragma: no cover
