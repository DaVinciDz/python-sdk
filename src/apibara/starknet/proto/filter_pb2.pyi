"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import apibara.starknet.proto.types_pb2 as types_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Filter(google.protobuf.message.Message):
    """Filter describing what data to return for each block."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADER_FIELD_NUMBER: builtins.int
    TRANSACTIONS_FIELD_NUMBER: builtins.int
    STATE_UPDATE_FIELD_NUMBER: builtins.int
    EVENTS_FIELD_NUMBER: builtins.int
    MESSAGES_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___HeaderFilter:
        """Header information."""
    @property
    def transactions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___TransactionFilter
    ]:
        """Transactions."""
    @property
    def state_update(self) -> global___StateUpdateFilter:
        """State update."""
    @property
    def events(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___EventFilter
    ]:
        """Emitted events."""
    @property
    def messages(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___L2ToL1MessageFilter
    ]:
        """Messages from L2 to L1."""
    def __init__(
        self,
        *,
        header: global___HeaderFilter | None = ...,
        transactions: collections.abc.Iterable[global___TransactionFilter] | None = ...,
        state_update: global___StateUpdateFilter | None = ...,
        events: collections.abc.Iterable[global___EventFilter] | None = ...,
        messages: collections.abc.Iterable[global___L2ToL1MessageFilter] | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "header", b"header", "state_update", b"state_update"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "events",
            b"events",
            "header",
            b"header",
            "messages",
            b"messages",
            "state_update",
            b"state_update",
            "transactions",
            b"transactions",
        ],
    ) -> None: ...

global___Filter = Filter

@typing_extensions.final
class HeaderFilter(google.protobuf.message.Message):
    """Filter header.

    This filter matches _all_ headers, so it's only necessary
    to include it in the filter to receive header data.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___HeaderFilter = HeaderFilter

@typing_extensions.final
class TransactionFilter(google.protobuf.message.Message):
    """Filter transactions.

    An empty transaction filter matches _any_ transaction.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INVOKE_V0_FIELD_NUMBER: builtins.int
    INVOKE_V1_FIELD_NUMBER: builtins.int
    DEPLOY_FIELD_NUMBER: builtins.int
    DECLARE_FIELD_NUMBER: builtins.int
    L1_HANDLER_FIELD_NUMBER: builtins.int
    DEPLOY_ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def invoke_v0(self) -> global___InvokeTransactionV0Filter: ...
    @property
    def invoke_v1(self) -> global___InvokeTransactionV1Filter: ...
    @property
    def deploy(self) -> global___DeployTransactionFilter: ...
    @property
    def declare(self) -> global___DeclareTransactionFilter: ...
    @property
    def l1_handler(self) -> global___L1HandlerTransactionFilter: ...
    @property
    def deploy_account(self) -> global___DeployAccountTransactionFilter: ...
    def __init__(
        self,
        *,
        invoke_v0: global___InvokeTransactionV0Filter | None = ...,
        invoke_v1: global___InvokeTransactionV1Filter | None = ...,
        deploy: global___DeployTransactionFilter | None = ...,
        declare: global___DeclareTransactionFilter | None = ...,
        l1_handler: global___L1HandlerTransactionFilter | None = ...,
        deploy_account: global___DeployAccountTransactionFilter | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "declare",
            b"declare",
            "deploy",
            b"deploy",
            "deploy_account",
            b"deploy_account",
            "filter",
            b"filter",
            "invoke_v0",
            b"invoke_v0",
            "invoke_v1",
            b"invoke_v1",
            "l1_handler",
            b"l1_handler",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "declare",
            b"declare",
            "deploy",
            b"deploy",
            "deploy_account",
            b"deploy_account",
            "filter",
            b"filter",
            "invoke_v0",
            b"invoke_v0",
            "invoke_v1",
            b"invoke_v1",
            "l1_handler",
            b"l1_handler",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["filter", b"filter"]
    ) -> typing_extensions.Literal[
        "invoke_v0", "invoke_v1", "deploy", "declare", "l1_handler", "deploy_account"
    ] | None: ...

global___TransactionFilter = TransactionFilter

@typing_extensions.final
class InvokeTransactionV0Filter(google.protobuf.message.Message):
    """Receive invoke transactions, v0"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTRACT_ADDRESS_FIELD_NUMBER: builtins.int
    ENTRY_POINT_SELECTOR_FIELD_NUMBER: builtins.int
    CALLDATA_FIELD_NUMBER: builtins.int
    @property
    def contract_address(self) -> types_pb2.FieldElement:
        """Filter by contract address."""
    @property
    def entry_point_selector(self) -> types_pb2.FieldElement:
        """Filter by selector."""
    @property
    def calldata(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        types_pb2.FieldElement
    ]:
        """Filter by calldata prefix."""
    def __init__(
        self,
        *,
        contract_address: types_pb2.FieldElement | None = ...,
        entry_point_selector: types_pb2.FieldElement | None = ...,
        calldata: collections.abc.Iterable[types_pb2.FieldElement] | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "contract_address",
            b"contract_address",
            "entry_point_selector",
            b"entry_point_selector",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "calldata",
            b"calldata",
            "contract_address",
            b"contract_address",
            "entry_point_selector",
            b"entry_point_selector",
        ],
    ) -> None: ...

