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
    # 統計検定2級 学習ノート: 記述統計（1変数データ）

    ## なぜ記述統計が必要か？

    毎日の売上データ、ウェブサイトのアクセス数、テストの点数...
    実務では膨大なデータが得られます。しかし、100個の数値を眺めてもデータの特徴は見えません。

    **記述統計**は、データを少数の統計量とグラフで要約し、データの特徴を「一目で分かる形」にする手法です。

    このノートブックでは、実務で使えるデータセットを例に、記述統計の基本を学びます。
    パラメータを動かしたり、自分で分析したりしながら、「何がわかるか」を体験してください。
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 1. 実例1: ECサイトの日次売上分析

    **シナリオ**: あなたはECサイトのデータアナリストです。
    過去90日間の日次売上データが渡されました。
    「今月の売上はどうだったのか？」「安定しているか？」「異常な日はあるか？」
    こうした質問に答えるために、データを分析します。

    ---
    """)
    return


@app.cell
def _(mo, np, pd):
    # ECサイト売上データの生成（90日間）
    np.random.seed(42)

    # ベース: 平日は平均50万円、標準偏差10万円
    weekday_sales = np.random.normal(loc=50, scale=10, size=64)

    # 週末: 30%多い（平均65万円、標準偏差15万円）
    weekend_sales = np.random.normal(loc=65, scale=15, size=18)

    # セール日: 外れ値として大きな売上
    sale_day_values = np.array([120, 115, 125])

    # 90日間のデータを組み立て
    daily_sales = np.concatenate([weekday_sales, weekend_sales, sale_day_values])
    np.random.shuffle(daily_sales)

    df_ec = pd.DataFrame({
        'Day': range(1, 91),
        'Sales': daily_sales  # 万円
    })

    df_ec


@app.cell
def _(mo, df_ec):
    mo.md(f"""
    ### 中心傾向の指標：「データの中心はどこか？」

    #### 平均値 (Mean)
    全データを足して個数で割った値。データの「代表値」として最もよく使われます。

    $$\\bar{{x}} = \\frac{{1}}{{n}} \\sum_{{i=1}}^{{n}} x_i$$

    #### 中央値 (Median)
    データを小さい順に並べたとき、ちょうど真ん中にくる値。
    外れ値（異常に大きい/小さい値）の影響を受けにくいのが特徴です。

    #### 最頻値 (Mode)
    最も頻繁に出現する値。

    ---

    ### ECサイト売上データの分析結果
    """)

    mean_sales = df_ec['Sales'].mean()
    median_sales = df_ec['Sales'].median()
    mode_sales = df_ec['Sales'].round(0).mode()

    mo.md(f"""
    - **平均売上**: {mean_sales:.1f}万円
    - **中央値**: {median_sales:.1f}万円
    - **最頻値**: 計算省略（連続データのため多くの値が1回ずつ）

    💡 **ポイント**: 平均と中央値がほぼ同じです。これは、セール日（外れ値）の影響が限定的
    （90日中たった3日）であることを示しています。
    """)

    return mean_sales, median_sales


@app.cell
def _(mo, df_ec):
    mo.md("""
    ---

    ## 2. 散らばりの指標：「データの安定性は？」

    データの「ばらつき」を数値化することで、
    「ほぼ毎日同じくらいの売上か」「日によって大きく変わるか」を判定できます。

    #### 分散 (Variance)
    偏差（各データと平均の差）の二乗の平均。

    $$s^2 = \\frac{{1}}{{n-1}} \\sum_{{i=1}}^{{n}} (x_i - \\bar{{x}})^2$$

    #### 標準偏差 (Standard Deviation)
    分散の正の平方根。元のデータと同じ単位になるため、直感的に理解しやすい。

    $$s = \\sqrt{{s^2}}$$

    #### 範囲 (Range) / 四分位範囲 (IQR)
    - **範囲**: 最大値と最小値の差
    - **IQR**: 中央より下の50%（第1四分位数）から中央より上の50%（第3四分位数）までの範囲

    ---

    ### ECサイト売上データの分析結果
    """)

    var_sales = df_ec['Sales'].var(ddof=1)
    std_sales = df_ec['Sales'].std(ddof=1)
    range_sales = df_ec['Sales'].max() - df_ec['Sales'].min()
    q1_sales = df_ec['Sales'].quantile(0.25)
    q3_sales = df_ec['Sales'].quantile(0.75)
    iqr_sales = q3_sales - q1_sales

    mo.md(f"""
    - **分散**: {var_sales:.1f}
    - **標準偏差**: {std_sales:.1f}万円
    - **範囲**: {range_sales:.1f}万円（最小 {df_ec['Sales'].min():.1f}、最大 {df_ec['Sales'].max():.1f}）
    - **四分位範囲 (IQR)**: {iqr_sales:.1f}万円

    💡 **ポイント**: 標準偏差が約19万円です。つまり、ほとんどのデータは
    [平均 - 標準偏差, 平均 + 標準偏差] = [{mean_sales - std_sales:.1f}, {mean_sales + std_sales:.1f}]
    の範囲に収まります（正規分布の68%ルール）。
    """)

    return var_sales, std_sales, iqr_sales, q1_sales, q3_sales


@app.cell
def _(mo, df_ec, mean_sales, std_sales, plt, sns, q1_sales, q3_sales):
    mo.md("""
    ---

    ## 3. データの可視化：「分布を見える化する」

    数値だけでなく、グラフで見ることで、分布の形が一目で分かります。

    """)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # ヒストグラム
    axes[0].hist(df_ec['Sales'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    axes[0].axvline(mean_sales, color='red', linestyle='--', linewidth=2, label=f'平均: {mean_sales:.1f}万円')
    axes[0].axvline(mean_sales - std_sales, color='green', linestyle=':', linewidth=2, label=f'±1 標準偏差')
    axes[0].axvline(mean_sales + std_sales, color='green', linestyle=':', linewidth=2)
    axes[0].set_xlabel('売上（万円）')
    axes[0].set_ylabel('日数')
    axes[0].set_title('ヒストグラム：売上分布の形状')
    axes[0].legend()
    axes[0].grid(alpha=0.3)

    # 箱ひげ図
    bp = axes[1].boxplot(df_ec['Sales'], vert=True, patch_artist=True)
    bp['boxes'][0].set_facecolor('lightgreen')
    axes[1].set_ylabel('売上（万円）')
    axes[1].set_title('箱ひげ図：四分位範囲と外れ値')
    axes[1].grid(alpha=0.3, axis='y')

    plt.tight_layout()
    fig

    return


@app.cell
def _(mo):
    mo.md("""
    ### グラフから読み取れること

    - **ヒストグラム**: 分布がほぼ正規分布（釣鐘型）に見えます。
      平日と週末の二つの山が見えるかもしれません。
    - **箱ひげ図**: セール日（点で表示される外れ値）が右側に見えます。
      通常の営業日は箱（IQR）内に集中しています。
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 4. 実例2: 複数データセットの比較

    記述統計を複数のデータセット比較に使える例を示します。

    ### シナリオ: 異なる商品カテゴリの売上比較

    あなたの会社には3つの商品カテゴリがあります：
    - **カテゴリA**: 安定した売上（変動小）
    - **カテゴリB**: 成長中だが変動大（トレンド上昇中）
    - **カテゴリC**: 市場が小さい（売上金額も小さい）

    これらを比較する際、「カテゴリBは変動が大きいから不安定」と判断するのは早計です。
    **相対的な変動**（変動係数）を見る必要があります。
    """)
    return


@app.cell
def _(mo, np, pd):
    np.random.seed(42)

    # 3つのカテゴリのデータ生成
    cat_a = np.random.normal(loc=30, scale=5, size=90)      # 平均30, 標準偏差5（安定）
    cat_b = np.random.normal(loc=50, scale=20, size=90)     # 平均50, 標準偏差20（変動大）
    cat_c = np.random.normal(loc=10, scale=3, size=90)      # 平均10, 標準偏差3（小規模）

    df_comparison = pd.DataFrame({
        'カテゴリA': cat_a,
        'カテゴリB': cat_b,
        'カテゴリC': cat_c
    })

    # 統計量を計算
    stats = pd.DataFrame({
        'カテゴリ': ['A', 'B', 'C'],
        '平均売上': [cat_a.mean(), cat_b.mean(), cat_c.mean()],
        '標準偏差': [cat_a.std(ddof=1), cat_b.std(ddof=1), cat_c.std(ddof=1)],
    })

    # 変動係数（相対的な変動）= 標準偏差 / 平均
    stats['変動係数'] = stats['標準偏差'] / stats['平均売上']

    mo.md("""
    ### 複数カテゴリの統計量比較

    変動係数 = 標準偏差 / 平均売上
    （0に近いほど安定、大きいほど変動が大きい）
    """)

    stats


@app.cell
def _(mo, df_comparison, plt):
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    for idx, category in enumerate(['カテゴリA', 'カテゴリB', 'カテゴリC']):
        axes[idx].hist(df_comparison[category], bins=15, color=['skyblue', 'lightcoral', 'lightgreen'][idx],
                       edgecolor='black', alpha=0.7)
        axes[idx].set_title(f'{category}の売上分布')
        axes[idx].set_xlabel('売上')
        axes[idx].set_ylabel('日数')
        axes[idx].grid(alpha=0.3)

    plt.tight_layout()
    fig
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 5. 応用: データ変換で複数科目を比較

    テストの点数は科目によって満点が異なることがあります。
    - 数学：100点満点
    - 英語：80点満点

    こうした異なるスケールのデータを比較するには、**標準化（Z-score）** や
    **偏差値**を使います。
    """)
    return


