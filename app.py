
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="평균변화율과 미분가능성 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("📈 평균변화율로 알아보는 미분가능성")
st.caption("기준점에 가까워질수록 왼쪽과 오른쪽 할선의 기울기는 어떻게 변할까요?")

# -----------------------------
# 탐구 함수 6가지
# -----------------------------
FUNCTIONS = {
    "이차함수  f(x) = x²": lambda x: x**2,
    "삼차함수  f(x) = x³": lambda x: x**3,
    "사차함수  f(x) = x⁴": lambda x: x**4,
    "다항함수  f(x) = x⁴ - 2x³ - x² + 2x + 1":
        lambda x: x**4 - 2*x**3 - x**2 + 2*x + 1,
    "절댓값 함수  f(x) = |x|": lambda x: np.abs(x),
    "구간에 따라 식이 달라지는 함수":
        lambda x: np.where(x < 0, x**2, 2*x**2)
}

FUNCTION_EXPLANATIONS = {
    "이차함수  f(x) = x²":
        "부드럽게 이어지는 포물선입니다. 기준점을 바꾸어 가며 할선의 기울기가 어떻게 변하는지 관찰해 보세요.",
    "삼차함수  f(x) = x³":
        "원점 부근에서 그래프가 완만하게 지나갑니다. 기준점이 달라질 때 기울기 변화도 확인해 보세요.",
    "사차함수  f(x) = x⁴":
        "원점 근처에서는 그래프가 매우 완만합니다. 이동점이 가까워질 때 기울기가 어떻게 변하는지 살펴보세요.",
    "다항함수  f(x) = x⁴ - 2x³ - x² + 2x + 1":
        "여러 항이 함께 있는 다항함수입니다. 그래프 모양이 복잡해져도 좌우 할선의 기울기가 가까워지는지 확인해 보세요.",
    "절댓값 함수  f(x) = |x|":
        "원점에서 그래프가 꺾입니다. 특히 기준점을 0으로 설정하면 왼쪽과 오른쪽 기울기가 어떻게 나타나는지 확인할 수 있습니다.",
    "구간에 따라 식이 달라지는 함수":
        "0을 기준으로 왼쪽과 오른쪽의 식이 다릅니다. 식이 달라지는 지점에서도 좌우 기울기가 가까워지는지 관찰해 보세요."
}

# -----------------------------
# 계산 함수
# -----------------------------
def function_value(func, x):
    result = func(np.asarray(x))
    if np.isscalar(x):
        return float(result)
    return result


def secant_slope(func, a, x):
    """기준점과 이동점을 연결한 할선의 기울기"""
    if abs(x - a) < 1e-12:
        return np.nan

    return (function_value(func, x) - function_value(func, a)) / (x - a)


def get_slope_data(func, a, h):
    """왼쪽과 오른쪽의 세 이동점 기울기 계산"""
    fa = function_value(func, a)
    rows = []

    for multiple in [1, 2, 3]:
        distance = multiple * h
        left_x = a - distance
        right_x = a + distance

        left_slope = secant_slope(func, a, left_x)
        right_slope = secant_slope(func, a, right_x)

        rows.append({
            "이동 거리": distance,
            "왼쪽 이동점의 x좌표": left_x,
            "왼쪽 할선의 기울기": left_slope,
            "오른쪽 이동점의 x좌표": right_x,
            "오른쪽 할선의 기울기": right_slope,
            "좌우 기울기의 차이": abs(right_slope - left_slope)
        })

    return pd.DataFrame(rows)


def estimate_tangent(func, a):
    """아주 작은 간격으로 좌우 기울기를 비교해 접선 존재 여부 확인"""
    epsilon = 0.00001
    left = secant_slope(func, a, a - epsilon)
    right = secant_slope(func, a, a + epsilon)

    if abs(left - right) < 0.001:
        return (left + right) / 2

    return None


def make_convergence_data(func, a, start_h):
    """이동 거리를 계속 줄였을 때 좌우 기울기 변화"""
    rows = []

    for i in range(7):
        current_h = start_h / (2 ** i)
        left_slope = secant_slope(func, a, a - current_h)
        right_slope = secant_slope(func, a, a + current_h)

        rows.append({
            "이동 거리": current_h,
            "왼쪽 할선의 기울기": left_slope,
            "오른쪽 할선의 기울기": right_slope,
            "좌우 기울기의 차이": abs(right_slope - left_slope)
        })

    return pd.DataFrame(rows)


# -----------------------------
# 탐구 설정
# -----------------------------
st.sidebar.header("탐구 설정")

selected_name = st.sidebar.selectbox(
    "탐구할 함수 선택",
    list(FUNCTIONS.keys())
)
func = FUNCTIONS[selected_name]

a = st.sidebar.slider(
    "기준점 A의 x좌표",
    min_value=-3.0,
    max_value=3.0,
    value=1.0,
    step=0.1
)

h = st.sidebar.slider(
    "기본 이동 거리",
    min_value=0.05,
    max_value=1.0,
    value=0.5,
    step=0.05
)

