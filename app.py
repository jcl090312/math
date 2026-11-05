
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# --------------------------------------------------
# 1. 페이지 설정
# --------------------------------------------------

st.set_page_config(
    page_title="대칭 할선과 극한 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("대칭 할선의 기울기와 극한 탐구")

st.markdown("""
기준점 a를 중심으로 양쪽에 두 점을 놓고,
두 점을 연결한 할선의 기울기를 관찰하는 프로그램입니다.

슬라이더를 움직이면 그래프와 계산 결과가 함께 바뀝니다.
""")

st.latex(
    r"\lim_{h\to0}\frac{f(a+h)-f(a-h)}{2h}"
)

st.info(
    "핵심 탐구: h를 0에 가깝게 만들면 대칭 할선의 기울기는 "
    "어떤 값에 가까워질까? 그리고 그 값은 항상 미분계수일까?"
)


# --------------------------------------------------
# 2. 탐구 함수 4개
# --------------------------------------------------

FUNCTIONS = {
    "이차함수": {
        "formula": r"f(x)=x^2",
        "func": lambda x: x**2
    },
    "삼차함수": {
        "formula": r"f(x)=x^3",
        "func": lambda x: x**3
    },
    "절댓값 함수": {
        "formula": r"f(x)=|x|",
        "func": lambda x: np.abs(x)
    },
    "구간별 함수": {
        "formula": r"f(x)=\begin{cases}x &(x<0)\\x^2 &(x\geq0)\end{cases}",
        "func": lambda x: np.where(x < 0, x, x**2)
    }
}


def f_value(name, x):
    """선택한 함수의 함숫값"""
    return float(FUNCTIONS[name]["func"](np.asarray(x)))


# --------------------------------------------------
# 3. 기울기 계산
# --------------------------------------------------

def calculate(name, a, h):
    """
    왼쪽 점: a-h
    기준점: a
    오른쪽 점: a+h

    왼쪽 평균변화율:
    [f(a)-f(a-h)] / h

    오른쪽 평균변화율:
    [f(a+h)-f(a)] / h

    대칭 할선의 기울기:
    [f(a+h)-f(a-h)] / 2h
    """

    left_x = a - h
    right_x = a + h

    left_y = f_value(name, left_x)
    center_y = f_value(name, a)
    right_y = f_value(name, right_x)

    left_slope = (center_y - left_y) / h
    right_slope = (right_y - center_y) / h

    symmetric_slope = (right_y - left_y) / (2 * h)

    return {
        "left_x": left_x,
        "right_x": right_x,
        "left_y": left_y,
        "center_y": center_y,
        "right_y": right_y,
        "left_slope": left_slope,
        "right_slope": right_slope,
        "symmetric_slope": symmetric_slope
    }


# --------------------------------------------------
# 4. 사이드바 - 실시간 조절
# --------------------------------------------------

st.sidebar.header("그래프 조절")

selected_name = st.sidebar.selectbox(
    "함수 선택",
    list(FUNCTIONS.keys())
)

a = st.sidebar.slider(
    "기준점 a",
    min_value=-3.0,
    max_value=3.0,
    value=0.0,
    step=0.01,
    format="%.2f"
)

h = st.sidebar.slider(
    "거리 h",
    min_value=0.001,
    max_value=2.0,
    value=0.5,
    step=0.001,
    format="%.3f"
)

view_width = st.sidebar.slider(
    "그래프 확대 범위",
    min_value=0.5,
    max_value=5.0,
    value=2.0,
    step=0.1
)

st.sidebar.caption(
    "a를 움직이면 기준점이 바뀌고, h를 줄이면 양쪽 점이 기준점에 가까워집니다."
)


# --------------------------------------------------
# 5. 현재 함수와 계산 결과
# --------------------------------------------------

function = FUNCTIONS[selected_name]
result = calculate(selected_name, a, h)

st.header("현재 탐구 조건")

st.markdown(f"**선택한 함수:** {function['formula']}")

c1, c2, c3 = st.columns(3)

c1.metric("기준점 a", f"{a:.3f}")
c2.metric("왼쪽 점 a-h", f"{result['left_x']:.3f}")
c3.metric("오른쪽 점 a+h", f"{result['right_x']:.3f}")

st.subheader("현재 계산된 기울기")

c1, c2, c3 = st.columns(3)

c1.metric(
    "왼쪽 평균변화율",
    f"{result['left_slope']:.6f}"
)

c2.metric(
    "오른쪽 평균변화율",
    f"{result['right_slope']:.6f}"
)

c3.metric(
    "대칭 할선의 기울기",
    f"{result['symmetric_slope']:.6f}"
)

st.latex(
    r"\frac{f(a+h)-f(a-h)}{2h}"
)

st.caption(
    "대칭 할선은 왼쪽 점과 오른쪽 점을 직접 연결한 하나의 직선입니다."
)


# --------------------------------------------------
# 6. 그래프 표시
# --------------------------------------------------

st.divider()
st.header("1. 그래프에서 대칭 할선 관찰하기")

st.markdown("""
- 파란색 곡선: 선택한 함수
- 초록색 점: 왼쪽 점
- 검은색 점: 기준점
- 빨간색 점: 오른쪽 점
- 보라색 직선: 두 점을 연결한 대칭 할선

기준점과 h를 바꾸면서 할선의 방향이 어떻게 달라지는지 관찰해 보세요.
""")

x_min = a - view_width
x_max = a + view_width

# 두 점이 화면에서 잘 보이도록 범위 보정
x_min = min(x_min, result["left_x"] - 0.1)
x_max = max(x_max, result["right_x"] + 0.1)

x_values = np.linspace(x_min, x_max, 700)
y_values = function["func"](x_values)

fig = go.Figure()

# 함수 그래프
fig.add_trace(go.Scatter(
    x=x_values,
    y=y_values,
    mode="lines",
    name="함수 그래프",
    line=dict(color="#2563EB", width=3)
))

# 대칭 할선
fig.add_trace(go.Scatter(
    x=[result["left_x"], result["right_x"]],
    y=[result["left_y"], result["right_y"]],
    mode="lines",
    name="대칭 할선",
    line=dict(color="#9333EA", width=3)
))

# 왼쪽 점
fig.add_trace(go.Scatter(
    x=[result["left_x"]],
    y=[result["left_y"]],
    mode="markers",
    name="왼쪽 점",
    marker=dict(color="#16A34A", size=12)
))

# 기준점
fig.add_trace(go.Scatter(
    x=[a],
    y=[result["center_y"]],
    mode="markers",
    name="기준점",
    marker=dict(color="#111827", size=13, symbol="diamond")
))

# 오른쪽 점
fig.add_trace(go.Scatter(
    x=[result["right_x"]],
    y=[result["right_y"]],
    mode="markers",
    name="오른쪽 점",
    marker=dict(color="#DC2626", size=12)
))

fig.update_layout(
    height=620,
    xaxis_title="x",
    yaxis_title="f(x)",
    hovermode="closest",
    legend=dict(orientation="h", y=1.08),
    margin=dict(l=25, r=25, t=60, b=25)
)

fig.update_xaxes(
    range=[x_min, x_max],
    showgrid=True,
    zeroline=True
)

fig.update_yaxes(
    showgrid=True,
    zeroline=True,
    autorange=True
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={
        "scrollZoom": True,
        "displaylogo": False,
        "modeBarButtonsToRemove": ["lasso2d", "select2d"]
    }
)


# --------------------------------------------------
# 7. h를 줄였을 때의 변화
# --------------------------------------------------

st.divider()
st.header("2. h를 0에 가깝게 만들기")

st.markdown("""
현재 설정한 h를 계속 절반으로 줄여 가며 기울기를 계산합니다.

두 점이 기준점에 가까워질 때 대칭 할선의 기울기가
어떤 값에 가까워지는지 확인할 수 있습니다.
""")

h_values = [h / (2 ** i) for i in range(11)]

records = []

for current_h in h_values:
    r = calculate(selected_name, a, current_h)

    records.append({
        "h": current_h,
        "왼쪽 평균변화율": r["left_slope"],
        "오른쪽 평균변화율": r["right_slope"],
        "대칭 할선의 기울기": r["symmetric_slope"]
    })

df = pd.DataFrame(records)

st.subheader("기울기 변화 표")

st.dataframe(
    df.style.format({
        "h": "{:.8f}",
        "왼쪽 평균변화율": "{:.8f}",
        "오른쪽 평균변화율": "{:.8f}",
        "대칭 할선의 기울기": "{:.8f}"
    }),
    use_container_width=True,
    hide_index=True
)

# 기울기 변화 그래프
fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=df["h"],
    y=df["왼쪽 평균변화율"],
    mode="lines+markers",
    name="왼쪽 평균변화율",
    line=dict(color="#16A34A", width=2)
))

