import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle
import numpy as np


def plot_comparison(before_error, after_error, before_health, after_health):
    """Create a figure with bar plots comparing error rates and health scores."""
    labels = ["Before", "After"]
    error_vals = [before_error, after_error]
    health_vals = [before_health, after_health]

    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    fig.patch.set_facecolor("#000000")

    ax_err = axes[0]
    ax_err.set_facecolor("#000000")
    ax_err.bar(labels, error_vals, color=["#facc15", "#facc15"])
    ax_err.set_ylabel("Error Rate", color="#facc15")
    ax_err.set_title("Error Rate Comparison", color="#facc15")
    ax_err.tick_params(colors="#facc15")

    ax_health = axes[1]
    ax_health.set_facecolor("#000000")
    ax_health.bar(labels, health_vals, color=["#facc15", "#facc15"])
    ax_health.set_ylabel("Health Score", color="#facc15")
    ax_health.set_title("Health Score Comparison", color="#facc15")
    ax_health.tick_params(colors="#facc15")

    fig.tight_layout()

    return fig


def _health_speedometer(health: float, title: str):
    """Create a semicircular speedometer for a health score in [0, 100]."""

    value = max(0, min(100, health))

    fig, ax = plt.subplots(figsize=(3.5, 2))
    fig.patch.set_facecolor("#000000")
    ax.set_aspect("equal")
    ax.axis("off")

    # Background arc
    bg = Wedge((0, 0), 1, 180, 0, facecolor="#111111", edgecolor="#facc15", linewidth=1.5)
    ax.add_patch(bg)

    # Colored arc for value
    angle = 180 * (value / 100.0)
    fg = Wedge((0, 0), 1, 180, 180 - angle, facecolor="#facc15", edgecolor="#facc15")
    ax.add_patch(fg)

    # Needle
    needle_angle_deg = 180 - angle
    needle_angle_rad = needle_angle_deg * np.pi / 180.0
    needle_length = 0.9
    x = needle_length * np.cos(needle_angle_rad)
    y = needle_length * np.sin(needle_angle_rad)
    ax.plot([0, x], [0, y], color="#facc15", linewidth=2)

    # Center cap
    ax.add_patch(Circle((0, 0), 0.04, color="#facc15"))

    # Ticks and labels
    for t in [0, 25, 50, 75, 100]:
        t_angle = 180 - 180 * (t / 100.0)
        t_rad = t_angle * np.pi / 180.0
        tx = 1.05 * np.cos(t_rad)
        ty = 1.05 * np.sin(t_rad)
        ax.text(tx, ty, str(t), ha="center", va="center", fontsize=7, color="#facc15")

    ax.text(0, -0.25, f"{value:.1f}%", ha="center", va="center", fontsize=9, color="#facc15")
    ax.text(0, 0.4, title, ha="center", va="center", fontsize=9, color="#facc15")

    return fig


def health_speedometer_before(health: float):
    return _health_speedometer(health, "Before Health Score")


def health_speedometer_after(health: float):
    return _health_speedometer(health, "After Health Score")
