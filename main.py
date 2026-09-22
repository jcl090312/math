import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# --------------------------------------------------
# 기본 설정
# --------------------------------------------------

st.set_page_config(
    page_title="좌우 할선의 수렴과 미분가능성 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("📈 좌우 할선의 수렴과 미분가능성 탐구")
st.markdown(
    """
    **미적분Ⅰ의 평균변화율과 미분계수**를 바탕으로  
    한 점에 왼쪽과 오른쪽에서 접근하는 두 점의 할선 기울기가
    어떤 값으로 수렴하는지 관찰합니다.
    """
)

st.divider()

# --------------------------------------------------
# 함수 정의
# --------------------------------------------------

functions = {
    "이차함수 · x²": "x2",
    "삼차함수 · x³": "x3",
    "사차함수 · x⁴": "x4",
    "복잡한 다항함수 · x⁴ - 2x³ - x² + 2x + 1": "poly",
    "절댓값 함수 · |x|": "abs",
    "구간으로 나뉜 함수": "piecewise"
}

selected_name = st.selectbox(
    "탐구할 함수를 선택하세요.",
    list(functions.keys())
)

selected_function = functions[selected_name]


# --------------------------------------------------
# 함수 계산
# --------------------------------------------------

def f(x):
    if selected_function == "x2":
        return x ** 2

    elif selected_function == "x3":
        return x ** 3

    elif selected_function == "x4":
        return x ** 4

    elif selected_function == "poly":
        return x ** 4 - 2 * x ** 3 - x ** 2 + 2 * x + 1

    elif selected_function == "abs":
        return np.abs(x)

    elif selected_function == "piecewise":
        # x < 0 : x²
        # x >= 0 : 2x²
        return np.where(x < 0, x ** 2, 2 * x ** 2)


# --------------------------------------------------
# 함수 설명
# --------------------------------------------------

if selected_function == "x2":
    st.info("선택한 함수: **f(x) = x²**")

elif selected_function == "x3":
    st.info("선택한 함수: **f(x) = x³**")

elif selected_function == "x4":
    st.info("선택한 함수: **f(x) = x⁴**")

elif selected_function == "poly":
    st.info(
        "선택한 함수: **f(x) = x⁴ - 2x³ - x² + 2x + 1**"
    )

elif selected_function == "abs":
    st.info("선택한 함수: **f(x) = |x|**")

else:
    st.info(
        """
        선택한 함수는 구간에 따라 식이 달라집니다.

        **x < 0 : f(x) = x²**

        **x ≥ 0 : f(x) = 2x²**
        """
    )


# --------------------------------------------------
# 조작 영역
# --------------------------------------------------

st.sidebar.header("⚙️ 탐구 조건")

# 절댓값과 구간함수는 0에서 변화가 중요하므로
# 기본값을 0으로 설정
if selected_function in ["abs", "piecewise"]:
    default_a = 0.0
else:
    default_a = 1.0

a = st.sidebar.slider(
    "기준점 a",
    min_value=-3.0,
    max_value=3.0,
    value=default_a,
    step=0.1
)

h = st.sidebar.slider(
    "접근 거리 h",
    min_value=0.01,
    max_value=2.0,
    value=0.5,
    step=0.01
)

graph_range = st.sidebar.slider(
    "그래프 범위",
    min_value=3,
    max_value=10,
    value=5
)


# --------------------------------------------------
# 점 계산
# --------------------------------------------------

# 기준점
x_a = a
y_a = f(np.array([a]))[0]

# 왼쪽에서 접근하는 점
x_left = a - h
y_left = f(np.array([x_left]))[0]

# 오른쪽에서 접근하는 점
x_right = a + h
y_right = f(np.array([x_right]))[0]


# --------------------------------------------------
# 좌우 할선의 기울기 계산
# --------------------------------------------------

left_slope = (y_a - y_left) / h
right_slope = (y_right - y_a) / h

slope_difference = abs(right_slope - left_slope)


# --------------------------------------------------
# 그래프
# --------------------------------------------------

x = np.linspace(
    a - graph_range,
    a + graph_range,
    800
)

y = f(x)

fig = go.Figure()

# 함수 그래프
fig.add_trace(
    go.Scatter(
        x=x,
        y=y,
        mode="lines",
        name="함수 그래프",
        line=dict(width=3)
    )
)

# 기준점
fig.add_trace(
    go.Scatter(
        x=[x_a],
        y=[y_a],
        mode="markers",
        name="기준점 A",
        marker=dict(size=12)
    )
)

# 왼쪽 접근점
fig.add_trace(
    go.Scatter(
        x=[x_left],
        y=[y_left],
        mode="markers",
        name="왼쪽 점",
        marker=dict(size=10)
    )
)

# 오른쪽 접근점
fig.add_trace(
    go.Scatter(
        x=[x_right],
        y=[y_right],
        mode="markers",
        name="오른쪽 점",
        marker=dict(size=10)
    )
)

# 왼쪽 할선
fig.add_trace(
    go.Scatter(
        x=[x_left, x_a],
        y=[y_left, y_a],
        mode="lines",
        name="왼쪽 할선",
        line=dict(dash="dash", width=3)
    )
)

# 오른쪽 할선
fig.add_trace(
    go.Scatter(
        x=[x_a, x_right],
        y=[y_a, y_right],
        mode="lines",
        name="오른쪽 할선",
        line=dict(dash="dot", width=3)
    )
)

fig.update_layout(
    title="기준점에 접근하는 두 할선",
    xaxis_title="x",
    yaxis_title="f(x)",
    height=600,
    hovermode="closest"
)

st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------
# 현재 값 표시
# --------------------------------------------------

st.subheader("📊 현재 탐구 결과")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "왼쪽 할선의 기울기",
        f"{left_slope:.6f}"
    )