fig2.add_trace(go.Scatter(
    x=df["h"],
    y=df["오른쪽 평균변화율"],
    mode="lines+markers",
    name="오른쪽 평균변화율",
    line=dict(color="#DC2626", width=2)
))

fig2.add_trace(go.Scatter(
    x=df["h"],
    y=df["대칭 할선의 기울기"],
    mode="lines+markers",
    name="대칭 할선의 기울기",
    line=dict(color="#9333EA", width=3)
))

fig2.update_layout(
    height=500,
    xaxis_title="h (오른쪽으로 갈수록 0에 가까워짐)",
    yaxis_title="기울기",
    hovermode="x unified",
    legend=dict(orientation="h", y=1.12),
    margin=dict(l=25, r=25, t=60, b=25)
)

fig2.update_xaxes(
    type="log",
    autorange="reversed"
)

fig2.update_yaxes(showgrid=True)

st.plotly_chart(
    fig2,
    use_container_width=True
)


# --------------------------------------------------
# 8. 대칭 할선의 기울기와 좌우 기울기의 관계
# --------------------------------------------------

st.divider()
st.header("3. 세 기울기는 어떤 관계일까?")

st.markdown("""
대칭 할선의 기울기는 왼쪽 평균변화율과 오른쪽 평균변화율의 평균입니다.
""")

