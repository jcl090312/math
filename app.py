"""기울기 실험실: 대칭 할선의 기울기와 극한 탐구.

실행: python -m streamlit run app.py
HTML/CSS/JavaScript를 포함한 단일 파일이며 외부 차트 CDN을 사용하지 않습니다.
생성 원본: dist/; 재생성: python tools/build_streamlit.py
"""
import streamlit as st

st.set_page_config(
    page_title="기울기 실험실 · 대칭 할선과 극한 탐구",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """<style>
    .block-container { max-width: 1500px; padding: 1rem 1rem 2rem; }
    [data-testid="stAppViewContainer"] { background: #f6f7f5; }
    </style>""",
    unsafe_allow_html=True,
)

# This is fixed application code, never HTML supplied by a visitor.
HTML = r"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="그래프 위의 점을 직접 움직이며 대칭 할선, 평균변화율, 미분계수의 관계를 탐구하는 수학 실험실입니다.">
  <meta name="theme-color" content="#087c75">
  <title>기울기 실험실 · 대칭 할선과 극한 탐구</title>
  <style>
:root {
  color-scheme: light;
  --page: #f6f7f5;
  --paper: #ffffff;
  --ink: #182d45;
  --muted: #667483;
  --faint: #8a959f;
  --line: #e3e8e7;
  --teal: #087c75;
  --teal-dark: #06645f;
  --teal-wash: #edf7f4;
  --blue: #3477d6;
  --green: #119773;
  --coral: #dc654c;
  --purple: #8254bd;
  --radius: 19px;
  --shadow: 0 4px 22px rgb(25 48 59 / 3%);
  font-family: "Pretendard", "Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  font-synthesis: none;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--page); color: var(--ink); line-height: 1.6; }
button, input, textarea, select { font: inherit; }
button, input, textarea { -webkit-tap-highlight-color: transparent; }
button { color: inherit; cursor: pointer; }
button:disabled { cursor: not-allowed; opacity: .46; }
button, a, input, textarea, summary { outline-offset: 4px; }
button:focus-visible, a:focus-visible, input:focus-visible, textarea:focus-visible, summary:focus-visible {
  outline: 3px solid #4fa6a0;
}
button { touch-action: manipulation; }
a { color: var(--teal); text-underline-offset: 3px; }
svg { vertical-align: middle; }
p { margin: 0; }
h1, h2, h3, h4 { color: var(--ink); margin: 0; line-height: 1.4; word-break: keep-all; }
h2 { font-size: 19px; font-weight: 750; letter-spacing: -.55px; }
h3 { font-size: 16px; font-weight: 720; letter-spacing: -.3px; }
[hidden] { display: none !important; }
.sr-only, .visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.topbar {
  min-height: 78px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 17px max(32px, calc((100vw - 1376px) / 2));
  background: rgb(255 255 255 / 94%);
  border-bottom: 1px solid var(--line);
}
.brand { display: flex; align-items: center; gap: 12px; text-decoration: none; color: var(--ink); }
.brand-mark {
  width: 42px;
  height: 42px;
  flex: 0 0 42px;
  display: grid;
  place-items: center;
  border-radius: 13px;
  background: var(--teal);
  color: #fff;
}
.brand-mark svg { width: 28px; height: 28px; }
.brand-title { display: block; font-size: 18px; line-height: 1.35; font-weight: 800; letter-spacing: -.7px; }
.brand-sub { display: block; margin-top: 3px; color: var(--muted); font-size: 11px; letter-spacing: .2px; }
.actions, .header-actions, .topbar-actions, .graph-actions { display: flex; align-items: center; gap: 10px; }
.graph-actions { gap: 6px; }
.header-tag, .project-tag, .project-label {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 6px 11px;
  color: #5f6e7c;
  background: #f7f9f8;
  border: 1px solid var(--line);
  border-radius: 7px;
  font-size: 11px;
  white-space: nowrap;
}

.page { width: min(1440px, 100%); margin: 0 auto; padding: 40px 32px 26px; }
.hero { margin-bottom: 28px; }
.mobile-break { display: none; }
.eyebrow, .section-kicker {
  display: block;
  color: var(--teal);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1.1px;
  line-height: 1.5;
}
.eyebrow { margin-bottom: 10px; }
.hero h1 { font-size: clamp(28px, 2.8vw, 39px); font-weight: 800; letter-spacing: -1.5px; line-height: 1.36; }
.hero-copy { max-width: 780px; margin-top: 12px; color: var(--muted); font-size: 14px; line-height: 1.85; word-break: keep-all; }
.hero-copy strong { color: #394e61; font-weight: 650; }
.hero-step-row { display: flex; align-items: center; flex-wrap: wrap; gap: 9px 22px; margin-top: 20px; }
.step { display: inline-flex; align-items: center; gap: 8px; color: #607282; font-size: 12px; }
.step > span:first-child, .step > b:first-child, .step-number {
  display: inline-grid;
  width: 22px;
  height: 22px;
  place-items: center;
  border: 1px solid #d6e3de;
  border-radius: 50%;
  background: #fff;
  color: var(--teal);
  font-size: 10px;
  font-weight: 800;
}
.step-arrow { color: #b1bdb7; font-size: 12px; }

.workspace { display: grid; grid-template-columns: 292px minmax(0, 1fr); align-items: start; gap: 22px; }
.controls, .main-column { min-width: 0; }
.main-column { display: flex; flex-direction: column; gap: 18px; }
.panel { background: var(--paper); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); }
.control-panel { padding: 22px; }
.panel-heading { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 16px; }
.panel-heading .section-kicker { margin-bottom: 5px; }
.control-panel .panel-heading .section-kicker { margin-bottom: 0; }
.panel-heading p { margin-top: 5px; font-size: 12px; color: var(--muted); line-height: 1.75; }
.control-title { font-size: 14px; letter-spacing: -.3px; margin-bottom: 13px; }
.function-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px; }
.function-card {
  appearance: none;
  border: 1px solid #e1e7e5;
  border-radius: 11px;
  min-height: 81px;
  background: #fff;
  padding: 10px 8px;
  text-align: left;
  transition: background .15s, border-color .15s, box-shadow .15s;
}
.function-card:hover { background: #f8fbfa; border-color: #aecdc5; }
.function-card.active, .function-card[aria-pressed="true"] {
  background: var(--teal-wash);
  border-color: var(--teal);
  box-shadow: inset 0 0 0 1px var(--teal);
}
.function-formula { display: block; color: var(--ink); font-size: 20px; font-weight: 750; letter-spacing: -.6px; line-height: 1.45; }
.function-card.active .function-formula { color: var(--teal-dark); }
.function-name { display: block; margin-top: 4px; color: var(--muted); font-size: 11px; }
.function-card:last-child .function-formula { font-size: 16px; letter-spacing: -.2px; }
.control-section { border-top: 1px solid #e9edeb; margin-top: 19px; padding-top: 18px; }
.control-section > h3, .control-section > .section-kicker { margin-bottom: 12px; }
.field-row { display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 11px; }
.field-row label, .field-label { color: #44596b; font-size: 12px; font-weight: 650; line-height: 1.6; }
.field-row small, .field-label small { display: block; color: var(--faint); font-size: 10px; font-weight: 400; }
.field-value { color: var(--ink); font-size: 13px; font-weight: 700; font-variant-numeric: tabular-nums; }
.h-field { margin-top: 19px; }
.number-input, .field-row input[type="number"] {
  width: 111px;
  min-width: 0;
  border: 1px solid #dce3e2;
  border-radius: 8px;
  padding: 8px 9px;
  background: #fbfcfb;
  color: var(--ink);
  font-size: 12px;
  font-weight: 650;
  text-align: right;
  font-variant-numeric: tabular-nums;
}
.number-input:hover { border-color: #a5bbb5; }
input[type="range"] { width: 100%; accent-color: var(--teal); cursor: pointer; }
.button-row { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 9px; }
.button-row .btn { min-width: 0; padding-inline: 5px; }
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
  border: 1px solid transparent;
  border-radius: 9px;
  min-height: 38px;
  padding: 9px 13px;
  background: #fff;
  font-size: 12px;
  font-weight: 650;
  line-height: 1.5;
  text-decoration: none;
  transition: background .15s, border-color .15s, color .15s;
}
.btn svg { flex: 0 0 16px; width: 16px; height: 16px; }
.btn-primary { background: var(--teal); border-color: var(--teal); color: #fff; }
.btn-primary:hover:not(:disabled) { background: var(--teal-dark); border-color: var(--teal-dark); }
.btn-secondary { color: #41586b; background: #fff; border-color: #dde5e3; }
.btn-secondary:hover:not(:disabled) { border-color: #a5c1b9; background: #f6faf8; }
.btn-quiet { color: #526777; background: #f4f7f6; border-color: #edf0ef; }
.btn-quiet:hover:not(:disabled) { background: #eaf1ee; color: var(--teal-dark); }
.btn-small { min-height: 31px; padding: 6px 10px; font-size: 11px; border-radius: 7px; }
.btn-icon, .icon-button {
  width: 33px;
  height: 33px;
  min-height: 33px;
  flex: 0 0 33px;
  padding: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  color: #586d7d;
  border: 1px solid #e1e7e5;
  border-radius: 8px;
  font-size: 18px;
  font-weight: 450;
}
.btn-icon:hover, .icon-button:hover { background: #f1f7f4; color: var(--teal); border-color: #b5cfc5; }
.icon-button svg { width: 16px; height: 16px; }
.control-panel > .btn, .control-section > .btn { width: 100%; margin-top: 9px; }
.full-width { width: 100%; }
.counterexample-banner {
  display: flex;
  flex-direction: column;
  gap: 3px;
  width: 100%;
  margin-top: 14px;
  border: 1px solid #eee2c8;
  border-radius: 9px;
  padding: 11px 12px;
  background: #fffaf0;
  color: #916620;
  text-align: left;
  font-size: 11px;
  line-height: 1.65;
}
.counterexample-banner:hover { background: #fff4da; border-color: #dfc99c; }
.counterexample-banner strong { font-size: 12px; font-weight: 750; }
.selected-point { margin-top: 12px; }
.selected-point > label, .selected-point > .field-label { display: block; margin-bottom: 8px; }
.segmented { display: flex; align-items: stretch; gap: 3px; padding: 4px; border: 1px solid #e5ebe8; border-radius: 9px; background: #f5f8f6; }
.segmented button {
  flex: 1 1 0;
  border: 1px solid transparent;
  border-radius: 6px;
  padding: 7px 3px;
  background: transparent;
  color: #748271;
  font-size: 11px;
  line-height: 1.6;
  white-space: nowrap;
}
.segmented button[aria-pressed="true"], .segmented button.active { border-color: #d7e4dd; background: #fff; color: var(--teal-dark); font-weight: 750; box-shadow: 0 1px 3px rgb(25 57 38 / 5%); }
.toggle-row { display: flex; align-items: center; gap: 9px; margin-top: 10px; color: #586c7b; font-size: 12px; cursor: pointer; line-height: 1.55; }
.toggle-row input { width: 15px; height: 15px; flex: 0 0 15px; margin: 0; accent-color: var(--teal); }
.toggle-row:has(input:disabled) { opacity: .53; cursor: not-allowed; }
.tiny-note { margin-top: 10px; color: #7c8a92; font-size: 10px; line-height: 1.8; word-break: keep-all; }

.graph-panel { overflow: hidden; }
.graph-toolbar { display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 20px 24px 13px; }
.graph-toolbar h2 { font-size: 17px; }
.graph-toolbar .section-kicker { margin-bottom: 4px; }
.graph-toolbar .actions { gap: 6px; }
.graph-toolbar .btn-small { min-height: 33px; }
.legend { display: flex; align-items: center; flex-wrap: wrap; gap: 8px 17px; color: #75828e; font-size: 10px; line-height: 1.6; }
.graph-panel > .legend { padding: 0 24px 8px; }
.legend-item { display: inline-flex; align-items: center; gap: 6px; white-space: nowrap; }
.swatch { display: inline-block; width: 17px; height: 0; border-top: 2px solid currentColor; }
.swatch.dashed { border-top-style: dashed; }
.dot { display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: currentColor; }
.left-green { color: var(--green); }
.right-coral { color: var(--coral); }
.symmetric-purple { color: var(--purple); }
.curve-blue { color: var(--blue); }
.center-navy { color: #172d4b; }
.text-left-green { color: var(--green); }
.text-right-coral { color: var(--coral); }
.text-symmetric-purple { color: var(--purple); }
.graph-stage { width: 100%; min-height: 0; aspect-ratio: 820 / 460; overflow: hidden; position: relative; }
.graph-stage svg { display: block; width: 100%; height: 100%; user-select: none; -webkit-user-select: none; }
#main-graph, #graph { touch-action: none; }
.graph-tip { display: flex; align-items: flex-start; gap: 8px; margin: 0 24px; padding: 10px 0 14px; color: #7a8893; font-size: 11px; line-height: 1.7; word-break: keep-all; }
.graph-tip svg { width: 14px; height: 14px; flex: 0 0 14px; margin-top: 2px; color: #8c9d9a; }
.coordinate-row { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0; padding: 13px 20px; border-top: 1px solid #e9eeeb; background: #fcfdfc; }
.coordinate-row > * { min-width: 0; display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 4px 8px; padding: 0 8px; color: #71808c; font-size: 10px; font-variant-numeric: tabular-nums; }
.coordinate-row > * + * { border-left: 1px solid #e5ebe8; }
.coordinate-row strong { color: #405568; font-size: 11px; font-weight: 700; }
.coordinate-chip b { color: #405568; font-weight: 750; }

.plot-grid { fill: none; stroke: #e9eef1; stroke-width: 1; }
.plot-axis { fill: none; stroke: #a3afbb; stroke-width: 1.25; }
.axis-label { fill: #7b8996; font-size: 11px; font-weight: 450; }
.axis-title { fill: #778795; font-size: 12px; font-weight: 650; }
.curve-path { fill: none; stroke: var(--blue); stroke-width: 3.4; stroke-linecap: round; stroke-linejoin: round; }
.secant-path { fill: none; stroke: var(--purple); stroke-width: 3; stroke-linecap: round; }
.left-path { fill: none; stroke: var(--green); stroke-width: 2.1; stroke-dasharray: 6 4; stroke-linecap: round; }
.right-path { fill: none; stroke: var(--coral); stroke-width: 2.1; stroke-dasharray: 6 4; stroke-linecap: round; }
.tangent-path { fill: none; stroke: #263f5a; stroke-width: 1.9; stroke-dasharray: 8 5; opacity: .78; }
.guide-line { fill: none; stroke: #cbd6de; stroke-width: 1; stroke-dasharray: 4 5; }
.graph-point { cursor: grab; touch-action: none; outline: none; }
.point-dragging, .point-dragging .graph-point, .graph-point.dragging { cursor: grabbing; }
.point-halo { fill: #fff; opacity: .85; }
.point-hit { fill: transparent; stroke: none; pointer-events: all; }
circle.point-core { fill: var(--point-color, #182d45); stroke: #fff; stroke-width: 3; }
.graph-point:hover .point-halo { fill: var(--point-color, #182d45); opacity: .14; }
.graph-point:focus-visible .point-halo, .graph-point.selected .point-halo, .graph-point[data-selected="true"] .point-halo { fill: none; stroke: var(--point-color, #182d45); stroke-width: 2; opacity: .7; }
.graph-point:focus-visible .point-core { stroke-width: 4; }
.point-label { fill: var(--point-color, #182d45); font-size: 12px; font-weight: 800; paint-order: stroke; stroke: #fff; stroke-width: 5px; stroke-linejoin: round; pointer-events: none; }
.span-label { fill: #8594a1; font-size: 11px; font-style: italic; font-weight: 600; paint-order: stroke; stroke: #fff; stroke-width: 4px; }
.span-line { stroke: #bbc8ce; stroke-width: 1; fill: none; }
.coord-label { fill: #83919e; font-size: 10px; }

.metrics-heading { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 5px 12px; margin: 0 2px 10px; }
.metrics-heading h2 { font-size: 14px; letter-spacing: -.3px; }
.metrics-heading > span { color: #8a979e; font-size: 10px; }
.metric-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.metric { position: relative; min-width: 0; overflow: hidden; padding: 17px 18px 16px; border: 1px solid var(--line); border-radius: 13px; background: #fff; box-shadow: var(--shadow); }
.metric::before { position: absolute; content: ""; left: 0; right: 0; top: 0; height: 3px; background: var(--metric-color, #c4d0d4); }
.metric-left { --metric-color: var(--green); }
.metric-right { --metric-color: var(--coral); }
.metric-symmetric { --metric-color: var(--purple); background: #fcfaff; }
.metric-label { display: flex; align-items: center; gap: 6px; color: #6f7e8a; font-size: 11px; font-weight: 600; }
.metric-number { display: block; margin-top: 6px; font-size: clamp(21px, 2.15vw, 29px); line-height: 1.35; letter-spacing: -.8px; font-weight: 740; color: var(--metric-color, var(--ink)); font-variant-numeric: tabular-nums; }
.metric-formula { display: block; margin-top: 6px; color: #919aa4; font-size: 10px; line-height: 1.5; font-family: Georgia, "Times New Roman", serif; white-space: nowrap; }

.insight-panel { display: grid; grid-template-columns: minmax(0, 1fr) auto; grid-template-areas: "title limits" "copy limits" "note note"; column-gap: 22px; row-gap: 9px; padding: 20px 22px; border: 1px solid #d9e9e2; border-radius: 14px; background: #f0f8f4; }
.insight-panel[data-kind="warning"], .insight-panel.warning { border-color: #eddec2; background: #fff8e9; }
.insight-status { grid-area: title; display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 0; font-size: 13px; font-weight: 750; }
.insight-status h2 { font-size: 15px; letter-spacing: -.5px; }
.status-pill { display: inline-flex; align-items: center; gap: 5px; padding: 3px 8px; border: 1px solid #d0e4d9; border-radius: 6px; background: #fff; color: #36755d; font-size: 10px; line-height: 1.6; white-space: nowrap; }
.status-pill[data-kind="warning"], [data-kind="warning"] .status-pill, .warning .status-pill { border-color: #ecd4a5; color: #966c2a; background: #fffdf7; }
.insight-body { grid-area: copy; color: #648073; font-size: 12px; line-height: 1.8; word-break: keep-all; }
[data-kind="warning"] .insight-body, .warning .insight-body { color: #92743f; }
.insight-body p + p { margin-top: 6px; }
.limit-values { grid-area: limits; display: flex; flex-direction: column; align-self: center; min-width: 155px; border-left: 1px solid #d5e6dd; padding-left: 20px; }
.limit-values > span:first-child { margin-bottom: 4px; color: #708d7f; font-size: 9px; font-weight: 650; }
.insight-panel > .tiny-note { grid-area: note; margin-top: 1px; color: #869b90; font-size: 9px; }
[data-kind="warning"].insight-panel > .tiny-note { color: #a48c65; }
[data-kind="warning"] .limit-values { border-left-color: #ead9b4; }
.limit-values > * { display: flex; justify-content: space-between; gap: 15px; color: #729181; font-size: 10px; line-height: 1.9; }
.limit-values strong, .limit-values b { color: #315d4b; font-size: 12px; font-weight: 750; font-variant-numeric: tabular-nums; }
[data-kind="warning"] .limit-values > * { color: #96794d; }
[data-kind="warning"] .limit-values strong, [data-kind="warning"] .limit-values b { color: #8a6227; }

.below-grid { display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); gap: 22px; margin-top: 24px; }
.convergence-panel, .data-panel { padding: 22px 24px; min-width: 0; }
.section-header { display: flex; align-items: flex-start; justify-content: space-between; gap: 14px; margin-bottom: 15px; }
.section-header .section-kicker { margin-bottom: 5px; }
.section-header h2 { font-size: 17px; }
.section-header p { margin-top: 5px; color: var(--muted); font-size: 11px; line-height: 1.75; word-break: keep-all; }
.section-header .btn { flex: 0 0 auto; }
.mini-badge { flex: 0 0 auto; display: inline-block; margin-top: 3px; padding: 5px 8px; border: 1px solid #e1e9e4; border-radius: 6px; background: #f8fbf8; color: #7c9283; font-size: 10px; font-family: Georgia, "Times New Roman", serif; }
.section-description { color: #82918f; font-size: 11px; line-height: 1.9; word-break: keep-all; }
.convergence-panel > .legend { margin-bottom: 9px; }
.legend.compact { justify-content: center; margin-top: 6px; margin-bottom: 0; font-size: 10px; }
#convergence-graph { display: block; width: 100%; aspect-ratio: 820 / 280; height: auto; overflow: visible; }
.convergence-left, .convergence-right, .convergence-symmetric { fill: none; stroke-width: 2.6; stroke-linecap: round; stroke-linejoin: round; }
.convergence-left { stroke: var(--green); }
.convergence-right { stroke: var(--coral); }
.convergence-symmetric { stroke: var(--purple); }
.data-scroll { max-height: 274px; overflow: auto; scrollbar-width: thin; scrollbar-color: #cbd8d2 transparent; border: 1px solid #e6ece8; border-radius: 9px; }
table { width: 100%; border-collapse: collapse; font-size: 10px; line-height: 1.5; font-variant-numeric: tabular-nums; white-space: nowrap; }
th { position: sticky; top: 0; z-index: 1; background: #f6f9f7; color: #708375; font-weight: 600; text-align: right; padding: 10px 11px; border-bottom: 1px solid #e1e9e4; }
td { color: #6e7d88; text-align: right; padding: 9px 11px; border-bottom: 1px solid #eef2ef; }
th:first-child, td:first-child { text-align: left; }
tbody tr:last-child td { border-bottom: 0; }
tbody tr:nth-child(even) { background: #fcfdfc; }
tbody tr:hover { background: #f2f8f5; }
td:last-child { color: var(--purple); font-weight: 600; }
.data-panel .tiny-note { margin-top: 9px; }

.theory-strip { display: flex; align-items: center; gap: 32px; margin-top: 22px; padding: 23px 28px; border: 1px solid #dde6e0; border-radius: 14px; background: #eef3ef; }
.theory-strip > div:first-child { flex: 0 1 285px; }
.theory-strip .section-kicker { font-size: 9px; letter-spacing: .6px; margin-bottom: 5px; }
.theory-strip h2 { font-size: 14px; color: #385f50; }
.theory-formula { display: flex; align-items: center; gap: 10px; }
.theory-formula > span:not(.fraction) { color: #8da598; }
.fraction { display: inline-flex; flex-direction: column; align-items: center; text-align: center; vertical-align: middle; font-size: 18px; line-height: 1.6; }
.fraction > span:first-child { padding: 0 6px 3px; border-bottom: 1px solid #80a18c; }
.fraction > span:last-child { padding-top: 2px; font-size: 17px; }
.theory-strip > strong, .theory-strip > .formula, .theory-strip .theory-formula { color: #496e5f; font-size: 23px; font-weight: 600; letter-spacing: -.6px; white-space: nowrap; font-family: Georgia, "Times New Roman", serif; }
.theory-strip h3 { font-size: 13px; margin-bottom: 5px; color: #385f50; }
.theory-strip p { color: #72887c; font-size: 11px; line-height: 1.9; word-break: keep-all; }
.theory-strip p strong { color: #476b5b; font-weight: 650; }
.notes-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 22px; margin-top: 22px; }
.notes-grid > .panel { padding: 23px 24px; min-width: 0; }
.question-list { margin-top: 16px; }
.question-list details { border-top: 1px solid #e6ece8; }
.question-list details:last-child { border-bottom: 1px solid #e6ece8; }
.question-list summary { position: relative; list-style: none; padding: 13px 23px 13px 0; color: #586f80; font-size: 12px; line-height: 1.75; cursor: pointer; word-break: keep-all; }
.question-list summary::-webkit-details-marker { display: none; }
.question-list summary::after { position: absolute; right: 1px; top: 13px; content: "+"; color: #83988c; font-size: 17px; font-weight: 400; }
.question-list details[open] summary { color: var(--teal); font-weight: 650; }
.question-list details[open] summary::after { content: "−"; }
.question-list details p, .question-list details .answer { padding: 0 15px 14px 0; color: #7d8c96; font-size: 11px; line-height: 1.9; word-break: keep-all; }
.note-area, textarea.note-area { display: block; width: 100%; min-height: 158px; resize: vertical; border: 1px solid #e0e7e3; border-radius: 10px; padding: 13px 14px; margin-top: 13px; background: #fbfcfa; color: #415969; font-size: 12px; line-height: 1.95; }
.note-label { display: block; color: #83938a; font-size: 11px; line-height: 1.9; word-break: keep-all; }
textarea::placeholder { color: #a0aaa8; }
.note-actions { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-top: 12px; }
.note-actions .tiny-note { margin-top: 0; }
.status-message { min-height: 18px; color: #4c8271; font-size: 11px; line-height: 1.7; }
.status-message[data-kind="error"] { color: #a65843; }
.notice { padding: 9px 12px; margin-top: 10px; background: #fff7e8; border: 1px solid #eedebf; border-radius: 8px; color: #997236; font-size: 11px; line-height: 1.75; }
.footer, footer { display: flex; justify-content: space-between; align-items: flex-start; gap: 14px; margin: 28px 0 0; padding: 18px 0 4px; border-top: 1px solid #e0e7e2; color: #91a098; font-size: 10px; line-height: 1.9; }
.footer strong, footer strong { font-weight: 650; color: #72877a; }
.footer a, footer a { color: #72877a; }

@media (min-width: 1320px) {
  .workspace { grid-template-columns: 304px minmax(0, 1fr); gap: 26px; }
  .control-panel { padding: 24px; }
  .graph-toolbar { padding-top: 22px; }
  .graph-stage { min-height: 0; }
}

@media (max-width: 1100px) {
  .topbar { padding-inline: 26px; }
  .page { padding: 32px 26px 24px; }
  .workspace { grid-template-columns: 260px minmax(0, 1fr); gap: 17px; }
  .control-panel { padding: 18px; }
  .graph-toolbar { padding: 18px 18px 12px; }
  .graph-panel > .legend { padding-inline: 18px; }
  .graph-tip { margin-inline: 18px; }
  .graph-stage { min-height: 0; }
  .metric-grid { gap: 9px; }
  .metric { padding: 15px 13px; }
  .metric-label { font-size: 10px; }
  .metric-formula { font-size: 9px; }
  .insight-panel { grid-template-columns: 1fr; grid-template-areas: "title" "copy" "limits" "note"; gap: 10px; padding: 18px; }
  .limit-values { display: flex; flex-direction: row; align-items: center; gap: 12px; border-left: 0; border-top: 1px solid #d5e6dd; padding-left: 0; padding-top: 9px; }
  .limit-values > span:first-child { margin-bottom: 0; }
  [data-kind="warning"] .limit-values { border-top-color: #ead9b4; }
  .limit-values > * { flex: 1; gap: 8px; }
  .below-grid { grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); gap: 17px; }
  .convergence-panel, .data-panel { padding: 20px 18px; }
  .notes-grid { gap: 17px; }
  .notes-grid > .panel { padding: 20px; }
}

@media (max-width: 900px) {
  .below-grid { grid-template-columns: 1fr; }
  .convergence-panel, .data-panel { padding: 22px; }
  #convergence-graph { max-height: 270px; }
  .data-scroll { max-height: 255px; }
  table { font-size: 11px; }
  .theory-strip { gap: 24px; padding-inline: 22px; }
  .theory-strip { flex-wrap: wrap; }
  .theory-strip > div:first-child { flex-basis: auto; flex-grow: 1; }
  .theory-strip > p { flex-basis: 100%; }
  .theory-strip > strong, .theory-strip > .formula, .theory-strip .theory-formula { font-size: 21px; }
}

@media (max-width: 760px) {
  .topbar { min-height: 68px; gap: 12px; padding: 13px 20px; }
  .brand-mark { width: 36px; height: 36px; flex-basis: 36px; border-radius: 11px; }
  .brand-mark svg { width: 24px; height: 24px; }
  .brand-title { font-size: 16px; }
  .brand-sub { font-size: 9px; }
  .topbar .header-tag, .topbar .project-tag, .topbar .project-label { display: none; }
  .topbar .btn { min-height: 32px; padding: 6px 9px; font-size: 10px; }
  .page { padding: 27px 18px 20px; }
  .hero { margin-bottom: 23px; }
  .mobile-break { display: initial; }
  .hero h1 { font-size: 29px; letter-spacing: -1.2px; line-height: 1.4; }
  .eyebrow { font-size: 10px; }
  .hero-copy { margin-top: 11px; font-size: 12px; }
  .hero-step-row { gap: 8px 15px; margin-top: 17px; }
  .step { font-size: 10px; gap: 6px; }
  .step > span:first-child, .step > b:first-child, .step-number { width: 20px; height: 20px; font-size: 9px; }
  .workspace { grid-template-columns: 1fr; gap: 18px; }
  .controls, .control-panel { position: static; }
  .control-panel { padding: 20px; }
  .function-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; }
  .function-card { min-height: 76px; padding: 9px 9px; }
  .function-formula { font-size: 20px; }
  .function-name { font-size: 10px; }
  .function-card:last-child .function-formula { font-size: 14px; }
  .field-row { gap: 20px; }
  .number-input, .field-row input[type="number"] { width: 150px; }
  .control-section { margin-top: 17px; padding-top: 16px; }
  .counterexample-banner { flex-direction: row; flex-wrap: wrap; gap: 4px 10px; align-items: center; }
  .control-section .tiny-note { font-size: 11px; }
  .segmented button { font-size: 12px; }
  .graph-toolbar { padding: 18px 18px 12px; }
  .graph-toolbar h2 { font-size: 16px; }
  .graph-panel > .legend { gap: 8px 13px; padding: 0 18px 4px; }
  .graph-stage { min-height: 0; aspect-ratio: 820 / 460; }
  .graph-tip { font-size: 10px; padding-top: 5px; }
  .coordinate-row { padding: 11px 8px; }
  .coordinate-row > * { gap: 3px 5px; padding-inline: 5px; font-size: 9px; }
  .coordinate-row strong { font-size: 10px; }
  .metric-number { font-size: 26px; }
  .metric-label { font-size: 11px; }
  .metric-formula { font-size: 10px; }
  .insight-panel { padding: 19px; }
  .insight-status { font-size: 13px; }
  .insight-body { font-size: 12px; }
  .below-grid { margin-top: 18px; gap: 18px; }
  .convergence-panel, .data-panel { padding: 19px; }
  .theory-strip { margin-top: 18px; flex-direction: column; align-items: flex-start; gap: 12px; padding: 20px; }
  .theory-strip > div:first-child { flex-basis: auto; flex-grow: 0; }
  .theory-strip > strong, .theory-strip > .formula, .theory-strip .theory-formula { font-size: 23px; }
  .notes-grid { grid-template-columns: 1fr; margin-top: 18px; gap: 18px; }
  .notes-grid > .panel { padding: 21px; }
  .question-list summary { font-size: 12px; }
  .question-list details p, .question-list details .answer { font-size: 11px; }
  .note-area, textarea.note-area { min-height: 150px; }
  .footer, footer { flex-direction: column; gap: 5px; margin-top: 23px; }
}

@media (max-width: 430px) {
  .topbar { padding-inline: 15px; }
  .brand { gap: 9px; }
  .brand-sub { max-width: 180px; }
  .page { padding-inline: 12px; }
  .hero { padding-inline: 5px; }
  .hero h1 { font-size: 27px; }
  .hero-step-row { gap: 8px 11px; }
  .step { font-size: 9px; }
  .control-panel { padding: 18px; }
  .function-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .function-card { min-height: 70px; padding: 9px 12px; }
  .function-formula { font-size: 21px; }
  .function-card:last-child .function-formula { font-size: 17px; }
  .function-name { font-size: 11px; }
  .graph-toolbar { padding: 16px 14px 11px; gap: 8px; }
  .graph-toolbar .actions, .graph-actions { gap: 4px; }
  .graph-toolbar .icon-button, .graph-toolbar .btn-icon { width: 28px; height: 28px; min-height: 28px; flex-basis: 28px; border-radius: 6px; }
  .graph-toolbar .btn-small { min-height: 28px; padding: 5px 7px; font-size: 9px; }
  .graph-toolbar h2 { font-size: 14px; }
  .graph-panel > .legend { padding-inline: 14px; gap: 5px 11px; font-size: 9px; }
  .graph-stage { min-height: 0; aspect-ratio: 820 / 460; }
  .graph-tip { margin-inline: 14px; }
  .coordinate-row > * { flex-direction: column; gap: 1px; font-size: 9px; }
  .metric-grid { gap: 7px; }
  .metric { border-radius: 10px; padding: 13px 9px 12px; }
  .metric-label { font-size: 9px; }
  .metric-number { font-size: 21px; letter-spacing: -.7px; overflow-wrap: anywhere; }
  .metric-formula { font-size: 8px; letter-spacing: -.1px; }
  .insight-panel { padding: 16px; }
  .limit-values { gap: 9px; flex-wrap: wrap; }
  .limit-values > span:first-child { flex-basis: 100%; }
  .limit-values > * { flex-wrap: wrap; gap: 0 5px; font-size: 9px; }
  .limit-values strong { font-size: 11px; }
  .section-header { gap: 8px; }
  .section-header h2 { font-size: 16px; }
  .section-header p { font-size: 10px; }
  .section-header .btn-small { font-size: 10px; padding-inline: 8px; }
  .convergence-panel, .data-panel, .notes-grid > .panel { padding: 18px 16px; }
  table { font-size: 10px; }
  td, th { padding: 9px 10px; }
  .theory-strip { padding: 18px; }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
}

@media print {
  :root { --ink: #111; --muted: #555; --shadow: none; }
  body, .page { background: #fff; }
  .page { width: 100%; padding: 12px 0; }
  .topbar { padding: 8px 0; min-height: 0; border-bottom: 1px solid #bbb; }
  .topbar .actions, .header-actions, .topbar-actions, .controls, .control-panel, .graph-toolbar .actions, .graph-actions, .section-header .btn, .note-actions, .footer, footer { display: none !important; }
  .workspace, .below-grid, .notes-grid { grid-template-columns: 1fr; }
  .hero { margin-bottom: 15px; }
  .hero h1 { font-size: 25px; }
  .hero-copy, .hero-step-row { margin-top: 7px; }
  .panel, .metric, .insight-panel, .theory-strip { box-shadow: none; break-inside: avoid; }
  .graph-stage { min-height: 0; aspect-ratio: 820 / 460; }
  .data-scroll { max-height: none; overflow: visible; }
  th { position: static; }
  .notes-grid > .panel { break-inside: avoid; }
  .note-area { border-color: #aaa; }
}

/* Keep the two branches explicit; the slash would suggest division. */
.function-formula.piecewise-formula { display: flex; flex-direction: column; align-items: center; gap: 1px; font-size: 21px; line-height: 1.1; }
.piecewise-formula > span { white-space: nowrap; }
.piecewise-formula small { font-family: inherit; font-size: 11px; font-weight: 450; }

</style>
</head>
<body>
  <header class="topbar">
    <a class="brand" href="#main" aria-label="기울기 실험실 처음으로">
      <span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 32 32" width="29" height="29"><path d="M5 25V7M5 25H27" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".45"/><path d="M8 23C13 24 16 19 18 14S22 6 27 6" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/><path d="M9 25L25 7" stroke="currentColor" stroke-width="1.4" opacity=".55"/><circle cx="17" cy="16" r="3" fill="currentColor"/></svg></span>
      <span><span class="brand-title">기울기 실험실</span><span class="brand-sub">SECANT LAB</span></span>
    </a>
    <div class="topbar-actions"><span class="project-label">미적분 · 탐구 도구</span><a class="btn btn-quiet btn-small" href="#explore">탐구 가이드 <span aria-hidden="true">↗</span></a></div>
  </header>

  <main class="page" id="main">
    <section class="hero" aria-labelledby="page-title">
      <div class="eyebrow"><span></span> 대칭 할선의 기울기와 극한 탐구</div>
      <h1 id="page-title">기울기가 모이면,<br class="mobile-break"> 미분할 수 있을까?</h1>
      <p class="hero-copy">점을 직접 움직이고, 두 점 사이를 좁혀 보세요.<br class="mobile-break"> 그래프와 세 기울기를 함께 보면 새로운 질문이 보입니다.</p>
      <div class="hero-step-row" aria-label="탐구 순서"><span class="step"><b>01</b> 함수 고르기</span><span class="step-arrow" aria-hidden="true">→</span><span class="step"><b>02</b> 점 움직이기</span><span class="step-arrow" aria-hidden="true">→</span><span class="step"><b>03</b> 극한 비교하기</span></div>
    </section>

    <div class="workspace">
      <aside class="panel control-panel" aria-label="실험 설정">
        <div class="panel-heading"><span class="section-kicker">실험 설정</span><button id="reset" class="btn btn-quiet btn-small" type="button">↺ 처음으로</button></div>
        <h2 class="control-title">어떤 함수를 살펴볼까요?</h2>
        <div class="function-grid" role="group" aria-label="함수 선택">
          <button class="function-card active" data-function="quadratic" aria-pressed="true" type="button"><span class="function-formula">x²</span><span class="function-name">이차함수</span></button>
          <button class="function-card" data-function="cubic" aria-pressed="false" type="button"><span class="function-formula">x³</span><span class="function-name">삼차함수</span></button>
          <button class="function-card" data-function="absolute" aria-pressed="false" type="button"><span class="function-formula">|x|</span><span class="function-name">절댓값 함수</span></button>
          <button class="function-card" data-function="piecewise" aria-pressed="false" type="button"><span class="function-formula piecewise-formula"><span>x <small>(x &lt; 0)</small></span><span>x² <small>(x ≥ 0)</small></span></span><span class="function-name">구간별 함수</span></button>
        </div>
        <p class="tiny-note" id="function-detail">모든 실수에서 f(x) = x²</p>

        <div class="control-section">
          <label class="field-row" for="a-input"><span class="field-label">기준점 <i>a</i><small>가운데 점 A의 x좌표</small></span><input class="number-input" type="number" id="a-input" min="-3" max="3" step="0.01" value="1" inputmode="decimal"></label>
          <button id="a-zero" class="btn btn-quiet btn-small" type="button">기준점을 원점으로</button>
          <label class="field-row h-field" for="h-input"><span class="field-label">거리 <i>h</i><small>A에서 양쪽 점까지의 가로 거리</small></span><input class="number-input" type="number" id="h-input" min="0.000001" max="2" step="any" value="1" inputmode="decimal"></label>
          <div class="button-row"><button id="halve" class="btn btn-secondary btn-small" type="button">h ÷ 2</button><button id="double" class="btn btn-secondary btn-small" type="button">h × 2</button></div>
          <button id="animate" class="btn btn-primary full-width" type="button" aria-pressed="false"><span aria-hidden="true">▶</span> h → 0 자동 관찰</button>
          <p class="tiny-note">h는 0이 되지 않아요. 최소 0.000001까지 줄일 수 있어요.</p>
        </div>

        <div class="control-section selected-point">
          <label class="field-label" id="point-selector-label">움직일 점 선택</label>
          <div class="segmented" role="group" aria-labelledby="point-selector-label">
            <button type="button" data-point="left" aria-pressed="false"><span class="dot left-green"></span> L</button>
            <button type="button" data-point="center" aria-pressed="true"><span class="dot center-navy"></span> A</button>
            <button type="button" data-point="right" aria-pressed="false"><span class="dot right-coral"></span> R</button>
          </div>
          <p class="tiny-note">점이 겹치면 여기에서 골라 주세요.<br>선택한 점은 방향키 ← →로도 움직여요.</p>
        </div>
        <div class="control-section">
          <label class="toggle-row"><input type="checkbox" id="show-sides" checked><span>왼쪽·오른쪽 할선 함께 보기</span></label>
          <label class="toggle-row"><input type="checkbox" id="show-tangent"><span>실제 접선 보기</span></label>
          <p class="tiny-note" id="tangent-note">접선은 기준점 A를 지나며, 기울기는 f′(a)입니다.</p>
        </div>
        <button class="counterexample-banner" id="counterexample" type="button"><span>꼭 해 볼 실험</span><strong>|x|의 원점에서는 어떨까? <span aria-hidden="true">→</span></strong></button>
        <p id="input-status" class="status-message" role="status" aria-live="polite"></p>
      </aside>

      <div class="main-column">
        <section class="panel graph-panel" aria-labelledby="graph-title">
          <div class="graph-toolbar"><div><div class="section-kicker">직접 움직이는 그래프</div><h2 id="graph-title">f(x) = x²</h2></div><div class="graph-actions"><button id="zoom-in" class="btn btn-icon" type="button" aria-label="그래프 확대" title="확대">＋</button><button id="zoom-out" class="btn btn-icon" type="button" aria-label="그래프 축소" title="축소">−</button><button id="fit" class="btn btn-quiet btn-small" type="button">화면 맞춤</button><button id="download-svg" class="btn btn-quiet btn-small" type="button" title="현재 그래프 SVG 다운로드">그림 저장 <span aria-hidden="true">↓</span></button></div></div>
          <div class="legend" aria-label="그래프 범례"><span class="legend-item"><span class="swatch curve-blue"></span>함수</span><span class="legend-item"><span class="swatch symmetric-purple"></span>대칭 할선</span><span class="legend-item" id="side-legend-left"><span class="swatch left-green dashed"></span>왼쪽 할선</span><span class="legend-item" id="side-legend-right"><span class="swatch right-coral dashed"></span>오른쪽 할선</span><span class="legend-item" id="tangent-legend" hidden><span class="swatch center-navy dashed"></span>접선</span></div>
          <div class="graph-stage">
            <svg id="main-graph" viewBox="0 0 820 460" aria-labelledby="graph-svg-title graph-svg-desc">
              <title id="graph-svg-title">함수와 대칭 할선 그래프</title>
              <desc id="graph-svg-desc">점 A를 좌우로 끌면 기준점이 바뀝니다. 점 L 또는 R을 끌면 거리 h가 바뀌며 반대편 점도 대칭으로 움직입니다.</desc>
              <defs><clipPath id="plot-clip"><rect x="61" y="21" width="736" height="386"/></clipPath></defs>
              <rect x="0" y="0" width="820" height="460" fill="#ffffff"/>
              <g id="grid-layer"></g>
              <g id="plot-layer" clip-path="url(#plot-clip)"><path id="curve" class="curve-path"/><path id="tangent" class="tangent-path"/><path id="left-secant" class="left-path"/><path id="right-secant" class="right-path"/><path id="symmetric-secant" class="secant-path"/><g id="guides-layer"></g></g>
              <g id="labels-layer"></g>
              <g id="points-layer">
                <g id="point-left" class="graph-point" data-point="left" tabindex="0" role="slider" aria-label="왼쪽 점 L: 거리 h 조절" aria-orientation="horizontal" style="--point-color:#119773"><circle class="point-hit" r="21"/><circle class="point-halo" r="13"/><circle class="point-core" r="7"/><text class="point-label" x="-15" y="-17">L</text></g>
                <g id="point-right" class="graph-point" data-point="right" tabindex="0" role="slider" aria-label="오른쪽 점 R: 거리 h 조절" aria-orientation="horizontal" style="--point-color:#e46b52"><circle class="point-hit" r="21"/><circle class="point-halo" r="13"/><circle class="point-core" r="7"/><text class="point-label" x="10" y="-17">R</text></g>
                <g id="point-center" class="graph-point selected" data-point="center" tabindex="0" role="slider" aria-label="기준점 A: 기준점 a 조절" aria-orientation="horizontal" style="--point-color:#172d4b"><circle class="point-hit" r="21"/><circle class="point-halo" r="14"/><circle class="point-core" r="8"/><text class="point-label" x="10" y="22">A</text></g>
              </g>
            </svg>
          </div>
          <div class="graph-tip"><span aria-hidden="true">↔</span><span id="drag-tip"><strong>점을 잡고 좌우로 끌어 보세요.</strong> A는 기준점, L·R은 거리 h를 바꿉니다.</span></div>
          <div class="coordinate-row"><span class="coordinate-chip"><i class="dot left-green"></i><b>L</b> <span id="left-coord">(0, 0)</span></span><span class="coordinate-chip"><i class="dot center-navy"></i><b>A</b> <span id="center-coord">(1, 1)</span></span><span class="coordinate-chip"><i class="dot right-coral"></i><b>R</b> <span id="right-coord">(2, 4)</span></span></div>
        </section>

        <section aria-labelledby="slopes-title">
          <div class="metrics-heading"><h2 id="slopes-title">지금의 세 기울기</h2><span>현재 거리 h에서 계산한 평균변화율</span></div>
          <div class="metric-grid">
            <div class="metric metric-left"><div class="metric-label"><span class="dot left-green"></span>왼쪽 할선</div><div class="metric-number" id="left-value">1.000000</div><div class="metric-formula">L<sub>h</sub> = [f(a) − f(a−h)] / h</div></div>
            <div class="metric metric-right"><div class="metric-label"><span class="dot right-coral"></span>오른쪽 할선</div><div class="metric-number" id="right-value">3.000000</div><div class="metric-formula">R<sub>h</sub> = [f(a+h) − f(a)] / h</div></div>
            <div class="metric metric-symmetric"><div class="metric-label"><span class="dot symmetric-purple"></span>대칭 할선</div><div class="metric-number" id="symmetric-value">2.000000</div><div class="metric-formula">S<sub>h</sub> = [f(a+h) − f(a−h)] / (2h)</div></div>
          </div>
        </section>

        <section class="insight-panel" id="insight-panel" aria-labelledby="insight-title">
          <div class="insight-status"><h2 id="insight-title">이 지점에서는 미분할 수 있어요</h2><span class="status-pill" id="derivative-status" data-kind="success">미분 가능</span></div>
          <p class="insight-body" id="insight-copy"></p>
          <div class="limit-values"><span>h → 0⁺일 때</span><span>왼쪽 <b id="left-limit">2</b></span><span>오른쪽 <b id="right-limit">2</b></span><span>대칭 <b id="symmetric-limit">2</b></span><span>f′(a) <b id="derivative-value">2</b></span></div>
          <p class="tiny-note">미분가능성은 알려진 함수의 수학적 성질로 판단합니다. 지금 보이는 숫자 몇 개가 비슷하다는 것만으로 판단하지 않아요.</p>
        </section>
      </div>
    </div>

    <section id="convergence" class="below-grid" aria-label="거리 h를 줄이는 실험">
      <div class="panel convergence-panel">
        <div class="section-header"><div><div class="section-kicker">한 걸음 더</div><h2>h를 줄이면 어디로 모일까요?</h2></div><span class="mini-badge">h → h / 2¹⁰</span></div>
        <p class="section-description">현재 h에서 시작해 10번 절반으로 줄였습니다. 오른쪽으로 갈수록 h가 작아집니다.</p>
        <svg id="convergence-graph" viewBox="0 0 820 285" role="img" aria-labelledby="convergence-title convergence-desc"><title id="convergence-title">거리를 절반씩 줄일 때 세 기울기의 변화</title><desc id="convergence-desc">가로축은 h를 절반으로 줄인 횟수, 세로축은 기울기입니다.</desc><g id="convergence-grid"></g><g id="convergence-lines"></g><g id="convergence-labels"></g></svg>
        <div class="legend compact"><span class="legend-item"><span class="swatch left-green"></span>왼쪽</span><span class="legend-item"><span class="swatch right-coral"></span>오른쪽</span><span class="legend-item"><span class="swatch symmetric-purple"></span>대칭</span></div>
      </div>
      <div class="panel data-panel">
        <div class="section-header"><div><div class="section-kicker">계산 기록</div><h2>숫자로 확인하기</h2></div><button id="download-csv" class="btn btn-quiet btn-small" type="button">CSV 저장 ↓</button></div>
        <div class="data-scroll" tabindex="0" aria-label="기울기 변화 표"><table><caption class="sr-only">현재 함수와 기준점에서 거리를 절반으로 줄이는 기울기 계산</caption><thead><tr><th scope="col">h</th><th scope="col" class="text-left-green">왼쪽</th><th scope="col" class="text-right-coral">오른쪽</th><th scope="col" class="text-symmetric-purple">대칭</th></tr></thead><tbody id="data-body"></tbody></table></div>
        <p class="tiny-note" id="table-note">원래 값은 CSV에 더 높은 정밀도로 저장됩니다.</p>
      </div>
    </section>

    <section class="theory-strip" aria-labelledby="relation-title">
      <div><span class="section-kicker">세 기울기를 연결하는 식</span><h2 id="relation-title">대칭 기울기는 좌우 기울기의 평균이에요.</h2></div>
      <div class="theory-formula">S<sub>h</sub> <span>=</span> <span class="fraction"><span>L<sub>h</sub> + R<sub>h</sub></span><span>2</span></span></div>
      <p>평균이 한 값으로 모여도 두 값이 같은 곳으로 모인다는 뜻은 아닙니다.<br>미분가능하려면 왼쪽과 오른쪽 기울기의 극한이 <strong>같은 유한한 값</strong>이어야 해요.</p>
    </section>

    <section class="notes-grid" id="explore" aria-label="탐구 가이드와 관찰 메모">
      <div class="panel question-panel"><div class="section-header"><div><div class="section-kicker">관찰에서 설명으로</div><h2>이 질문을 따라가 보세요</h2></div></div>
        <div class="question-list">
          <details><summary>x²에서는 왜 대칭 기울기가 바뀌지 않을까요?</summary><p>(a+h)² − (a−h)² = 4ah이므로 S<sub>h</sub> = 2a입니다. h가 양수인 동안 항상 같은 값이에요. 하지만 할선 자체는 보통 A를 지나지 않으며, h를 줄이면 접선에 가까워집니다.</p></details>
          <details><summary>x³에서 h를 절반으로 줄이면 오차는 어떻게 될까요?</summary><p>S<sub>h</sub> = 3a² + h²이고 f′(a) = 3a²입니다. 둘의 차이는 h²이므로 h를 절반으로 줄이면 차이는 1/4이 됩니다.</p></details>
          <details><summary>|x|의 원점에서 대칭 기울기 0은 미분계수일까요?</summary><p>아니에요. a=0이면 왼쪽 기울기는 −1, 오른쪽 기울기는 1이고, 평균인 대칭 기울기만 0입니다. 좌우 극한이 다르므로 미분계수는 없어요. 실제 대칭 할선은 y=h입니다.</p></details>
          <details><summary>구간별 함수의 원점에서는 무엇이 다를까요?</summary><p>f(x)=x (x&lt;0), f(x)=x² (x≥0)에서 a=0이면 왼쪽 기울기는 1, 오른쪽 기울기는 h, 대칭 기울기는 (1+h)/2입니다. 대칭 기울기는 0.5로 모이지만 좌우 극한은 1과 0이므로 미분 불가능합니다.</p></details>
        </div>
      </div>
      <div class="panel note-panel"><div class="section-header"><div><div class="section-kicker">나의 발견</div><h2>관찰한 것을 남겨 보세요</h2></div><button class="btn btn-quiet btn-small" id="save-note" type="button">메모 저장</button></div>
        <label for="experiment-note" class="note-label">어떤 함수를, 어떤 기준점에서 관찰했나요? 좌우 기울기와 대칭 기울기를 비교해 보세요.</label>
        <textarea class="note-area" id="experiment-note" rows="7" maxlength="8000" placeholder="예: |x|의 원점에서 h를 줄여도 왼쪽은 −1, 오른쪽은 1이었다. 대칭 기울기만 보고 판단하면…"></textarea>
        <p class="tiny-note" id="note-status" role="status">저장한 메모는 이 브라우저에만 남아요.</p>
      </div>
    </section>

    <footer class="footer"><span>기울기 실험실 <span aria-hidden="true">·</span> 대칭 할선과 극한 탐구</span><span>그래프는 관찰의 도구, 결론은 수학적 설명으로.</span></footer>
    <p class="sr-only" id="announcement" aria-live="polite"></p>
    <noscript><p class="notice">그래프를 움직이려면 브라우저에서 JavaScript를 허용해 주세요.</p></noscript>
  </main>
  <script>
/* Pure mathematics shared by the browser lab and its Node.js checks. */
(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.MathLab = factory();
  }
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  const FUNCTIONS = Object.freeze({
    quadratic: Object.freeze({ name: "이차함수", formula: "f(x) = x²" }),
    cubic: Object.freeze({ name: "삼차함수", formula: "f(x) = x³" }),
    absolute: Object.freeze({ name: "절댓값 함수", formula: "f(x) = |x|" }),
    piecewise: Object.freeze({
      name: "구간별 함수",
      formula: "f(x) = x (x < 0), x² (x ≥ 0)"
    })
  });

  // These limits belong to the controls. Calculations may use smaller h
  // values, for example when making a table of h, h/2, ..., h/1024.
  const MIN_H = 1e-6;
  const MAX_H = 2;
  const A_MIN = -3;
  const A_MAX = 3;

  function requireFunction(id) {
    if (typeof id !== "string") {
      throw new TypeError("Function id must be a string.");
    }
    if (!Object.prototype.hasOwnProperty.call(FUNCTIONS, id)) {
      throw new RangeError("Unknown function id: " + id);
    }
  }

  function requireFinite(value, label) {
    if (typeof value !== "number") {
      throw new TypeError(label + " must be a number.");
    }
    if (!Number.isFinite(value)) {
      throw new RangeError(label + " must be finite.");
    }
    // Avoid displaying a mathematical zero as -0 in the interface.
    return value === 0 ? 0 : value;
  }

  function evaluate(id, x) {
    requireFunction(id);
    x = requireFinite(x, "x");
    let value;
    switch (id) {
      case "quadratic":
        value = x * x;
        break;
      case "cubic":
        value = x * x * x;
        break;
      case "absolute":
        value = Math.abs(x);
        break;
      case "piecewise":
        value = x < 0 ? x : x * x;
        break;
    }
    return requireFinite(value, "f(x)");
  }

  function calculate(id, a, h) {
    requireFunction(id);
    a = requireFinite(a, "a");
    h = requireFinite(h, "h");
    if (h <= 0) {
      throw new RangeError("h must be greater than zero.");
    }

    const leftX = requireFinite(a - h, "a - h");
    const rightX = requireFinite(a + h, "a + h");
    const leftY = evaluate(id, leftX);
    const centerY = evaluate(id, a);
    const rightY = evaluate(id, rightX);
    let left;
    let right;

    // Algebraically simplified divided differences avoid subtracting nearly
    // equal function values. The returned endpoints remain the actual
    // function points; a symmetric secant need not pass through (a, f(a)).
    switch (id) {
      case "quadratic":
        left = 2 * a - h;
        right = 2 * a + h;
        break;
      case "cubic": {
        const common = 3 * a * a + h * h;
        const offset = 3 * a * h;
        left = common - offset;
        right = common + offset;
        break;
      }
      case "absolute":
        left = a <= 0 ? -1 : leftX >= 0 ? 1 : 2 * (a / h) - 1;
        right = a >= 0 ? 1 : rightX <= 0 ? -1 : 2 * (a / h) + 1;
        break;
      case "piecewise":
        // A crossing interval is a weighted combination of its negative
        // linear segment and its nonnegative quadratic segment.
        left = a <= 0 ? 1 : leftX >= 0
          ? 2 * a - h
          : (-leftX / h) + a * (a / h);
        right = a >= 0 ? 2 * a + h : rightX <= 0
          ? 1
          : (-a / h) + rightX * (rightX / h);
        break;
    }

    left = requireFinite(left, "Left slope");
    right = requireFinite(right, "Right slope");
    const symmetric = requireFinite((left + right) / 2, "Symmetric slope");
    return { a, h, leftX, rightX, leftY, centerY, rightY, left, right, symmetric };
  }

  function sharedLimit(derivative, explanation) {
    derivative = requireFinite(derivative, "Derivative");
    return {
      differentiable: true,
      derivative,
      leftLimit: derivative,
      rightLimit: derivative,
      symmetricLimit: derivative,
      explanation
    };
  }

  function analyze(id, a) {
    requireFunction(id);
    a = requireFinite(a, "a");
    switch (id) {
      case "quadratic":
        return sharedLimit(2 * a,
          "이차함수는 모든 실수에서 미분가능합니다. 왼쪽과 오른쪽 기울기의 극한이 모두 2a이므로, 대칭 할선의 극한도 미분계수 2a와 같습니다.");
      case "cubic":
        return sharedLimit(3 * a * a,
          "삼차함수는 모든 실수에서 미분가능합니다. 대칭 할선의 기울기 3a² + h²는 h가 0에 가까워지면 미분계수 3a²에 수렴합니다.");
      case "absolute":
        // This is an exact mathematical branch, not a numerical tolerance.
        // A tiny nonzero a is still a differentiable point of this function.
        if (a === 0) {
          return {
            differentiable: false,
            derivative: null,
            leftLimit: -1,
            rightLimit: 1,
            symmetricLimit: 0,
            explanation: "대칭 할선의 기울기는 0으로 일정하지만, 왼쪽 기울기의 극한은 −1, 오른쪽 기울기의 극한은 1로 서로 다릅니다. 따라서 a = 0에서 미분가능하지 않습니다."
          };
        }
        return a < 0
          ? sharedLimit(-1, "a < 0에서는 원점에 닿지 않을 만큼 h를 줄이면 양쪽 기울기가 모두 −1입니다. 따라서 이 점의 미분계수는 −1입니다.")
          : sharedLimit(1, "a > 0에서는 원점에 닿지 않을 만큼 h를 줄이면 양쪽 기울기가 모두 1입니다. 따라서 이 점의 미분계수는 1입니다.");
      case "piecewise":
        if (a === 0) {
          return {
            differentiable: false,
            derivative: null,
            leftLimit: 1,
            rightLimit: 0,
            symmetricLimit: 0.5,
            explanation: "대칭 할선의 기울기 (1 + h) / 2는 0.5에 수렴하지만, 왼쪽 기울기의 극한은 1, 오른쪽 기울기의 극한은 0입니다. 두 극한이 다르므로 a = 0에서 미분가능하지 않습니다."
          };
        }
        return a < 0
          ? sharedLimit(1, "a < 0의 주변에서는 f(x) = x이므로 왼쪽과 오른쪽 기울기의 극한은 모두 1입니다. 따라서 이 점의 미분계수는 1입니다.")
          : sharedLimit(2 * a, "a > 0의 주변에서는 f(x) = x²이므로 왼쪽과 오른쪽 기울기의 극한은 모두 2a입니다. 따라서 이 점의 미분계수는 2a입니다.");
    }
  }

  return Object.freeze({
    FUNCTIONS,
    MIN_H,
    MAX_H,
    A_MIN,
    A_MAX,
    evaluate,
    calculate,
    analyze
  });
});

</script>
  <script>
/* The interface runs entirely in the browser; the same assets are embedded in Streamlit. */
(() => {
  "use strict";
  const M = window.MathLab;
  const $ = (id) => document.getElementById(id);
  const NS = "http://www.w3.org/2000/svg";
  const COLORS = { left: "#119773", right: "#e46b52", symmetric: "#8254bd", center: "#172d4b" };
  const PLOT = { left: 61, right: 797, top: 21, bottom: 407 };
  const state = { fn: "quadratic", a: 1, h: 1, selected: "center", sides: true, tangent: false };
  let view;
  let rows = [];
  let dragging = null;
  let renderRequest = 0;
  let animationRequest = 0;
  let animationLast = null;
  let playing = false;
  let lastAnnouncement = "";
  const graph = $("main-graph");
  const pointNames = { left: "왼쪽 점 L", center: "기준점 A", right: "오른쪽 점 R" };
  const clamp = (x, low, high) => Math.min(high, Math.max(low, x));

  if (!M) {
    $("input-status").textContent = "계산 파일을 불러오지 못했어요. 페이지를 새로고침해 주세요.";
    return;
  }

  function format(value, digits = 6, fixed = false) {
    if (!Number.isFinite(value)) return "—";
    if (value === 0 || Object.is(value, -0)) return fixed ? (0).toFixed(digits) : "0";
    if (Math.abs(value) < 0.0001 || Math.abs(value) >= 1000000) {
      return value.toExponential(Math.min(digits, 4)).replace(/\.?(0+)(?=e)/, "").replace("e+", "e");
    }
    const rounded = value.toFixed(digits);
    return fixed ? rounded : String(Number(rounded));
  }

  function element(name, attrs = {}, text) {
    const node = document.createElementNS(NS, name);
    Object.entries(attrs).forEach(([key, val]) => node.setAttribute(key, String(val)));
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function say(text) {
    if (lastAnnouncement !== text) {
      $("announcement").textContent = text;
      lastAnnouncement = text;
    }
  }

  function announceSelection() {
    say(`${M.FUNCTIONS[state.fn].name}, 기준점 a는 ${format(state.a)}, 거리 h는 ${format(state.h)}입니다.`);
  }

  function syncInputs() {
    $("a-input").value = String(state.a);
    $("h-input").value = String(Number(state.h.toPrecision(10)));
  }

  function yRange(xMin, xMax) {
    const values = [];
    for (let i = 0; i <= 140; i++) values.push(M.evaluate(state.fn, xMin + (xMax - xMin) * i / 140));
    if (xMin <= 0 && xMax >= 0) values.push(M.evaluate(state.fn, 0));
    const result = M.calculate(state.fn, state.a, state.h);
    [result.leftX, state.a, result.rightX].forEach((x) => {
      if (x >= xMin && x <= xMax) values.push(M.evaluate(state.fn, x));
    });
    let min = Math.min(...values);
    let max = Math.max(...values);
    const span = Math.max(max - min, 0.000001);
    return { yMin: min - span * 0.13, yMax: max + span * 0.13 };
  }

  function fitView() {
    const radius = Math.max(1.8, state.h * 1.45);
    const xMin = state.a - radius;
    const xMax = state.a + radius;
    view = { xMin, xMax, ...yRange(xMin, xMax) };
  }

  function ensureVisible() {
    const r = M.calculate(state.fn, state.a, state.h);
    const xMargin = (view.xMax - view.xMin) * 0.035;
    const outside = r.leftX < view.xMin + xMargin || r.rightX > view.xMax - xMargin ||
      Math.min(r.leftY, r.centerY, r.rightY) < view.yMin || Math.max(r.leftY, r.centerY, r.rightY) > view.yMax;
    if (outside) {
      const radius = Math.max((view.xMax - view.xMin) / 2, state.h * 1.35, 0.00002);
      const xMin = state.a - radius;
      const xMax = state.a + radius;
      view = { xMin, xMax, ...yRange(xMin, xMax) };
    }
  }

  const sx = (x) => PLOT.left + (x - view.xMin) / (view.xMax - view.xMin) * (PLOT.right - PLOT.left);
  const sy = (y) => PLOT.bottom - (y - view.yMin) / (view.yMax - view.yMin) * (PLOT.bottom - PLOT.top);

  function niceStep(span, target = 7) {
    const base = Math.pow(10, Math.floor(Math.log10(span / target)));
    const fraction = span / target / base;
    return base * (fraction <= 1 ? 1 : fraction <= 2 ? 2 : fraction <= 5 ? 5 : 10);
  }

  function ticks(min, max, target) {
    const step = niceStep(max - min, target);
    const output = [];
    let first = Math.ceil(min / step - 1e-10);
    const last = Math.floor(max / step + 1e-10);
    for (let n = first; n <= last && output.length < 50; n++) output.push(n * step);
    return output;
  }

  function tickLabel(n) {
    return format(Math.abs(n) < 1e-12 ? 0 : n, 5);
  }

  function pathLine(x1, y1, x2, y2) {
    return `M${sx(x1).toFixed(3)},${sy(y1).toFixed(3)}L${sx(x2).toFixed(3)},${sy(y2).toFixed(3)}`;
  }

  function renderGrid() {
    const grid = $("grid-layer");
    const nodes = [];
    ticks(view.xMin, view.xMax, 8).forEach((x) => {
      const p = sx(x);
      nodes.push(element("line", { x1: p, y1: PLOT.top, x2: p, y2: PLOT.bottom, class: Math.abs(x) < 1e-12 ? "plot-axis" : "plot-grid" }));
      nodes.push(element("text", { x: p, y: PLOT.bottom + 19, "text-anchor": "middle", class: "axis-label" }, tickLabel(x)));
    });
    ticks(view.yMin, view.yMax, 6).forEach((y) => {
      const p = sy(y);
      nodes.push(element("line", { x1: PLOT.left, y1: p, x2: PLOT.right, y2: p, class: Math.abs(y) < 1e-12 ? "plot-axis" : "plot-grid" }));
      nodes.push(element("text", { x: PLOT.left - 10, y: p + 4, "text-anchor": "end", class: "axis-label" }, tickLabel(y)));
    });
    nodes.push(element("text", { x: PLOT.right + 11, y: PLOT.bottom + 19, class: "axis-label", "font-style": "italic" }, "x"));
    nodes.push(element("text", { x: PLOT.left - 13, y: PLOT.top - 7, class: "axis-label", "text-anchor": "end", "font-style": "italic" }, "f(x)"));
    grid.replaceChildren(...nodes);
  }

  function renderCurve() {
    const xs = [];
    for (let i = 0; i <= 420; i++) xs.push(view.xMin + (view.xMax - view.xMin) * i / 420);
    if (view.xMin < 0 && view.xMax > 0 && ["absolute", "piecewise"].includes(state.fn)) xs.push(0);
    xs.sort((a, b) => a - b);
    $("curve").setAttribute("d", xs.map((x, i) => `${i ? "L" : "M"}${sx(x).toFixed(3)},${sy(M.evaluate(state.fn, x)).toFixed(3)}`).join(""));
  }

  function renderMainGraph(r, analysis) {
    renderGrid();
    renderCurve();
    $("symmetric-secant").setAttribute("d", pathLine(r.leftX, r.leftY, r.rightX, r.rightY));
    $("left-secant").setAttribute("d", pathLine(r.leftX, r.leftY, state.a, r.centerY));
    $("right-secant").setAttribute("d", pathLine(state.a, r.centerY, r.rightX, r.rightY));
    $("left-secant").style.display = state.sides ? "" : "none";
    $("right-secant").style.display = state.sides ? "" : "none";
    const showTangent = state.tangent && analysis.differentiable;
    $("tangent").style.display = showTangent ? "" : "none";
    if (showTangent) {
      const f = (x) => r.centerY + analysis.derivative * (x - state.a);
      $("tangent").setAttribute("d", pathLine(view.xMin, f(view.xMin), view.xMax, f(view.xMax)));
    }
    $("tangent-legend").hidden = !showTangent;
    $("side-legend-left").hidden = !state.sides;
    $("side-legend-right").hidden = !state.sides;

    const guides = [];
    const points = { left: [r.leftX, r.leftY], center: [state.a, r.centerY], right: [r.rightX, r.rightY] };
    Object.entries(points).forEach(([which, [x, y]]) => {
      const group = $(`point-${which}`);
      group.setAttribute("transform", `translate(${sx(x)},${sy(y)})`);
      group.classList.toggle("selected", state.selected === which);
      group.setAttribute("aria-valuenow", String(x));
      group.setAttribute("aria-valuemin", String(which === "center" ? M.A_MIN : which === "left" ? state.a - M.MAX_H : state.a + M.MIN_H));
      group.setAttribute("aria-valuemax", String(which === "center" ? M.A_MAX : which === "left" ? state.a - M.MIN_H : state.a + M.MAX_H));
      group.setAttribute("aria-valuetext", `x ${format(x)}, y ${format(y)}${which !== "center" ? `, 거리 h ${format(state.h)}` : ""}`);
      guides.push(element("line", { x1: sx(x), y1: sy(y), x2: sx(x), y2: PLOT.bottom, class: "guide-line" }));
    });
    $("guides-layer").replaceChildren(...guides);
    const labels = [];
    const px = [sx(r.leftX), sx(state.a), sx(r.rightX)];
    if (px[0] >= PLOT.left && px[2] <= PLOT.right) {
      [[px[0], px[1]], [px[1], px[2]]].forEach(([start, end]) => {
        if (end - start > 18) {
          labels.push(element("path", { d: `M${start},437v5H${end}v-5`, fill: "none", stroke: "#b5c1cb", "stroke-width": "1" }));
          labels.push(element("text", { x: (start + end) / 2, y: 456, "text-anchor": "middle", class: "span-label" }, "h"));
        }
      });
    }
    $("labels-layer").replaceChildren(...labels);
    $("left-coord").textContent = `(${format(r.leftX)}, ${format(r.leftY)})`;
    $("center-coord").textContent = `(${format(state.a)}, ${format(r.centerY)})`;
    $("right-coord").textContent = `(${format(r.rightX)}, ${format(r.rightY)})`;
    $("graph-svg-title").textContent = `${M.FUNCTIONS[state.fn].formula}, a=${format(state.a)}, h=${format(state.h)}`;
    graph.dataset.function = state.fn;
    graph.dataset.a = String(state.a);
    graph.dataset.h = String(state.h);
  }

  function renderInsights(r, analysis) {
    $("left-value").textContent = format(r.left, 6, true);
    $("right-value").textContent = format(r.right, 6, true);
    $("symmetric-value").textContent = format(r.symmetric, 6, true);
    $("insight-title").textContent = analysis.differentiable ? "이 지점에서는 미분할 수 있어요" : "대칭 기울기가 모여도, 미분할 수 없어요";
    $("derivative-status").textContent = analysis.differentiable ? "미분 가능" : "미분 불가능";
    $("derivative-status").dataset.kind = analysis.differentiable ? "success" : "warning";
    $("insight-panel").dataset.kind = analysis.differentiable ? "success" : "warning";
    $("insight-copy").textContent = analysis.explanation;
    $("left-limit").textContent = format(analysis.leftLimit);
    $("right-limit").textContent = format(analysis.rightLimit);
    $("symmetric-limit").textContent = format(analysis.symmetricLimit);
    $("derivative-value").textContent = analysis.differentiable ? format(analysis.derivative) : "존재하지 않음";
    $("tangent-note").textContent = analysis.differentiable
      ? `접선은 A를 지나며 기울기는 f′(a) = ${format(analysis.derivative)}입니다.`
      : "이 기준점에는 미분계수가 없어 접선을 표시하지 않습니다.";
  }

  function renderConvergence() {
    rows = Array.from({ length: 11 }, (_, step) => ({ step, ...M.calculate(state.fn, state.a, state.h / 2 ** step) }));
    const bounds = { left: 60, right: 793, top: 19, bottom: 229 };
    const values = rows.flatMap((r) => [r.left, r.right, r.symmetric]);
    let low = Math.min(...values);
    let high = Math.max(...values);
    const spread = Math.max(high - low, Math.max(1, Math.abs(high)) * 0.08);
    low -= spread * 0.18;
    high += spread * 0.18;
    if (high - low < spread) {
      const center = (low + high) / 2;
      low = center - spread / 2;
      high = center + spread / 2;
    }
    const x = (step) => bounds.left + step / 10 * (bounds.right - bounds.left);
    const y = (value) => bounds.bottom - (value - low) / (high - low) * (bounds.bottom - bounds.top);
    const grids = [];
    ticks(low, high, 5).forEach((value) => {
      grids.push(element("line", { x1: bounds.left, y1: y(value), x2: bounds.right, y2: y(value), class: "plot-grid" }));
      grids.push(element("text", { x: bounds.left - 10, y: y(value) + 4, "text-anchor": "end", class: "axis-label" }, tickLabel(value)));
    });
    [0, 2, 4, 6, 8, 10].forEach((step) => {
      grids.push(element("text", { x: x(step), y: bounds.bottom + 21, "text-anchor": "middle", class: "axis-label" }, String(step)));
    });
    grids.push(element("text", { x: (bounds.left + bounds.right) / 2, y: 276, "text-anchor": "middle", class: "axis-label" }, "h를 절반으로 줄인 횟수  →"));
    grids.push(element("text", { x: bounds.left, y: 11, class: "axis-label" }, "기울기"));
    $("convergence-grid").replaceChildren(...grids);
    const lines = [];
    ["left", "right", "symmetric"].forEach((key) => {
      lines.push(element("path", { d: rows.map((r, i) => `${i ? "L" : "M"}${x(i)},${y(r[key])}`).join(""), fill: "none", stroke: COLORS[key], "stroke-width": key === "symmetric" ? 2.8 : 2.2, "stroke-dasharray": key === "left" ? "5 4" : "", class: `convergence-${key}` }));
      rows.forEach((r, i) => {
        const point = element("circle", { cx: x(i), cy: y(r[key]), r: key === "symmetric" ? 3.1 : 2.7, fill: COLORS[key], stroke: "white", "stroke-width": 1 });
        point.append(element("title", {}, `h=${format(r.h, 9)}, ${key === "left" ? "왼쪽" : key === "right" ? "오른쪽" : "대칭"}=${format(r[key], 9)}`));
        lines.push(point);
      });
    });
    $("convergence-lines").replaceChildren(...lines);
    $("convergence-desc").textContent = `${M.FUNCTIONS[state.fn].formula}, 기준점 ${format(state.a)}. h=${format(state.h)}부터 ${format(rows[10].h, 9)}까지 절반씩 줄인 세 기울기입니다. 자세한 값은 옆 표에서 확인할 수 있습니다.`;
    const tableRows = rows.map((r) => {
      const tr = document.createElement("tr");
      [r.h, r.left, r.right, r.symmetric].forEach((value, index) => {
        const td = document.createElement("td");
        td.textContent = format(value, index === 0 ? 7 : 6);
        td.title = String(value);
        tr.append(td);
      });
      return tr;
    });
    $("data-body").replaceChildren(...tableRows);
    $("table-note").textContent = `a = ${format(state.a)} 고정 · 11개 표본입니다. 더 정확한 값은 CSV로 저장하세요.`;
  }

  function render() {
    renderRequest = 0;
    const result = M.calculate(state.fn, state.a, state.h);
    const analysis = M.analyze(state.fn, state.a);
    renderMainGraph(result, analysis);
    renderInsights(result, analysis);
    renderConvergence();
    $("graph-title").textContent = M.FUNCTIONS[state.fn].formula;
    $("function-detail").textContent = state.fn === "piecewise"
      ? "x < 0이면 f(x) = x, x ≥ 0이면 f(x) = x²"
      : `모든 실수에서 ${M.FUNCTIONS[state.fn].formula}`;
    document.querySelectorAll("[data-function]").forEach((button) => {
      if (button.tagName !== "BUTTON") return;
      const active = button.dataset.function === state.fn;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", String(active));
    });
    document.querySelectorAll("button[data-point]").forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.point === state.selected)));
    $("halve").disabled = state.h <= M.MIN_H;
    $("double").disabled = state.h >= M.MAX_H;
    $("zoom-in").disabled = (view.xMax - view.xMin) / 2 <= Math.max(state.h * 1.1, 0.00002) * 1.001;
    $("zoom-out").disabled = (view.xMax - view.xMin) / 2 >= 16;
    syncInputs();
  }

  function scheduleRender() {
    if (!renderRequest) renderRequest = window.requestAnimationFrame(render);
  }

  function stopAnimation() {
    if (animationRequest) window.cancelAnimationFrame(animationRequest);
    animationRequest = 0;
    animationLast = null;
    playing = false;
    $("animate").textContent = "▶ h → 0 자동 관찰";
    $("animate").setAttribute("aria-pressed", "false");
  }

  function setSelected(which) {
    state.selected = which;
    const point = $(`point-${which}`);
    if ($( "points-layer").lastElementChild !== point) $("points-layer").append(point);
    scheduleRender();
  }

  function update({ a = state.a, h = state.h, fn = state.fn }, { fit = false, announce = true } = {}) {
    stopAnimation();
    state.a = clamp(a, M.A_MIN, M.A_MAX);
    state.h = clamp(h, M.MIN_H, M.MAX_H);
    state.fn = fn;
    if (fit) fitView(); else ensureVisible();
    render();
    if (announce) announceSelection();
  }

  function pointerX(event) {
    const matrix = graph.getScreenCTM();
    if (!matrix) return state.a;
    const point = new DOMPoint(event.clientX, event.clientY).matrixTransform(matrix.inverse());
    return view.xMin + (point.x - PLOT.left) / (PLOT.right - PLOT.left) * (view.xMax - view.xMin);
  }

  function movePoint(which, x, quantize = false) {
    if (which === "center") {
      state.a = clamp(quantize ? Math.round(x * 100) / 100 : x, M.A_MIN, M.A_MAX);
      if (Object.is(state.a, -0)) state.a = 0;
    } else {
      state.h = clamp(which === "left" ? state.a - x : x - state.a, M.MIN_H, M.MAX_H);
    }
    scheduleRender();
  }

  graph.addEventListener("pointerdown", (event) => {
    const target = event.target.closest(".graph-point");
    if (!target || event.button !== 0 || dragging) return;
    event.preventDefault();
    stopAnimation();
    const which = target.dataset.point;
    setSelected(which);
    dragging = { which, pointerId: event.pointerId };
    graph.classList.add("point-dragging");
    target.focus({ preventScroll: true });
    graph.setPointerCapture(event.pointerId);
    $("drag-tip").textContent = which === "center" ? "기준점 A를 옮기는 중 · a는 0.01 간격으로 움직여요." : `${pointNames[which]}을 옮기는 중 · 반대편 점도 같은 거리로 움직여요.`;
  });

  graph.addEventListener("pointermove", (event) => {
    if (!dragging || event.pointerId !== dragging.pointerId) return;
    movePoint(dragging.which, pointerX(event), dragging.which === "center");
  });

  function finishDrag(event) {
    if (!dragging || (event.pointerId !== undefined && event.pointerId !== dragging.pointerId)) return;
    const pointerId = dragging.pointerId;
    dragging = null;
    graph.classList.remove("point-dragging");
    if (graph.hasPointerCapture(pointerId)) graph.releasePointerCapture(pointerId);
    ensureVisible();
    render();
    $("drag-tip").textContent = "점을 잡고 좌우로 끌어 보세요. A는 기준점, L·R은 거리 h를 바꿉니다.";
    announceSelection();
  }
  graph.addEventListener("pointerup", finishDrag);
  graph.addEventListener("pointercancel", finishDrag);
  graph.addEventListener("lostpointercapture", finishDrag);

  function handlePointKey(event, which) {
    if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
    event.preventDefault();
    stopAnimation();
    setSelected(which);
    const direction = event.key === "ArrowLeft" ? -1 : 1;
    if (which === "center") {
      const next = event.key === "Home" ? M.A_MIN : event.key === "End" ? M.A_MAX : state.a + direction * (event.shiftKey ? 0.1 : 0.01);
      state.a = clamp(Math.round(next * 1e8) / 1e8, M.A_MIN, M.A_MAX);
    } else {
      if (event.key === "Home") state.h = which === "left" ? M.MAX_H : M.MIN_H;
      else if (event.key === "End") state.h = which === "left" ? M.MIN_H : M.MAX_H;
      else {
        const step = Math.max(M.MIN_H, Math.min(0.01, state.h / 10)) * (event.shiftKey ? 10 : 1);
        state.h = clamp(state.h + direction * (which === "left" ? -1 : 1) * step, M.MIN_H, M.MAX_H);
      }
    }
    ensureVisible();
    render();
    announceSelection();
  }
  document.querySelectorAll(".graph-point, button[data-point]").forEach((node) => {
    node.addEventListener("keydown", (event) => handlePointKey(event, node.dataset.point));
    if (node.tagName === "BUTTON") node.addEventListener("click", () => setSelected(node.dataset.point));
  });

  document.querySelectorAll("button[data-function]").forEach((button) => {
    button.addEventListener("click", () => update({ fn: button.dataset.function }, { fit: true }));
  });

  ["a", "h"].forEach((key) => {
    const input = $(`${key}-input`);
    input.addEventListener("focus", stopAnimation);
    const commit = () => {
      const value = input.valueAsNumber;
      if (!Number.isFinite(value)) {
        $("input-status").textContent = "숫자를 입력해 주세요. 마지막 값으로 돌아갔어요.";
        syncInputs();
        return;
      }
      const [minimum, maximum] = key === "a" ? [M.A_MIN, M.A_MAX] : [M.MIN_H, M.MAX_H];
      $("input-status").textContent = value < minimum || value > maximum ? `${key}는 ${minimum}부터 ${maximum}까지 조절할 수 있어요. 범위 안으로 맞췄어요.` : "";
      update({ [key]: clamp(value, minimum, maximum) });
    };
    input.addEventListener("change", commit);
    input.addEventListener("keydown", (event) => {
      if (event.key === "Enter") { event.preventDefault(); commit(); input.blur(); }
    });
  });

  $("a-zero").addEventListener("click", () => update({ a: 0 }, { fit: true }));
  $("halve").addEventListener("click", () => update({ h: state.h / 2 }));
  $("double").addEventListener("click", () => update({ h: state.h * 2 }));
  $("counterexample").addEventListener("click", () => {
    update({ fn: "absolute", a: 0, h: 1 }, { fit: true });
    say("절댓값 함수의 원점입니다. 왼쪽 기울기는 -1, 오른쪽 기울기는 1, 대칭 기울기는 0입니다. 미분계수는 존재하지 않습니다.");
  });
  $("reset").addEventListener("click", () => {
    state.sides = true;
    state.tangent = false;
    $("show-sides").checked = true;
    $("show-tangent").checked = false;
    $("input-status").textContent = "";
    setSelected("center");
    update({ fn: "quadratic", a: 1, h: 1 }, { fit: true });
  });
  $("show-sides").addEventListener("change", (event) => { state.sides = event.target.checked; render(); });
  $("show-tangent").addEventListener("change", (event) => { state.tangent = event.target.checked; render(); });

  function zoom(factor) {
    stopAnimation();
    const radius = clamp((view.xMax - view.xMin) / 2 * factor, Math.max(state.h * 1.1, 0.00002), 16);
    const xMin = state.a - radius;
    const xMax = state.a + radius;
    view = { xMin, xMax, ...yRange(xMin, xMax) };
    render();
  }
  $("zoom-in").addEventListener("click", () => zoom(0.72));
  $("zoom-out").addEventListener("click", () => zoom(1.4));
  $("fit").addEventListener("click", () => { fitView(); render(); });

  $("animate").addEventListener("click", () => {
    if (playing) { stopAnimation(); say("자동 관찰을 멈췄어요."); return; }
    if (state.h <= M.MIN_H * 1.01) state.h = 1;
    playing = true;
    animationLast = null;
    $("animate").textContent = "Ⅱ 자동 관찰 일시정지";
    $("animate").setAttribute("aria-pressed", "true");
    ensureVisible();
    const frame = (now) => {
      if (!playing) return;
      const dt = animationLast === null ? 0 : Math.min(100, now - animationLast);
      animationLast = now;
      state.h = Math.max(M.MIN_H, state.h * Math.exp(-dt / 1250));
      render();
      if (state.h <= M.MIN_H * (1 + 1e-8)) {
        state.h = M.MIN_H;
        stopAnimation();
        render();
        say("h가 0.000001에 도달했어요. 0에 대입한 값이 아니라, 0에 가까워지는 과정을 관찰한 것입니다.");
      } else animationRequest = window.requestAnimationFrame(frame);
    };
    animationRequest = window.requestAnimationFrame(frame);
  });
  document.addEventListener("visibilitychange", () => { if (document.hidden) stopAnimation(); });

  function download(blob, filename) {
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    link.style.display = "none";
    document.body.append(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 1500);
  }

  $("download-csv").addEventListener("click", () => {
    const quote = (value) => `"${String(value).replaceAll('"', '""')}"`;
    const header = ["함수", "기준점 a", "절반으로 줄인 횟수", "거리 h", "왼쪽 평균변화율", "오른쪽 평균변화율", "대칭 할선 기울기"];
    const records = rows.map((r) => [M.FUNCTIONS[state.fn].formula, state.a, r.step, r.h, r.left, r.right, r.symmetric]);
    const csv = "\uFEFF" + [header, ...records].map((row) => row.map(quote).join(",")).join("\r\n");
    download(new Blob([csv], { type: "text/csv;charset=utf-8" }), `secant-${state.fn}-a${format(state.a)}.csv`);
    say("현재 함수와 기준점의 기울기 변화 표를 CSV로 저장합니다.");
  });

  $("download-svg").addEventListener("click", () => {
    const svg = graph.cloneNode(true);
    svg.setAttribute("xmlns", NS);
    svg.setAttribute("width", "1230");
    svg.setAttribute("height", "690");
    svg.removeAttribute("data-function");
    svg.removeAttribute("data-a");
    svg.removeAttribute("data-h");
    const style = element("style", {}, ".plot-grid{stroke:#e7edf0;stroke-width:1}.plot-axis{stroke:#9daab7;stroke-width:1.2}.axis-label{fill:#697586;font:11px sans-serif}.curve-path{fill:none;stroke:#3477d6;stroke-width:3.4}.secant-path{fill:none;stroke:#8254bd;stroke-width:3}.left-path{fill:none;stroke:#119773;stroke-width:2;stroke-dasharray:5 4}.right-path{fill:none;stroke:#e46b52;stroke-width:2;stroke-dasharray:5 4}.tangent-path{fill:none;stroke:#172d4b;stroke-width:2;stroke-dasharray:7 5}.guide-line{stroke:#c7d1da;stroke-width:1;stroke-dasharray:3 5}.point-hit{fill:transparent}.point-halo{fill:white}.point-core{fill:var(--point-color);stroke:white;stroke-width:3}.point-label{fill:#24394e;font:bold 12px sans-serif;paint-order:stroke;stroke:white;stroke-width:5}.span-label{fill:#697586;font:italic 12px sans-serif}");
    svg.insertBefore(style, svg.firstChild);
    const serialized = new XMLSerializer().serializeToString(svg);
    download(new Blob([serialized], { type: "image/svg+xml;charset=utf-8" }), `secant-graph-${state.fn}.svg`);
    say("현재 그래프를 확대해도 선명한 SVG 그림으로 저장합니다.");
  });

  const noteKey = "secant-lab-observation-note-v1";
  try {
    const saved = window.localStorage.getItem(noteKey);
    if (saved !== null) {
      $("experiment-note").value = saved.slice(0, 8000);
      $("note-status").textContent = "이 브라우저에 저장했던 메모를 불러왔어요.";
    }
  } catch (_) {
    $("note-status").textContent = "이 브라우저에서는 저장 공간을 사용할 수 없어요. 메모를 따로 복사해 주세요.";
  }
  $("save-note").addEventListener("click", () => {
    try {
      window.localStorage.setItem(noteKey, $("experiment-note").value);
      $("note-status").textContent = "이 브라우저에 메모를 저장했어요.";
    } catch (_) {
      $("note-status").textContent = "메모를 저장하지 못했어요. 내용을 따로 복사해 주세요.";
    }
  });

  fitView();
  render();
})();

</script>
</body>
</html>
"""

if hasattr(st, "iframe"):
    st.iframe(HTML, height="content", alt="점을 직접 움직이는 대칭 할선과 미분계수 실험실")
else:
    # Compatibility with older Streamlit installations.
    import streamlit.components.v1 as components
    components.html(HTML, height=1800, scrolling=True)
