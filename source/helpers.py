

import pandas as pd


def churn_rate_by(df: pd.DataFrame, column: str, target: str = "Churn") -> pd.DataFrame:
    """Return customer count and churn rate (%) for each value of `column`.

    The churn rate is calculated within each group, not across the whole dataset.
    """
    churned = df[target].eq("Yes")
    summary = churned.groupby(df[column]).agg(["size", "mean"])
    summary.columns = ["customers", "churn_rate_pct"]
    summary["churn_rate_pct"] = (summary["churn_rate_pct"] * 100).round(2)
    return summary.sort_values("churn_rate_pct", ascending=False)




def plot_churn_rate(
    summary: pd.DataFrame,
    title: str,
    ax=None,
    baseline: float | None = None,
    sort: bool = True,
):
    """Horizontal bar chart of churn rate per group, with group sizes in the labels.

    `baseline` draws a dashed reference line (e.g. the overall churn rate).
    """
    import matplotlib.pyplot as plt

    if ax is None:
        _, ax = plt.subplots(figsize=(7, 3.5))

    # barh places the first row at the bottom, so order rows for display.
    data = (
        summary.sort_values("churn_rate_pct")
        if sort
        else summary.iloc[::-1]
    )
    labels = [
        f"{group} (n={customers:,})"
        for group, customers in zip(data.index, data["customers"])
    ]
    rates = data["churn_rate_pct"]
    bars = ax.barh(labels, rates)
    ax.bar_label(bars, fmt="%.1f%%", padding=3)

    if baseline is not None:
        ax.axvline(baseline, color="gray", linestyle="--", linewidth=1)

    ax.set_xlabel("Churn rate (%)")
    ax.set_title(title)

    # Preserve a shared x-axis limit while leaving room for bar labels.
    current_limit = ax.get_xlim()[1]
    required_limit = rates.max() * 1.2
    ax.set_xlim(0, max(current_limit, required_limit))
    return ax



def tenureSegments(df: pd.DataFrame) -> pd.DataFrame:
    """Saperates the tenure by 6 months.

    Args:
        df (pd.DataFrame): The overall data frame

    Returns:
        pd.DataFrame: The data frame that has the new cutted tenure.
    """

    df["tenure_segment"] = pd.cut(
    df["tenure"], bins=[-1, 12, 24, 48, 72], labels=["0-12", "13-24", "25-48", "49-72"])
    return df

