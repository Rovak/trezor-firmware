# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class TronProposalParameters(p.MessageType):

    def __init__(
        self,
        key: int = None,
        value: int = None,
    ) -> None:
        self.key = key
        self.value = value

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('key', p.UVarintType, 0),
            2: ('value', p.UVarintType, 0),
        }
