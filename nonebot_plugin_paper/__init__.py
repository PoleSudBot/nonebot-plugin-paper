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
## 🔍 核心指令 (Core Commands)

- **paper -s [keyword]** - 通过关键词搜索论文
  示例：`paper -s LLM agents`
- **paper -id [Paper ID]** - 通过 ID 获取论文详情
  示例：`paper -id 1706.03762`

## 🔗 自动解析 (Auto Detection)

- **[arXiv Link]** - 直接监听链接解析
  支持 abstract/PDF 链接

## ⚙️ 高级过滤 (Advanced Filters,配合 -s 使用)

- **--number [int]** - 结果数量上限 (默认 1)
- **--sort [criterion]** - 排序依据 (relevance / lastUpdatedDate / submittedDate)
- **--order [order]** - 排序规则 (ascending / descending)
- **--start [index]** - 结果偏移量

> 💡 提示：示例：`paper -s transformer --number 3 --sort submittedDate`
""".strip(),
    type="application",
    homepage="https://github.com/BalconyJH/nonebot-plugin-paper",
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna", "nonebot_plugin_uninfo"
    ),
    config=Config,
    extra={
        "author": "BalconyJH",
        "version": "unknown",
        "menu_type": "一些工具",
    },
)

driver = get_driver()


@driver.on_startup
async def init():
    await connection_verification()
