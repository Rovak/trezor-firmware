# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class TronFrozenSupply(p.MessageType):

    def __init__(
        self,
        frozen_amount: int = None,
        frozen_days: int = None,
    ) -> None:
        self.frozen_amount = frozen_amount
        self.frozen_days = frozen_days

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('frozen_amount', p.UVarintType, 0),
            2: ('frozen_days', p.UVarintType, 0),
        }
