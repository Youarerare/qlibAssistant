"""
将表转为 utf8mb4（与 sync_dolt 一致，走 DoltHub HTTPS 写 API）。

说明：直连 MySQL（如 db.dolthub.com）在部分网络/DNS 环境下会报
2005 Unknown MySQL server host；写 API 使用 https://www.dolthub.com，通常可解析。
"""
from __future__ import annotations

import os
import sys
import uuid
from pathlib import Path

# 以 `python script/fix.py` 从项目根运行时，保证能 import 同目录下的 sync_dolt
_script_dir = Path(__file__).resolve().parent
if str(_script_dir) not in sys.path:
    sys.path.insert(0, str(_script_dir))

from sync_dolt import (  # noqa: E402
    DoltHubSqlError,
    dolt_merge_branches,
    dolt_sql_write,
)


def _sql_ident(name: str) -> str:
    return f"`{name.replace('`', '``')}`"


def force_fix_encoding() -> None:
    if not os.getenv("DOLT_TOKEN", "").strip():
        raise RuntimeError("未设置环境变量 DOLT_TOKEN（写入 DoltHub 需要有效 token）")

    fb = (os.getenv("DOLT_REF") or "main").strip() or "main"
    tb = f"fix-utf8-{uuid.uuid4().hex[:12]}"

    target_tables = [
        "qlib_score_ret",
        "qlib_score_filter_ret",
        "review_ret",
        "review_filter_ret",
    ]

    print("🛠️ 通过 DoltHub 写 API 转换表编码（utf8mb4）…")
    print(f"   基线分支 `{fb}` → 临时分支 `{tb}`")

    for table in target_tables:
        safe = _sql_ident(table)
        print(f" - ALTER {table} …")
        q = (
            f"ALTER TABLE {safe} CONVERT TO CHARACTER SET utf8mb4 "
            "COLLATE utf8mb4_unicode_ci"
        )
        dolt_sql_write(q, fb, tb)

    print("💾 CALL DOLT_COMMIT …")
    dolt_sql_write(
        "CALL DOLT_COMMIT('-am', 'System: Force reset encoding to utf8mb4')",
        fb,
        tb,
    )

    print(f"🔀 将 `{tb}` 合并进 `{fb}` …")
    dolt_merge_branches(tb, fb, message="fix: utf8mb4 for qlib_score/review tables")

    print("✅ 修复完成。")


if __name__ == "__main__":
    try:
        force_fix_encoding()
    except DoltHubSqlError as e:
        print(f"❌ 修复失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 修复失败: {e}")
        sys.exit(1)