global___InvokeTransactionV0Filter = InvokeTransactionV0Filter

@typing_extensions.final
class InvokeTransactionV1Filter(google.protobuf.message.Message):
    """Receive invoke transactions, v1"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_ADDRESS_FIELD_NUMBER: builtins.int
    CALLDATA_FIELD_NUMBER: builtins.int
    @property
    def sender_address(self) -> types_pb2.FieldElement:
        """Filter by sender address."""
    @property
    def calldata(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        types_pb2.FieldElement
    ]:
        """Filter by calldata prefix."""
    def __init__(
        self,
        *,
        sender_address: types_pb2.FieldElement | None = ...,
        calldata: collections.abc.Iterable[types_pb2.FieldElement] | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["sender_address", b"sender_address"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "calldata", b"calldata", "sender_address", b"sender_address"
        ],
    ) -> None: ...

global___InvokeTransactionV1Filter = InvokeTransactionV1Filter

@typing_extensions.final
class DeployTransactionFilter(google.protobuf.message.Message):
    """Receive deploy transactions."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTRACT_ADDRESS_SALT_FIELD_NUMBER: builtins.int
    CLASS_HASH_FIELD_NUMBER: builtins.int
    CONSTRUCTOR_CALLDATA_FIELD_NUMBER: builtins.int
    @property
    def contract_address_salt(self) -> types_pb2.FieldElement:
        """Filter by contract address salt."""
    @property
    def class_hash(self) -> types_pb2.FieldElement:
        """Filter by class hash."""
    @property
    def constructor_calldata(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        types_pb2.FieldElement
    ]:
        """Filter by calldata prefix."""
    def __init__(
        self,
        *,
        contract_address_salt: types_pb2.FieldElement | None = ...,
        class_hash: types_pb2.FieldElement | None = ...,
        constructor_calldata: collections.abc.Iterable[types_pb2.FieldElement]
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "class_hash",
            b"class_hash",
            "contract_address_salt",
            b"contract_address_salt",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "class_hash",
            b"class_hash",
            "constructor_calldata",
            b"constructor_calldata",
            "contract_address_salt",
            b"contract_address_salt",
        ],
    ) -> None: ...

global___DeployTransactionFilter = DeployTransactionFilter

