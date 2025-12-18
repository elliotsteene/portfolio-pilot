import os
from pathlib import Path

from pydantic_yaml import parse_yaml_file_as

from src.models.portfolio import Portfolio


def build_portfolio_path(
    dir: str = r"quarterly-research", file_name: str = "portfolio.yaml"
) -> Path:
    return Path(os.getcwd()) / dir / file_name


def initialise_portfolio() -> Portfolio:
    return parse_yaml_file_as(
        model_type=Portfolio,
        file=build_portfolio_path(),
    )
