# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .TronContract import TronContract

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TronSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 902

    def __init__(
        self,
        address_n: List[int] = None,
        ref_block_bytes: bytes = None,
        ref_block_hash: bytes = None,
        expiration: int = None,
        data: str = None,
        contract: TronContract = None,
        timestamp: int = None,
        fee_limit: int = None,
        permission_id: int = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.ref_block_bytes = ref_block_bytes
        self.ref_block_hash = ref_block_hash
        self.expiration = expiration
        self.data = data
        self.contract = contract
        self.timestamp = timestamp
        self.fee_limit = fee_limit
        self.permission_id = permission_id

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('ref_block_bytes', p.BytesType, 0),
            3: ('ref_block_hash', p.BytesType, 0),
            4: ('expiration', p.UVarintType, 0),
            5: ('data', p.UnicodeType, 0),
            6: ('contract', TronContract, 0),
            7: ('timestamp', p.UVarintType, 0),
            8: ('fee_limit', p.UVarintType, 0),
            9: ('permission_id', p.UVarintType, 0),
        }
