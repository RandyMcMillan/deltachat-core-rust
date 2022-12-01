from typing import TYPE_CHECKING

from .rpc import Rpc

if TYPE_CHECKING:
    from .message import Message


class Chat:
    def __init__(self, rpc: Rpc, account_id: int, chat_id: int) -> None:
        self.rpc = rpc
        self.account_id = account_id
        self.chat_id = chat_id

    async def block(self) -> None:
        """Block the chat."""
        await self.rpc.block_chat(self.account_id, self.chat_id)

    async def accept(self) -> None:
        """Accept the contact request."""
        await self.rpc.accept_chat(self.account_id, self.chat_id)

    async def delete(self) -> None:
        await self.rpc.delete_chat(self.account_id, self.chat_id)

    async def get_encryption_info(self) -> str:
        return await self.rpc.get_chat_encryption_info(self.account_id, self.chat_id)

    async def send_text(self, text: str) -> "Message":
        from .message import Message

        msg_id = await self.rpc.misc_send_text_message(
            self.account_id, self.chat_id, text
        )
        return Message(self.rpc, self.account_id, msg_id)

    async def leave(self) -> None:
        await self.rpc.leave_group(self.account_id, self.chat_id)

    async def get_fresh_message_count(self) -> int:
        return await self.rpc.get_fresh_msg_cnt(self.account_id, self.chat_id)
