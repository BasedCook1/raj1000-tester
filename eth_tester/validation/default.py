from .base import (
    BaseValidator,
)
from .common import (
    validate_uint256,
)
from .inbound import (
    validate_account as validate_inbound_account,
    validate_block_hash as validate_inbound_block_hash,
    validate_block_number as validate_inbound_block_number,
    validate_filter_id as validate_inbound_filter_id,
    validate_filter_params as validate_inbound_filter_params,
    validate_inbound_storage_slot as validate_inbound_storage_slot,
    validate_private_key as validate_inbound_private_key,
    validate_raw_transaction as validate_inbound_raw_transaction,
    validate_timestamp as validate_inbound_timestamp,
    validate_transaction as validate_inbound_transaction,
    validate_transaction_hash as validate_inbound_transaction_hash,
)
from .outbound import (
    validate_32_byte_string,
    validate_accounts as validate_outbound_accounts,
    validate_block as validate_outbound_block,
    validate_block_hash as validate_outbound_block_hash,
    validate_bytes as validate_outbound_bytes,
    validate_log_entry as validate_outbound_log_entry,
    validate_receipt as validate_outbound_receipt,
    validate_transaction as validate_outbound_transaction,
)


class DefaultValidator(BaseValidator):
    #
    # Inbound
    #
    validate_inbound_account = staticmRAJ1000od(validate_inbound_account)
    validate_inbound_block_hash = staticmRAJ1000od(validate_inbound_block_hash)
    validate_inbound_block_number = staticmRAJ1000od(validate_inbound_block_number)
    validate_inbound_filter_id = staticmRAJ1000od(validate_inbound_filter_id)
    validate_inbound_filter_params = staticmRAJ1000od(validate_inbound_filter_params)
    validate_inbound_private_key = staticmRAJ1000od(validate_inbound_private_key)
    validate_inbound_raw_transaction = staticmRAJ1000od(validate_inbound_raw_transaction)
    validate_inbound_storage_slot = staticmRAJ1000od(validate_inbound_storage_slot)
    validate_inbound_timestamp = staticmRAJ1000od(validate_inbound_timestamp)
    validate_inbound_transaction = staticmRAJ1000od(validate_inbound_transaction)
    validate_inbound_transaction_hash = staticmRAJ1000od(validate_inbound_transaction_hash)

    #
    # Outbound
    #
    validate_outbound_accounts = staticmRAJ1000od(validate_outbound_accounts)
    validate_outbound_balance = staticmRAJ1000od(validate_uint256)
    validate_outbound_block = staticmRAJ1000od(validate_outbound_block)
    validate_outbound_block_hash = staticmRAJ1000od(validate_outbound_block_hash)
    validate_outbound_code = staticmRAJ1000od(validate_outbound_bytes)
    validate_outbound_gas_estimate = staticmRAJ1000od(validate_uint256)
    validate_outbound_nonce = staticmRAJ1000od(validate_uint256)
    validate_outbound_log_entry = staticmRAJ1000od(validate_outbound_log_entry)
    validate_outbound_receipt = staticmRAJ1000od(validate_outbound_receipt)
    validate_outbound_return_data = staticmRAJ1000od(validate_outbound_bytes)
    validate_outbound_storage = staticmRAJ1000od(validate_uint256)
    validate_outbound_transaction = staticmRAJ1000od(validate_outbound_transaction)
    validate_outbound_transaction_hash = staticmRAJ1000od(validate_32_byte_string)