st.sidebar.info(
    "이동 거리는 h, 2h, 3h로 설정됩니다. "
    "h를 작게 바꾸면 이동점들이 기준점에 더 가까워집니다."
)

# -----------------------------
# 데이터 계산
# -----------------------------
slope_df = get_slope_data(func, a, h)
convergence_df = make_convergence_data(func, a, h)

fa = function_value(func, a)
tangent_slope = estimate_tangent(func, a)

left_nearest = slope_df.iloc[0]["왼쪽 할선의 기울기"]
right_nearest = slope_df.iloc[0]["오른쪽 할선의 기울기"]
nearest_difference = abs(right_nearest - left_nearest)

# -----------------------------
# 현재 탐구 요약
# -----------------------------
st.subheader("현재 탐구 조건")

col1, col2, col3 = st.columns(3)
col1.metric("기준점 A", f"({a:.2f}, {fa:.2f})")
col2.metric("기본 이동 거리", f"{h:.2f}")
col3.metric("가장 가까운 두 기울기의 차이", f"{nearest_difference:.4f}")

st.write(FUNCTION_EXPLANATIONS[selected_name])

# -----------------------------
# 탭 구성
# -----------------------------
tab1, tab2, tab3 = st.tabs([
    "① 함수와 할선 그래프",
    "② 기울기 변화 관찰",
    "③ 결과와 해석"
])

# =========================================================
# 탭 1. 함수 그래프와 할선
# =========================================================
with tab1:
    st.subheader("함수 그래프에서 기준점과 이동점 확인하기")
    st.write(
        "A는 기준점입니다. 왼쪽과 오른쪽에 있는 세 이동점을 "
        "각각 A와 연결하면 여섯 개의 할선이 만들어집니다."
    )

    x_min = min(a - 3*h - 1, -3)
    x_max = max(a + 3*h + 1, 3)
    x_values = np.linspace(x_min, x_max, 500)
    y_values = function_value(func, x_values)

    fig = go.Figure()

    # 함수 그래프
    fig.add_trace(go.Scatter(
        x=x_values,
        y=y_values,
        mode="lines",
        name="함수 그래프",
        line=dict(width=3, color="#2563eb")
    ))

    # 기준점
    fig.add_trace(go.Scatter(
        x=[a],
        y=[fa],
        mode="markers+text",
        name="기준점 A",
        text=["A"],
        textposition="top center",
        marker=dict(size=13, color="black")
    ))

    # 왼쪽과 오른쪽 이동점 및 할선
    left_colors = ["#16a34a", "#65a30d", "#a3a3a3"]
    right_colors = ["#dc2626", "#ea580c", "#f59e0b"]

    for i, multiple in enumerate([1, 2, 3]):
        distance = multiple * h

        # 왼쪽 이동점
        lx = a - distance
        ly = function_value(func, lx)

        fig.add_trace(go.Scatter(
            x=[a, lx],
            y=[fa, ly],
            mode="lines",
            name=f"왼쪽 할선 {i+1}",
            line=dict(color=left_colors[i], width=2, dash="dash")
        ))

        fig.add_trace(go.Scatter(
            x=[lx],
            y=[ly],
            mode="markers+text",
            name=f"왼쪽 이동점 {i+1}",
            text=[f"L{i+1}"],
            textposition="bottom center",
            marker=dict(size=9, color=left_colors[i])
        ))

        # 오른쪽 이동점
        rx = a + distance
        ry = function_value(func, rx)

        fig.add_trace(go.Scatter(
            x=[a, rx],
            y=[fa, ry],
            mode="lines",
            name=f"오른쪽 할선 {i+1}",
            line=dict(color=right_colors[i], width=2, dash="dash")
        ))

        fig.add_trace(go.Scatter(
            x=[rx],
            y=[ry],
            mode="markers+text",
            name=f"오른쪽 이동점 {i+1}",
            text=[f"R{i+1}"],
            textposition="top center",
            marker=dict(size=9, color=right_colors[i])
        ))

    # 접선이 존재하는 경우 표시
    if tangent_slope is not None:
        tangent_x = np.array([x_min, x_max])
        tangent_y = fa + tangent_slope * (tangent_x - a)

        fig.add_trace(go.Scatter(
            x=tangent_x,
            y=tangent_y,
            mode="lines",
            name="기준점에서의 접선",
            line=dict(color="#9333ea", width=2.5)
        ))

    fig.update_layout(
        height=600,
        xaxis_title="x",
        yaxis_title="y",
        hovermode="closest",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.2,
            xanchor="left",
            x=0
        ),
        margin=dict(l=20, r=20, t=30, b=120)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "L1·L2·L3은 왼쪽 이동점, R1·R2·R3은 오른쪽 이동점입니다. "
        "숫자가 커질수록 기준점에서 더 멀리 떨어져 있습니다."
    )

    if tangent_slope is None:
        st.warning(
            "현재 기준점에서는 왼쪽과 오른쪽의 기울기가 서로 다르게 나타납니다. "
            "따라서 하나의 접선 기울기로 정하기 어렵습니다."
        )
    else:
        st.success(
            f"현재 기준점에서는 접선을 그릴 수 있습니다. "
            f"접선의 기울기는 약 {tangent_slope:.4f}입니다."
        )


