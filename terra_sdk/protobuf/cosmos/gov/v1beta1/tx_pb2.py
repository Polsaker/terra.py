# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmos/gov/v1beta1/tx.proto",
    package="cosmos.gov.v1beta1",
    syntax="proto3",
    serialized_options=b"Z(github.com/cosmos/cosmos-sdk/x/gov/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1b\x63osmos/gov/v1beta1/tx.proto\x12\x12\x63osmos.gov.v1beta1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1c\x63osmos/gov/v1beta1/gov.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"\xeb\x01\n\x11MsgSubmitProposal\x12\x32\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x0b\xca\xb4-\x07\x43ontent\x12~\n\x0finitial_deposit\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBJ\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x16yaml:"initial_deposit"\x12\x10\n\x08proposer\x18\x03 \x01(\t:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00"W\n\x19MsgSubmitProposalResponse\x12:\n\x0bproposal_id\x18\x01 \x01(\x04\x42%\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:"proposal_id""\x96\x01\n\x07MsgVote\x12:\n\x0bproposal_id\x18\x01 \x01(\x04\x42%\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:"proposal_id"\x12\r\n\x05voter\x18\x02 \x01(\t\x12.\n\x06option\x18\x03 \x01(\x0e\x32\x1e.cosmos.gov.v1beta1.VoteOption:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00"\x11\n\x0fMsgVoteResponse"\x9e\x01\n\x0fMsgVoteWeighted\x12+\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x16\xf2\xde\x1f\x12yaml:"proposal_id"\x12\r\n\x05voter\x18\x02 \x01(\t\x12=\n\x07options\x18\x03 \x03(\x0b\x32&.cosmos.gov.v1beta1.WeightedVoteOptionB\x04\xc8\xde\x1f\x00:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00"\x19\n\x17MsgVoteWeightedResponse"\xca\x01\n\nMsgDeposit\x12:\n\x0bproposal_id\x18\x01 \x01(\x04\x42%\xea\xde\x1f\x0bproposal_id\xf2\xde\x1f\x12yaml:"proposal_id"\x12\x11\n\tdepositor\x18\x02 \x01(\t\x12[\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x10\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x80\xdc \x00\x88\xa0\x1f\x00"\x14\n\x12MsgDepositResponse2\xec\x02\n\x03Msg\x12\x66\n\x0eSubmitProposal\x12%.cosmos.gov.v1beta1.MsgSubmitProposal\x1a-.cosmos.gov.v1beta1.MsgSubmitProposalResponse\x12H\n\x04Vote\x12\x1b.cosmos.gov.v1beta1.MsgVote\x1a#.cosmos.gov.v1beta1.MsgVoteResponse\x12`\n\x0cVoteWeighted\x12#.cosmos.gov.v1beta1.MsgVoteWeighted\x1a+.cosmos.gov.v1beta1.MsgVoteWeightedResponse\x12Q\n\x07\x44\x65posit\x12\x1e.cosmos.gov.v1beta1.MsgDeposit\x1a&.cosmos.gov.v1beta1.MsgDepositResponseB*Z(github.com/cosmos/cosmos-sdk/x/gov/typesb\x06proto3',
    dependencies=[
        cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,
        cosmos_dot_gov_dot_v1beta1_dot_gov__pb2.DESCRIPTOR,
        cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
    ],
)


_MSGSUBMITPROPOSAL = _descriptor.Descriptor(
    name="MsgSubmitProposal",
    full_name="cosmos.gov.v1beta1.MsgSubmitProposal",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="content",
            full_name="cosmos.gov.v1beta1.MsgSubmitProposal.content",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\312\264-\007Content",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="initial_deposit",
            full_name="cosmos.gov.v1beta1.MsgSubmitProposal.initial_deposit",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\026yaml:"initial_deposit"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="proposer",
            full_name="cosmos.gov.v1beta1.MsgSubmitProposal.proposer",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\350\240\037\000\230\240\037\000\200\334 \000\210\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=190,
    serialized_end=425,
)


_MSGSUBMITPROPOSALRESPONSE = _descriptor.Descriptor(
    name="MsgSubmitProposalResponse",
    full_name="cosmos.gov.v1beta1.MsgSubmitProposalResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="proposal_id",
            full_name="cosmos.gov.v1beta1.MsgSubmitProposalResponse.proposal_id",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\352\336\037\013proposal_id\362\336\037\022yaml:"proposal_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=427,
    serialized_end=514,
)


_MSGVOTE = _descriptor.Descriptor(
    name="MsgVote",
    full_name="cosmos.gov.v1beta1.MsgVote",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="proposal_id",
            full_name="cosmos.gov.v1beta1.MsgVote.proposal_id",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\352\336\037\013proposal_id\362\336\037\022yaml:"proposal_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="voter",
            full_name="cosmos.gov.v1beta1.MsgVote.voter",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="option",
            full_name="cosmos.gov.v1beta1.MsgVote.option",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\350\240\037\000\230\240\037\000\200\334 \000\210\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=517,
    serialized_end=667,
)


_MSGVOTERESPONSE = _descriptor.Descriptor(
    name="MsgVoteResponse",
    full_name="cosmos.gov.v1beta1.MsgVoteResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=669,
    serialized_end=686,
)


_MSGVOTEWEIGHTED = _descriptor.Descriptor(
    name="MsgVoteWeighted",
    full_name="cosmos.gov.v1beta1.MsgVoteWeighted",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="proposal_id",
            full_name="cosmos.gov.v1beta1.MsgVoteWeighted.proposal_id",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\022yaml:"proposal_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="voter",
            full_name="cosmos.gov.v1beta1.MsgVoteWeighted.voter",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="options",
            full_name="cosmos.gov.v1beta1.MsgVoteWeighted.options",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\350\240\037\000\230\240\037\000\200\334 \000\210\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=689,
    serialized_end=847,
)


_MSGVOTEWEIGHTEDRESPONSE = _descriptor.Descriptor(
    name="MsgVoteWeightedResponse",
    full_name="cosmos.gov.v1beta1.MsgVoteWeightedResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=849,
    serialized_end=874,
)


_MSGDEPOSIT = _descriptor.Descriptor(
    name="MsgDeposit",
    full_name="cosmos.gov.v1beta1.MsgDeposit",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="proposal_id",
            full_name="cosmos.gov.v1beta1.MsgDeposit.proposal_id",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\352\336\037\013proposal_id\362\336\037\022yaml:"proposal_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="depositor",
            full_name="cosmos.gov.v1beta1.MsgDeposit.depositor",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="amount",
            full_name="cosmos.gov.v1beta1.MsgDeposit.amount",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\350\240\037\000\230\240\037\000\200\334 \000\210\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=877,
    serialized_end=1079,
)


_MSGDEPOSITRESPONSE = _descriptor.Descriptor(
    name="MsgDepositResponse",
    full_name="cosmos.gov.v1beta1.MsgDepositResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1081,
    serialized_end=1101,
)

_MSGSUBMITPROPOSAL.fields_by_name[
    "content"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MSGSUBMITPROPOSAL.fields_by_name[
    "initial_deposit"
].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_MSGVOTE.fields_by_name[
    "option"
].enum_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._VOTEOPTION
_MSGVOTEWEIGHTED.fields_by_name[
    "options"
].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._WEIGHTEDVOTEOPTION
_MSGDEPOSIT.fields_by_name[
    "amount"
].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name["MsgSubmitProposal"] = _MSGSUBMITPROPOSAL
DESCRIPTOR.message_types_by_name[
    "MsgSubmitProposalResponse"
] = _MSGSUBMITPROPOSALRESPONSE
DESCRIPTOR.message_types_by_name["MsgVote"] = _MSGVOTE
DESCRIPTOR.message_types_by_name["MsgVoteResponse"] = _MSGVOTERESPONSE
DESCRIPTOR.message_types_by_name["MsgVoteWeighted"] = _MSGVOTEWEIGHTED
DESCRIPTOR.message_types_by_name["MsgVoteWeightedResponse"] = _MSGVOTEWEIGHTEDRESPONSE
DESCRIPTOR.message_types_by_name["MsgDeposit"] = _MSGDEPOSIT
DESCRIPTOR.message_types_by_name["MsgDepositResponse"] = _MSGDEPOSITRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgSubmitProposal = _reflection.GeneratedProtocolMessageType(
    "MsgSubmitProposal",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGSUBMITPROPOSAL,
        "__module__": "cosmos.gov.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgSubmitProposal)
    },
)
_sym_db.RegisterMessage(MsgSubmitProposal)

MsgSubmitProposalResponse = _reflection.GeneratedProtocolMessageType(
    "MsgSubmitProposalResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGSUBMITPROPOSALRESPONSE,
        "__module__": "cosmos.gov.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgSubmitProposalResponse)
    },
)
_sym_db.RegisterMessage(MsgSubmitProposalResponse)

MsgVote = _reflection.GeneratedProtocolMessageType(
    "MsgVote",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGVOTE,
        "__module__": "cosmos.gov.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgVote)
    },
)
_sym_db.RegisterMessage(MsgVote)

MsgVoteResponse = _reflection.GeneratedProtocolMessageType(
    "MsgVoteResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGVOTERESPONSE,
        "__module__": "cosmos.gov.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgVoteResponse)
    },
)
_sym_db.RegisterMessage(MsgVoteResponse)

MsgVoteWeighted = _reflection.GeneratedProtocolMessageType(
    "MsgVoteWeighted",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGVOTEWEIGHTED,
        "__module__": "cosmos.gov.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgVoteWeighted)
    },
)
_sym_db.RegisterMessage(MsgVoteWeighted)

MsgVoteWeightedResponse = _reflection.GeneratedProtocolMessageType(
    "MsgVoteWeightedResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGVOTEWEIGHTEDRESPONSE,
        "__module__": "cosmos.gov.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgVoteWeightedResponse)
    },
)
_sym_db.RegisterMessage(MsgVoteWeightedResponse)

MsgDeposit = _reflection.GeneratedProtocolMessageType(
    "MsgDeposit",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGDEPOSIT,
        "__module__": "cosmos.gov.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgDeposit)
    },
)
_sym_db.RegisterMessage(MsgDeposit)

MsgDepositResponse = _reflection.GeneratedProtocolMessageType(
    "MsgDepositResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGDEPOSITRESPONSE,
        "__module__": "cosmos.gov.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.MsgDepositResponse)
    },
)
_sym_db.RegisterMessage(MsgDepositResponse)


DESCRIPTOR._options = None
_MSGSUBMITPROPOSAL.fields_by_name["content"]._options = None
_MSGSUBMITPROPOSAL.fields_by_name["initial_deposit"]._options = None
_MSGSUBMITPROPOSAL._options = None
_MSGSUBMITPROPOSALRESPONSE.fields_by_name["proposal_id"]._options = None
_MSGVOTE.fields_by_name["proposal_id"]._options = None
_MSGVOTE._options = None
_MSGVOTEWEIGHTED.fields_by_name["proposal_id"]._options = None
_MSGVOTEWEIGHTED.fields_by_name["options"]._options = None
_MSGVOTEWEIGHTED._options = None
_MSGDEPOSIT.fields_by_name["proposal_id"]._options = None
_MSGDEPOSIT.fields_by_name["amount"]._options = None
_MSGDEPOSIT._options = None

_MSG = _descriptor.ServiceDescriptor(
    name="Msg",
    full_name="cosmos.gov.v1beta1.Msg",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1104,
    serialized_end=1468,
    methods=[
        _descriptor.MethodDescriptor(
            name="SubmitProposal",
            full_name="cosmos.gov.v1beta1.Msg.SubmitProposal",
            index=0,
            containing_service=None,
            input_type=_MSGSUBMITPROPOSAL,
            output_type=_MSGSUBMITPROPOSALRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Vote",
            full_name="cosmos.gov.v1beta1.Msg.Vote",
            index=1,
            containing_service=None,
            input_type=_MSGVOTE,
            output_type=_MSGVOTERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="VoteWeighted",
            full_name="cosmos.gov.v1beta1.Msg.VoteWeighted",
            index=2,
            containing_service=None,
            input_type=_MSGVOTEWEIGHTED,
            output_type=_MSGVOTEWEIGHTEDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Deposit",
            full_name="cosmos.gov.v1beta1.Msg.Deposit",
            index=3,
            containing_service=None,
            input_type=_MSGDEPOSIT,
            output_type=_MSGDEPOSITRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name["Msg"] = _MSG

# @@protoc_insertion_point(module_scope)