@app.cell
def _(mo, np, pd):
    np.random.seed(42)

    # 2つの科目のテスト点数（50人）
    math_scores = np.random.normal(loc=70, scale=12, size=50)
    english_scores = np.random.normal(loc=65, scale=10, size=50)

    # クリッピング（100点満点、0点以上の制約）
    math_scores = np.clip(math_scores, 0, 100)
    english_scores = np.clip(english_scores, 0, 100)

    df_scores = pd.DataFrame({
        '数学': math_scores,
        '英語': english_scores
    })

    # 標準化（Z-score）
    df_scores['数学_z'] = (df_scores['数学'] - df_scores['数学'].mean()) / df_scores['数学'].std(ddof=1)
    df_scores['英語_z'] = (df_scores['英語'] - df_scores['英語'].mean()) / df_scores['英語'].std(ddof=1)

    # 偏差値（平均50、標準偏差10）
    df_scores['数学_偏差値'] = 50 + 10 * df_scores['数学_z']
    df_scores['英語_偏差値'] = 50 + 10 * df_scores['英語_z']

    mo.md("""
    ### 標準化と偏差値の計算

    **標準化（Z-score）**:
    $$z_i = \\frac{{x_i - \\bar{{x}}}}{{s}}$$

    **偏差値**:
    $$T_i = 50 + 10 \\times z_i$$

    ---

    ### 結果の先頭5行
    """)

    df_scores.head()


