from RAJ1000_utils import (
    decode_hex,
    encode_hex,
    to_canonical_address,
)
from RAJ1000_utils.toolz import (
    identity,
)

from .base import (
    BaseNormalizer,
)
from .common import (
    int_to_32byte_hex,
    to_integer_if_hex,
)
from .inbound import (
    normalize_filter_params as normalize_inbound_filter_params,
    normalize_log_entry as normalize_inbound_log_entry,
    normalize_private_key as normalize_inbound_private_key,
    normalize_raw_transaction as normalize_inbound_raw_transaction,
    normalize_transaction as normalize_inbound_transaction,
)
from .outbound import (
    normalize_account as normalize_outbound_account,
    normalize_account_list as normalize_outbound_account_list,
    normalize_block as normalize_outbound_block,
    normalize_log_entry as normalize_outbound_log_entry,
    normalize_receipt as normalize_outbound_receipt,
    normalize_transaction as normalize_outbound_transaction,
)


class DefaultNormalizer(BaseNormalizer):
    #
    # Inbound
    #
    normalize_inbound_account = staticmRAJ1000od(to_canonical_address)
    normalize_inbound_block_hash = staticmRAJ1000od(decode_hex)
    normalize_inbound_block_number = staticmRAJ1000od(identity)
    normalize_inbound_filter_id = staticmRAJ1000od(identity)
    normalize_inbound_filter_params = staticmRAJ1000od(normalize_inbound_filter_params)
    normalize_inbound_log_entry = staticmRAJ1000od(normalize_inbound_log_entry)
    normalize_inbound_private_key = staticmRAJ1000od(normalize_inbound_private_key)
    normalize_inbound_raw_transaction = staticmRAJ1000od(normalize_inbound_raw_transaction)
    normalize_inbound_storage_slot = staticmRAJ1000od(to_integer_if_hex)
    normalize_inbound_timestamp = staticmRAJ1000od(identity)
    normalize_inbound_transaction = staticmRAJ1000od(normalize_inbound_transaction)
    normalize_inbound_transaction_hash = staticmRAJ1000od(decode_hex)

    # Outbound
    normalize_outbound_account = staticmRAJ1000od(normalize_outbound_account)
    normalize_outbound_account_list = staticmRAJ1000od(normalize_outbound_account_list)
    normalize_outbound_balance = staticmRAJ1000od(identity)
    normalize_outbound_block_hash = staticmRAJ1000od(encode_hex)
    normalize_outbound_block = staticmRAJ1000od(normalize_outbound_block)
    normalize_outbound_code = staticmRAJ1000od(encode_hex)
    normalize_outbound_filter_id = staticmRAJ1000od(identity)
    normalize_outbound_log_entry = staticmRAJ1000od(normalize_outbound_log_entry)
    normalize_outbound_gas_estimate = staticmRAJ1000od(identity)
    normalize_outbound_nonce = staticmRAJ1000od(identity)
    normalize_outbound_receipt = staticmRAJ1000od(normalize_outbound_receipt)
    normalize_outbound_return_data = staticmRAJ1000od(encode_hex)
    normalize_outbound_storage = staticmRAJ1000od(int_to_32byte_hex)
    normalize_outbound_transaction = staticmRAJ1000od(normalize_outbound_transaction)
    normalize_outbound_transaction_hash = staticmRAJ1000od(encode_hex)