st.latex(
    r"\frac{f(a+h)-f(a-h)}{2h}"
    r"="
    r"\frac{1}{2}"
    r"\left("
    r"\frac{f(a)-f(a-h)}{h}"
    r"+"
    r"\frac{f(a+h)-f(a)}{h}"
    r"\right)"
)

st.write(
    "따라서 대칭 할선의 기울기 하나만 확인하면 "
    "왼쪽과 오른쪽의 기울기가 서로 다른 경우를 놓칠 수 있습니다."
)


# --------------------------------------------------
# 9. 선택 함수에 따른 해석
# --------------------------------------------------

st.divider()
st.header("4. 현재 함수의 결과 해석")

near_zero = abs(a) < 0.000001

if selected_name == "이차함수":
    st.success(
        "이차함수는 모든 기준점에서 미분 가능합니다. "
        "h를 줄이면 대칭 할선의 기울기는 2a에 가까워집니다."
    )
    st.latex(r"\lim_{h\to0}\frac{(a+h)^2-(a-h)^2}{2h}=2a")

elif selected_name == "삼차함수":
    st.success(
        "삼차함수는 모든 기준점에서 미분 가능합니다. "
        "h를 줄이면 대칭 할선의 기울기는 3a²에 가까워집니다."
    )
    st.latex(
        r"\lim_{h\to0}\frac{(a+h)^3-(a-h)^3}{2h}=3a^2"
    )