@typing_extensions.final
class DeclareTransactionFilter(google.protobuf.message.Message):
    """Receive declare transactions."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLASS_HASH_FIELD_NUMBER: builtins.int
    SENDER_ADDRESS_FIELD_NUMBER: builtins.int
    @property
    def class_hash(self) -> types_pb2.FieldElement:
        """Filter by class hash."""
    @property
    def sender_address(self) -> types_pb2.FieldElement:
        """Filter by sender address."""
    def __init__(
        self,
        *,
        class_hash: types_pb2.FieldElement | None = ...,
        sender_address: types_pb2.FieldElement | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "class_hash", b"class_hash", "sender_address", b"sender_address"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "class_hash", b"class_hash", "sender_address", b"sender_address"
        ],
    ) -> None: ...

global___DeclareTransactionFilter = DeclareTransactionFilter

@typing_extensions.final
class L1HandlerTransactionFilter(google.protobuf.message.Message):
    """Receive l1 handler transactions."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTRACT_ADDRESS_FIELD_NUMBER: builtins.int
    ENTRY_POINT_SELECTOR_FIELD_NUMBER: builtins.int
    CALLDATA_FIELD_NUMBER: builtins.int
    @property
    def contract_address(self) -> types_pb2.FieldElement:
        """Filter by contract address."""
    @property
    def entry_point_selector(self) -> types_pb2.FieldElement:
        """Filter by selector."""
    @property
    def calldata(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        types_pb2.FieldElement
    ]:
        """Filter by calldata prefix."""
    def __init__(
        self,
        *,
        contract_address: types_pb2.FieldElement | None = ...,
        entry_point_selector: types_pb2.FieldElement | None = ...,
        calldata: collections.abc.Iterable[types_pb2.FieldElement] | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "contract_address",
            b"contract_address",
            "entry_point_selector",
            b"entry_point_selector",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "calldata",
            b"calldata",
            "contract_address",
            b"contract_address",
            "entry_point_selector",
            b"entry_point_selector",
        ],
    ) -> None: ...

global___L1HandlerTransactionFilter = L1HandlerTransactionFilter

@typing_extensions.final
class DeployAccountTransactionFilter(google.protobuf.message.Message):
    """Receive deploy account transactions."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTRACT_ADDRESS_SALT_FIELD_NUMBER: builtins.int
    CLASS_HASH_FIELD_NUMBER: builtins.int
    CONSTRUCTOR_CALLDATA_FIELD_NUMBER: builtins.int
    @property
    def contract_address_salt(self) -> types_pb2.FieldElement:
        """Filter by contract address salt."""
    @property
    def class_hash(self) -> types_pb2.FieldElement:
        """Filter by class hash."""
    @property
    def constructor_calldata(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        types_pb2.FieldElement
    ]:
        """Filter by calldata prefix."""
    def __init__(
        self,
        *,
        contract_address_salt: types_pb2.FieldElement | None = ...,
        class_hash: types_pb2.FieldElement | None = ...,
        constructor_calldata: collections.abc.Iterable[types_pb2.FieldElement]
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "class_hash",
            b"class_hash",
            "contract_address_salt",
            b"contract_address_salt",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "class_hash",
            b"class_hash",
            "constructor_calldata",
            b"constructor_calldata",
            "contract_address_salt",
            b"contract_address_salt",
        ],
    ) -> None: ...

global___DeployAccountTransactionFilter = DeployAccountTransactionFilter

@typing_extensions.final
class L2ToL1MessageFilter(google.protobuf.message.Message):
    """Filter L2 to L1 messages."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TO_ADDRESS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def to_address(self) -> types_pb2.FieldElement:
        """Filter by destination address."""
    @property
    def payload(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        types_pb2.FieldElement
    ]:
        """Filter payloads that prefix-match the given data."""
    def __init__(
        self,
        *,
        to_address: types_pb2.FieldElement | None = ...,
        payload: collections.abc.Iterable[types_pb2.FieldElement] | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["to_address", b"to_address"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "payload", b"payload", "to_address", b"to_address"
        ],
    ) -> None: ...

global___L2ToL1MessageFilter = L2ToL1MessageFilter