# =========================================================
# 탭 2. 기울기 변화
# =========================================================
with tab2:
    st.subheader("이동 거리에 따른 왼쪽·오른쪽 기울기 변화")

    st.write(
        "이동 거리를 줄이면 할선의 기울기가 어떤 값에 가까워지는지 "
        "왼쪽과 오른쪽을 나누어 비교합니다."
    )

    slope_fig = go.Figure()

    slope_fig.add_trace(go.Scatter(
        x=convergence_df["이동 거리"],
        y=convergence_df["왼쪽 할선의 기울기"],
        mode="lines+markers",
        name="왼쪽 할선",
        line=dict(width=3, color="#16a34a")
    ))

    slope_fig.add_trace(go.Scatter(
        x=convergence_df["이동 거리"],
        y=convergence_df["오른쪽 할선의 기울기"],
        mode="lines+markers",
        name="오른쪽 할선",
        line=dict(width=3, color="#dc2626")
    ))

    slope_fig.update_layout(
        height=420,
        xaxis_title="기준점과 이동점 사이의 거리",
        yaxis_title="할선의 기울기",
        xaxis=dict(autorange="reversed"),
        hovermode="x unified",
        legend=dict(orientation="h", y=1.12)
    )

    st.plotly_chart(slope_fig, use_container_width=True)

    st.subheader("왼쪽과 오른쪽 기울기의 차이")

    difference_fig = go.Figure()
    difference_fig.add_trace(go.Scatter(
        x=convergence_df["이동 거리"],
        y=convergence_df["좌우 기울기의 차이"],
        mode="lines+markers",
        name="좌우 기울기의 차이",
        line=dict(width=3, color="#7c3aed"),
        fill="tozeroy"
    ))

    difference_fig.update_layout(
        height=350,
        xaxis_title="기준점과 이동점 사이의 거리",
        yaxis_title="두 기울기의 차이",
        xaxis=dict(autorange="reversed"),
        hovermode="x unified"
    )

    st.plotly_chart(difference_fig, use_container_width=True)

    st.caption(
        "두 기울기의 차이가 0에 가까워질수록 왼쪽과 오른쪽의 기울기가 "
        "서로 비슷해진다는 뜻입니다."
    )


# =========================================================
# 탭 3. 결과와 해석
# =========================================================
with tab3:
    st.subheader("현재 이동점 6개의 계산 결과")

    display_df = slope_df.copy()
    for column in display_df.columns:
        display_df[column] = display_df[column].round(4)

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("이동 거리를 줄였을 때의 변화")

    convergence_display = convergence_df.copy()
    for column in convergence_display.columns:
        convergence_display[column] = convergence_display[column].round(5)

    st.dataframe(
        convergence_display,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("탐구 결과 해석")

    if nearest_difference < 0.01:
        st.success(
            "가장 가까운 두 이동점에서 계산한 왼쪽과 오른쪽 기울기가 "
            "매우 비슷합니다. 현재 설정에서는 두 방향의 기울기가 "
            "같은 값에 가까워지는 모습을 관찰할 수 있습니다."
        )
    else:
        st.info(
            "가장 가까운 두 이동점에서 계산한 왼쪽과 오른쪽 기울기 사이에 "
            "차이가 있습니다. 이동 거리를 더 줄여도 이 차이가 줄어드는지 "
            "기울기 변화 그래프에서 확인해 보세요."
        )

    if tangent_slope is None:
        st.warning(
            "현재 기준점에서는 좌우 기울기가 서로 다른 값에 가까워집니다. "
            "이 지점에서는 미분가능하지 않은 모습을 확인할 수 있습니다."
        )
    else:
        st.success(
            "현재 기준점에서는 좌우 기울기가 같은 값에 가까워집니다. "
            "이 지점에서는 미분가능한 모습을 확인할 수 있습니다."
        )

    st.subheader("탐구할 때 생각해 볼 질문")
    st.markdown(
        """
        1. 이동 거리를 줄일수록 왼쪽과 오른쪽 기울기는 어떻게 변하나요?
        2. 두 기울기의 차이가 계속 작아지는 함수와 그렇지 않은 함수는 무엇인가요?
        3. 그래프가 꺾이는 지점에서는 어떤 차이가 나타나나요?
        4. 함수의 식이 달라지는 지점에서도 좌우 기울기가 같아질 수 있나요?
        """
    )

    # CSV 다운로드
    csv_data = convergence_df.to_csv(
        index=False,
        encoding="utf-8-sig"
    )

    st.download_button(
        label="수렴 분석 결과 CSV 다운로드",
        data=csv_data,
        file_name="좌우_할선_수렴_분석.csv",
        mime="text/csv"
    )
