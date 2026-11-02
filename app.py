
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# =====================================
# 1. 페이지 설정
# =====================================
st.set_page_config(
    page_title="평균변화율과 미분가능성 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("📈 평균변화율로 알아보는 미분가능성")
st.write(
    "기준점에 왼쪽과 오른쪽에서 가까워지는 점을 움직이며 "
    "할선의 기울기와 미분가능성을 탐구합니다."
)

# =====================================
# 2. 탐구 함수 8가지
# =====================================
FUNCTIONS = {
    "이차함수  f(x) = x²":
        lambda x: np.asarray(x) ** 2,

    "삼차함수  f(x) = x³":
        lambda x: np.asarray(x) ** 3,

    "사차함수  f(x) = x⁴":
        lambda x: np.asarray(x) ** 4,

    "다항함수  f(x) = x⁴ - 2x³ - x² + 2x + 1":
        lambda x: (
            np.asarray(x) ** 4
            - 2 * np.asarray(x) ** 3
            - np.asarray(x) ** 2
            + 2 * np.asarray(x) + 1
        ),

    "절댓값 함수  f(x) = |x|":
        lambda x: np.abs(np.asarray(x)),

    "구간에 따라 식이 달라지는 함수":
        lambda x: np.where(
            np.asarray(x) < 0,
            np.asarray(x) ** 2,
            2 * np.asarray(x) ** 2
        ),

    "극값을 가지는 삼차함수  f(x) = x³ - 3x":
        lambda x: np.asarray(x) ** 3 - 3 * np.asarray(x),

    "극값을 가지는 사차함수  f(x) = x⁴ - 4x²":
        lambda x: np.asarray(x) ** 4 - 4 * np.asarray(x) ** 2
}

EXPLANATIONS = {
    "이차함수  f(x) = x²":
        "포물선 모양의 그래프입니다. 기준점을 바꾸면서 기울기가 어떻게 달라지는지 살펴보세요.",

    "삼차함수  f(x) = x³":
        "원점 부근에서 완만하게 지나가는 그래프입니다. 기준점에 가까워지는 방향에 따라 기울기를 비교해 보세요.",

    "사차함수  f(x) = x⁴":
        "원점 근처에서 그래프가 매우 완만해집니다. 이동 거리를 줄였을 때 기울기가 어떻게 변하는지 확인해 보세요.",

    "다항함수  f(x) = x⁴ - 2x³ - x² + 2x + 1":
        "여러 항이 더해진 다항함수입니다. 그래프 모양이 복잡해도 좌우 기울기가 가까워지는지 확인해 보세요.",

    "절댓값 함수  f(x) = |x|":
        "원점에서 그래프가 꺾이는 모양입니다. 기준점을 0으로 설정하면 왼쪽과 오른쪽 기울기의 차이를 확인할 수 있습니다.",

    "구간에 따라 식이 달라지는 함수":
        "0을 기준으로 왼쪽과 오른쪽의 식이 다릅니다. 식이 달라져도 미분이 가능할 수 있다는 점을 확인해 보세요.",

    "극값을 가지는 삼차함수  f(x) = x³ - 3x":
        "극댓값과 극솟값이 각각 하나씩 나타나는 삼차함수입니다. 극값이 나타나는 지점에서 좌우 기울기를 비교해 보세요.",

    "극값을 가지는 사차함수  f(x) = x⁴ - 4x²":
        "극댓값 하나와 극솟값 두 개가 나타나는 사차함수입니다. 세 극값의 위치에서 기울기가 어떻게 나타나는지 살펴보세요."
}


# =====================================
# 3. 계산 함수
# =====================================
def f_value(func, x):
    result = func(x)

    if np.isscalar(x):
        return float(result)

    return np.asarray(result, dtype=float)


def slope(func, a, x):
    """기준점과 이동점을 연결한 할선의 기울기"""
    if abs(x - a) < 1e-12:
        return np.nan

    return (
        f_value(func, x) - f_value(func, a)
    ) / (x - a)


def slope_table(func, a, h):
    rows = []

    for n in [1, 2, 3]:
        distance = n * h

        lx = a - distance
        rx = a + distance

        rows.append({
            "이동점": f"L{n}",
            "방향": "왼쪽",
            "이동 거리": distance,
            "x좌표": lx,
            "y좌표": f_value(func, lx),
            "할선의 기울기": slope(func, a, lx)
        })

        rows.append({
            "이동점": f"R{n}",
            "방향": "오른쪽",
            "이동 거리": distance,
            "x좌표": rx,
            "y좌표": f_value(func, rx),
            "할선의 기울기": slope(func, a, rx)
        })

    return pd.DataFrame(rows)


def convergence_table(func, a, h):
    rows = []

    for i in range(8):
        distance = h / (2 ** i)

        left = slope(func, a, a - distance)
        right = slope(func, a, a + distance)

        rows.append({
            "이동 거리": distance,
            "왼쪽 기울기": left,
            "오른쪽 기울기": right,
            "두 기울기의 차이": abs(right - left)
        })

    return pd.DataFrame(rows)


# =====================================
# 4. 미분가능 여부 판정
# =====================================
def is_differentiable_here(name, a):
    # 절댓값 함수는 원점에서 미분 불가능
    if (
        name == "절댓값 함수  f(x) = |x|"
        and abs(a) < 1e-9
    ):
        return False

    # 나머지 함수는 이 코드에서 정의한 모든 점에서 미분 가능
    return True


def tangent_slope(func, a):
    """아주 작은 간격으로 접선 기울기를 근사"""
    epsilon = 0.00001

    left = slope(func, a, a - epsilon)
    right = slope(func, a, a + epsilon)

    if abs(left - right) < 0.001:
        return (left + right) / 2

    return None


def final_explanation(name, a):
    if (
        name == "절댓값 함수  f(x) = |x|"
        and abs(a) < 1e-9
    ):
        return (
            "현재 기준점은 절댓값 그래프가 꺾이는 원점입니다. "
            "왼쪽 기울기는 -1, 오른쪽 기울기는 1에 가까워집니다. "
            "두 기울기가 서로 다른 값에 가까워지므로 미분이 불가능합니다."
        )

    if (
        name == "구간에 따라 식이 달라지는 함수"
        and abs(a) < 1e-9
    ):
        return (
            "현재 기준점은 함수의 식이 바뀌는 원점입니다. "
            "왼쪽은 x², 오른쪽은 2x²이지만 두 방향의 기울기는 "
            "모두 0에 가까워집니다. 따라서 원점에서 미분이 가능합니다."
        )

    if (
        name == "극값을 가지는 삼차함수  f(x) = x³ - 3x"
        and abs(abs(a) - 1) < 1e-9
    ):
        if a < 0:
            return (
                "현재 기준점은 삼차함수의 극댓값이 나타나는 지점입니다. "
                "왼쪽과 오른쪽의 기울기가 모두 0에 가까워집니다. "
                "따라서 이 지점에서 미분이 가능합니다."
            )
        return (
            "현재 기준점은 삼차함수의 극솟값이 나타나는 지점입니다. "
            "왼쪽과 오른쪽의 기울기가 모두 0에 가까워집니다. "
            "따라서 이 지점에서 미분이 가능합니다."
        )

    if (
        name == "극값을 가지는 사차함수  f(x) = x⁴ - 4x²"
        and (
            abs(a) < 1e-9
            or abs(abs(a) - np.sqrt(2)) < 0.01
        )
    ):
        if abs(a) < 1e-9:
            point_type = "극댓값"
        else:
            point_type = "극솟값"

        return (
            f"현재 기준점은 사차함수의 {point_type}이 나타나는 지점입니다. "
            "왼쪽과 오른쪽의 기울기가 모두 0에 가까워집니다. "
            "따라서 이 지점에서 미분이 가능합니다."
        )

    return (
        "현재 기준점에서는 그래프가 부드럽게 이어집니다. "
        "이동 거리를 줄이면 왼쪽과 오른쪽의 기울기가 "
        "같은 값에 가까워집니다. 따라서 미분이 가능합니다."
    )


# =====================================
# 5. 사이드바 설정
# =====================================
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
    value=0.0,
    step=0.1
)

