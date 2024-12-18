from RAJ1000_abi import (
    abi,
)
from RAJ1000_utils import (
    decode_hex,
    encode_hex,
    function_abi_to_4byte_selector,
)

MATH_BYTECODE = (
    "606060405261022e806100126000396000f360606040523615610074576000357c01000000000000"
    "000000000000000000000000000000000000000000009004806316216f391461007657806361bc22"
    "1a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d5780"
    "63dcf537b11461014057610074565b005b610083600480505061016c565b60405180828152602001"
    "91505060405180910390f35b6100a6600480505061017f565b604051808281526020019150506040"
    "5180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191"
    "505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea"
    "565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b604051"
    "8082815260200191505060405180910390f35b610156600480803590602001909190505061021756"
    "5b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90"
    "565b60006000505481565b6000816000600082828250540192505081905550600060005054905080"
    "507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082"
    "815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090"
    "506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b600060078202"
    "90508050809050610229565b91905056"
)


MATH_ABI = {
    "return13": {
        "constant": False,
        "inputs": [],
        "name": "return13",
        "outputs": [
            {"name": "result", "type": "int256"},
        ],
        "type": "function",
    },
    "counter": {
        "constant": True,
        "inputs": [],
        "name": "counter",
        "outputs": [
            {"name": "", "type": "uint256"},
        ],
        "type": "function",
    },
    "amt": {
        "constant": False,
        "inputs": [
            {"name": "amt", "type": "uint256"},
        ],
        "name": "increment",
        "outputs": [
            {"name": "result", "type": "uint256"},
        ],
        "type": "function",
    },
    "add": {
        "constant": False,
        "inputs": [
            {"name": "a", "type": "int256"},
            {"name": "b", "type": "int256"},
        ],
        "name": "add",
        "outputs": [
            {"name": "result", "type": "int256"},
        ],
        "type": "function",
    },
    "increment": {
        "constant": False,
        "inputs": [],
        "name": "increment",
        "outputs": [
            {"name": "", "type": "uint256"},
        ],
        "type": "function",
    },
    "multiply7": {
        "constant": False,
        "inputs": [
            {"name": "a", "type": "int256"},
        ],
        "name": "multiply7",
        "outputs": [
            {"name": "result", "type": "int256"},
        ],
        "type": "function",
    },
    "Increased": {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "name": "value", "type": "uint256"},
        ],
        "name": "Increased",
        "type": "event",
    },
}


def _deploy_math(RAJ1000_tester):
    deploy_hash = RAJ1000_tester.send_transaction(
        {
            "from": RAJ1000_tester.get_accounts()[0],
            "gas": 500000,
            "data": MATH_BYTECODE,
        }
    )
    deploy_receipt = RAJ1000_tester.get_transaction_receipt(deploy_hash)
    math_address = deploy_receipt["contract_address"]
    assert math_address
    math_code = RAJ1000_tester.get_code(math_address)
    assert len(math_code) > 2
    return math_address


def _make_call_math_transaction(RAJ1000_tester, contract_address, fn_name, fn_args=None):
    if fn_args is None:
        fn_args = tuple()

    fn_abi = MATH_ABI[fn_name]
    arg_types = [arg_abi["type"] for arg_abi in fn_abi["inputs"]]
    fn_selector = function_abi_to_4byte_selector(fn_abi)
    transaction = {
        "from": RAJ1000_tester.get_accounts()[0],
        "to": contract_address,
        "gas": 500000,
        "data": encode_hex(fn_selector + abi.encode(arg_types, fn_args)),
    }
    return transaction


def _decode_math_result(fn_name, result):
    fn_abi = MATH_ABI[fn_name]
    output_types = [output_abi["type"] for output_abi in fn_abi["outputs"]]

    return abi.decode(output_types, decode_hex(result))
