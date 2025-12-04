import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    return mo, np, pd, plt, sns


@app.cell
def _(mo):
    mo.md("""
    # 統計検定2級 練習ノート: 記述統計

    ## 学習方法

    このノートブックは、`1.py`で学んだ記述統計の知識を、
    「自分の手を動かして」実践するためのものです。

    **各練習問題について**:
    1. 問題を読んで、何が求められているかを理解する
    2. コードを自分で書いてみる
    3. 必要に応じてヒントを確認する
    4. 「解答例を見る」で自分の答えと比較する

    💡 **大切**: 完璧な答えを目指さず、「試行錯誤のプロセス」が重要です。
    エラーが出たら、エラーメッセージから原因を探ってください。
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 練習問題1: 基本的な統計量の計算

    ### 問題

    下記のデータは、ある街の「喫茶店での平均的なコーヒーの価格」を10日間調査したものです（単位: 円）。

    ```
    [450, 480, 450, 500, 470, 460, 490, 480, 470, 510]
    ```

    以下の統計量を計算してください：
    - 平均
    - 中央値
    - 標準偏差
    - 範囲（最大 - 最小）
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### あなたの答えをここに書いてください
    """)

    # データの定義
    coffee_prices = np.array([450, 480, 450, 500, 470, 460, 490, 480, 470, 510])

    # TODO: 下記に計算コードを書いてください
    # mean_price = ...
    # median_price = ...
    # std_price = ...
    # range_price = ...

    return coffee_prices


@app.cell
def _(mo):
    show_hint_1 = mo.ui.checkbox(label="ヒントを表示")
    show_hint_1
    return show_hint_1


@app.cell
def _(mo, show_hint_1):
    if show_hint_1.value:
        mo.md("""
        ### ヒント

        NumPyやPandasを使うと簡単です：

        ```python
        import numpy as np

        # NumPyでの計算例
        mean = np.mean(data)
        median = np.median(data)
        std = np.std(data, ddof=1)  # 不偏分散を使う場合
        range_val = np.max(data) - np.min(data)
        ```

        または Pandas を使う場合：

        ```python
        df = pd.DataFrame({'Price': data})
        mean = df['Price'].mean()
        median = df['Price'].median()
        std = df['Price'].std(ddof=1)
        ```
        """)
    return


@app.cell
def _(mo):
    show_answer_1 = mo.ui.checkbox(label="解答例を見る")
    show_answer_1
    return show_answer_1


