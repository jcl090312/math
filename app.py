
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# ==========================================
# 1. 페이지 설정
# ==========================================
st.set_page_config(
    page_title="세 할선과 미분계수 탐구",
    page_icon="📐",
    layout="wide"
)

st.title("📐 평균변화율과 미분계수의 관계 탐구")
st.markdown("""
### 수학 × 정보 융합 주제탐구

**세 할선의 기울기 비교를 통한 평균변화율과 미분계수 분석**

하나의 기준점에 세 개의 이동점을 연결하고,
이동 거리 h에 따른 기울기 변화를 관찰합니다.
""")

st.divider()

# ==========================================
# 2. 함수 및 미분계수
# ==========================================
def f(x):
    return x ** 2

def derivative(x):
    return 2 * x

def secant_slope(a, x):
    return (f(x) - f(a)) / (x - a)

# ==========================================
# 3. 탐구 조건 설정
# ==========================================
st.sidebar.title("⚙️ 탐구 조건")

a = st.sidebar.slider(
    "기준점 a",
    -3.0, 3.0, 1.9, 0.1
)

h = st.sidebar.slider(
    "이동 거리 h",
    0.01, 2.0, 0.5, 0.01
)

direction = st.sidebar.radio(
    "이동 방향",
    ["오른쪽 접근", "왼쪽 접근"]
)

show_tangent = st.sidebar.checkbox(
    "접선 표시", True
)

show_points = st.sidebar.checkbox(
    "이동점 표시", True
)

show_function = st.sidebar.checkbox(
    "함수 그래프 표시", True
)

show_analysis = st.sidebar.checkbox(
    "수학적 분석 표시", True
)

sign = 1 if direction == "오른쪽 접근" else -1

# ==========================================
# 4. 세 할선 계산
# ==========================================
multipliers = [1, 2, 3]

point_x = [
    a + sign * k * h for k in multipliers
]

point_y = [
    f(x) for x in point_x
]

slopes = [
    secant_slope(a, x) for x in point_x
]

true_slope = derivative(a)

errors = [
    abs(m - true_slope) for m in slopes
]

# ==========================================
# 5. 핵심 결과
# ==========================================
st.header("1. 현재 탐구 결과")

c1, c2, c3, c4 = st.columns(4)

c1.metric("기준점 a", f"{a:.2f}")
c2.metric("이동 거리 h", f"{h:.3f}")
c3.metric("실제 미분계수", f"{true_slope:.4f}")
c4.metric("평균 절대 오차", f"{np.mean(errors):.4f}")

st.subheader("세 할선의 기울기")

cols = st.columns(3)

for i in range(3):
    cols[i].metric(
        f"{i+1}번째 할선",
        f"{slopes[i]:.4f}",
        delta=f"오차 {errors[i]:.4f}",
        delta_color="inverse"
    )

# ==========================================
# 6. 함수와 할선 그래프
# ==========================================
st.header("2. 세 할선과 접선의 시각화")

xmin = min(-5, a - 3*h - 1)
xmax = max(5, a + 3*h + 1)

x = np.linspace(xmin, xmax, 500)

fig = go.Figure()

# 함수 그래프
if show_function:
    fig.add_trace(go.Scatter(
        x=x,
        y=f(x),
        mode="lines",
        name="f(x) = x²",
        line=dict(width=3)
    ))

# 기준점
fig.add_trace(go.Scatter(
    x=[a],
    y=[f(a)],
    mode="markers+text",
    name="기준점 A",
    text=["A"],
    textposition="bottom center",
    marker=dict(size=13)
))

# 세 할선
for i in range(3):
    k = i + 1
    px = point_x[i]
    py = point_y[i]
    slope = slopes[i]

    line_x = np.linspace(
        min(a, px),
        max(a, px),
        100
    )

    line_y = f(a) + slope * (line_x - a)

    fig.add_trace(go.Scatter(
        x=line_x,
        y=line_y,
        mode="lines",
        name=f"{k}번째 할선",
        line=dict(width=2, dash="dash")
    ))

    # 이동점
    if show_points:
        fig.add_trace(go.Scatter(
            x=[px],
            y=[py],
            mode="markers+text",
            name=f"{k}번째 이동점",
            text=[["B", "C", "D"][i]],
            textposition="top center",
            marker=dict(size=11)
        ))

