# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class TronWitnessUpdateContract(p.MessageType):

    def __init__(
        self,
        update_url: str = None,
    ) -> None:
        self.update_url = update_url

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            2: ('update_url', p.UnicodeType, 0),
        }