h = st.sidebar.slider(
    "처음 이동 거리",
    min_value=0.05,
    max_value=1.0,
    value=0.5,
    step=0.05
)

graph_width = st.sidebar.slider(
    "그래프 가로 범위",
    min_value=0.5,
    max_value=6.0,
    value=2.0,
    step=0.25
)

st.sidebar.info(
    "L1, L2, L3은 기준점의 왼쪽 이동점입니다. "
    "R1, R2, R3은 오른쪽 이동점입니다."
)


# =====================================
# 6. 데이터 계산
# =====================================
fa = f_value(func, a)

slope_df = slope_table(func, a, h)
convergence_df = convergence_table(func, a, h)

left_near = slope(func, a, a - h)
right_near = slope(func, a, a + h)

near_gap = abs(right_near - left_near)

differentiable = is_differentiable_here(
    selected_name, a
)

estimated_slope = tangent_slope(func, a)


# =====================================
# 7. 현재 탐구 조건
# =====================================
st.subheader("현재 탐구 조건")

col1, col2, col3 = st.columns(3)

col1.metric(
    "기준점 A",
    f"({a:.2f}, {fa:.2f})"
)

col2.metric(
    "처음 이동 거리",
    f"{h:.2f}"
)

col3.metric(
    "가장 가까운 좌우 기울기 차이",
    f"{near_gap:.4f}"
)

