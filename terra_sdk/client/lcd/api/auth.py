from typing import Union

from terra_sdk.core import AccAddress
from terra_sdk.core.auth import Account, LazyGradedVestingAccount

from ._base import BaseAsyncAPI, sync_bind

__all__ = ["AsyncAuthAPI", "AuthAPI"]


class AsyncAuthAPI(BaseAsyncAPI):
    async def account_info(
        self, address: AccAddress
    ) -> Union[Account, LazyGradedVestingAccount]:
        """Fetches the account information.

        Args:
            address (AccAddress): account address

        Returns:
            Union[Account, LazyGradedVestingAccount]: account information
        """
        result = await self._c._get(f"/auth/accounts/{address}")
        if result["type"] == "core/Account":
            return Account.from_data(result)
        else:
            return LazyGradedVestingAccount.from_data(result)


class AuthAPI(AsyncAuthAPI):
    @sync_bind(AsyncAuthAPI.account_info)
    def account_info(
        self, address: AccAddress
    ) -> Union[Account, LazyGradedVestingAccount]:
        pass
