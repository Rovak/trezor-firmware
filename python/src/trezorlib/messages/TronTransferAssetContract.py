# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TronTransferAssetContract(p.MessageType):

    def __init__(
        self,
        to_address: str = None,
        amount: int = None,
        asset_id: str = None,
        asset_name: str = None,
        asset_decimals: int = None,
        asset_signature: str = None,
    ) -> None:
        self.to_address = to_address
        self.amount = amount
        self.asset_id = asset_id
        self.asset_name = asset_name
        self.asset_decimals = asset_decimals
        self.asset_signature = asset_signature

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('to_address', p.UnicodeType, 0),
            2: ('amount', p.UVarintType, 0),
            3: ('asset_id', p.UnicodeType, 0),
            4: ('asset_name', p.UnicodeType, 0),
            5: ('asset_decimals', p.UVarintType, 0),
            6: ('asset_signature', p.UnicodeType, 0),
        }