st.info(EXPLANATIONS[selected_name])


# =====================================
# 8. 탭 구성
# =====================================
tab1, tab2, tab3 = st.tabs([
    "① 함수와 할선 그래프",
    "② 기울기 변화 그래프",
    "③ 탐구 질문과 답변"
])


# =====================================
# 탭 1. 함수와 할선 그래프
# =====================================
with tab1:

    st.subheader("기준점과 여섯 개의 이동점")

    st.write(
        "검은 점 A가 기준점입니다. 초록색 점은 왼쪽 이동점, "
        "빨간색 점은 오른쪽 이동점입니다. "
        "각 점과 기준점을 연결한 선이 할선입니다."
    )

    x_min = a - graph_width
    x_max = a + graph_width

    x_values = np.linspace(x_min, x_max, 700)
    y_values = f_value(func, x_values)

    fig = go.Figure()

    # 함수 그래프
    fig.add_trace(go.Scatter(
        x=x_values,
        y=y_values,
        mode="lines",
        name="함수 그래프",
        line=dict(color="#2563eb", width=4)
    ))

    # 기준점
    fig.add_trace(go.Scatter(
        x=[a],
        y=[fa],
        mode="markers+text",
        name="기준점 A",
        text=["A"],
        textposition="top center",
        marker=dict(color="black", size=15)
    ))

    left_colors = [
        "#16a34a",
        "#65a30d",
        "#a3a3a3"
    ]

    right_colors = [
        "#dc2626",
        "#ea580c",
        "#f59e0b"
    ]

    for i, n in enumerate([1, 2, 3]):

        distance = n * h

        lx = a - distance
        rx = a + distance

        ly = f_value(func, lx)
        ry = f_value(func, rx)

        # 왼쪽 할선
        fig.add_trace(go.Scatter(
            x=[a, lx],
            y=[fa, ly],
            mode="lines",
            name=f"왼쪽 할선 L{i+1}",
            line=dict(
                color=left_colors[i],
                width=2.5,
                dash="dash"
            )
        ))

        # 왼쪽 이동점
        fig.add_trace(go.Scatter(
            x=[lx],
            y=[ly],
            mode="markers+text",
            name=f"왼쪽 점 L{i+1}",
            text=[f"L{i+1}"],
            textposition="bottom left",
            marker=dict(
                color=left_colors[i],
                size=11
            )
        ))

        # 오른쪽 할선
        fig.add_trace(go.Scatter(
            x=[a, rx],
            y=[fa, ry],
            mode="lines",
            name=f"오른쪽 할선 R{i+1}",
            line=dict(
                color=right_colors[i],
                width=2.5,
                dash="dash"
            )
        ))

        # 오른쪽 이동점
        fig.add_trace(go.Scatter(
            x=[rx],
            y=[ry],
            mode="markers+text",
            name=f"오른쪽 점 R{i+1}",
            text=[f"R{i+1}"],
            textposition="top right",
            marker=dict(
                color=right_colors[i],
                size=11
            )
        ))

    # 접선 표시
    if estimated_slope is not None:

        tangent_x = np.linspace(x_min, x_max, 100)

        tangent_y = (
            fa + estimated_slope * (tangent_x - a)
        )

        fig.add_trace(go.Scatter(
            x=tangent_x,
            y=tangent_y,
            mode="lines",
            name="기준점의 접선",
            line=dict(
                color="#9333ea",
                width=3
            )
        ))

    fig.update_layout(
        height=650,
        xaxis=dict(
            title="x좌표",
            range=[x_min, x_max],
            showgrid=True,
            gridcolor="#dddddd",
            zeroline=True
        ),
        yaxis=dict(
            title="y좌표",
            autorange=True,
            showgrid=True,
            gridcolor="#dddddd",
            zeroline=True
        ),
        hovermode="closest",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.22,
            xanchor="left",
            x=0
        ),
        margin=dict(
            l=30,
            r=30,
            t=30,
            b=150
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption(
        "그래프 가로 범위를 줄이면 기준점 주변을 확대할 수 있습니다. "
        "이동점이 화면 밖으로 나가지 않도록 범위를 조절해 주세요."
    )

    st.subheader("이동점의 좌표와 기울기")

    point_display = slope_df[
        [
            "이동점",
            "방향",
            "이동 거리",
            "x좌표",
            "y좌표",
            "할선의 기울기"
        ]
    ].copy()

    st.dataframe(
        point_display.round(4),
        use_container_width=True,
        hide_index=True
    )


# =====================================
# 탭 2. 기울기 변화 그래프
# =====================================
with tab2:

    st.subheader("이동 거리를 줄이면 기울기는 어떻게 변할까?")

    st.write(
        "처음 이동 거리를 절반씩 줄이면서 "
        "왼쪽과 오른쪽 할선의 기울기를 계산했습니다."
    )

    slope_fig = go.Figure()

    slope_fig.add_trace(go.Scatter(
        x=convergence_df["이동 거리"],
        y=convergence_df["왼쪽 기울기"],
        mode="lines+markers",
        name="왼쪽 할선",
        line=dict(
            color="#16a34a",
            width=3
        ),
        marker=dict(size=8)
    ))

    slope_fig.add_trace(go.Scatter(
        x=convergence_df["이동 거리"],
        y=convergence_df["오른쪽 기울기"],
        mode="lines+markers",
        name="오른쪽 할선",
        line=dict(
            color="#dc2626",
            width=3
        ),
        marker=dict(size=8)
    ))

    slope_fig.update_layout(
        height=480,
        xaxis=dict(
            title="기준점과 이동점 사이의 거리",
            autorange="reversed",
            showgrid=True
        ),
        yaxis=dict(
            title="할선의 기울기",
            showgrid=True,
            zeroline=True
        ),
        hovermode="x unified",
        legend=dict(
            orientation="h",
            y=1.12
        )
    )

    st.plotly_chart(
        slope_fig,
        use_container_width=True
    )

    st.subheader("왼쪽과 오른쪽 기울기의 차이")

    gap_fig = go.Figure()

    gap_fig.add_trace(go.Scatter(
        x=convergence_df["이동 거리"],
        y=convergence_df["두 기울기의 차이"],
        mode="lines+markers",
        name="좌우 기울기 차이",
        line=dict(
            color="#7c3aed",
            width=3
        ),
        marker=dict(size=8),
        fill="tozeroy"
    ))

    gap_fig.update_layout(
        height=400,
        xaxis=dict(
            title="기준점과 이동점 사이의 거리",
            autorange="reversed",
            showgrid=True
        ),
        yaxis=dict(
            title="왼쪽과 오른쪽 기울기의 차이",
            showgrid=True,
            rangemode="tozero"
        )
    )

    st.plotly_chart(
        gap_fig,
        use_container_width=True
    )

    st.write(
        "두 기울기의 차이가 0에 가까워지면 "
        "왼쪽과 오른쪽 기울기가 서로 비슷해진다는 뜻입니다."
    )

    st.subheader("이동 거리에 따른 계산 결과")

    st.dataframe(
        convergence_df.round(5),
        use_container_width=True,
        hide_index=True
    )


# =====================================
# 탭 3. 탐구 질문과 답변
# =====================================
with tab3:

    st.subheader("탐구 질문에 대한 답변")

    # 질문 1
    st.markdown(
        "### 질문 1. 이동 거리를 줄일수록 왼쪽과 오른쪽 기울기는 어떻게 변할까?"
    )

    first = convergence_df.iloc[0]
    last = convergence_df.iloc[-1]

    st.write(
        f"이동 거리가 {first['이동 거리']:.5f}에서 "
        f"{last['이동 거리']:.5f}로 줄어들었습니다."
    )

    st.write(
        f"왼쪽 기울기는 {first['왼쪽 기울기']:.5f}에서 "
        f"{last['왼쪽 기울기']:.5f}로 변했고, "
        f"오른쪽 기울기는 {first['오른쪽 기울기']:.5f}에서 "
        f"{last['오른쪽 기울기']:.5f}로 변했습니다."
    )

    if differentiable:
        st.success(
            "현재 기준점에서는 왼쪽과 오른쪽 기울기가 "
            "같은 값에 가까워지는 모습을 확인할 수 있습니다."
        )
    else:
        st.warning(
            "현재 기준점에서는 왼쪽과 오른쪽 기울기가 "
            "서로 다른 값에 가까워집니다."
        )

    st.divider()

    # 질문 2
    st.markdown(
        "### 질문 2. 두 방향의 기울기가 같은 값에 가까워지는 함수와 그렇지 않은 함수는 무엇일까?"
    )

    if differentiable:
        st.success(
            f"현재 선택한 {selected_name}의 기준점 x={a:.2f}에서는 "
            "두 방향의 기울기가 같은 값에 가까워집니다."
        )
    else:
        st.warning(
            f"현재 선택한 {selected_name}의 기준점 x={a:.2f}에서는 "
            "두 방향의 기울기가 서로 다른 값에 가까워집니다."
        )

    st.write(
        "함수의 종류만으로 결과가 결정되는 것은 아닙니다. "
        "같은 함수라도 기준점을 어디에 정하느냐에 따라 결과가 달라질 수 있습니다. "
        "예를 들어 절댓값 함수는 원점에서는 미분할 수 없지만 "
        "원점이 아닌 곳에서는 미분할 수 있습니다."
    )

    st.divider()

    # 질문 3
    st.markdown(
        "### 질문 3. 그래프가 꺾이는 지점에서는 어떤 차이가 나타날까?"
    )

    st.write(
        "그래프가 꺾이는 지점에서는 왼쪽에서 다가갈 때의 기울기와 "
        "오른쪽에서 다가갈 때의 기울기가 다르게 나타날 수 있습니다."
    )

    st.write(
        "대표적인 예는 절댓값 함수 f(x)=|x|의 원점입니다. "
        "왼쪽 기울기는 -1, 오른쪽 기울기는 1에 가까워집니다. "
        "두 기울기의 차이는 2이므로 하나의 기울기로 모이지 않습니다."
    )

    st.write(
        "반면 극댓값이나 극솟값을 가지는 부드러운 그래프에서는 "
        "그 지점의 왼쪽과 오른쪽 기울기가 모두 0에 가까워질 수 있습니다."
    )

    st.divider()

    # 질문 4
    st.markdown(
        "### 질문 4. 함수의 식이 달라지는 지점에서도 좌우 기울기가 같아질 수 있을까?"
    )

    st.write(
        "그럴 수 있습니다. 식이 달라진다는 사실만으로 "
        "미분할 수 없다고 판단하면 안 됩니다."
    )

    st.write(
        "이번 탐구의 구간별 함수는 왼쪽에서 x², 오른쪽에서 2x²을 사용합니다. "
        "원점에서 왼쪽과 오른쪽의 기울기는 모두 0에 가까워집니다. "
        "따라서 원점에서 미분이 가능합니다."
    )

    st.write(
        "반대로 절댓값 함수처럼 왼쪽과 오른쪽의 기울기가 "
        "서로 다른 값에 가까워지면 미분할 수 없습니다."
    )

    st.divider()

    # 최종 결론
    st.subheader("현재 선택한 함수의 최종 결론")

    st.write(final_explanation(selected_name, a))

    if differentiable:
        st.success("현재 기준점에서는 미분이 가능합니다.")
    else:
        st.error("현재 기준점에서는 미분이 불가능합니다.")

    st.divider()

    st.subheader("극값을 가지는 함수 추가 탐구")

    st.write(
        "극댓값이나 극솟값이 나타나는 지점에서도 "
        "좌우 기울기가 같은 값에 가까워질 수 있습니다."
    )

    st.markdown(
        """
        **삼차함수** \(f(x)=x^3-3x\)

        - x=-1: 극댓값 2
        - x=1: 극솟값 -2
        - 두 지점 모두 접선의 기울기는 0입니다.

        **사차함수** \(f(x)=x^4-4x^2\)

        - x=0: 극댓값 0
        - x=-√2, x=√2: 극솟값 -4
        - 세 지점 모두 접선의 기울기는 0입니다.
        """
    )

    st.write(
        "이처럼 극값을 가진다는 이유만으로 미분이 불가능한 것은 아닙니다. "
        "중요한 것은 왼쪽과 오른쪽에서 다가갈 때 기울기가 "
        "같은 값에 가까워지는지 확인하는 것입니다."
    )

    # CSV 다운로드
    csv = convergence_df.to_csv(
        index=False,
        encoding="utf-8-sig"
    )

    st.download_button(
        label="수렴 분석 결과 CSV 다운로드",
        data=csv,
        file_name="좌우_할선_수렴_분석.csv",
        mime="text/csv"
    )
