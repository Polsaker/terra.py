import base64
import json
from typing import Any, List, Union

from terra_sdk.core import Numeric
from terra_sdk.core.wasm.data import AbsoluteTxPosition, HistoryEntry

from ._base import BaseAsyncAPI, sync_bind

__all__ = ["AsyncWasmAPI", "WasmAPI"]


class AsyncWasmAPI(BaseAsyncAPI):
    async def code_info(self, code_id: int) -> dict:
        """Fetches information about an uploaded code.

        Args:
            code_id (int): code ID

        Returns:
            dict: code information
        """
        res = await self._c._get(f"/cosmwasm/wasm/v1/code/{code_id}")
        code_info = res.get("code_info")
        return {
            "code_id": Numeric.parse(code_info["code_id"]),
            "data_hash": code_info["data_hash"],
            "creator": code_info["creator"],
            "instantiate_permission": code_info["instantiate_permission"],
        }

    async def contract_history(self, contract_address: str) -> List[HistoryEntry]:
        """Fetches contract history.

        Args:
            contract_address (str): contract address

        Returns:
            List[HistoryEntry]: contract histories
        """

        res = await self._c._get(
            f"/cosmwasm/wasm/v1/contract/{contract_address}/history"
        )

        return [HistoryEntry.from_data(entry) for entry in res["entries"]]

    async def contract_info(self, contract_address: str) -> dict:
        """Fetches information about an instantiated contract.

        Args:
            contract_address (str): contract address

        Returns:
            dict: contract information
        """
        res = await self._c._get(f"/cosmwasm/wasm/v1/contract/{contract_address}")
        contract_info = res.get("contract_info")
        contract_address = res.get("address")
        history_entries = self.contract_history(contract_address)
        return {
            "code_id": Numeric.parse(contract_info["code_id"]),
            "address": contract_address,
            "creator": contract_info["creator"],
            "admin": contract_info.get("admin", None),
            "label": contract_info.get("label", None),
            "init_msg": history_entries[0].msg,
            "created": AbsoluteTxPosition.from_data(contract_info.get("created"))
            if contract_info.get("created", None)
            else None,
            "ibc_port_id": contract_info.get("ibc_port_id", None),
        }

    async def contract_query(
        self, contract_address: str, query: Union[dict, str]
    ) -> Any:
        """Runs a QueryMsg on a contract.

        Args:
            contract_address (str): contract address
            query (dict): QueryMsg to run

        Returns:
            Any: results of query
        """
        query_msg = base64.b64encode(json.dumps(query).encode("utf-8")).decode("utf-8")
        res = await self._c._get(
            f"/cosmwasm/wasm/v1/contract/{contract_address}/smart/{query_msg}"
        )
        return res.get("data")

    async def pinned_codes(self) -> dict:
        """Fetches the Wasm module pinned codes.

        Returns:
            dict: Wasm module pinned codes
        """
        res = await self._c._get("/cosmwasm/wasm/v1/codes/pinned")
        params = res.get("code_ids")
        return {
            "code_ids": params,
        }


class WasmAPI(AsyncWasmAPI):
    @sync_bind(AsyncWasmAPI.code_info)
    def code_info(self, code_id: int) -> dict:
        pass

    code_info.__doc__ = AsyncWasmAPI.code_info.__doc__

    @sync_bind(AsyncWasmAPI.contract_info)
    def contract_info(self, contract_address: str) -> dict:
        pass

    contract_info.__doc__ = AsyncWasmAPI.contract_info.__doc__

    @sync_bind(AsyncWasmAPI.contract_query)
    def contract_query(self, contract_address: str, query: Union[dict, str]) -> Any:
        pass

    contract_query.__doc__ = AsyncWasmAPI.contract_query.__doc__

    @sync_bind(AsyncWasmAPI.pinned_codes)
    def pinned_codes(self) -> dict:
        pass

    pinned_codes.__doc__ = AsyncWasmAPI.pinned_codes.__doc__

    @sync_bind(AsyncWasmAPI.contract_history)
    def contract_history(self, contract_address: str) -> List[HistoryEntry]:
        pass

    contract_history.__doc__ = AsyncWasmAPI.contract_history.__doc__
