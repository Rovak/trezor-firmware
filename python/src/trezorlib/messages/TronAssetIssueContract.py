# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .TronFrozenSupply import TronFrozenSupply

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class TronAssetIssueContract(p.MessageType):

    def __init__(
        self,
        name: str = None,
        abbr: str = None,
        total_supply: int = None,
        frozen_supply: List[TronFrozenSupply] = None,
        trx_num: int = None,
        precision: int = None,
        num: int = None,
        start_time: int = None,
        end_time: int = None,
        description: str = None,
        url: str = None,
    ) -> None:
        self.name = name
        self.abbr = abbr
        self.total_supply = total_supply
        self.frozen_supply = frozen_supply if frozen_supply is not None else []
        self.trx_num = trx_num
        self.precision = precision
        self.num = num
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.url = url

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            2: ('name', p.UnicodeType, 0),
            3: ('abbr', p.UnicodeType, 0),
            4: ('total_supply', p.UVarintType, 0),
            5: ('frozen_supply', TronFrozenSupply, p.FLAG_REPEATED),
            6: ('trx_num', p.UVarintType, 0),
            7: ('precision', p.UVarintType, 0),
            8: ('num', p.UVarintType, 0),
            9: ('start_time', p.UVarintType, 0),
            10: ('end_time', p.UVarintType, 0),
            11: ('description', p.UnicodeType, 0),
            12: ('url', p.UnicodeType, 0),
        }