# 접선
if show_tangent:
    tangent_y = f(a) + true_slope * (x - a)

    fig.add_trace(go.Scatter(
        x=x,
        y=tangent_y,
        mode="lines",
        name="접선",
        line=dict(width=3, dash="dot")
    ))

fig.update_layout(
    xaxis_title="x",
    yaxis_title="f(x)",
    height=600,
    hovermode="closest",
    legend=dict(
        orientation="h",
        y=-0.2
    )
)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "그래프에서 세 할선은 모두 동일한 기준점 A를 지나며, "
    "각각 다른 이동점과 연결됩니다."
)

# ==========================================
# 7. 현재 기울기 상세 분석
# ==========================================
st.header("3. 세 할선의 상세 분석")

current_data = []

for i in range(3):
    k = i + 1

    current_data.append({
        "할선": f"{k}번째",
        "기준점 x": a,
        "이동점 x": point_x[i],
        "이동점 y": point_y[i],
        "이동 거리": k * h,
        "평균변화율": slopes[i],
        "미분계수": true_slope,
        "절대 오차": errors[i]
    })

current_df = pd.DataFrame(current_data)

st.dataframe(
    current_df.round(5),
    use_container_width=True,
    hide_index=True
)

# ==========================================
# 8. h 변화에 따른 수렴 분석
# ==========================================
st.header("4. 이동 거리 h에 따른 수렴 분석")

st.markdown("""
현재 기준점을 고정한 상태에서 이동 거리 h를
점점 작게 만들면 세 할선의 기울기가 어떻게 변할까요?
""")

h_values = [
    h,
    h / 2,
    h / 4,
    h / 8,
    h / 16,
    h / 32,
    h / 64
]

experiment_data = []

for current_h in h_values:

    row = {"h": current_h}

    for k in multipliers:

        px = a + sign * k * current_h
        slope = secant_slope(a, px)

        row[f"{k}번째 기울기"] = slope
        row[f"{k}번째 오차"] = abs(
            slope - true_slope
        )

    experiment_data.append(row)

experiment_df = pd.DataFrame(experiment_data)

st.dataframe(
    experiment_df.round(6),
    use_container_width=True,
    hide_index=True
)

# ==========================================
# 9. 기울기 변화 그래프
# ==========================================
st.header("5. h에 따른 할선의 기울기 변화")

slope_fig = go.Figure()

for k in multipliers:

    values = []

    for current_h in h_values:
        px = a + sign * k * current_h
        values.append(secant_slope(a, px))

    slope_fig.add_trace(go.Scatter(
        x=h_values,
        y=values,
        mode="lines+markers",
        name=f"{k}번째 할선"
    ))

slope_fig.add_hline(
    y=true_slope,
    line_dash="dash",
    annotation_text="실제 미분계수"
)

slope_fig.update_layout(
    xaxis_title="이동 거리 h",
    yaxis_title="할선의 기울기",
    height=450,
    xaxis=dict(autorange="reversed")
)

st.plotly_chart(
    slope_fig,
    use_container_width=True
)

# ==========================================
# 10. 오차 변화 그래프
# ==========================================
st.header("6. 미분계수와의 오차 변화")

error_fig = go.Figure()

for k in multipliers:

    values = [
        k * current_h for current_h in h_values
    ]

    error_fig.add_trace(go.Scatter(
        x=h_values,
        y=values,
        mode="lines+markers",
        name=f"{k}번째 할선 오차"
    ))

error_fig.update_layout(
    xaxis_title="이동 거리 h",
    yaxis_title="절대 오차",
    height=450,
    xaxis=dict(autorange="reversed")
)

st.plotly_chart(
    error_fig,
    use_container_width=True
)

# ==========================================
# 11. 세 할선 사이의 기울기 차이
# ==========================================
st.header("7. 세 할선의 기울기 차이")

difference_data = {
    "비교": [
        "1번과 2번",
        "2번과 3번",
        "1번과 3번"
    ],
    "기울기 차이": [
        abs(slopes[0] - slopes[1]),
        abs(slopes[1] - slopes[2]),
        abs(slopes[0] - slopes[2])
    ]
}

