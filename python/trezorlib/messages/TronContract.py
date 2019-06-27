# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .TronAccountUpdateContract import TronAccountUpdateContract
from .TronAssetIssueContract import TronAssetIssueContract
from .TronExchangeCreateContract import TronExchangeCreateContract
from .TronExchangeInjectContract import TronExchangeInjectContract
from .TronExchangeTransactionContract import TronExchangeTransactionContract
from .TronExchangeWithdrawContract import TronExchangeWithdrawContract
from .TronFreezeBalanceContract import TronFreezeBalanceContract
from .TronParticipateAssetIssueContract import TronParticipateAssetIssueContract
from .TronProposalApproveContract import TronProposalApproveContract
from .TronProposalCreateContract import TronProposalCreateContract
from .TronProposalDeleteContract import TronProposalDeleteContract
from .TronSetAccountIdContract import TronSetAccountIdContract
from .TronTransferAssetContract import TronTransferAssetContract
from .TronTransferContract import TronTransferContract
from .TronTriggerSmartContract import TronTriggerSmartContract
from .TronUnfreezeAssetContract import TronUnfreezeAssetContract
from .TronUnfreezeBalanceContract import TronUnfreezeBalanceContract
from .TronUpdateAssetContract import TronUpdateAssetContract
from .TronVoteWitnessContract import TronVoteWitnessContract
from .TronWithdrawBalanceContract import TronWithdrawBalanceContract
from .TronWitnessCreateContract import TronWitnessCreateContract
from .TronWitnessUpdateContract import TronWitnessUpdateContract


class TronContract(p.MessageType):

    def __init__(
        self,
        transfer_contract: TronTransferContract = None,
        transfer_asset_contract: TronTransferAssetContract = None,
        vote_witness_contract: TronVoteWitnessContract = None,
        witness_create_contract: TronWitnessCreateContract = None,
        asset_issue_contract: TronAssetIssueContract = None,
        witness_update_contract: TronWitnessUpdateContract = None,
        participate_asset_issue_contract: TronParticipateAssetIssueContract = None,
        account_update_contract: TronAccountUpdateContract = None,
        freeze_balance_contract: TronFreezeBalanceContract = None,
        unfreeze_balance_contract: TronUnfreezeBalanceContract = None,
        withdraw_balance_contract: TronWithdrawBalanceContract = None,
        unfreeze_asset_contract: TronUnfreezeAssetContract = None,
        update_asset_contract: TronUpdateAssetContract = None,
        proposal_create_contract: TronProposalCreateContract = None,
        proposal_approve_contract: TronProposalApproveContract = None,
        proposal_delete_contract: TronProposalDeleteContract = None,
        set_account_id: TronSetAccountIdContract = None,
        trigger_smart_contract: TronTriggerSmartContract = None,
        exchange_create_contract: TronExchangeCreateContract = None,
        exchange_inject_contract: TronExchangeInjectContract = None,
        exchange_withdraw_contract: TronExchangeWithdrawContract = None,
        exchange_transaction_contract: TronExchangeTransactionContract = None,
    ) -> None:
        self.transfer_contract = transfer_contract
        self.transfer_asset_contract = transfer_asset_contract
        self.vote_witness_contract = vote_witness_contract
        self.witness_create_contract = witness_create_contract
        self.asset_issue_contract = asset_issue_contract
        self.witness_update_contract = witness_update_contract
        self.participate_asset_issue_contract = participate_asset_issue_contract
        self.account_update_contract = account_update_contract
        self.freeze_balance_contract = freeze_balance_contract
        self.unfreeze_balance_contract = unfreeze_balance_contract
        self.withdraw_balance_contract = withdraw_balance_contract
        self.unfreeze_asset_contract = unfreeze_asset_contract
        self.update_asset_contract = update_asset_contract
        self.proposal_create_contract = proposal_create_contract
        self.proposal_approve_contract = proposal_approve_contract
        self.proposal_delete_contract = proposal_delete_contract
        self.set_account_id = set_account_id
        self.trigger_smart_contract = trigger_smart_contract
        self.exchange_create_contract = exchange_create_contract
        self.exchange_inject_contract = exchange_inject_contract
        self.exchange_withdraw_contract = exchange_withdraw_contract
        self.exchange_transaction_contract = exchange_transaction_contract

    @classmethod
    def get_fields(cls):
        return {
            1: ('transfer_contract', TronTransferContract, 0),
            2: ('transfer_asset_contract', TronTransferAssetContract, 0),
            4: ('vote_witness_contract', TronVoteWitnessContract, 0),
            5: ('witness_create_contract', TronWitnessCreateContract, 0),
            6: ('asset_issue_contract', TronAssetIssueContract, 0),
            8: ('witness_update_contract', TronWitnessUpdateContract, 0),
            9: ('participate_asset_issue_contract', TronParticipateAssetIssueContract, 0),
            10: ('account_update_contract', TronAccountUpdateContract, 0),
            11: ('freeze_balance_contract', TronFreezeBalanceContract, 0),
            12: ('unfreeze_balance_contract', TronUnfreezeBalanceContract, 0),
            13: ('withdraw_balance_contract', TronWithdrawBalanceContract, 0),
            14: ('unfreeze_asset_contract', TronUnfreezeAssetContract, 0),
            15: ('update_asset_contract', TronUpdateAssetContract, 0),
            16: ('proposal_create_contract', TronProposalCreateContract, 0),
            17: ('proposal_approve_contract', TronProposalApproveContract, 0),
            18: ('proposal_delete_contract', TronProposalDeleteContract, 0),
            19: ('set_account_id', TronSetAccountIdContract, 0),
            31: ('trigger_smart_contract', TronTriggerSmartContract, 0),
            41: ('exchange_create_contract', TronExchangeCreateContract, 0),
            42: ('exchange_inject_contract', TronExchangeInjectContract, 0),
            43: ('exchange_withdraw_contract', TronExchangeWithdrawContract, 0),
            44: ('exchange_transaction_contract', TronExchangeTransactionContract, 0),
        }
