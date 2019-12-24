# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TronTransferContract(p.MessageType):

    def __init__(
        self,
        to_address: str = None,
        amount: int = None,
    ) -> None:
        self.to_address = to_address
        self.amount = amount

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('to_address', p.UnicodeType, 0),
            2: ('amount', p.UVarintType, 0),
        }