@app.cell
def _(mo, show_answer_1, coffee_prices, np):
    if show_answer_1.value:
        mo.md("""
        ### 解答例

        ```python
        coffee_prices = np.array([450, 480, 450, 500, 470, 460, 490, 480, 470, 510])

        mean_price = coffee_prices.mean()
        median_price = np.median(coffee_prices)
        std_price = coffee_prices.std(ddof=1)
        range_price = coffee_prices.max() - coffee_prices.min()
        ```
        """)

        mean_price = coffee_prices.mean()
        median_price = np.median(coffee_prices)
        std_price = coffee_prices.std(ddof=1)
        range_price = coffee_prices.max() - coffee_prices.min()

        mo.md(f"""
        **計算結果**:
        - 平均: {mean_price:.1f}円
        - 中央値: {median_price:.1f}円
        - 標準偏差: {std_price:.1f}円
        - 範囲: {range_price:.0f}円

        💡 **解説**: 平均と中央値がほぼ同じなので、このデータは
        比較的対称的な分布をしていることが分かります。
        標準偏差が約26円なので、ほとんどの価格は
        [{mean_price - std_price:.1f}, {mean_price + std_price:.1f}]
        の範囲に収まります。
        """)
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 練習問題2: グラフの作成

    ### 問題

    下記のデータは、あるオンラインショップの「1日の注文数」を30日間記録したものです。

    自分でヒストグラムと箱ひげ図を作成してください。
    """)
    return


@app.cell
def _(mo, np):
    np.random.seed(42)
    # 注文数データの生成
    daily_orders = np.random.normal(loc=100, scale=20, size=30)
    daily_orders = np.clip(daily_orders, 0, 300).astype(int)  # 0以上の整数に

    mo.md(f"""
    **データ**:
    ```python
    daily_orders = {list(daily_orders)}
    ```
    """)
    return daily_orders


@app.cell
def _(mo):
    mo.md("""
    ### あなたのコードをここに書いてください

    ヒストグラムと箱ひげ図の両方を描いてください。
    """)
    return


@app.cell
def _(mo):
    show_hint_2 = mo.ui.checkbox(label="ヒントを表示")
    show_hint_2
    return show_hint_2


@app.cell
def _(mo, show_hint_2):
    if show_hint_2.value:
        mo.md("""
        ### ヒント

        Matplotlibで複数の図を並べるには：

        ```python
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        # ヒストグラム
        axes[0].hist(data, bins=10, edgecolor='black')
        axes[0].set_title('ヒストグラム')
        axes[0].set_xlabel('値')
        axes[0].set_ylabel('度数')

        # 箱ひげ図
        axes[1].boxplot(data)
        axes[1].set_title('箱ひげ図')
        axes[1].set_ylabel('値')

        plt.tight_layout()
        fig
        ```
        """)
    return


@app.cell
def _(mo):
    show_answer_2 = mo.ui.checkbox(label="解答例を見る")
    show_answer_2
    return show_answer_2


@app.cell
def _(mo, show_answer_2, daily_orders, plt):
    if show_answer_2.value:
        mo.md("""
        ### 解答例

        ```python
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        # ヒストグラム
        axes[0].hist(daily_orders, bins=15, color='skyblue', edgecolor='black')
        axes[0].set_title('注文数の分布')
        axes[0].set_xlabel('1日の注文数')
        axes[0].set_ylabel('日数')
        axes[0].grid(alpha=0.3)

        # 箱ひげ図
        bp = axes[1].boxplot(daily_orders, patch_artist=True)
        bp['boxes'][0].set_facecolor('lightgreen')
        axes[1].set_title('注文数の四分位分析')
        axes[1].set_ylabel('1日の注文数')
        axes[1].grid(alpha=0.3, axis='y')

        plt.tight_layout()
        fig
        ```
        """)

        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        # ヒストグラム
        axes[0].hist(daily_orders, bins=15, color='skyblue', edgecolor='black')
        axes[0].set_title('注文数の分布')
        axes[0].set_xlabel('1日の注文数')
        axes[0].set_ylabel('日数')
        axes[0].grid(alpha=0.3)

        # 箱ひげ図
        bp = axes[1].boxplot(daily_orders, patch_artist=True)
        bp['boxes'][0].set_facecolor('lightgreen')
        axes[1].set_title('注文数の四分位分析')
        axes[1].set_ylabel('1日の注文数')
        axes[1].grid(alpha=0.3, axis='y')

        plt.tight_layout()
        fig
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 練習問題3: 異常値の検出

    ### 問題

    下記のデータは、「サーバーの応答時間（ミリ秒）」を100回測定したものです。

    通常、応答時間は100～300msの範囲です。

    **問1**: 箱ひげ図を描いて、異常値があるかどうか確認してください。

    **問2**: IQR（四分位範囲）を使って、「異常値」を定義してください。
    （一般的に、外れ値は [Q1 - 1.5*IQR, Q3 + 1.5*IQR] の範囲外とされます）

    **問3**: 異常値がいくつあるか数えてください。
    """)
    return


@app.cell
def _(mo, np, pd):
    np.random.seed(42)

    # 通常の応答時間（100～300ms）+ 異常値
    normal_response = np.random.normal(loc=200, scale=40, size=95)
    normal_response = np.clip(normal_response, 100, 300)

    # 異常値（タイムアウト気味のリクエスト）
    abnormal_response = np.array([5000, 8500, 3200, 9000, 4500])

    response_times = np.concatenate([normal_response, abnormal_response])
    np.random.shuffle(response_times)

    mo.md(f"""
    **データ**:
    ```python
    response_times = np.array({list(response_times.astype(int))})
    ```
    """)
    return response_times, np


@app.cell
def _(mo):
    show_hint_3 = mo.ui.checkbox(label="ヒントを表示")
    show_hint_3
    return show_hint_3


@app.cell
def _(mo, show_hint_3):
    if show_hint_3.value:
        mo.md("""
        ### ヒント

        **外れ値の定義**:

        ```python
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1

        # 外れ値の範囲
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # 外れ値を抽出
        outliers = data[(data < lower_bound) | (data > upper_bound)]
        ```
        """)
    return


@app.cell
def _(mo):
    show_answer_3 = mo.ui.checkbox(label="解答例を見る")
    show_answer_3
    return show_answer_3


