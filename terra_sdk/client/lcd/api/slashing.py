from datetime import datetime
from typing import List, Optional, Union

from terra_sdk.core import ValConsPubKey, Numeric, Dec

from ._base import BaseAsyncAPI, sync_bind

__all__ = ["AsyncSlashingAPI", "SlashingAPI"]


class AsyncSlashingAPI(BaseAsyncAPI):

    # TODO: untested
    async def signing_info(
        self, val_cons_pub_key: ValConsPubKey
    ) -> Union[List[dict], dict]:
        """Fetches signing info for a validator consensus public key.

        Args:
            val_cons_pub_key (ValConsPubKey): validator consensus public key.

        Returns:
            Union[List[dict], dict]: signing info
        """
        res = await self._c._get(f'/cosmos/slashing/v1beta1/signing_infos/${val_cons_pub_key}')
        info = res["info"]
        return {
            "address": info["address"],
            "start_height": Numeric.parse(info["start_height"]),
            "index_offset": Numeric.parse(info["index_offset"]),
            "jailed_until": info["jailed_until"],  # TODO: convert to datetime
            "tombstoned": bool(info["tombstoned"]),
            "missed_blocks_counter": Numeric.parse(info["missed_blocks_counter"])
        }

    async def signing_infos(self): # -> Union[List[dict], dict]:
        """Fetches all signing info.

        Returns:
            Union[List[dict], dict]: signing infos
        """
        res = await self._c._get('/cosmos/slashing/v1beta1/signing_infos')
        infos = res["info"]
        return [
            {
                "address": info["address"],
                "start_height": Numeric.parse(info["start_height"]),
                "index_offset": Numeric.parse(info["index_offset"]),
                "jailed_until": info["jailed_until"],  # TODO: convert to datetime
                "tombstoned": bool(info["tombstoned"]),
                "missed_blocks_counter": Numeric.parse(info["missed_blocks_counter"])
            }
            for info in infos
        ]

    async def parameters(self) -> dict:
        """Fetches Slashing module parameters.

        Returns:
            dict: Slashing module parameters
        """
        res = await self._c._get("/cosmos/slashing/v1beta1/params")
        params = res.get("params")
        return {
            "signed_blocks_window": Numeric.parse(params["signed_blocks_window"]),
            "min_signed_per_window": Dec(params["min_signed_per_window"]),
            "downtime_jail_duration": params["downtime_jail_duration"],
            "slash_fraction_double_sign": Dec(params["slash_fraction_double_sign"]),
            "slash_fraction_downtime": Dec(params["slash_fraction_downtime"])
        }


class SlashingAPI(AsyncSlashingAPI):

    @sync_bind(AsyncSlashingAPI.signing_info)
    def signing_info(
        self, val_cons_pub_key: ValConsPubKey
    ) -> List[dict]:
        pass

    signing_info.__doc__ = AsyncSlashingAPI.signing_info.__doc__

    @sync_bind(AsyncSlashingAPI.signing_infos)
    def signing_infos(self) -> List[dict]:
        pass

    signing_infos.__doc__ = AsyncSlashingAPI.signing_infos.__doc__


    @sync_bind(AsyncSlashingAPI.parameters)
    def parameters(self) -> dict:
        pass

    parameters.__doc__ = AsyncSlashingAPI.parameters.__doc__
