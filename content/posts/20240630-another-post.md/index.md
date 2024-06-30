---
date: 2024-06-30
draft: false
author: ハチアン
title: マークダウンお試し
categories: ["test"]
tags: ["markdown", "cat"]
---

> どこで生れたかとんと見当けんとうがつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。

## h2h2h2吾輩わがはいは猫である。名前はまだ無い。

### h3h3h3吾輩わがはいは猫である。名前はまだ無い。

#### h4h4h4吾輩わがはいは猫である。名前はまだ無い。

##### h5h5h5吾輩わがはいは猫である。名前はまだ無い。

## h2h2h2

どこで生れたか**とんと**見当けんとうがつかぬ。何でも薄暗い*じめじめした*所で`ニャーニャー(meow, meow)`泣いていた事だけは記憶している。吾輩はここで始めて<mark>人間</mark>というものを見た。

### h3h3h3

どこで生れたか**とんと**見当けんとうがつかぬ。何でも薄暗い*じめじめした*所で`ニャーニャー(meow, meow)`泣いていた事だけは記憶している。吾輩はここで始めて<mark>人間</mark>というものを見た。

#### h4h4h4吾輩わがはいは猫である。名前はまだ無い。

どこで生れたか**とんと**見当けんとうがつかぬ。何でも薄暗い*じめじめした*所で`ニャーニャー(meow, meow)`泣いていた事だけは記憶している。吾輩はここで始めて<mark>人間</mark>というものを見た。

##### h5h5h5吾輩わがはいは猫である。名前はまだ無い。

どこで生れたか**とんと**見当けんとうがつかぬ。何でも薄暗い*じめじめした*所で`ニャーニャー(meow, meow)`泣いていた事だけは記憶している。吾輩はここで始めて<mark>人間</mark>というものを見た。

## h2h2h2吾輩わがはいは猫である。名前はまだ無い。

- どこで生れたか**とんと**見当けんとうがつかぬ
    - 何でも薄暗い*じめじめした*所で`ニャーニャー(meow, meow)`泣いていた事だけは記憶している
        - 吾輩はここで始めて<mark>人間</mark>というものを見た


## h2h2h2吾輩わがはいは猫である。名前はまだ無い。

1. どこで生れたか**とんと**見当けんとうがつかぬ
1. 何でも薄暗い*じめじめした*所で`ニャーニャー(meow, meow)`泣いていた事だけは記憶している
1. 吾輩はここで始めて<mark>人間</mark>というものを見た

## 画像テスト

![alt text](image-1.png)

![alt text](image-2.png)

## テーブルテスト

| type1 | type2  | core | GB | USD    | Yen    | hours | Yen/M  | hours | Yen/M   |
| ----- | ------ | ---- | -- | ------ | ------ | ----- | ------ | ----- | ------- |
| t3    | medium | 2    | 4  | 0.0544 | ¥8.06  | 90    | ¥726   | 720   | ¥5,804  |
| r6g   | medium | 1    | 8  | 0.0608 | ¥9.01  | 90    | ¥811   | 720   | ¥6,487  |
| t4g   | medium | 2    | 4  | 0.0336 | ¥4.98  | 90    | ¥448   | 720   | ¥3,585  |
| t3    | large  | 2    | 8  | 0.1088 | ¥16.12 | 90    | ¥1,451 | 720   | ¥11,608 |
| a1    | xlarge | 4    | 8  | 0.1284 | ¥19.03 | 90    | ¥1,712 | 720   | ¥13,699 |
| t4g   | large  | 2    | 8  | 0.0864 | ¥12.80 | 90    | ¥1,152 | 720   | ¥9,218  |
| m6g   | large  | 2    | 8  | 0.099  | ¥14.67 | 90    | ¥1,320 | 720   | ¥10,563 |
| t3    | xlarge | 4    | 16 | 0.2176 | ¥32.25 | 90    | ¥2,902 | 720   | ¥23,216 |
| r6i   | large  | 2    | 16 | 0.152  | ¥22.52 | 90    | ¥2,027 | 720   | ¥16,217 |

## code

```python
import numpy as np
print(123)
print("abc")
for i in [1, 2, 3]:
    if i == 2:
        break
    print("meow")  # test
def func(a, b, c=3):
    print(a + b + c)
    for i in [1, 2, 3]:
        print("どこで生れたかとんと見当けんとうがつかぬ。何でも薄暗いじめじめした所でニャーニャー(meow, meow)泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。")
```

## quote

> どこで生れたか**とんと**見当けんとうがつかぬ。何でも薄暗い*じめじめした*所で`ニャーニャー(meow, meow)`泣いていた事だけは記憶している。吾輩はここで始めて<mark>人間</mark>というものを見た。
> ```python
> import numpy as np
> print(123)
> print("abc")
> for i in [1, 2, 3]:
>     if i == 2:
>         break
>     print("meow")  # test
> def func(a, b, c=3):
>     print(a + b + c)
> for i in [1, 2, 3]:
> print("どこで生れたかとんと見当けんとうがつかぬ。何でも薄暗いじめじめした所でニャーニャー(meow, meow)泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。")
> ```

## admonition

### note

{{< alert >}}
**Warning!** This action is destructive!
{{< /alert >}}

something between

{{< alert "twitter" >}}
Don't forget to [follow me](https://twitter.com/nunocoracao) on Twitter.
{{< /alert >}}

```
something between
```

{{< alert icon="fire" cardColor="#e63946" iconColor="#1d3557" textColor="#f1faee" >}}
This is an error!
{{< /alert >}}

combination

{{< alert icon="fire" cardColor="#e63946" iconColor="#1d3557" textColor="#f1faee" >}}
```python
import numpy as np
print(123)
print("abc")
for i in [1, 2, 3]:
    if i == 2:
        break
    print("meow")  # test
def func(a, b, c=3):
    print(a + b + c)
    for i in [1, 2, 3]:
        print("どこで生れたかとんと見当けんとうがつかぬ。何でも薄暗いじめじめした所でニャーニャー(meow, meow)泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。")
```

> どこで生れたか**とんと**見当けんとうがつかぬ。何でも薄暗い*じめじめした*所で`ニャーニャー(meow, meow)`泣いていた事だけは記憶している。吾輩はここで始めて<mark>人間</mark>というものを見た。

{{< /alert >}}
