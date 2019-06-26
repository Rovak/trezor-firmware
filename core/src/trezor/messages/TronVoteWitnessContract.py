# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .TronVote import TronVote

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class TronVoteWitnessContract(p.MessageType):

    def __init__(
        self,
        votes: List[TronVote] = None,
    ) -> None:
        self.votes = votes if votes is not None else []

    @classmethod
    def get_fields(cls):
        return {
            1: ('votes', TronVote, p.FLAG_REPEATED),
        }
