import numpy as np
import pandas as pd

from datetime import time 
from datetime import datetime
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union

from pandas.core.groupby import DataFrameGroupBy
from pandas.core.window import RollingGroupby

class StockFrame():

    def __init__(self, data: list[dict]) -> None:

        self.data = data
        self._frame: pd.DataFrame = self.create_frame()
        self._symbol_groups: DataFrameGroupBy = None
        self._symbol_rolling_groups: RollingGroupby = None

    @property
    def frame(self) -> pd.DataFrame:
        return self._frame

    @property
    def symbol_groups(self) -> DataFrameGroupBy:
        self._symbol_groups = self.frame.groupby(
            by = 'symbol',
            as_index = False,
            sort = True
         )