elif selected_name == "절댓값 함수":
    if near_zero:
        st.warning(
            "원점에서는 대칭 할선의 기울기가 0에 가까워집니다. "
            "하지만 왼쪽 평균변화율은 -1, 오른쪽 평균변화율은 1에 "
            "가까워지므로 원점에서 미분 가능하지 않습니다."
        )
        st.latex(
            r"\lim_{h\to0}\frac{|h|-|-h|}{2h}=0"
        )
    elif a > 0:
        st.success(
            "기준점이 양수인 곳에서는 함수가 직선 y=x처럼 "
            "나타나므로 대칭 할선의 기울기는 1에 가까워집니다."
        )
    else:
        st.success(
            "기준점이 음수인 곳에서는 함수가 직선 y=-x처럼 "
            "나타나므로 대칭 할선의 기울기는 -1에 가까워집니다."
        )

elif selected_name == "구간별 함수":
    if near_zero:
        st.warning(
            "원점에서 대칭 할선의 기울기는 0.5에 가까워집니다. "
            "하지만 왼쪽 평균변화율은 1, 오른쪽 평균변화율은 0에 "
            "가까워지므로 원점에서 미분 가능하지 않습니다."
        )
        st.latex(
            r"\lim_{h\to0}\frac{h^2-(-h)}{2h}"
            r"=\frac{1}{2}"
        )
    elif a < 0:
        st.success(
            "기준점이 음수인 곳에서는 함수가 y=x이므로 "
            "대칭 할선의 기울기는 1에 가까워집니다."
        )
    else:
        st.success(
            "기준점이 양수인 곳에서는 함수가 y=x²이므로 "
            "대칭 할선의 기울기는 2a에 가까워집니다."
        )


# --------------------------------------------------
# 10. 핵심 탐구 질문
# --------------------------------------------------

st.divider()
st.header("5. 탐구 질문")

with st.expander("질문 1. h를 0에 가깝게 만들면 무엇을 알 수 있을까?"):
    st.write("""
    h가 작아지면 왼쪽 점 a-h와 오른쪽 점 a+h가 기준점 a에 가까워집니다.
    이때 두 점을 연결한 대칭 할선의 기울기가 어떤 값에 가까워지는지
    관찰할 수 있습니다.
    """)

with st.expander("질문 2. 대칭 할선의 기울기가 수렴하면 미분 가능할까?"):
    st.write("""
    반드시 그렇지는 않습니다.

    절댓값 함수와 구간별 함수의 원점에서는 대칭 할선의 기울기가
    각각 0과 0.5에 수렴합니다.

    하지만 왼쪽과 오른쪽 평균변화율의 극한이 서로 다르므로
    두 함수 모두 원점에서 미분 가능하지 않습니다.
    """)

with st.expander("질문 3. 대칭 할선의 기울기만으로 미분가능성을 판단할 수 있을까?"):
    st.write("""
    대칭 할선의 기울기만으로는 충분하지 않습니다.

    대칭 할선의 기울기는 왼쪽 평균변화율과 오른쪽 평균변화율의
    평균이기 때문에 서로 다른 두 기울기를 하나의 값으로 나타낼 수 있습니다.

    따라서 미분가능성을 판단하려면 왼쪽과 오른쪽 평균변화율도
    함께 확인해야 합니다.
    """)

with st.expander("질문 4. 이번 탐구에서 알 수 있는 점은 무엇일까?"):
    st.write("""
    대칭 할선의 기울기는 함수의 한 점 주변에서 나타나는
    평균적인 변화 방향을 보여줍니다.

    하지만 미분계수는 그 점에서 왼쪽과 오른쪽의 변화율이
    같은 값에 가까워질 때 존재합니다.

    따라서 대칭 할선의 극한과 미분가능성은 구분해서 해석해야 합니다.
    """)


# --------------------------------------------------
# 11. 데이터 다운로드
# --------------------------------------------------

st.divider()
st.header("6. 탐구 결과 저장")

csv = df.to_csv(index=False).encode("utf-8-sig")

st.download_button(
    label="기울기 변화 데이터 CSV 다운로드",
    data=csv,
    file_name="symmetric_secant_results.csv",
    mime="text/csv"
)

st.caption(
    "계산 결과는 선택한 함수, 기준점 a, 현재 h에 따라 달라집니다."
)
