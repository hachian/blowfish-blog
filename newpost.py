import datetime
import shutil
from pathlib import Path


current = datetime.datetime.now()
dir_date_format = current.strftime("%Y%m%d")
front_date_format = current.strftime("%Y-%m-%d")
basedir = Path(f"./content/posts/{dir_date_format}-title")
basedir.mkdir(parents=True, exist_ok=True)
shutil.copyfile("./content/posts/20240629-template/feature.png", basedir / "feature.png")

content = f"""\
---
date: {front_date_format}
draft: false
author: ハチアン
title: タイトル
categories: ["Category"]
tags: ["#Tag1", "#Tag2"]
series: DELETE THIS LINE
series_order: 2  (DELETE THIS LINE)
lastmod: {front_date_format}
---
"""

with open(basedir / "index.md", 'w', encoding='utf-8') as ofs:
    ofs.write(content)