with col2:
    st.metric(
        "오른쪽 할선의 기울기",
        f"{right_slope:.6f}"
    )

with col3:
    st.metric(
        "두 기울기의 차이",
        f"{slope_difference:.6f}"
    )

with col4:
    if slope_difference < 0.001:
        status = "거의 일치"
    elif slope_difference < 0.1:
        status = "가까워지는 중"
    else:
        status = "차이가 있음"

    st.metric(
        "수렴 상태",
        status
    )


# --------------------------------------------------
# 수학적 설명
# --------------------------------------------------

st.divider()

st.subheader("📐 두 할선의 기울기는 어떻게 계산할까?")

st.markdown(
    f"""
    기준점은

    **A = ({a:.2f}, f({a:.2f}))**

    입니다.

    기준점의 왼쪽에 있는 점은 **x = a - h**,
    오른쪽에 있는 점은 **x = a + h**입니다.

    따라서 평균변화율을 이용하면 두 할선의 기울기를 각각 계산할 수 있습니다.
    """
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ◀ 왼쪽 할선")
    st.latex(
        r"""
        m_L =
        \frac{f(a)-f(a-h)}{h}
        """
    )
    st.write(f"현재 값: **{left_slope:.6f}**")

with col2:
    st.markdown("### 오른쪽 할선 ▶")
    st.latex(
        r"""
        m_R =
        \frac{f(a+h)-f(a)}{h}
        """
    )
    st.write(f"현재 값: **{right_slope:.6f}**")


# --------------------------------------------------
# h를 점점 작게 만드는 실험
# --------------------------------------------------

st.divider()

st.subheader("🔬 h를 점점 0에 가깝게 만들면 어떻게 될까?")

st.write(
    """
    이제 기준점은 그대로 유지하고 두 점이 기준점에 점점 가까워지도록
    **h의 값을 작게 하면서 왼쪽과 오른쪽 할선의 기울기를 비교합니다.**
    """
)

h_values = [
    1,
    0.5,
    0.2,
    0.1,
    0.05,
    0.02,
    0.01
]

results = []

for h_value in h_values:

    left_x = a - h_value
    right_x = a + h_value

    left_y = f(np.array([left_x]))[0]
    right_y = f(np.array([right_x]))[0]

    left_m = (y_a - left_y) / h_value
    right_m = (right_y - y_a) / h_value

    difference = abs(right_m - left_m)

    results.append(
        {
            "h": h_value,
            "왼쪽 할선 기울기": left_m,
            "오른쪽 할선 기울기": right_m,
            "두 기울기의 차이": difference
        }
    )

result_df = pd.DataFrame(results)

st.dataframe(
    result_df.style.format(
        {
            "h": "{:.3f}",
            "왼쪽 할선 기울기": "{:.6f}",
            "오른쪽 할선 기울기": "{:.6f}",
            "두 기울기의 차이": "{:.6f}"
        }
    ),
    use_container_width=True
)


# --------------------------------------------------
# 수렴 그래프
# --------------------------------------------------

st.subheader("📉 h에 따른 좌우 할선 기울기의 변화")

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=result_df["h"],
        y=result_df["왼쪽 할선 기울기"],
        mode="lines+markers",
        name="왼쪽 할선"
    )
)

