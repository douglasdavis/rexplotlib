import numpy as np


def draw_ratio_with_line(ax, data, mc_sum, mc_err, yline=1.0, autoxscale=True):
    """ draw the ratio with a horizontal line on the axis """
    x1 = data.bins[0]
    x2 = data.bins[-1]
    err = np.sqrt(
        data.content / (mc_sum ** 2) + np.power(data.content * mc_err / (mc_sum ** 2), 2)
    )
    ax.plot([x1, x2], [yline, yline], color="gray", linestyle="solid", marker=None)
    ax.errorbar(data.bin_centers, data.content / mc_sum, yerr=err, fmt="ko", zorder=999)
    ax.set_ylabel("Data / MC")
    if autoxscale:
        ax.autoscale(enable=True, axis="x", tight=True)


def draw_atlas_label(ax, internal=True, extra_lines=[], x=0.050, y=0.905, s1=14, s2=12):
    """ draw the ATLAS label on the plot, with extra lines if desired """
    # fmt: off
    ax.text(x, y, "ATLAS", fontstyle="italic", fontweight="bold", transform=ax.transAxes, size=s1)
    if internal:
        ax.text(x + 0.15, y, r"Internal", transform=ax.transAxes, size=s1)
    for i, exline in enumerate(extra_lines):
        ax.text(x, y - (i + 1) * 0.06, exline, transform=ax.transAxes, size=s2)
    # fmt: on


def set_labels(ax, histogram):
    """ define the axis labels """
    if histogram.has_uniform_bins():
        ylabel_suffix = f" / {histogram.bin_width} {histogram.unit}"
    else:
        ylabel_suffix = f" / bin"
    ax.set_ylabel(f"Events{ylabel_suffix}", horizontalalignment="right", y=1.0)