difference_df = pd.DataFrame(difference_data)

st.dataframe(
    difference_df.round(6),
    use_container_width=True,
    hide_index=True
)

st.markdown(f"""
현재 세 할선의 기울기 차이는 다음과 같습니다.

- 첫 번째와 두 번째: {abs(slopes[0]-slopes[1]):.4f}
- 두 번째와 세 번째: {abs(slopes[1]-slopes[2]):.4f}
- 첫 번째와 세 번째: {abs(slopes[0]-slopes[2]):.4f}

이동 거리 h가 작아지면 세 할선 사이의 기울기 차이도 작아집니다.
""")

# ==========================================
# 12. 자동 수학적 해석
# ==========================================
if show_analysis:

    st.header("8. 수학적 분석")

    st.markdown(f"""
    ### 현재 탐구 조건

    - 함수: f(x) = x²
    - 기준점: a = {a:.2f}
    - 이동 거리: h = {h:.3f}
    - 접근 방향: {direction}

    ### 실제 미분계수

    f'(a) = 2a = **{true_slope:.4f}**

    ### 세 할선의 기울기

    | 할선 | 계산된 기울기 | 절대 오차 |
    |---|---:|---:|
    | 첫 번째 | {slopes[0]:.4f} | {errors[0]:.4f} |
    | 두 번째 | {slopes[1]:.4f} | {errors[1]:.4f} |
    | 세 번째 | {slopes[2]:.4f} | {errors[2]:.4f} |

    ### 분석 결과

    {direction}을 선택했을 때 세 할선의 기울기는
    각각 {slopes[0]:.4f}, {slopes[1]:.4f}, {slopes[2]:.4f}입니다.

    세 할선의 기울기는 서로 다르지만,
    h가 작아질수록 실제 미분계수 {true_slope:.4f}에 가까워집니다.

    또한 세 번째 할선은 첫 번째 할선보다 이동 거리가
    세 배 크기 때문에 미분계수와의 오차도 세 배 크게 나타납니다.
    """)

    st.markdown("""
    ### 수학적 원리 확인

    함수 f(x) = x²에서 세 할선의 기울기는 다음과 같습니다.

    첫 번째: 2a + sh

    두 번째: 2a + 2sh

    세 번째: 2a + 3sh

    여기서 s는 접근 방향을 나타내며,
    오른쪽 접근은 1, 왼쪽 접근은 -1입니다.

    따라서 h가 0에 가까워지면 세 기울기가
    모두 2a에 가까워집니다.
    """)

# ==========================================
# 13. 탐구 결론
# ==========================================
st.header("9. 탐구 결론")

st.markdown("""
이번 탐구에서는 하나의 기준점에 세 개의 이동점을 설정하고,
각 이동점을 연결한 할선의 기울기를 비교했습니다.

그 결과 이동 거리 h가 작아질수록 세 할선의 기울기와
실제 미분계수 사이의 차이가 감소한다는 사실을 확인했습니다.

특히 서로 다른 위치에 있는 세 이동점이 같은 기준점에
접근하면서 세 할선의 기울기가 하나의 접선 기울기에
가까워진다는 점을 확인할 수 있었습니다.

이를 통해 평균변화율과 미분계수의 관계를
계산뿐만 아니라 그래프와 데이터로 분석할 수 있었습니다.
""")

# ==========================================
# 14. CSV 데이터 다운로드
# ==========================================
st.header("10. 탐구 데이터 다운로드")

csv1 = current_df.to_csv(
    index=False
).encode("utf-8-sig")

csv2 = experiment_df.to_csv(
    index=False
).encode("utf-8-sig")

col1, col2 = st.columns(2)

with col1:
    st.download_button(
        "📥 현재 할선 분석 다운로드",
        data=csv1,
        file_name="current_secants.csv",
        mime="text/csv",
        use_container_width=True
    )

with col2:
    st.download_button(
        "📥 수렴 분석 데이터 다운로드",
        data=csv2,
        file_name="convergence_analysis.csv",
        mime="text/csv",
        use_container_width=True
    )

st.divider()

st.caption(
    "미적분Ⅰ × 정보 융합 프로젝트 | "
    "평균변화율과 미분계수의 관계 탐구"
)