fig2.add_trace(
    go.Scatter(
        x=result_df["h"],
        y=result_df["오른쪽 할선 기울기"],
        mode="lines+markers",
        name="오른쪽 할선"
    )
)

fig2.update_layout(
    title="h가 작아질수록 두 할선의 기울기는 어떻게 변하는가?",
    xaxis_title="h",
    yaxis_title="할선의 기울기",
    height=500
)

# h가 큰 값에서 작은 값으로 보이도록 역순
fig2.update_xaxes(autorange="reversed")

st.plotly_chart(fig2, use_container_width=True)


# --------------------------------------------------
# 자동 분석
# --------------------------------------------------

st.divider()

st.subheader("🧠 탐구 결과 해석")

final_left = result_df.iloc[-1]["왼쪽 할선 기울기"]
final_right = result_df.iloc[-1]["오른쪽 할선 기울기"]
final_difference = result_df.iloc[-1]["두 기울기의 차이"]


if final_difference < 0.001:

    st.success(
        f"""
        h를 0에 가깝게 줄였을 때 왼쪽 할선의 기울기는
        **{final_left:.6f}**, 오른쪽 할선의 기울기는
        **{final_right:.6f}**으로 서로 매우 가까워졌습니다.

        따라서 이 실험에서는 두 방향에서 접근한 평균변화율이
        **하나의 값에 가까워지는 현상**을 관찰할 수 있습니다.
        """
    )

else:

    st.warning(
        f"""
        h를 0에 가깝게 줄였을 때에도 왼쪽 할선의 기울기는
        **{final_left:.6f}**, 오른쪽 할선의 기울기는
        **{final_right:.6f}**으로 차이가 남아 있습니다.

        따라서 이 실험에서는 두 방향에서 접근한 평균변화율이
        **하나의 값으로 모이지 않는 현상**을 관찰할 수 있습니다.
        """
    )


# --------------------------------------------------
# 함수별 탐구 포인트
# --------------------------------------------------

st.divider()

st.subheader("🔎 이 함수에서 무엇을 관찰할까?")

if selected_function == "x2":

    st.markdown(
        """
        **이차함수에서는**

        기준점에 가까워질수록 왼쪽과 오른쪽 할선의 기울기가
        하나의 값에 가까워지는 모습을 관찰할 수 있습니다.

        이를 통해 곡선 위의 한 점에서 접선의 기울기를 생각할 때
        평균변화율을 이용할 수 있다는 점을 확인할 수 있습니다.
        """
    )

elif selected_function == "x3":

    st.markdown(
        """
        **삼차함수에서는**

        이차함수와 비교하여 함수의 모양은 더 복잡하지만,
        한 점에 가까이 접근했을 때 좌우 할선의 기울기가 어떻게
        변화하는지 관찰할 수 있습니다.

        함수의 차수가 달라져도 같은 탐구 방법을 적용할 수 있다는 점이
        중요한 관찰 대상입니다.
        """
    )

