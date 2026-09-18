import streamlit as st
import numpy as np
import plotly.graph_objects as go

# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="평균변화율과 미분계수 탐구",
    page_icon="📐",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
    .main {
        background-color: #f7f8fc;
    }

    .title-box {
        background: linear-gradient(135deg, #eef2ff, #f8faff);
        padding: 30px;
        border-radius: 20px;
        margin-bottom: 25px;
        border: 1px solid #e3e7f5;
    }

    .title {
        font-size: 34px;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 8px;
    }

    .subtitle {
        font-size: 17px;
        color: #64748b;
    }

    .section-title {
        font-size: 25px;
        font-weight: 750;
        color: #1f2937;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .result-card {
        background: white;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 3px 12px rgba(0,0,0,0.04);
        text-align: center;
    }

    .result-label {
        color: #64748b;
        font-size: 15px;
        margin-bottom: 8px;
    }

    .result-value {
        font-size: 30px;
        font-weight: 800;
        color: #111827;
    }

    .explanation {
        background: white;
        border-left: 5px solid #6366f1;
        padding: 20px;
        border-radius: 10px;
        line-height: 1.8;
        margin-top: 15px;
    }

    .conclusion {
        background: linear-gradient(135deg, #f5f3ff, #eef2ff);
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #ddd6fe;
        line-height: 1.9;
        font-size: 16px;
    }

    .formula-box {
        background: #111827;
        color: white;
        padding: 20px;
        border-radius: 14px;
        text-align: center;
        font-size: 20px;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)


# =========================================================
# 제목
# =========================================================
st.markdown("""
<div class="title-box">
    <div class="title">📐 평균변화율과 미분계수의 관계 탐구</div>
    <div class="subtitle">
        두 점을 이용한 할선의 기울기가 한 점에서의 순간변화율에 어떻게 가까워지는지 살펴봅니다.
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# 탐구 소개
# =========================================================
st.markdown('<div class="section-title">🔎 탐구 주제</div>', unsafe_allow_html=True)

st.write(
    "함수 f(x) = x²에서 두 점을 지나는 할선의 기울기와 "
    "한 점에서의 미분계수를 비교하여, 평균변화율과 순간변화율의 관계를 탐구합니다."
)

st.info(
    "핵심 질문: 두 점 사이의 거리를 점점 줄이면 할선의 기울기는 "
    "한 점에서의 접선의 기울기에 가까워질까?"
)


# =========================================================
# 입력 영역
# =========================================================
st.markdown('<div class="section-title">⚙️ 탐구 조건 설정</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    a = st.slider(
        "기준점 a",
        min_value=-3.0,
        max_value=3.0,
        value=1.9,
        step=0.1
    )

with col2:
    h = st.slider(
        "두 점 사이의 거리 h",
        min_value=0.1,
        max_value=2.0,
        value=0.5,
        step=0.1
    )

b = a + h


# =========================================================
# 함수 계산
# =========================================================
def f(x):
    return x ** 2


# A, B 좌표
xA = a
yA = f(a)

xB = b
yB = f(b)

# 할선 기울기
secant_slope = (f(a + h) - f(a)) / h

# f(x)=x²의 미분계수
derivative = 2 * a

# 오차
error = abs(secant_slope - derivative)


# =========================================================
# 계산 결과
# =========================================================
st.markdown('<div class="section-title">📊 계산 결과</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">할선의 기울기</div>
        <div class="result-value">{secant_slope:.4f}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">미분계수 f'({a:.1f})</div>
        <div class="result-value">{derivative:.4f}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">두 값의 차이</div>
        <div class="result-value">{error:.4f}</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 그래프
# =========================================================
st.markdown('<div class="section-title">📈 그래프로 확인하기</div>', unsafe_allow_html=True)

x_min = min(a - 1.0, -0.5)
x_max = max(b + 1.5, 3.5)

x = np.linspace(x_min, x_max, 500)
y = f(x)

# 할선
secant_x = np.linspace(x_min, x_max, 200)
secant_y = secant_slope * (secant_x - a) + f(a)

# 접선
tangent_x = np.linspace(x_min, x_max, 200)
tangent_y = derivative * (tangent_x - a) + f(a)

fig = go.Figure()

# 함수
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="lines",
    name="f(x) = x²",
    line=dict(width=4)
))

# 할선
fig.add_trace(go.Scatter(
    x=secant_x,
    y=secant_y,
    mode="lines",
    name="할선",
    line=dict(width=3, dash="dash")
))

# 접선
fig.add_trace(go.Scatter(
    x=tangent_x,
    y=tangent_y,
    mode="lines",
    name=f"접선 (기울기 = {derivative:.2f})",
    line=dict(width=3)
))

# A점
fig.add_trace(go.Scatter(
    x=[xA],
    y=[yA],
    mode="markers+text",
    name="A",
    text=["A"],
    textposition="top left",
    marker=dict(size=12)
))

# B점
fig.add_trace(go.Scatter(
    x=[xB],
    y=[yB],
    mode="markers+text",
    name="B",
    text=["B"],
    textposition="top right",
    marker=dict(size=12)
))

# 그래프 설명
fig.add_annotation(
    x=a,
    y=f(a),
    text=f"A = ({a:.1f}, {f(a):.2f})",
    showarrow=True,
    arrowhead=2,
    ax=-50,
    ay=45
)

fig.add_annotation(
    x=b,
    y=f(b),
    text=f"B = ({b:.1f}, {f(b):.2f})",
    showarrow=True,
    arrowhead=2,
    ax=55,
    ay=-45
)

fig.update_layout(
    height=600,
    template="plotly_white",
    hovermode="x unified",
    xaxis_title="x",
    yaxis_title="y",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    margin=dict(l=50, r=40, t=70, b=50)
)

fig.update_xaxes(
    zeroline=True,
    zerolinewidth=2
)

fig.update_yaxes(
    zeroline=True,
    zerolinewidth=2
)

st.plotly_chart(fig, use_container_width=True)


# =========================================================
# 그래프 해석
# =========================================================
st.markdown('<div class="section-title">🧠 그래프에서 확인할 수 있는 것</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="explanation">

<strong>① 파란색 곡선</strong><br>
함수 f(x) = x²의 그래프입니다.

<br><br>

<strong>② 점선으로 표시된 직선</strong><br>
A와 B 두 점을 지나는 <strong>할선</strong>입니다.
현재 두 점 사이의 거리는 h = {h:.1f}입니다.

<br><br>

<strong>③ 다른 직선</strong><br>
A에서의 <strong>접선</strong>이며, 접선의 기울기는 미분계수
f'({a:.1f}) = {derivative:.4f}입니다.

<br><br>

<strong>④ 두 기울기의 비교</strong><br>
할선의 기울기는 {secant_slope:.4f}, 미분계수는 {derivative:.4f}이므로
현재 두 값의 차이는 {error:.4f}입니다.

</div>
""", unsafe_allow_html=True)


# =========================================================
# 수학적 계산
# =========================================================
st.markdown('<div class="section-title">🧮 수학적으로 계산하기</div>', unsafe_allow_html=True)

st.markdown("""
<div class="formula-box">
평균변화율 = [f(a+h) - f(a)] / h
</div>
""", unsafe_allow_html=True)

st.latex(
    rf"""
    \frac{{f(a+h)-f(a)}}{{h}}
    =
    \frac{{(a+h)^2-a^2}}{{h}}
    """
)

st.latex(
    rf"""
    =
    \frac{{a^2+2ah+h^2-a^2}}{{h}}
    =
    2a+h
    """
)

st.write(
    f"따라서 현재 a = {a:.1f}, h = {h:.1f}이므로 "
    f"할선의 기울기는 2a+h = {secant_slope:.4f}입니다."
)

st.markdown("""
<div class="formula-box">
미분계수 = f'(a) = 2a
</div>
""", unsafe_allow_html=True)

st.write(
    f"f(x) = x²의 도함수는 f'(x) = 2x이므로, "
    f"x = {a:.1f}에서의 미분계수는 {derivative:.4f}입니다."
)


# =========================================================
# h 변화 실험
# =========================================================
st.markdown('<div class="section-title">🔬 h를 줄여가며 비교하기</div>', unsafe_allow_html=True)

st.write(
    "두 점 사이의 거리 h를 작게 만들수록 할선의 기울기가 "
    "미분계수에 가까워지는지 확인할 수 있습니다."
)

h_values = [1.0, 0.5, 0.2, 0.1, 0.05, 0.01]

rows = []

for hv in h_values:
    slope = (f(a + hv) - f(a)) / hv
    diff = abs(slope - derivative)

    rows.append({
        "h": hv,
        "할선의 기울기": slope,
        "미분계수": derivative,
        "차이": diff
    })

st.dataframe(
    rows,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# 탐구 결과
# =========================================================
st.markdown('<div class="section-title">📝 탐구 결과</div>', unsafe_allow_html=True)

if error < 0.05:
    conclusion = f"""
    이번 탐구에서는 f(x)=x²에서 두 점 사이의 거리를 h={h:.2f}로 설정하고
    평균변화율과 미분계수를 비교했습니다. 두 값의 차이는 {error:.4f}로 매우 작게
    나타났습니다. 이를 통해 두 점 사이의 거리가 작아질수록 할선이 접선에 가까워지고,
    평균변화율이 한 점에서의 순간변화율인 미분계수에 가까워진다는 것을 확인했습니다.
    """
elif error < 0.2:
    conclusion = f"""
    이번 탐구에서는 f(x)=x²에서 두 점 사이의 거리를 h={h:.2f}로 설정하여
    할선의 기울기와 미분계수를 비교했습니다. 할선의 기울기는 {secant_slope:.4f},
    미분계수는 {derivative:.4f}로 나타났으며 두 값의 차이는 {error:.4f}였습니다.
    h의 값을 더 작게 만들수록 두 기울기의 차이가 줄어드는 것을 확인할 수 있었습니다.
    """
else:
    conclusion = f"""
    이번 탐구에서는 f(x)=x²에서 두 점 사이의 거리를 h={h:.2f}로 설정하여
    평균변화율과 미분계수를 비교했습니다. 현재는 두 점 사이의 거리가 비교적 크기 때문에
    할선의 기울기와 미분계수 사이에 {error:.4f}의 차이가 나타났습니다.
    h를 더 작게 설정하면 할선이 접선에 가까워지면서 두 값의 차이도 감소하게 됩니다.
    """

st.markdown(
    f"""
    <div class="conclusion">
    {conclusion}
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 핵심 정리
# =========================================================
st.markdown('<div class="section-title">💡 핵심 정리</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **평균변화율**

    두 점 사이에서 함수가 얼마나 변했는지를 나타내는 값
    """)

with col2:
    st.markdown("""
    **미분계수**

    한 점에서 함수가 순간적으로 변하는 정도를 나타내는 값
    """)

with col3:
    st.markdown("""
    **두 개념의 관계**

    h → 0이면 할선의 기울기가 접선의 기울기에 가까워짐
    """)


# =========================================================
# 마무리
# =========================================================
st.markdown("---")

st.caption(
    "수학적 계산과 그래프를 함께 이용하여 평균변화율과 미분계수의 관계를 탐구한 결과입니다."
)
