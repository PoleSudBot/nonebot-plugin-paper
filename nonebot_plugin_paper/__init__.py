from nonebot import get_driver, require

require("nonebot_plugin_alconna")
require("nonebot_plugin_localstore")
require("nonebot_plugin_uninfo")
require("nonebot_plugin_apscheduler")
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

from .command import paper_cmd  # noqa: F401
from .config import Config
from .utils import connection_verification

__plugin_meta__ = PluginMetadata(
    name="arXiv search",
    description="Nonebot-plugin-paper，a lightweight arXiv paper search tool—supports keyword/ID search and automatic link resolution, designed for academic research.",
    usage="""
🔍 Core Commands
• paper -s [keyword]
  └─ Search papers by keyword
  Example: `paper -s LLM agents`
• paper -id [Paper ID]
  └─ Get paper details by ID
  Example: `paper -id 1706.03762`

🔗 Auto Detection
• [arXiv Link]
  └─ Direct link parsing & preview
  Supports abstract/PDF links

⚙️ Advanced Filters (Use with -s)
• --number [int]: Result limit (default 1)
• --sort [criterion]: Sort basis
  (relevance / lastUpdatedDate / submittedDate)
• --order [order]: Sort order
  (ascending / descending)
• --start [index]: Result offset

> Example: `paper -s transformer --number 3 --sort submittedDate`

👥 Credits
• Authors: BalconyJH, HibiKier
""",
    type="application",
    homepage="https://github.com/BalconyJH/nonebot-plugin-paper",
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna", "nonebot_plugin_uninfo"
    ),
    config=Config,
)

driver = get_driver()


@driver.on_startup
async def init():
    await connection_verification()