elif selected_function == "x4":

    st.markdown(
        """
        **사차함수에서는**

        그래프의 모양이 더욱 복잡해지지만,
        평균변화율을 이용하여 좌우에서 접근하는 두 할선의 기울기를
        비교할 수 있습니다.

        이를 통해 함수의 복잡성과 관계없이 같은 수학적 탐구 방법을
        적용할 수 있는지 확인할 수 있습니다.
        """
    )

elif selected_function == "poly":

    st.markdown(
        """
        **복잡한 다항함수에서는**

        단순한 x², x³, x⁴보다 그래프의 형태가 복잡해집니다.

        그러나 기준점을 정하고 h를 감소시키면서 좌우 할선의 기울기를
        비교하는 방법은 동일하게 적용할 수 있습니다.

        따라서 함수의 식이 복잡해져도 평균변화율과 미분계수의 관계를
        관찰할 수 있는지 탐구할 수 있습니다.
        """
    )

elif selected_function == "abs":

    st.markdown(
        """
        **절댓값 함수에서는 특히 중요한 현상을 관찰할 수 있습니다.**

        기준점을 0으로 설정하면 왼쪽에서 접근할 때와 오른쪽에서
        접근할 때 할선의 기울기가 서로 다르게 나타납니다.

        따라서 두 방향의 평균변화율이 하나의 값으로 모이는지 확인하는
        것이 핵심적인 탐구 대상입니다.
        """
    )

else:

    st.markdown(
        """
        **구간으로 나뉜 함수에서는**

        기준점의 위치에 따라 함수의 식이 달라질 수 있습니다.

        특히 두 구간이 만나는 지점을 기준점으로 설정했을 때
        왼쪽과 오른쪽에서 접근하는 할선의 기울기를 비교하면
        구간이 바뀌는 지점에서 어떤 현상이 나타나는지 관찰할 수 있습니다.
        """
    )


# --------------------------------------------------
# 프로젝트의 핵심 질문
# --------------------------------------------------

st.divider()

st.subheader("🎯 이 탐구의 핵심 질문")

st.markdown(
    """
    ### 질문 1
    **h를 0에 가깝게 만들면 왼쪽과 오른쪽 할선의 기울기는
    항상 같은 값에 가까워질까?**

    ### 질문 2
    **함수의 종류가 달라져도 이러한 현상이 나타날까?**

    ### 질문 3
    **두 방향에서 접근한 할선의 기울기가 서로 다르게 나타나는
    함수에서는 어떤 특징이 있을까?**

    ### 질문 4
    **평균변화율을 반복적으로 관찰하는 과정을 통해
    미분계수의 의미를 어떻게 이해할 수 있을까?**
    """
)


# --------------------------------------------------
# 교육적 의미
# --------------------------------------------------

st.divider()

st.subheader("📚 수학교육과와 연결되는 의미")

st.markdown(
    """
    이 프로그램은 단순히 미분계수를 계산하는 것이 아니라,
    **평균변화율이 어떻게 미분계수로 연결되는지를 시각적으로
    관찰하는 것**을 목적으로 합니다.

    특히 하나의 함수만 사용하는 것이 아니라 이차함수, 삼차함수,
    사차함수, 복잡한 다항함수, 절댓값 함수, 구간함수를 비교함으로써
    함수의 형태에 따라 좌우 할선의 변화가 어떻게 달라지는지
    직접 확인할 수 있습니다.

    이러한 방식은 수학 개념을 공식만으로 학습하는 것이 아니라
    **그래프 → 수치 변화 → 규칙 발견 → 수학적 해석**의 과정으로
    연결할 수 있다는 점에서 수학교육과 관련된 탐구로 발전시킬 수 있습니다.
    """
)

st.caption(
    "※ 이 프로그램의 수치 실험은 유한한 h를 사용하므로, "
    "수렴 여부는 실험값을 통해 관찰하는 방식으로 해석합니다."
)