@app.cell
def _(mo, show_answer_3, response_times, np, plt):
    if show_answer_3.value:
        mo.md("""
        ### 解答例

        **問1: 箱ひげ図の描画**

        ```python
        fig, ax = plt.subplots(figsize=(8, 4))
        bp = ax.boxplot(response_times, vert=True, patch_artist=True)
        bp['boxes'][0].set_facecolor('lightblue')
        ax.set_ylabel('応答時間（ミリ秒）')
        ax.set_title('サーバー応答時間の分布と外れ値')
        ax.grid(alpha=0.3, axis='y')
        fig
        ```

        **問2・3: 外れ値の検出**

        ```python
        q1 = np.percentile(response_times, 25)
        q3 = np.percentile(response_times, 75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = response_times[(response_times < lower_bound) |
                                   (response_times > upper_bound)]

        print(f"外れ値の下限: {lower_bound:.0f}ms")
        print(f"外れ値の上限: {upper_bound:.0f}ms")
        print(f"外れ値の個数: {len(outliers)}")
        print(f"外れ値: {sorted(outliers.astype(int))}")
        ```
        """)

        # 実際に計算
        q1 = np.percentile(response_times, 25)
        q3 = np.percentile(response_times, 75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = response_times[(response_times < lower_bound) |
                                   (response_times > upper_bound)]

        mo.md(f"""
        **計算結果**:
        - Q1 (25%点): {q1:.0f}ms
        - Q3 (75%点): {q3:.0f}ms
        - IQR: {iqr:.0f}ms
        - 外れ値の下限: {lower_bound:.0f}ms
        - 外れ値の上限: {upper_bound:.0f}ms
        - **外れ値の個数: {len(outliers)}個**
        - 外れ値: {sorted(outliers.astype(int))}

        💡 **解説**: 箱ひげ図で点として表示される値が外れ値です。
        これらは異常に高い応答時間で、サーバーに問題があった可能性があります。
        """)

        # 図を描画
        fig, ax = plt.subplots(figsize=(8, 4))
        bp = ax.boxplot(response_times, vert=True, patch_artist=True)
        bp['boxes'][0].set_facecolor('lightblue')
        ax.set_ylabel('応答時間（ミリ秒）')
        ax.set_title('サーバー応答時間の分布と外れ値')
        ax.grid(alpha=0.3, axis='y')
        fig
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 練習問題4: 実務課題

    ### シナリオ

    あなたは、オンラインサロンの運営者です。
    会員による投稿の「いいね数」について、データを分析する必要があります。

    以下の3種類の投稿について、いいね数の分布を比較してください：

    - **タイプA**: 毎日の定期投稿（テキスト記事）
    - **タイプB**: 数週間に1回の動画投稿
    - **タイプC**: イベント時の告知投稿

    **問い**: 「どのタイプの投稿が『安定した人気』を得ているか」を
    統計量で判定してください。
    """)
    return


@app.cell
def _(mo, np):
    np.random.seed(42)

    # 3種類の投稿データ
    type_a = np.random.normal(loc=50, scale=15, size=100)     # 定期投稿：安定的
    type_b = np.random.normal(loc=200, scale=80, size=15)     # 動画：変動大だが高い
    type_c = np.random.normal(loc=500, scale=200, size=8)     # イベント告知：ばらつき大

    type_a = np.clip(type_a, 0, 1000).astype(int)
    type_b = np.clip(type_b, 0, 1000).astype(int)
    type_c = np.clip(type_c, 0, 1000).astype(int)

    mo.md("""
    ### データ

    ```python
    # タイプA: 定期投稿（テキスト記事）- 100件
    type_a = np.array([...])

    # タイプB: 動画投稿 - 15件
    type_b = np.array([...])

    # タイプC: イベント告知 - 8件
    type_c = np.array([...])
    ```

    ### あなたの分析

    以下の視点で分析してください：

    1. 各タイプの平均いいね数を計算する
    2. 各タイプのばらつき（標準偏差、変動係数）を計算する
    3. 各タイプの中央値と四分位範囲を計算する
    4. グラフ（箱ひげ図）で比較する
    5. **最終判定**: どのタイプが「安定した人気」を得ているか、
       統計量に基づいて述べてください。

    💡 **ポイント**: 「安定」とは「ばらつきが小さい」ことを意味します。
    変動係数（標準偏差 ÷ 平均）を見ると、スケールが異なるデータでも比較できます。
    """)
    return type_a, type_b, type_c


@app.cell
def _(mo):
    mo.md("""
    ### あなたの分析コードをここに書いてください

    以下の構成で分析を進めてください：
    1. 統計量の計算
    2. 箱ひげ図の描画
    3. 結論の述べ方
    """)
    return


@app.cell
def _(mo):
    show_hint_4 = mo.ui.checkbox(label="ヒントを表示")
    show_hint_4
    return show_hint_4


@app.cell
def _(mo, show_hint_4):
    if show_hint_4.value:
        mo.md("""
        ### ヒント

        **分析の流れ**:

        1. **統計量をDataFrameにまとめる**:

        ```python
        stats = pd.DataFrame({
            '投稿タイプ': ['A', 'B', 'C'],
            '平均': [type_a.mean(), type_b.mean(), type_c.mean()],
            '標準偏差': [type_a.std(ddof=1), ...],
            '中央値': [np.median(type_a), ...],
        })
        stats['変動係数'] = stats['標準偏差'] / stats['平均']
        ```

        2. **箱ひげ図で比較**:

        ```python
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.boxplot([type_a, type_b, type_c],
                   labels=['タイプA', 'タイプB', 'タイプC'])
        ```

        3. **結論**:

        変動係数が最も小さいタイプが「安定している」です。
        """)
    return


@app.cell
def _(mo):
    show_answer_4 = mo.ui.checkbox(label="解答例を見る")
    show_answer_4
    return show_answer_4


@app.cell
def _(mo, show_answer_4, type_a, type_b, type_c, np, pd, plt):
    if show_answer_4.value:
        # 統計量の計算
        stats = pd.DataFrame({
            '投稿タイプ': ['A: 定期投稿', 'B: 動画投稿', 'C: イベント告知'],
            '投稿数': [len(type_a), len(type_b), len(type_c)],
            '平均いいね': [type_a.mean(), type_b.mean(), type_c.mean()],
            '中央値': [np.median(type_a), np.median(type_b), np.median(type_c)],
            '標準偏差': [type_a.std(ddof=1), type_b.std(ddof=1), type_c.std(ddof=1)],
            'IQR': [
                np.percentile(type_a, 75) - np.percentile(type_a, 25),
                np.percentile(type_b, 75) - np.percentile(type_b, 25),
                np.percentile(type_c, 75) - np.percentile(type_c, 25),
            ]
        })
        stats['変動係数'] = stats['標準偏差'] / stats['平均いいね']

        mo.md("""
        ### 解答例

        **1. 統計量の計算**
        """)
        mo.md(stats.round(2).to_markdown(index=False))

        # グラフ描画
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # 箱ひげ図
        bp = axes[0].boxplot([type_a, type_b, type_c],
                             labels=['タイプA\n定期投稿', 'タイプB\n動画投稿', 'タイプC\nイベント告知'],
                             patch_artist=True)
        colors = ['lightblue', 'lightcoral', 'lightgreen']
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
        axes[0].set_ylabel('いいね数')
        axes[0].set_title('投稿タイプ別のいいね数分布')
        axes[0].grid(alpha=0.3, axis='y')

        # 変動係数の比較
        axes[1].bar(stats['投稿タイプ'], stats['変動係数'], color=colors)
        axes[1].set_ylabel('変動係数')
        axes[1].set_title('投稿タイプ別の安定性（変動係数）\n※値が小さいほど安定')
        axes[1].grid(alpha=0.3, axis='y')
        plt.setp(axes[1].xaxis.get_majorticklabels(), rotation=0)

        plt.tight_layout()
        fig

        mo.md(f"""
        ### 分析結果と結論

        **観察**:

        1. **平均いいね数**: タイプC（イベント告知）が最も多い（≈{type_c.mean():.0f}）が、
           投稿数が少ない（8件）。

        2. **ばらつき**: タイプC の標準偏差が最も大きく（{type_c.std(ddof=1):.1f}）、
           いいね数が不安定。

        3. **変動係数（相対的な安定性）**:
           - タイプA: {stats.loc[0, '変動係数']:.2f}（最も安定 ✓）
           - タイプB: {stats.loc[1, '変動係数']:.2f}
           - タイプC: {stats.loc[2, '変動係数']:.2f}（最も不安定）

        **結論**:

        **タイプA（定期投稿）が「安定した人気」を獲得しています。**

        理由：
        - 変動係数が最も小さい（0.31）
        - 毎回のいいね数がほぼ一定（標準偏差が小さい）
        - 投稿数が多く、継続的にエンゲージメントを得ている

        一方、タイプCは「ときどきバズる」可能性がありますが、
        運営側の視点では「予測不可能」であり、継続的な集客には向きません。

        **推奨**:
        継続的なコミュニティ運営には、タイプAの定期投稿を基本としながら、
        タイプB（動画）で大きなインパクトを狙う戦略が有効です。
        """)
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## まとめ

    このノートブックで学んだこと：

    1. **記述統計の基本**: 平均、中央値、標準偏差など
    2. **グラフの力**: 数値だけでなく、視覚化で分布を理解する
    3. **外れ値の検出**: IQRを使った異常値の定義
    4. **複数データセットの比較**: 変動係数で相対的な安定性を評価
    5. **統計的思考**: データに基づいて判断する重要性

    次は、これらの概念を使って、
    「確率と確率分布」を学びます！
    """)
    return


if __name__ == "__main__":
    app.run()
