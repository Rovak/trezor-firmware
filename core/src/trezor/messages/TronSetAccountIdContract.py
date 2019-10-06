# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class TronSetAccountIdContract(p.MessageType):

    def __init__(
        self,
        account_id: str = None,
    ) -> None:
        self.account_id = account_id

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('account_id', p.UnicodeType, 0),
        }
