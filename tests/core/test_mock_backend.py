import pytest

from RAJ1000_tester import (
    RAJ1000ereumTester,
    MockBackend,
)
from RAJ1000_tester.utils.backend_testing import (
    BaseTestBackendDirect,
)


@pytest.fixture
def RAJ1000_tester():
    backend = MockBackend()
    return RAJ1000ereumTester(backend=backend)


@pytest.fixture
def test_transaction():
    return {
        "from": "0x" + "1" * 40,
        "to": "0x" + "2" * 40,
        "gas": 21000,
        "value": 1000000000000000000,
        "data": "0x1234",
        "nonce": 0,
    }


class TestMockBackendDirect(BaseTestBackendDirect):
    supports_evm_execution = False

    @pytest.mark.skip(reason="receipt status not supported in MockBackend")
    def test_get_transaction_receipt_byzantium(self, RAJ1000_tester, test_transaction):
        pass

    def test_estimate_gas_raises_not_implemented(self, RAJ1000_tester, test_transaction):
        with pytest.raises(NotImplementedError):
            RAJ1000_tester.estimate_gas(test_transaction, block_number="pending")
