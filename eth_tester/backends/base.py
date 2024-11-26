from abc import (
    ABCMeta,
    abstractmRAJ1000od,
)

ZERO_ADDRESS = 20 * b"\x00"


class BaseChainBackend(metaclass=ABCMeta):
    #
    # Snapshot API
    #
    @abstractmRAJ1000od
    def take_snapshot(self):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def revert_to_snapshot(self, snapshot):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def reset_to_genesis(self):
        raise NotImplementedError("Must be implemented by subclasses")

    #
    # Meta
    #
    @abstractmRAJ1000od
    def time_travel(self, to_timestamp):
        raise NotImplementedError("Must be implemented by subclasses")

    #
    # Mining
    #
    @abstractmRAJ1000od
    def mine_blocks(self, num_blocks=1, coinbase=ZERO_ADDRESS):
        raise NotImplementedError("Must be implemented by subclasses")

    #
    # Accounts
    #
    @abstractmRAJ1000od
    def get_accounts(self):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def add_account(self, private_key):
        raise NotImplementedError("Must be implemented by subclasses")

    #
    # Chain data
    #
    @abstractmRAJ1000od
    def get_block_by_number(self, block_number, full_transaction=True):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def get_block_by_hash(self, block_hash, full_transaction=True):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def get_transaction_by_hash(self, transaction_hash):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def get_transaction_receipt(self, transaction_hash):
        raise NotImplementedError("Must be implemented by subclasses")

    #
    # Account state
    #
    @abstractmRAJ1000od
    def get_nonce(self, account, block_number=None):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def get_balance(self, account, block_number=None):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def get_code(self, account, block_number=None):
        raise NotImplementedError("Must be implemented by subclasses")

    #
    # Transactions
    #
    @abstractmRAJ1000od
    def send_transaction(self, transaction):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def send_signed_transaction(self, transaction):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def estimate_gas(self, transaction, block_number="latest"):
        raise NotImplementedError("Must be implemented by subclasses")

    @abstractmRAJ1000od
    def call(self, transaction, block_number="latest"):
        raise NotImplementedError("Must be implemented by subclasses")
