import os
from pathlib import Path
from unittest.mock import patch


from src.models.portfolio import FundProvider, Portfolio
from src.utils import build_portfolio_path, initialise_portfolio


def test_build_portfolio_path_with_defaults():
    """Test build_portfolio_path with default parameters."""
    # Arrange
    expected_path = Path(os.getcwd()) / "quarterly-research" / "portfolio.yaml"

    # Act
    result = build_portfolio_path()

    # Assert
    assert result == expected_path


def test_build_portfolio_path_with_custom_parameters():
    """Test build_portfolio_path with custom directory and filename."""
    # Arrange
    custom_dir = "custom-dir"
    custom_file = "custom.yaml"
    expected_path = Path(os.getcwd()) / custom_dir / custom_file

    # Act
    result = build_portfolio_path(dir=custom_dir, file_name=custom_file)

    # Assert
    assert result == expected_path


def test_initialise_portfolio_parses_yaml_correctly():
    """Test initialise_portfolio successfully parses the portfolio YAML file."""
    # Arrange & Act
    portfolio = initialise_portfolio()

    # Assert
    assert isinstance(portfolio, Portfolio)
    assert portfolio.name == "Vanguard ISA"
    assert portfolio.provider == FundProvider.VANGUARD
    assert portfolio.investment_horizon_years == 10
    assert len(portfolio.funds) == 4


@patch("src.utils.parse_yaml_file_as")
@patch("src.utils.build_portfolio_path")
def test_initialise_portfolio_uses_correct_path(mock_build_path, mock_parse_yaml):
    """Test initialise_portfolio calls parse_yaml_file_as with correct parameters."""
    # Arrange
    mock_path = Path("/mock/path/portfolio.yaml")
    mock_build_path.return_value = mock_path

    # Act
    initialise_portfolio()

    # Assert
    mock_build_path.assert_called_once()
    mock_parse_yaml.assert_called_once_with(
        model_type=Portfolio,
        file=mock_path,
    )
