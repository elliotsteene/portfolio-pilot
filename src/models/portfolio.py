from collections.abc import Sequence
from enum import StrEnum

from pydantic import BaseModel


class Fund(BaseModel):
    name: str
    value: float


class FundProvider(StrEnum):
    VANGUARD = "Vanguard"


class Portfolio(BaseModel):
    name: str
    provider: FundProvider
    investment_horizon_years: int
    funds: Sequence[Fund]