@app.cell
def _(mo, df_scores):
    mo.md(f"""
    ### 統計量の確認

    | 科目 | 平均点 | 標準偏差 | 平均偏差値 | 偏差値の標準偏差 |
    |-----|-------|--------|---------|-------------|
    | 数学 | {df_scores['数学'].mean():.1f} | {df_scores['数学'].std(ddof=1):.1f} | {df_scores['数学_偏差値'].mean():.1f} | {df_scores['数学_偏差値'].std(ddof=1):.1f} |
    | 英語 | {df_scores['英語'].mean():.1f} | {df_scores['英語'].std(ddof=1):.1f} | {df_scores['英語_偏差値'].mean():.1f} | {df_scores['英語_偏差値'].std(ddof=1):.1f} |

    💡 **ポイント**: 偏差値に変換することで、異なる満点や平均を持つ科目を公平に比較できます。
    偏差値60以上なら、その科目で上位～約16%に入っていることを意味します。
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 6. インタラクティブ実験室

    ここまで、実務的なデータセットを分析してきました。

    ここからは、正規分布のパラメータを自由に変えて、
    「統計量やグラフがどのように変わるか」を体験することで、
    統計的な直感を磨きます。
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### パラメータを調整してデータを生成
    """)

    mu_slider = mo.ui.slider(start=0, stop=100, step=5, value=50, label="平均 (Mean)")
    sigma_slider = mo.ui.slider(start=1, stop=30, step=1, value=10, label="標準偏差 (Std Dev)")
    n_slider = mo.ui.slider(start=10, stop=500, step=10, value=100, label="サンプルサイズ (N)")

    mo.hstack([mu_slider, sigma_slider, n_slider], justify="center")
    return mu_slider, sigma_slider, n_slider


@app.cell
def _(mo, mu_slider, sigma_slider, n_slider, np, pd):
    np.random.seed(42)
    data = np.random.normal(loc=mu_slider.value, scale=sigma_slider.value, size=n_slider.value)
    df_experiment = pd.DataFrame(data, columns=['Value'])

    mean_exp = df_experiment['Value'].mean()
    median_exp = df_experiment['Value'].median()
    std_exp = df_experiment['Value'].std(ddof=1)

    mo.md(f"""
    ### 統計量の自動計算

    **パラメータ**:
    - 平均: {mu_slider.value}
    - 標準偏差: {sigma_slider.value}
    - サンプルサイズ: {n_slider.value}

    **計算結果**:
    - 平均: {mean_exp:.2f}
    - 中央値: {median_exp:.2f}
    - 標準偏差: {std_exp:.2f}

    💡 **観察**: スライダーを動かすと、統計量がリアルタイムで変わります。
    サンプルサイズを大きくすると、計算結果が「指定した値」に近づくことに気づきます。
    """)
    return df_experiment, mean_exp, std_exp


@app.cell
def _(df_experiment, mean_exp, std_exp, plt, sns):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # ヒストグラム
    axes[0].hist(df_experiment['Value'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    axes[0].axvline(mean_exp, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_exp:.2f}')
    axes[0].axvline(mean_exp + std_exp, color='green', linestyle=':', linewidth=2, label=f'±1 Std Dev')
    axes[0].axvline(mean_exp - std_exp, color='green', linestyle=':', linewidth=2)
    axes[0].set_xlabel('Value')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Histogram')
    axes[0].legend()
    axes[0].grid(alpha=0.3)

    # 箱ひげ図
    bp = axes[1].boxplot(df_experiment['Value'], vert=True, patch_artist=True)
    bp['boxes'][0].set_facecolor('lightgreen')
    axes[1].set_ylabel('Value')
    axes[1].set_title('Boxplot')
    axes[1].grid(alpha=0.3, axis='y')

    plt.tight_layout()
    fig
    return


if __name__ == "__main__":
    app.run()
