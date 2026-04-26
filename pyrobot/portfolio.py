from typing import List
from typing import Dict
from typing import Union
from typing import Optional


class Portfolio():

    def __init__(self,account_number: Optional[str]):

        self.positions = {}
        self.positions_count = 0
        self.market_value = 0.0
        self.profit_loss = 0.0
        self.risk_tolerance = 0.0
        self.account_number = account_number

    def add_position(self, symbol: str, asset_type: str, purchase_date: Optional[str] ,quantity: int = 0,purchase_price: float = 0.0)-> dict:

        self.positions[symbol] = {}
        self.positions[symbol]['symbol'] = symbol
        self.positions[symbol]['quantity'] = quantity
        self.positions[symbol]['purchase_price'] = purchase_price
        self.positions[symbol]['purchase_date'] = purchase_date
        self.positions[symbol]['asset_type'] = asset_type

        return self.positions

    def add_positions(self, positions: List[dict]) -> dict:

        if isinstance(positions, list):

            for position in positions:

                self.add_position(
                    symbol = position['symbol'],
                    asset_type = position['asset_type'],
                    purchase_date = positions.get('purchase_date',None),
                    purchase_price = position.get('purchase_price',0.00),
                    quantity = position.get('quantity',0)
                )

                return self.positions

        else:
            raise TypeError('positions must be a list of dictionaires')

    def remove_positions(self, symbol: str) -> Tuple[bool,str]:

        if symbol in self.positions:
            del self.positions[symbol]
            return(True, "{symbol} was successfully removed".format(symbol=symbol))
        else:
            return (False, "{symbol} did not exist in the portfolio".format(symbol=symbol))
        
    def total_allocation(self):
        pass
    
    def risk_exposure(self):
        pass

    def  in_portfolio(self, symbol:str) -> bool:

        if symbol in self.positions:
            return True
        else:
            return False

    def is_profitable(self ):