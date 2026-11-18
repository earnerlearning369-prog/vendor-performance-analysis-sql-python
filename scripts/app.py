import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Enterprise Inventory Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for high-end aesthetic dark styling
st.markdown(
    """
    <style>
        .main { background-color: #07090e; }
        .stMetric { background-color: #0f172a; padding: 15px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.08); }
        .css-1544g2n { padding-top: 1rem; }
        h1, h2, h3 { color: #f8fafc !important; font-family: 'Inter', sans-serif; }
        p { color: #94a3b8; }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 2. DATA SIMULATION & MAPPING (All 7 Snippets)
# ---------------------------------------------------------
np.random.seed(42)

top_vendors_names = [
    "DIAGEO NORTH AMERICA",
    "MARTIGNETTI COMPANIES",
    "PERNOD RICARD USA",
    "JIM BEAM BRANDS",
    "BACARDI USA",
    "CONSTELLATION",
    "E&J GALLO",
    "BROWN-FORMAN",
    "ULTRA BEVERAGE",
    "M S WALKER",
]
top_vendors_vals = [68.0, 39.0, 32.0, 31.0, 25.0, 24.0, 18.0, 18.0, 17.0, 15.0]

top_brands_names = [
    "Jack Daniels No 7",
    "Tito's Vodka",
    "Grey Goose",
    "Capt Morgan",
    "Absolut",
    "Jameson",
    "Ketel One",
    "Baileys",
    "Kahlua",
    "Tanqueray",
]
top_brands_vals = [8.0, 7.4, 7.2, 6.4, 6.2, 5.7, 5.1, 4.2, 3.6, 3.5]

purchase_contribs = [16.3, 8.3, 7.8, 7.6, 5.7, 5.0, 4.3, 3.9, 3.6, 3.2]
total_contrib = sum(purchase_contribs)
cumulative_contrib = np.cumsum(purchase_contribs)

n_scatter = 200
all_sales = np.random.uniform(10, 800, n_scatter)
all_margins = np.random.uniform(10, 90, n_scatter)
target_sales = np.random.uniform(10, 200, 30)
target_margins = np.random.uniform(60, 95, 30)

order_sizes = ["Small", "Medium", "Large", "Bulk"]
box_data = {
    "Small": np.random.normal(25, 5, 50),
    "Medium": np.random.normal(20, 4, 50),
    "Large": np.random.normal(15, 3, 50),
    "Bulk": np.random.normal(10, 2, 50),
}

cat_vendors = ["DIAGEO", "MARTIGNETTI", "PERNOD", "JIM BEAM", "BACARDI"]
cat_counts = [120, 95, 80, 60, 45]

top_vendor_margins = np.random.normal(65, 8, 100)
low_vendor_margins = np.random.normal(35, 10, 100)
top_mean, top_lower, top_upper = (
    np.mean(top_vendor_margins),
    np.percentile(top_vendor_margins, 2.5),
    np.percentile(top_vendor_margins, 97.5),
)
low_mean, low_lower, low_upper = (
    np.mean(low_vendor_margins),
    np.percentile(low_vendor_margins, 2.5),
    np.percentile(low_vendor_margins, 97.5),
)

# ---------------------------------------------------------
# 3. SIDEBAR CONTROLS & FILTERS
# ---------------------------------------------------------
st.sidebar.title("🎛️ Control Hub")
st.sidebar.markdown(
    "Filter analytics views and explore deep operational parameters."
)

selected_view = st.sidebar.radio(
    "Navigate Analytics",
    [
        "Executive Master View",
        "1. Purchase & Contribution Analysis",
        "2. Brand Pricing Strategy (Scatter)",
        "3. Top Performers (Sales)",
        "4. Pareto Analysis",
        "6. Bulk Purchasing Impact",
        "7. Margin Distribution & CI",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Use Streamlit tabs or views to drill into insights.")

# ---------------------------------------------------------
# 4. MAIN APP HEADER & EXECUTIVE METRICS
# ---------------------------------------------------------
st.title("🚀 Enterprise Inventory & Vendor Intelligence Hub")
st.markdown(
    "A unified decision-making dashboard synthesizing multi-metric analytics models."
)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Tracked Sales", "$441.41M", "+12.4% YoY")
col2.metric("Total Purchase Allocation", "$307.34M", "-3.2% optimization")
col3.metric("Top 10 Contribution", f"{total_contrib:.1f}%", "High Concentration")
col4.metric("Average Profit Margin", "38.7%", "+2.1% target")

st.markdown("---")

# ---------------------------------------------------------
# 5. VIEW ROUTING LOGIC
# ---------------------------------------------------------

if selected_view == "Executive Master View":
    st.subheader("📊 Master Overview (All 7 Analytical Vectors)")

    # Row 1: Donut & Scatter
    r1_c1, r1_c2 = st.columns(2)

    with r1_c1:
        st.markdown("### 1. Purchase Contribution %")
        fig_donut = go.Figure(
            data=[
                go.Pie(
                    labels=top_vendors_names + ["Other Vendors"],
                    values=purchase_contribs + [100 - total_contrib],
                    hole=0.7,
                    textinfo="none",
                    hoverinfo="label+percent",
                )
            ]
        )
        fig_donut.update_layout(
            paper_bgcolor="#0f172a",
            plot_bgcolor="#1e293b",
            font=dict(color="#f8fafc"),
            height=350,
            margin=dict(t=20, b=20, l=20, r=20),
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    with r1_c2:
        st.markdown("### 2. Brands Pricing Targets")
        fig_scatter = go.Figure()
        fig_scatter.add_trace(
            go.Scatter(
                x=all_sales,
                y=all_margins,
                mode="markers",
                marker=dict(size=5, color="#60a5fa", opacity=0.4),
                name="All Brands",
            )
        )
        fig_scatter.add_trace(
            go.Scatter(
                x=target_sales,
                y=target_margins,
                mode="markers",
                marker=dict(size=7, color="#f43f5e", symbol="diamond"),
                name="Target Brands",
            )
        )
        fig_scatter.update_layout(
            paper_bgcolor="#0f172a",
            plot_bgcolor="#1e293b",
            font=dict(color="#f8fafc"),
            height=350,
            margin=dict(t=20, b=20, l=20, r=20),
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    # Row 2: Top Vendors & Top Brands Bars
    r2_c1, r2_c2 = st.columns(2)

    with r2_c1:
        st.markdown("### 3. Top 10 Vendors by Sales")
        fig_vbar = go.Figure(
            data=[
                go.Bar(
                    y=top_vendors_names[::-1],
                    x=top_vendors_vals[::-1],
                    orientation="h",
                    marker=dict(color="#3b82f6"),
                    text=[f"${v}M" for v in top_vendors_vals[::-1]],
                    textposition="inside",
                )
            ]
        )
        fig_vbar.update_layout(
            paper_bgcolor="#0f172a",
            plot_bgcolor="#1e293b",
            font=dict(color="#f8fafc"),
            height=350,
            margin=dict(t=20, b=20, l=20, r=20),
        )
        st.plotly_chart(fig_vbar, use_container_width=True)

    with r2_c2:
        st.markdown("### 3. Top 10 Brands by Sales")
        fig_bbar = go.Figure(
            data=[
                go.Bar(
                    y=top_brands_names[::-1],
                    x=top_brands_vals[::-1],
                    orientation="h",
                    marker=dict(color="#f43f5e"),
                    text=[f"${v}M" for v in top_brands_vals[::-1]],
                    textposition="inside",
                )
            ]
        )
        fig_bbar.update_layout(
            paper_bgcolor="#0f172a",
            plot_bgcolor="#1e293b",
            font=dict(color="#f8fafc"),
            height=350,
            margin=dict(t=20, b=20, l=20, r=20),
        )
        st.plotly_chart(fig_bbar, use_container_width=True)

elif selected_view == "1. Purchase & Contribution Analysis":
    st.subheader("Deep Dive: Vendor Purchase Contribution & Pareto Modeling")
    st.markdown(
        "Analyze how specific top-tier vendors drive overall capital allocation requirements."
    )

    fig_pareto = go.Figure()
    fig_pareto.add_trace(
        go.Bar(
            x=top_vendors_names,
            y=purchase_contribs,
            marker=dict(color="#0ea5e9"),
            name="Contribution %",
        )
    )
    fig_pareto.add_trace(
        go.Scatter(
            x=top_vendors_names,
            y=cumulative_contrib,
            mode="lines+markers",
            line=dict(color="#f43f5e", width=2, dash="dash"),
            name="Cumulative %",
            yaxis="y2",
        )
    )
    fig_pareto.update_layout(
        title="Pareto Analysis: Vendor Contribution vs Cumulative Share",
        yaxis=dict(title="Contribution %"),
        yaxis2=dict(
            title="Cumulative %", overlaying="y", side="right", range=[0, 105]
        ),
        paper_bgcolor="#0f172a",
        plot_bgcolor="#1e293b",
        font=dict(color="#f8fafc"),
        height=500,
    )
    st.plotly_chart(fig_pareto, use_container_width=True)

elif selected_view == "2. Brand Pricing Strategy (Scatter)":
    st.subheader("Deep Dive: Promotional & Pricing Adjustment Matrix")
    st.markdown(
        "Isolate underperforming or high-margin target brands requiring immediate pricing optimization."
    )

    fig_scatter_deep = go.Figure()
    fig_scatter_deep.add_trace(
        go.Scatter(
            x=all_sales,
            y=all_margins,
            mode="markers",
            marker=dict(size=8, color="#60a5fa", opacity=0.5),
            name="All Brands Inventory",
        )
    )
    fig_scatter_deep.add_trace(
        go.Scatter(
            x=target_sales,
            y=target_margins,
            mode="markers",
            marker=dict(size=12, color="#f43f5e", symbol="diamond"),
            name="Target Action Brands",
        )
    )
    fig_scatter_deep.update_layout(
        xaxis_title="Total Sales ($)",
        yaxis_title="Profit Margin (%)",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#1e293b",
        font=dict(color="#f8fafc"),
        height=600,
    )
    st.plotly_chart(fig_scatter_deep, use_container_width=True)

elif selected_view == "6. Bulk Purchasing Impact":
    st.subheader("Deep Dive: Impact of Order Size on Unit Cost")
    st.markdown(
        "Evaluate unit purchase price variances across scale brackets (Small to Bulk orders)."
    )

    fig_box = go.Figure()
    for size, vals in box_data.items():
        fig_box.add_trace(
            go.Box(y=vals, name=size, marker_color="#818cf8")
        )

    fig_box.update_layout(
        yaxis_title="Average Unit Purchase Price ($)",
        xaxis_title="Order Scale Bracket",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#1e293b",
        font=dict(color="#f8fafc"),
        height=500,
    )
    st.plotly_chart(fig_box, use_container_width=True)

else:
    st.subheader("Analytical Insights & Summary Module")
    st.info(
        "Select an active inspection vector from the sidebar to evaluate deep statistical distributions, confidence parameters, or category frequencies."
    )
    
    # Display Confidence interval overview snippet (Snippet 7)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### Top Vendors Margin CI (95%)")
        st.success(f"Mean: **{top_mean:.2f}%**\nRange: **({top_lower:.2f}, {top_upper:.2f})**")
    with col_b:
        st.markdown("### Low Vendors Margin CI (95%)")
        st.error(f"Mean: **{low_mean:.2f}%**\nRange: **({low_lower:.2f}, {low_upper:.2f})**") 
