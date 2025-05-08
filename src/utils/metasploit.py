from functools import lru_cache

from pymetasploit3.msfrpc import MsfRpcClient


@lru_cache(maxsize=1)
def create_metasploit_client() -> MsfRpcClient:
    # thread-safe か要確認
    return MsfRpcClient("password", username="msf", server="localhost", port=55553, ssl=False)
