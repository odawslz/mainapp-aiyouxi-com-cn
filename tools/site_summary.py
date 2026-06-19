#!/usr/bin/env python3

def load_site_entries():
    """Return a list of site entries as dictionaries."""
    return [
        {
            "url": "https://mainapp-aiyouxi.com.cn",
            "keywords": ["爱游戏", "游戏平台", "在线娱乐"],
            "tags": ["游戏", "平台", "娱乐"],
            "description": "爱游戏是一个提供多种在线游戏和娱乐内容的综合平台。"
        },
        {
            "url": "https://mainapp-aiyouxi.com.cn/about",
            "keywords": ["关于我们", "爱游戏简介", "公司介绍"],
            "tags": ["关于", "介绍", "公司"],
            "description": "了解爱游戏平台的背景、使命和发展历程。"
        },
        {
            "url": "https://mainapp-aiyouxi.com.cn/games",
            "keywords": ["游戏列表", "热门游戏", "新游戏"],
            "tags": ["游戏", "列表", "热门"],
            "description": "浏览爱游戏平台上的所有游戏，包括热门和新上架的游戏。"
        },
        {
            "url": "https://mainapp-aiyouxi.com.cn/help",
            "keywords": ["帮助中心", "客服", "常见问题"],
            "tags": ["帮助", "客服", "FAQ"],
            "description": "获取爱游戏平台的使用帮助和常见问题解答。"
        }
    ]


def format_entry(entry, index):
    """Format a single site entry into a readable string block."""
    lines = [
        f"站点 {index + 1}",
        f"URL: {entry['url']}",
        f"关键词: {', '.join(entry['keywords'])}",
        f"标签: {', '.join(entry['tags'])}",
        f"简介: {entry['description']}",
        "-" * 40
    ]
    return "\n".join(lines)


def generate_summary(entries):
    """Generate a structured summary from the list of entries."""
    if not entries:
        return "没有站点资料可输出。"

    header = "站点资料摘要\n" + "=" * 40 + "\n"
    body_parts = [header]
    for idx, entry in enumerate(entries):
        body_parts.append(format_entry(entry, idx))
    footer = f"共 {len(entries)} 个站点条目。"
    body_parts.append(footer)
    return "\n".join(body_parts)


def main():
    entries = load_site_entries()
    summary = generate_summary(entries)
    print(summary)


if __name__ == "__main__":
    main()