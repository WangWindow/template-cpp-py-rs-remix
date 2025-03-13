import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_test_data(n=100):
    """
    生成测试数据
    """
    np.random.seed(42)
    x = np.linspace(0, 10, n)
    y = 2 * x + 1 + np.random.normal(0, 2, n)
    categories = np.random.choice(["A", "B", "C", "D"], size=n)

    # 创建DataFrame
    df = pd.DataFrame({"x": x, "y": y, "category": categories})

    return df


def plot_data(df):
    """
    创建多种可视化图表
    """
    # 设置风格
    sns.set_style("whitegrid")

    # 创建一个2x2的子图布局
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 1. 散点图 (上左)
    sns.scatterplot(data=df, x="x", y="y", hue="category", ax=axes[0, 0])
    axes[0, 0].set_title("散点图 - 按类别着色")

    # 2. 回归图 (上右)
    sns.regplot(data=df, x="x", y="y", ax=axes[0, 1])
    axes[0, 1].set_title("线性回归拟合")

    # 3. 箱线图 (下左)
    sns.boxplot(data=df, x="category", y="y", ax=axes[1, 0])
    axes[1, 0].set_title("箱线图 - 按类别分组")

    # 4. 小提琴图 (下右)
    sns.violinplot(data=df, x="category", y="y", ax=axes[1, 1])
    axes[1, 1].set_title("小提琴图 - 按类别分组")

    plt.tight_layout()
    plt.savefig("out/visualization_demo.png")
    plt.show()


def analyze_data(df):
    """
    对数据进行简单分析
    """
    print("数据概述:")
    print(df.describe())

    print("\n按类别分组的统计:")
    print(df.groupby("category")["y"].agg(["mean", "std", "count"]))

    print("\n相关性:")
    print(df[["x", "y"]].corr())


def main():
    """
    主函数
    """
    print("生成测试数据并进行可视化分析...")

    # 生成测试数据
    df = generate_test_data(200)

    # 数据分析
    analyze_data(df)

    # 数据可视化
    plot_data(df)

    print("分析完成，图表已保存为 'visualization_demo.png'")


if __name__ == "__main__":
    main()
