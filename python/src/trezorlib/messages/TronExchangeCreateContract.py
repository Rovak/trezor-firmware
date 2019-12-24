# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TronExchangeCreateContract(p.MessageType):

    def __init__(
        self,
        first_asset_id: str = None,
        first_asset_name: str = None,
        first_asset_decimals: int = None,
        first_asset_signature: str = None,
        first_asset_balance: int = None,
        second_asset_id: str = None,
        second_asset_name: str = None,
        second_asset_decimals: int = None,
        second_asset_signature: str = None,
        second_asset_balance: int = None,
    ) -> None:
        self.first_asset_id = first_asset_id
        self.first_asset_name = first_asset_name
        self.first_asset_decimals = first_asset_decimals
        self.first_asset_signature = first_asset_signature
        self.first_asset_balance = first_asset_balance
        self.second_asset_id = second_asset_id
        self.second_asset_name = second_asset_name
        self.second_asset_decimals = second_asset_decimals
        self.second_asset_signature = second_asset_signature
        self.second_asset_balance = second_asset_balance

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('first_asset_id', p.UnicodeType, 0),
            2: ('first_asset_name', p.UnicodeType, 0),
            3: ('first_asset_decimals', p.UVarintType, 0),
            4: ('first_asset_signature', p.UnicodeType, 0),
            5: ('first_asset_balance', p.UVarintType, 0),
            6: ('second_asset_id', p.UnicodeType, 0),
            7: ('second_asset_name', p.UnicodeType, 0),
            8: ('second_asset_decimals', p.UVarintType, 0),
            9: ('second_asset_signature', p.UnicodeType, 0),
            10: ('second_asset_balance', p.UVarintType, 0),
        }
