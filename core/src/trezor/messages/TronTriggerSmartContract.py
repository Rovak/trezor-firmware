# Automatically generated by pb2py
# fmt: off
import protobuf as p


class TronTriggerSmartContract(p.MessageType):

    def __init__(
        self,
        contract_address: str = None,
        call_value: int = None,
        data: bytes = None,
        call_token_value: int = None,
        asset_id: str = None,
        asset_name: str = None,
        asset_decimals: int = None,
        asset_signature: str = None,
    ) -> None:
        self.contract_address = contract_address
        self.call_value = call_value
        self.data = data
        self.call_token_value = call_token_value
        self.asset_id = asset_id
        self.asset_name = asset_name
        self.asset_decimals = asset_decimals
        self.asset_signature = asset_signature

    @classmethod
    def get_fields(cls):
        return {
            1: ('contract_address', p.UnicodeType, 0),
            3: ('call_value', p.UVarintType, 0),
            4: ('data', p.BytesType, 0),
            5: ('call_token_value', p.UVarintType, 0),
            6: ('asset_id', p.UnicodeType, 0),
            7: ('asset_name', p.UnicodeType, 0),
            8: ('asset_decimals', p.UVarintType, 0),
            9: ('asset_signature', p.UnicodeType, 0),
        }
