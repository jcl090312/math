import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------
# 페이지 설정
# ---------------------------------------

st.set_page_config(
    page_title="미분계수 탐구 도구",
    page_icon="📐",
    layout="wide"
)


# ---------------------------------------
# 제목
# ---------------------------------------

st.title("📐 할선의 기울기에서 접선의 기울기로")

st.markdown("""
### 미분계수의 기하학적 의미 탐구

두 점 사이의 평균변화율을 나타내는 **할선의 기울기**가
한 점에서의 **접선의 기울기**, 즉 미분계수에
어떻게 가까워지는지 관찰해 봅시다.
""")


# ---------------------------------------
# 함수 정의
# ---------------------------------------

def f(x):
    return x ** 2


def derivative(x):
    return 2 * x


# ---------------------------------------
# 사용자 설정
# ---------------------------------------

st.sidebar.header("⚙️ 탐구 조건")

a = st.sidebar.slider(
    "기준점 a",
    min_value=-3.0,
    max_value=3.0,
    value=1.0,
    step=0.1
)

h = st.sidebar.slider(
    "두 점 사이의 거리 h",
    min_value=0.01,
    max_value=2.0,
    value=0.5,
    step=0.01
)


# ---------------------------------------
# 두 점 계산
# ---------------------------------------

x1 = a
x2 = a + h

y1 = f(x1)
y2 = f(x2)


# ---------------------------------------
# 할선의 기울기
# ---------------------------------------

secant_slope = (y2 - y1) / (x2 - x1)


# ---------------------------------------
# 미분계수
# ---------------------------------------

derivative_value = derivative(a)


# ---------------------------------------
# 오차
# ---------------------------------------

error = abs(secant_slope - derivative_value)


# ---------------------------------------
# 접선 함수
# ---------------------------------------

def tangent(x):
    return derivative_value * (x - a) + y1


# ---------------------------------------
# 그래프 범위
# ---------------------------------------

x_min = min(a - 2, x2 - 2)
x_max = max(a + 2, x2 + 2)

x = np.linspace(x_min, x_max, 400)

y = f(x)
y_tangent = tangent(x)


# ---------------------------------------
# 그래프
# ---------------------------------------

fig, ax = plt.subplots(figsize=(9, 6))

# 원래 함수
ax.plot(
    x,
    y,
    color="blue",
    linewidth=2.5,
    label=r"$f(x)=x^2$"
)

# 접선
ax.plot(
    x,
    y_tangent,
    color="red",
    linewidth=2,
    label="접선"
)

# 할선
ax.plot(
    [x1, x2],
    [y1, y2],
    color="green",
    linewidth=2,
    label="할선"
)

# 기준점 A
ax.scatter(
    x1,
    y1,
    color="black",
    s=70,
    zorder=5
)

# 점 B
ax.scatter(
    x2,
    y2,
    color="purple",
    s=70,
    zorder=5
)

# 점 이름
ax.annotate(
    "A",
    (x1, y1),
    xytext=(8, 8),
    textcoords="offset points",
    fontsize=12
)

ax.annotate(
    "B",
    (x2, y2),
    xytext=(8, 8),
    textcoords="offset points",
    fontsize=12
)


# 축 설정
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

ax.grid(True, alpha=0.25)

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.set_title("할선과 접선의 관계")

ax.legend()

st.pyplot(fig)


# ---------------------------------------
# 결과 표시
# ---------------------------------------

st.subheader("📊 계산 결과")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "할선의 기울기",
        f"{secant_slope:.6f}"
    )

with col2:
    st.metric(
        "미분계수",
        f"{derivative_value:.6f}"
    )

with col3:
    st.metric(
        "오차",
        f"{error:.6f}"
    )


# ---------------------------------------
# 수학적 설명
# ---------------------------------------

st.subheader("📚 수학적으로 해석하기")

st.markdown(
    f"""
현재 기준점은

**a = {a:.2f}**

이고, 두 점 사이의 거리는

**h = {h:.2f}**

입니다.

두 점 A, B를 이용한 할선의 기울기는 평균변화율이므로

\\[
\\frac{{f(a+h)-f(a)}}{{h}}
\\]

로 계산할 수 있습니다.

현재 할선의 기울기는

**{secant_slope:.6f}**

입니다.

한편,

\\[
f(x)=x^2
\\]

의 도함수는

\\[
f'(x)=2x
\\]

이므로 기준점 a에서의 미분계수는

**{derivative_value:.6f}**

입니다.

따라서 현재 두 값의 차이는

**{error:.6f}**

입니다.
"""
)


# ---------------------------------------
# 탐구 안내
# ---------------------------------------

st.subheader("🔍 탐구해 보기")

st.markdown("""
### 질문 1
h의 값을 점점 작게 만들면 할선의 기울기는 어떻게 변할까요?

### 질문 2
h가 작아질수록 할선은 접선에 가까워지는 모습을 보이나요?

### 질문 3
할선의 기울기와 미분계수 사이의 오차는 어떻게 변하나요?

### 질문 4
기준점 a를 변경해도 같은 현상이 나타날까요?
""")


# ---------------------------------------
# 핵심 개념
# ---------------------------------------

st.info(
    "💡 핵심: 두 점 사이의 거리를 점점 작게 하면 "
    "할선의 기울기는 한 점에서의 접선의 기울기, "
    "즉 미분계수에 가까워집니다."
)