@typing_extensions.final
class EventFilter(google.protobuf.message.Message):
    """Filter events."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FROM_ADDRESS_FIELD_NUMBER: builtins.int
    KEYS_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    @property
    def from_address(self) -> types_pb2.FieldElement:
        """Filter by contract emitting the event."""
    @property
    def keys(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        types_pb2.FieldElement
    ]:
        """Filter keys that prefix-match the given data."""
    @property
    def data(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        types_pb2.FieldElement
    ]:
        """Filter data that prefix-match the given data."""
    def __init__(
        self,
        *,
        from_address: types_pb2.FieldElement | None = ...,
        keys: collections.abc.Iterable[types_pb2.FieldElement] | None = ...,
        data: collections.abc.Iterable[types_pb2.FieldElement] | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["from_address", b"from_address"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "data", b"data", "from_address", b"from_address", "keys", b"keys"
        ],
    ) -> None: ...

global___EventFilter = EventFilter

@typing_extensions.final
class StateUpdateFilter(google.protobuf.message.Message):
    """Filter state update data."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STORAGE_DIFFS_FIELD_NUMBER: builtins.int
    DECLARED_CONTRACTS_FIELD_NUMBER: builtins.int
    DEPLOYED_CONTRACTS_FIELD_NUMBER: builtins.int
    NONCES_FIELD_NUMBER: builtins.int
    @property
    def storage_diffs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___StorageDiffFilter
    ]:
        """Filter storage changes."""
    @property
    def declared_contracts(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___DeclaredContractFilter
    ]:
        """Filter declared contracts."""
    @property
    def deployed_contracts(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___DeployedContractFilter
    ]:
        """Filter deployed contracts."""
    @property
    def nonces(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___NonceUpdateFilter
    ]:
        """Filter nonces updates."""
    def __init__(
        self,
        *,
        storage_diffs: collections.abc.Iterable[global___StorageDiffFilter]
        | None = ...,
        declared_contracts: collections.abc.Iterable[global___DeclaredContractFilter]
        | None = ...,
        deployed_contracts: collections.abc.Iterable[global___DeployedContractFilter]
        | None = ...,
        nonces: collections.abc.Iterable[global___NonceUpdateFilter] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "declared_contracts",
            b"declared_contracts",
            "deployed_contracts",
            b"deployed_contracts",
            "nonces",
            b"nonces",
            "storage_diffs",
            b"storage_diffs",
        ],
    ) -> None: ...

global___StateUpdateFilter = StateUpdateFilter

@typing_extensions.final
class StorageDiffFilter(google.protobuf.message.Message):
    """Filter storage changes."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTRACT_ADDRESS_FIELD_NUMBER: builtins.int
    @property
    def contract_address(self) -> types_pb2.FieldElement:
        """Filter by contract address."""
    def __init__(
        self,
        *,
        contract_address: types_pb2.FieldElement | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["contract_address", b"contract_address"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["contract_address", b"contract_address"],
    ) -> None: ...

global___StorageDiffFilter = StorageDiffFilter

@typing_extensions.final
class DeclaredContractFilter(google.protobuf.message.Message):
    """Filter declared contracts."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLASS_HASH_FIELD_NUMBER: builtins.int
    @property
    def class_hash(self) -> types_pb2.FieldElement:
        """Filter by class hash."""
    def __init__(
        self,
        *,
        class_hash: types_pb2.FieldElement | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["class_hash", b"class_hash"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["class_hash", b"class_hash"]
    ) -> None: ...

global___DeclaredContractFilter = DeclaredContractFilter

@typing_extensions.final
class DeployedContractFilter(google.protobuf.message.Message):
    """Filter deployed contracts."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTRACT_ADDRESS_FIELD_NUMBER: builtins.int
    CLASS_HASH_FIELD_NUMBER: builtins.int
    @property
    def contract_address(self) -> types_pb2.FieldElement:
        """Filter by contract address."""
    @property
    def class_hash(self) -> types_pb2.FieldElement:
        """Filter by class hash."""
    def __init__(
        self,
        *,
        contract_address: types_pb2.FieldElement | None = ...,
        class_hash: types_pb2.FieldElement | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "class_hash", b"class_hash", "contract_address", b"contract_address"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "class_hash", b"class_hash", "contract_address", b"contract_address"
        ],
    ) -> None: ...

global___DeployedContractFilter = DeployedContractFilter

@typing_extensions.final
class NonceUpdateFilter(google.protobuf.message.Message):
    """Filter nonce updates."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTRACT_ADDRESS_FIELD_NUMBER: builtins.int
    NONCE_FIELD_NUMBER: builtins.int
    @property
    def contract_address(self) -> types_pb2.FieldElement:
        """Filter by contract address."""
    @property
    def nonce(self) -> types_pb2.FieldElement:
        """Filter by new nonce value."""
    def __init__(
        self,
        *,
        contract_address: types_pb2.FieldElement | None = ...,
        nonce: types_pb2.FieldElement | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "contract_address", b"contract_address", "nonce", b"nonce"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "contract_address", b"contract_address", "nonce", b"nonce"
        ],
    ) -> None: ...

global___NonceUpdateFilter = NonceUpdateFilter
