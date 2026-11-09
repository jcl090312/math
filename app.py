"""기울기 실험실: 대칭 할선의 기울기와 극한 탐구.

실행: python -m streamlit run app.py
HTML/CSS/JavaScript를 포함한 단일 파일이며 외부 차트 CDN을 사용하지 않습니다.
생성 원본: web/ 및 server/; 재생성: python tools/build_streamlit.py
"""
from __future__ import annotations
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
<script>window.SECANT_COMMENTS_MODE = "streamlit";</script>
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
button, a, input, textarea, select, summary { outline-offset: 4px; }
button:focus-visible, a:focus-visible, input:focus-visible, textarea:focus-visible, select:focus-visible, summary:focus-visible {
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
.main-column { display: flex; flex-direction: column; gap: 18px; container: experiment / inline-size; }
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
.auto-observe { display: grid; gap: 9px; margin-top: 19px; padding-top: 17px; border-top: 1px solid #e9edeb; }
.experiment-state { color: #405e68; font-size: 13px; font-weight: 650; line-height: 1.65; text-align: center; font-variant-numeric: tabular-nums; overflow-wrap: anywhere; }
.auto-play { min-height: 48px; padding: 12px 10px; font-size: 14px; font-weight: 750; letter-spacing: -.2px; }
.auto-observe .btn-secondary { min-height: 40px; }
.animation-status { min-height: 34px; color: #70877d; font-size: 11px; line-height: 1.6; text-align: center; word-break: keep-all; }
.animation-status:empty { min-height: 0; }
.manual-controls { margin-top: 15px; border: 1px solid #e1e8e3; border-radius: 10px; background: #fbfcfa; }
.manual-controls > summary { display: flex; align-items: center; gap: 8px; list-style: none; padding: 12px; color: #587064; font-size: 11px; font-weight: 650; cursor: pointer; line-height: 1.6; }
.manual-controls > summary::-webkit-details-marker { display: none; }
.manual-controls > summary::after { content: "⌄"; font-size: 15px; line-height: 1; color: #91a497; }
.manual-controls[open] > summary { border-bottom: 1px solid #e5ece6; }
.manual-controls[open] > summary::after { content: "⌃"; }
.manual-summary-hint { margin-left: auto; color: #94a198; font-size: 9px; font-weight: 400; }
.manual-controls-body { padding: 14px 12px; }
.manual-controls-body .field-row { gap: 9px; margin-bottom: 8px; }
.manual-controls-body .number-input { width: 104px; max-width: 48%; }
.manual-controls-body .field-label { font-size: 11px; }
.manual-controls-body .field-label small { font-size: 9px; }
.manual-controls-body > .btn { width: 100%; }
.manual-controls-body .h-field { margin-top: 16px; }
.manual-controls-body .tiny-note { margin-top: 11px; font-size: 10px; }

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
.tangent-status { margin: 0 24px 14px; padding: 8px 10px; border-radius: 7px; background: #f4f7fa; color: #5c7385; font-size: 11px; line-height: 1.7; word-break: keep-all; }
.tangent-status:empty { display: none; }
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
.tangent-path { fill: none; stroke: #263f5a; stroke-width: 2.4; stroke-dasharray: 8 5; opacity: .78; }
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
.metric { position: relative; min-width: 0; padding: 17px 18px 16px; border: 1px solid var(--line); border-radius: 13px; background: #fff; box-shadow: var(--shadow); container-type: inline-size; }
.metric::before { position: absolute; content: ""; left: 0; right: 0; top: 0; height: 3px; background: var(--metric-color, #c4d0d4); }
.metric-left { --metric-color: var(--green); }
.metric-right { --metric-color: var(--coral); }
.metric-symmetric { --metric-color: var(--purple); background: #fcfaff; }
.metric-label { display: flex; align-items: center; gap: 6px; color: #6f7e8a; font-size: 11px; font-weight: 600; }
.metric-number { display: block; margin-top: 11px; color: var(--metric-color, var(--ink)); font-size: 27px; font-weight: 740; line-height: 1.4; letter-spacing: -.5px; font-variant-numeric: tabular-nums; white-space: nowrap; overflow-wrap: normal; word-break: normal; }
.metric-number.is-long { font-family: ui-monospace, "SFMono-Regular", Consolas, "Liberation Mono", monospace; font-size: clamp(16px, 6.4cqi, 21px); font-weight: 650; letter-spacing: -.2px; }
.metric-formula { display: flex; align-items: center; gap: 7px; min-height: 61px; margin-top: 10px; color: var(--metric-color, var(--ink)); font-family: Georgia, "Times New Roman", serif; font-size: 19px; line-height: 1.5; white-space: nowrap; }
.math-symbol { font-size: 21px; font-weight: 600; }
.math-equals { opacity: .7; }
.metric-formula .metric-fraction { font-size: 17px; font-weight: 500; }
.metric-fraction > span { white-space: nowrap; }
.metric-formula .metric-fraction > span:first-child { padding: 0 3px 3px; border-bottom-color: currentColor; }
.metric-formula .metric-fraction > span:last-child { font-size: 18px; }
.metric-value-note { margin-top: 5px; color: #8b97a0; font-size: 10px; line-height: 1.7; word-break: keep-all; }
.metric-value-note:empty { display: none; }
.slope-relation { display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; gap: 7px 22px; margin-top: 13px; padding: 17px 20px; border: 1px solid #e4ddef; border-radius: 12px; background: #f8f5fc; }
.slope-relation h2, .slope-relation h3 { font-size: 14px; color: #665380; letter-spacing: -.4px; }
.slope-relation > .theory-formula { grid-column: 2; grid-row: 1 / span 2; color: #74549c; font-size: 25px; }
.slope-relation .fraction { font-size: 22px; }
.slope-relation .fraction > span:last-child { font-size: 21px; }
.slope-relation > p { color: #8d819e; font-size: 11px; line-height: 1.8; word-break: keep-all; }
.reading-guide { margin-top: 10px; padding: 11px 14px; border-left: 3px solid #d0dddb; background: #eff5f3; border-radius: 0 8px 8px 0; color: #657f75; font-size: 12px; line-height: 1.85; word-break: keep-all; }
.reading-guide:empty { display: none; }

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

/* Fraction notation is shared by the three cards and their relationship. */
.theory-formula { display: flex; align-items: center; gap: 10px; color: #74549c; font-family: Georgia, "Times New Roman", serif; font-size: 25px; font-weight: 600; letter-spacing: -.4px; line-height: 1.4; white-space: nowrap; }
.theory-formula > span:nth-child(2) { opacity: .65; }
.fraction { display: inline-flex; flex-direction: column; align-items: center; text-align: center; vertical-align: middle; font-size: 18px; line-height: 1.6; }
.fraction > span:first-child { padding: 0 6px 3px; border-bottom: 1px solid currentColor; }
.fraction > span:last-child { padding-top: 2px; font-size: 17px; }
.notes-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); align-items: start; gap: 22px; margin-top: 22px; }
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
.comment-board { container: comments / inline-size; }
.comment-board .section-header { align-items: center; margin-bottom: 12px; }
.comment-count { display: inline-flex; align-items: center; justify-content: center; min-width: 36px; min-height: 28px; padding: 4px 10px; border: 1px solid #d6e7df; border-radius: 99px; background: #edf7f2; color: var(--teal); font-size: 12px; font-weight: 750; line-height: 1.5; font-variant-numeric: tabular-nums; white-space: nowrap; }
.comment-storage { margin: 0 0 17px; padding: 9px 11px; border: 1px solid #e0eae4; border-radius: 8px; background: #f4f8f5; color: #748a7e; font-size: 11px; line-height: 1.75; word-break: keep-all; }
.comment-storage[data-mode="offline"] { border-color: #eadcbe; background: #fff8eb; color: #977438; }
.comment-form { margin: 0; }
.comment-fields { min-width: 0; margin: 0; padding: 0; border: 0; }
.comment-identity { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1.7fr); gap: 10px; }
.comment-field { display: flex; flex-direction: column; gap: 6px; min-width: 0; color: #566e63; font-size: 12px; font-weight: 650; line-height: 1.65; }
.comment-field input, .comment-field select { width: 100%; min-width: 0; min-height: 41px; padding: 9px 10px; border: 1px solid #dce5df; border-radius: 8px; background: #fff; color: #405b4e; font-size: 13px; font-weight: 450; line-height: 1.6; }
.comment-field select { padding-right: 5px; cursor: pointer; }
.comment-field input:hover:not(:disabled), .comment-field select:hover:not(:disabled), .comment-field textarea:hover:not(:disabled) { border-color: #b2c9bd; }
.comment-field input::placeholder, .comment-field textarea::placeholder { color: #9daaa2; font-weight: 400; }
.comment-field [aria-invalid="true"] { border-color: #c7856e; background: #fffaf7; }
.comment-field input:disabled, .comment-field select:disabled, .comment-field textarea:disabled { background: #f0f3f0; color: #9ba79f; cursor: not-allowed; opacity: .8; }
.comment-content-field { margin-top: 15px; }
.comment-content-field .note-area { margin-top: 0; min-height: 145px; padding: 11px 12px; background: #fbfcfa; color: #405b4e; font-size: 13px; font-weight: 400; line-height: 1.9; }
.comment-form-meta { display: flex; align-items: flex-start; gap: 10px; margin-top: 7px; color: #8d9b92; font-size: 10px; line-height: 1.75; }
.comment-form-meta #comment-length { flex: 0 0 auto; color: #7e9387; font-variant-numeric: tabular-nums; white-space: nowrap; }
.comment-public-note { flex: 1 1 auto; text-align: left; word-break: keep-all; }
.comment-form-actions { display: flex; align-items: center; gap: 11px; margin-top: 14px; }
.comment-form-actions .btn { flex: 0 0 auto; min-width: 86px; min-height: 40px; }
.comment-form-status { color: #598571; font-size: 11px; line-height: 1.75; word-break: keep-all; }
.comment-form-status:empty { display: none; }
.comment-form-status[data-kind="error"], .comment-list-status[data-kind="error"] { color: #ae644b; }
.comment-list-section { margin-top: 23px; padding-top: 19px; border-top: 1px solid #e1e9e4; }
.comment-list-toolbar { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 9px; }
.comment-list-toolbar > strong { color: #425f50; font-size: 13px; font-weight: 750; }
.comment-list-toolbar > strong small { margin-left: 5px; color: #99a79d; font-size: 10px; font-weight: 400; }
.comment-list-actions { display: flex; align-items: center; gap: 6px; }
.comment-list-actions .btn { min-height: 30px; padding: 6px 9px; font-size: 10px; }
.comment-list-status { margin-top: 9px; color: #84968a; font-size: 11px; line-height: 1.75; word-break: keep-all; }
.comment-list-status:empty { display: none; }
.comment-empty { margin-top: 13px; padding: 24px 17px; border: 1px dashed #d9e4dc; border-radius: 10px; background: #f9fbf8; color: #8a9b8f; font-size: 12px; line-height: 1.9; text-align: center; word-break: keep-all; }
.comment-empty strong { color: #768d7c; font-weight: 650; }
.comments-list { display: grid; gap: 11px; margin: 13px 0 0; padding: 0; list-style: none; }
.comment-card { min-width: 0; padding: 14px 15px 13px; border: 1px solid #e1e9e3; border-radius: 11px; background: #fcfdfb; }
.comment-card-header { display: flex; align-items: baseline; justify-content: space-between; flex-wrap: wrap; gap: 5px 12px; }
.comment-author { min-width: 0; max-width: 100%; color: #486755; font-size: 12px; font-weight: 750; line-height: 1.65; overflow-wrap: anywhere; }
.comment-time { flex: 0 1 auto; min-width: 0; max-width: 100%; color: #a0ada3; font-size: 10px; line-height: 1.65; font-variant-numeric: tabular-nums; white-space: normal; overflow-wrap: anywhere; }
.comment-content { margin-top: 9px; color: #54695e; font-size: 13px; line-height: 1.9; white-space: pre-wrap; overflow-wrap: anywhere; word-break: normal; }
.comment-context { display: flex; flex-wrap: wrap; gap: 5px; margin-top: 11px; }
.comment-context > span { max-width: 100%; padding: 3px 7px; border: 1px solid #e5ece6; border-radius: 5px; background: #f1f6f1; color: #829487; font-size: 10px; line-height: 1.6; font-variant-numeric: tabular-nums; overflow-wrap: anywhere; }
.comment-list-section > .full-width { margin-top: 13px; }
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
  .tangent-status { margin-inline: 18px; }
  .graph-stage { min-height: 0; }
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
  .insight-panel { padding: 19px; }
  .insight-status { font-size: 13px; }
  .insight-body { font-size: 12px; }
  .below-grid { margin-top: 18px; gap: 18px; }
  .convergence-panel, .data-panel { padding: 19px; }
  .notes-grid { grid-template-columns: 1fr; margin-top: 18px; gap: 18px; }
  .notes-grid > .panel { padding: 21px; }
  .comment-identity { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .comment-identity > .comment-field:last-child { grid-column: 1 / -1; }
  .comment-field input, .comment-field select, .comment-content-field .note-area { font-size: 14px; }
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
  .tangent-status { margin-inline: 14px; }
  .coordinate-row > * { flex-direction: column; gap: 1px; font-size: 9px; }
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
}

/* Use the graph column's actual width, including beside the desktop sidebar. */
@container experiment (max-width: 810px) {
  .metric-grid { grid-template-columns: 1fr; gap: 10px; }
  .metric { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); column-gap: 22px; row-gap: 3px; padding: 16px 20px; }
  .metric-label { grid-column: 1; grid-row: 1; }
  .metric-formula { grid-column: 1; grid-row: 2; min-height: 54px; margin-top: 3px; }
  .metric-number { grid-column: 2; grid-row: 1 / span 2; align-self: center; margin-top: 0; font-size: 27px; }
  .metric-number.is-long { font-size: clamp(16px, 3.5cqi, 20px); }
  .metric-value-note { grid-column: 2; grid-row: 3; margin-top: -7px; }
}

@container experiment (max-width: 560px) {
  .metric { display: block; padding: 17px 20px; }
  .metric-label { font-size: 12px; }
  .metric-formula { margin-top: 8px; font-size: 20px; }
  .metric-formula .metric-fraction { font-size: 19px; }
  .metric-number { margin-top: 7px; font-size: 28px; }
  .metric-number.is-long { font-size: clamp(16px, 6.4cqi, 21px); }
  .metric-value-note { margin-top: 5px; font-size: 11px; }
  .slope-relation { grid-template-columns: 1fr; gap: 10px; padding: 17px 19px; }
  .slope-relation > .theory-formula { grid-column: 1; grid-row: auto; font-size: 27px; }
  .slope-relation h3 { font-size: 14px; }
  .slope-relation > p { font-size: 11px; }
  .reading-guide { font-size: 12px; }
}

@supports not (container-type: inline-size) {
  .metric-grid { grid-template-columns: 1fr; }
  .metric-number.is-long { font-size: 18px; }
}

@container comments (max-width: 420px) {
  .comment-identity { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .comment-identity > .comment-field:last-child { grid-column: 1 / -1; }
  .comment-form-meta { flex-wrap: wrap; gap: 3px 10px; }
  .comment-public-note { flex: 1 1 100%; margin-left: 0; text-align: left; }
  .comment-form-actions { align-items: flex-start; }
  .comment-card { padding: 13px; }
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
  .comment-form, .comment-storage, .comment-list-actions, .comment-list-section > .full-width { display: none !important; }
  .workspace, .below-grid, .notes-grid { grid-template-columns: 1fr; }
  .hero { margin-bottom: 15px; }
  .hero h1 { font-size: 25px; }
  .hero-copy, .hero-step-row { margin-top: 7px; }
  .panel, .metric, .insight-panel, .slope-relation { box-shadow: none; break-inside: avoid; }
  .graph-stage { min-height: 0; aspect-ratio: 820 / 460; }
  .data-scroll { max-height: none; overflow: visible; }
  th { position: static; }
  .notes-grid > .panel { break-inside: avoid; }
  .comment-card { break-inside: avoid; }
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
      <h1 id="page-title">기울기가 수렴하면,<br class="mobile-break"> 미분할 수 있을까?</h1>
      <p class="hero-copy">함수를 고르고 자동 관찰을 눌러 보세요.<br class="mobile-break"> 점을 직접 움직이며 좌우 기울기와 대칭 기울기를 비교할 수도 있어요.</p>
      <div class="hero-step-row" aria-label="탐구 순서"><span class="step"><b>01</b> 함수 고르기</span><span class="step-arrow" aria-hidden="true">→</span><span class="step"><b>02</b> 자동 관찰</span><span class="step-arrow" aria-hidden="true">→</span><span class="step"><b>03</b> 극한 비교하기</span></div>
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

        <div class="auto-observe" aria-label="자동 관찰">
          <p class="experiment-state" id="experiment-state">a = 1 · h = 1</p>
          <button id="animate" class="btn btn-primary full-width auto-play" type="button" aria-pressed="false"><span aria-hidden="true">▶</span> h → 0 자동 관찰</button>
          <button id="animate-origin" class="btn btn-secondary full-width" type="button">원점에서 자동 관찰</button>
          <p class="animation-status" id="animation-status" role="status" aria-live="polite">h가 작아질 때 세 기울기를 비교해 보세요.</p>
        </div>

        <details class="manual-controls" id="manual-controls">
          <summary><span>숫자로 직접 조절하기</span><span class="manual-summary-hint">선택</span></summary>
          <div class="manual-controls-body">
            <label class="field-row" for="a-input"><span class="field-label">기준점 <i>a</i><small>가운데 점 A의 x좌표</small></span><input class="number-input" type="number" id="a-input" min="-3" max="3" step="0.01" value="1" inputmode="decimal"></label>
            <button id="a-zero" class="btn btn-quiet btn-small" type="button">기준점을 원점으로</button>
            <label class="field-row h-field" for="h-input"><span class="field-label">거리 <i>h</i><small>A에서 양쪽 점까지의 가로 거리</small></span><input class="number-input" type="number" id="h-input" min="0.000001" max="2" step="any" value="1" inputmode="decimal"></label>
            <div class="button-row"><button id="halve" class="btn btn-secondary btn-small" type="button">h ÷ 2</button><button id="double" class="btn btn-secondary btn-small" type="button">h × 2</button></div>
            <p class="tiny-note">h는 0보다 큰 값으로 조절해요.</p>
          </div>
        </details>

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
          <label class="toggle-row"><input type="checkbox" id="show-tangent" checked><span>실제 접선 보기</span></label>
          <p class="tiny-note" id="tangent-note">접선은 기준점 A를 지나며, 기울기는 f′(a)입니다.</p>
        </div>
        <button class="counterexample-banner" id="counterexample" type="button"><span>꼭 해 볼 실험</span><strong>|x|의 원점에서는 어떨까? <span aria-hidden="true">→</span></strong></button>
        <p id="input-status" class="status-message" role="status" aria-live="polite"></p>
      </aside>

      <div class="main-column">
        <section class="panel graph-panel" aria-labelledby="graph-title">
          <div class="graph-toolbar"><div><div class="section-kicker">직접 움직이는 그래프</div><h2 id="graph-title">f(x) = x²</h2></div><div class="graph-actions"><button id="zoom-in" class="btn btn-icon" type="button" aria-label="그래프 확대" title="확대">＋</button><button id="zoom-out" class="btn btn-icon" type="button" aria-label="그래프 축소" title="축소">−</button><button id="fit" class="btn btn-quiet btn-small" type="button">화면 맞춤</button><button id="download-svg" class="btn btn-quiet btn-small" type="button" title="현재 그래프 SVG 다운로드">그림 저장 <span aria-hidden="true">↓</span></button></div></div>
          <div class="legend" aria-label="그래프 범례"><span class="legend-item"><span class="swatch curve-blue"></span>함수</span><span class="legend-item"><span class="swatch symmetric-purple"></span>대칭 할선</span><span class="legend-item" id="side-legend-left"><span class="swatch left-green dashed"></span>왼쪽 할선</span><span class="legend-item" id="side-legend-right"><span class="swatch right-coral dashed"></span>오른쪽 할선</span><span class="legend-item" id="tangent-legend"><span class="swatch center-navy dashed"></span>접선</span></div>
          <div class="graph-stage">
            <svg id="main-graph" viewBox="0 0 820 460" aria-labelledby="graph-svg-title graph-svg-desc">
              <title id="graph-svg-title">함수와 대칭 할선 그래프</title>
              <desc id="graph-svg-desc">점 A를 좌우로 끌면 기준점이 바뀝니다. 점 L 또는 R을 끌면 거리 h가 바뀌며 반대편 점도 대칭으로 움직입니다.</desc>
              <defs><clipPath id="plot-clip"><rect x="61" y="21" width="736" height="386"/></clipPath></defs>
              <rect x="0" y="0" width="820" height="460" fill="#ffffff"/>
              <g id="grid-layer"></g>
              <g id="plot-layer" clip-path="url(#plot-clip)"><path id="curve" class="curve-path"/><path id="left-secant" class="left-path"/><path id="right-secant" class="right-path"/><path id="symmetric-secant" class="secant-path"/><path id="tangent" class="tangent-path"/><g id="guides-layer"></g></g>
              <g id="labels-layer"></g>
              <g id="points-layer">
                <g id="point-left" class="graph-point" data-point="left" tabindex="0" role="slider" aria-label="왼쪽 점 L: 거리 h 조절" aria-orientation="horizontal" style="--point-color:#119773"><circle class="point-hit" r="21"/><circle class="point-halo" r="13"/><circle class="point-core" r="7"/><text class="point-label" x="-15" y="-17">L</text></g>
                <g id="point-right" class="graph-point" data-point="right" tabindex="0" role="slider" aria-label="오른쪽 점 R: 거리 h 조절" aria-orientation="horizontal" style="--point-color:#e46b52"><circle class="point-hit" r="21"/><circle class="point-halo" r="13"/><circle class="point-core" r="7"/><text class="point-label" x="10" y="-17">R</text></g>
                <g id="point-center" class="graph-point selected" data-point="center" tabindex="0" role="slider" aria-label="기준점 A: 기준점 a 조절" aria-orientation="horizontal" style="--point-color:#172d4b"><circle class="point-hit" r="21"/><circle class="point-halo" r="14"/><circle class="point-core" r="8"/><text class="point-label" x="10" y="22">A</text></g>
              </g>
            </svg>
          </div>
          <div class="graph-tip"><span aria-hidden="true">↔</span><span id="drag-tip"><strong>점을 잡고 좌우로 끌어 보세요.</strong> A는 기준점, L·R은 거리 h를 바꿉니다.</span></div>
          <p class="tangent-status" id="tangent-status">짙은 점선은 A를 지나는 실제 접선입니다.</p>
          <div class="coordinate-row"><span class="coordinate-chip"><i class="dot left-green"></i><b>L</b> <span id="left-coord">(0, 0)</span></span><span class="coordinate-chip"><i class="dot center-navy"></i><b>A</b> <span id="center-coord">(1, 1)</span></span><span class="coordinate-chip"><i class="dot right-coral"></i><b>R</b> <span id="right-coord">(2, 4)</span></span></div>
        </section>

        <section aria-labelledby="slopes-title">
          <div class="metrics-heading"><h2 id="slopes-title">지금의 세 기울기</h2><span>h &gt; 0 · 현재 거리에서 계산한 평균변화율</span></div>
          <div class="metric-grid">
            <div class="metric metric-left">
              <div class="metric-label"><span class="dot left-green"></span>왼쪽 할선</div>
              <div class="metric-formula math-formula" role="math" aria-label="L h는 f(a)에서 f(a-h)를 뺀 값을 h로 나눈 값"><span class="math-symbol">L<sub>h</sub></span><span class="math-equals">=</span><span class="fraction metric-fraction"><span>f(a) − f(a−h)</span><span>h</span></span></div>
              <div class="metric-number" id="left-value">1.000000</div>
              <p class="metric-value-note" id="left-value-note"></p>
            </div>
            <div class="metric metric-right">
              <div class="metric-label"><span class="dot right-coral"></span>오른쪽 할선</div>
              <div class="metric-formula math-formula" role="math" aria-label="R h는 f(a+h)에서 f(a)를 뺀 값을 h로 나눈 값"><span class="math-symbol">R<sub>h</sub></span><span class="math-equals">=</span><span class="fraction metric-fraction"><span>f(a+h) − f(a)</span><span>h</span></span></div>
              <div class="metric-number" id="right-value">3.000000</div>
              <p class="metric-value-note" id="right-value-note"></p>
            </div>
            <div class="metric metric-symmetric">
              <div class="metric-label"><span class="dot symmetric-purple"></span>대칭 할선</div>
              <div class="metric-formula math-formula" role="math" aria-label="S h는 f(a+h)에서 f(a-h)를 뺀 값을 2h로 나눈 값"><span class="math-symbol">S<sub>h</sub></span><span class="math-equals">=</span><span class="fraction metric-fraction"><span>f(a+h) − f(a−h)</span><span>2h</span></span></div>
              <div class="metric-number" id="symmetric-value">2.000000</div>
              <p class="metric-value-note" id="symmetric-value-note"></p>
            </div>
          </div>
          <div class="slope-relation" aria-labelledby="relation-title">
            <h3 id="relation-title">대칭 기울기는 좌우 기울기의 평균</h3>
            <div class="theory-formula" role="math" aria-label="S h는 L h와 R h의 합을 2로 나눈 값"><span>S<sub>h</sub></span><span>=</span><span class="fraction"><span>L<sub>h</sub> + R<sub>h</sub></span><span>2</span></span></div>
            <p>평균의 수렴만으로 미분가능성을 판단할 수 없어요.</p>
          </div>
          <p class="reading-guide" id="reading-guide" role="status" aria-live="polite">h를 줄이며 왼쪽과 오른쪽 기울기가 같은 값으로 수렴하는지 확인해 보세요.</p>
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

    <section class="notes-grid" id="explore" aria-label="탐구 가이드와 관찰 게시판">
      <div class="panel question-panel"><div class="section-header"><div><div class="section-kicker">관찰에서 설명으로</div><h2>이 질문을 따라가 보세요</h2></div></div>
        <div class="question-list">
          <details><summary>x²에서는 왜 대칭 기울기가 바뀌지 않을까요?</summary><p>(a+h)² − (a−h)² = 4ah이므로 S<sub>h</sub> = 2a입니다. h가 양수인 동안 항상 같은 값이에요. 하지만 할선 자체는 보통 A를 지나지 않으며, h를 줄이면 접선에 가까워집니다.</p></details>
          <details><summary>x³에서 h를 절반으로 줄이면 오차는 어떻게 될까요?</summary><p>S<sub>h</sub> = 3a² + h²이고 f′(a) = 3a²입니다. 둘의 차이는 h²이므로 h를 절반으로 줄이면 차이는 1/4이 됩니다.</p></details>
          <details><summary>|x|의 원점에서 대칭 기울기 0은 미분계수일까요?</summary><p>아니에요. a=0이면 왼쪽 기울기는 −1, 오른쪽 기울기는 1이고, 평균인 대칭 기울기만 0입니다. 좌우 극한이 다르므로 미분계수는 없어요. 실제 대칭 할선은 y=h입니다.</p></details>
          <details><summary>구간별 함수의 원점에서는 무엇이 다를까요?</summary><p>f(x)=x (x&lt;0), f(x)=x² (x≥0)에서 a=0이면 왼쪽 기울기는 1, 오른쪽 기울기는 h, 대칭 기울기는 (1+h)/2입니다. 대칭 기울기는 0.5로 모이지만 좌우 극한은 1과 0이므로 미분 불가능합니다.</p></details>
        </div>
      </div>
      <section class="panel note-panel comment-board" id="observation-board" aria-labelledby="comment-board-title">
        <div class="section-header"><div><div class="section-kicker">나의 발견을 함께</div><h2 id="comment-board-title">관찰 게시판</h2></div><span class="comment-count" id="comment-count" aria-label="등록된 관찰 수">—</span></div>
        <p class="comment-storage" id="comment-storage">게시판에 연결하는 중이에요.</p>
        <form class="comment-form" id="comment-form">
          <fieldset class="comment-fields" id="comment-fields" aria-label="관찰 등록 정보">
            <div class="comment-identity">
              <label class="comment-field" for="comment-grade"><span>학년</span><select id="comment-grade" name="grade" required><option value="">선택</option><option value="1">1학년</option><option value="2">2학년</option><option value="3">3학년</option><option value="4">4학년</option><option value="5">5학년</option><option value="6">6학년</option></select></label>
              <label class="comment-field" for="comment-class"><span>반</span><input id="comment-class" name="classroom" type="number" min="1" max="99" step="1" inputmode="numeric" placeholder="반" required></label>
              <label class="comment-field" for="comment-name"><span>이름</span><input id="comment-name" name="name" type="text" minlength="1" maxlength="30" autocomplete="off" placeholder="이름" required></label>
            </div>
            <label class="comment-field comment-content-field" for="experiment-note"><span>관찰 내용</span><textarea class="note-area" id="experiment-note" name="content" rows="5" minlength="1" maxlength="2000" required placeholder="예: |x|의 원점에서 h를 줄여도 왼쪽은 −1, 오른쪽은 1이었다. 대칭 기울기만 보고 판단하면…"></textarea></label>
            <div class="comment-form-meta"><span class="comment-public-note">등록한 학년·반·이름과 내용은 이 게시판에 표시됩니다.</span><span id="comment-length" aria-label="입력한 관찰 내용 글자 수">0 / 2,000</span></div>
          </fieldset>
          <div class="comment-form-actions"><button class="btn btn-primary" id="comment-submit" type="submit">관찰 등록</button><p class="comment-form-status" id="comment-form-status" role="status" aria-live="polite"></p></div>
        </form>
        <div class="comment-list-section">
          <div class="comment-list-toolbar"><strong>모두의 관찰 <small>최신순</small></strong><div class="comment-list-actions"><button class="btn btn-quiet btn-small" id="comments-refresh" type="button">새로고침</button><button class="btn btn-quiet btn-small" id="comments-export" type="button">CSV 저장</button></div></div>
          <p class="comment-list-status" id="comment-list-status" role="status" aria-live="polite">관찰 목록을 불러오는 중이에요.</p>
          <div class="comment-empty" id="comments-empty" hidden><strong>아직 등록된 관찰이 없어요.</strong><p>첫 번째 관찰을 남겨 보세요.</p></div>
          <ol class="comments-list" id="comments-list" aria-label="등록된 관찰, 최신순"></ol>
          <button class="btn btn-secondary full-width" id="comments-more" type="button" hidden>이전 관찰 더 보기</button>
        </div>
      </section>
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

  function formatNumber(value, significantDigits = 6) {
    if (!Number.isFinite(value)) return "—";
    if (!Number.isInteger(significantDigits) || significantDigits < 1 || significantDigits > 100) {
      throw new RangeError("significantDigits must be an integer from 1 to 100.");
    }
    if (value === 0) return "0";

    // Round once to significant digits, then arrange the decimal as text.
    // Converting the rounded string back to a number could underflow tiny
    // nonzero values, overflow large values, or reintroduce e notation.
    const [coefficient, exponentText] = Math.abs(value)
      .toExponential(significantDigits - 1).split("e");
    const exponent = Number(exponentText);
    const digits = coefficient.replace(".", "").replace(/0+$/, "");
    const sign = value < 0 ? "−" : "";

    // Use ordinary decimals from 10^-12 up to (but not including) 10^12,
    // applying the boundary after rounding so carries stay consistent.
    if (exponent >= -12 && exponent < 12) {
      const point = exponent + 1;
      if (point <= 0) return sign + "0." + "0".repeat(-point) + digits;
      if (point >= digits.length) return sign + digits + "0".repeat(point - digits.length);
      return sign + digits.slice(0, point) + "." + digits.slice(point);
    }

    const superscripts = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
      "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "-": "⁻" };
    const power = String(exponent).replace(/[0-9-]/g, (character) => superscripts[character]);
    const mantissa = digits[0] + (digits.length > 1 ? "." + digits.slice(1) : "");
    return sign + mantissa + " × 10" + power;
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
    analyze,
    formatNumber
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
  const state = { fn: "quadratic", a: 1, h: 1, selected: "center", sides: true, tangent: true };
  let view;
  let rows = [];
  let dragging = null;
  let renderRequest = 0;
  let animationRequest = 0;
  let animationLast = null;
  let playing = false;
  let animationFinished = false;
  let lastAnnouncement = "";
  const graph = $("main-graph");
  const pointNames = { left: "왼쪽 점 L", center: "기준점 A", right: "오른쪽 점 R" };
  const clamp = (x, low, high) => Math.min(high, Math.max(low, x));

  if (!M) {
    $("input-status").textContent = "계산 파일을 불러오지 못했어요. 페이지를 새로고침해 주세요.";
    return;
  }

  const format = (value, digits = 6) => M.formatNumber(value, digits);

  function setText(id, value) {
    const node = $(id);
    if (node.textContent !== value) node.textContent = value;
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

  function fullLine(x, y, slope) {
    // A secant is the line through its two function points, extended across
    // the plot. It is not replaced by a line through A unless A lies on it.
    return pathLine(view.xMin, y + slope * (view.xMin - x),
      view.xMax, y + slope * (view.xMax - x));
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
    $("symmetric-secant").setAttribute("d", fullLine(r.leftX, r.leftY, r.symmetric));
    $("left-secant").setAttribute("d", fullLine(state.a, r.centerY, r.left));
    $("right-secant").setAttribute("d", fullLine(state.a, r.centerY, r.right));
    $("left-secant").style.display = state.sides ? "" : "none";
    $("right-secant").style.display = state.sides ? "" : "none";
    const showTangent = state.tangent && analysis.differentiable;
    $("tangent").style.display = showTangent ? "" : "none";
    if (showTangent) {
      $("tangent").setAttribute("d", fullLine(state.a, r.centerY, analysis.derivative));
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
    ["left", "right", "symmetric"].forEach((key) => {
      const value = r[key];
      const text = format(value, 9);
      const node = $(`${key}-value`);
      node.textContent = text;
      node.classList.toggle("is-long", text.length > 10);
      node.title = `현재 h에서의 계산값: ${format(value, 12)}`;
      $(`${key}-value-note`).textContent = value !== 0 && Math.abs(value) < 0.0001
        ? (value < 0 ? "0에 가까운 음수 · 아직 0은 아니에요" : "0에 가까운 양수 · 아직 0은 아니에요")
        : "현재 h에서의 기울기";
    });
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
    $("show-tangent").disabled = !analysis.differentiable;
    $("tangent-status").textContent = !analysis.differentiable
      ? "이 기준점에는 접선이 없어요. 보라색 대칭 할선과 접선을 구별해 보세요."
      : state.tangent
        ? `진한 점선은 A에서의 접선 · 기울기 f′(a) = ${format(analysis.derivative)}`
        : "‘실제 접선 보기’를 켜면 할선과 접선을 비교할 수 있어요.";
    $("tangent-status").dataset.kind = analysis.differentiable ? "success" : "warning";
    let guide;
    if (state.fn === "quadratic" && state.a === 0) {
      guide = "왼쪽 기울기는 −h, 오른쪽은 h예요. h를 줄이면 둘 다 0에 가까워지고, 대칭 기울기는 항상 0입니다. 따라서 접선 y = 0의 기울기도 0이에요.";
    } else if (state.fn === "absolute" && state.a === 0) {
      guide = "왼쪽은 −1, 오른쪽은 1로 계속 달라요. 대칭 기울기가 0이어도, 이 원점에는 미분계수와 접선이 없어요.";
    } else if (state.fn === "piecewise" && state.a === 0) {
      guide = "왼쪽은 1, 오른쪽은 0으로 가까워져요. 대칭 기울기는 0.5로 모이지만, 좌우 극한이 달라 미분할 수 없어요.";
    } else {
      guide = `h를 줄이면 좌우 기울기는 모두 ${format(analysis.derivative)}에 가까워져요. 이 극한값이 A에서의 미분계수예요. 아래에서 현재 값과 극한값을 비교해 보세요.`;
    }
    setText("reading-guide", guide);
  }

  function renderExperienceStatus() {
    $("experiment-state").textContent = `기준점 a = ${format(state.a)} · 거리 h = ${format(state.h)} > 0`;
    setText("animation-status", playing
      ? "관찰 중 · 양쪽 점이 A에 가까워질 때, 세 기울기를 비교해 보세요."
      : animationFinished
        ? "관찰 완료 · h = 0.000001까지 줄였어요. h에 0을 대입한 것은 아니에요."
        : "버튼을 누르면 약 8초 동안 h가 작아져요. 중간에 멈출 수도 있어요.");
    $("animate").textContent = playing ? "Ⅱ 자동 관찰 일시정지"
      : animationFinished ? "↻ h → 0 다시 관찰" : "▶ h → 0 자동 관찰";
    $("animate").setAttribute("aria-pressed", String(playing));
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
    renderExperienceStatus();
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
    renderExperienceStatus();
  }

  function setSelected(which) {
    state.selected = which;
    const point = $(`point-${which}`);
    if ($( "points-layer").lastElementChild !== point) $("points-layer").append(point);
    scheduleRender();
  }

  function update({ a = state.a, h = state.h, fn = state.fn }, { fit = false, announce = true } = {}) {
    animationFinished = false;
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
    animationFinished = false;
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
    animationFinished = false;
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
    state.tangent = true;
    $("show-sides").checked = true;
    $("show-tangent").checked = true;
    $("manual-controls").open = false;
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

  function startAnimation() {
    if (state.h <= M.MIN_H * 1.01) state.h = 1;
    animationFinished = false;
    playing = true;
    animationLast = null;
    renderExperienceStatus();
    ensureVisible();
    const frame = (now) => {
      if (!playing) return;
      const dt = animationLast === null ? 0 : Math.max(0, now - animationLast);
      animationLast = now;
      state.h = Math.max(M.MIN_H, state.h * Math.exp(-dt / 600));
      render();
      if (state.h <= M.MIN_H * (1 + 1e-8)) {
        state.h = M.MIN_H;
        animationFinished = true;
        stopAnimation();
        render();
        say("h가 0.000001에 도달했어요. 0에 대입한 값이 아니라, 0에 가까워지는 과정을 관찰한 것입니다.");
      } else animationRequest = window.requestAnimationFrame(frame);
    };
    animationRequest = window.requestAnimationFrame(frame);
  }
  $("animate").addEventListener("click", () => {
    if (playing) { stopAnimation(); say("자동 관찰을 멈췄어요."); return; }
    startAnimation();
  });
  $("animate-origin").addEventListener("click", () => {
    update({ a: 0, h: 1 }, { fit: true });
    startAnimation();
    say(`${M.FUNCTIONS[state.fn].name}의 원점에서 자동 관찰을 시작했어요.`);
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

  window.SecantExperiment = Object.freeze({
    snapshot: () => ({ fn: state.fn, a: state.a, h: state.h })
  });

  fitView();
  render();
})();

</script>
  <script>
/* Shared comments: hosted API, Streamlit component bridge, or explicit offline mode. */
(() => {
  "use strict";
  const mode = window.SECANT_COMMENTS_MODE || (location.protocol === "file:" ? "offline" : "site");
  let storageLabel = mode === "offline"
    ? "이 HTML 파일의 기록은 이 기기에만 저장됩니다. 다른 기기와 공유하려면 웹앱을 이용해 주세요."
    : "등록한 기록은 서버에 저장되며, 이 게시판의 다른 방문자도 볼 수 있어요.";
  function uuid() {
    if (typeof window.crypto.randomUUID === "function") return window.crypto.randomUUID();
    // getRandomValues also works in an HTTP development iframe where
    // randomUUID is unavailable; keep the RPC identifier a valid UUID v4.
    const bytes = window.crypto.getRandomValues(new Uint8Array(16));
    bytes[6] = (bytes[6] & 15) | 64;
    bytes[8] = (bytes[8] & 63) | 128;
    const hex = Array.from(bytes, (byte) => byte.toString(16).padStart(2, "0")).join("");
    return `${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(12, 16)}-${hex.slice(16, 20)}-${hex.slice(20)}`;
  }

  async function api(path, options = {}) {
    let response;
    try {
      response = await fetch(path, { cache: "no-store", credentials: "same-origin", ...options });
    } catch (_) {
      throw new Error("서버에 연결하지 못했어요. 인터넷 연결을 확인하고 다시 눌러 주세요.");
    }
    let result;
    try { result = await response.json(); }
    catch (_) { throw new Error("댓글 서버의 응답을 확인하지 못했어요. 잠시 후 다시 눌러 주세요."); }
    if (!response.ok) throw new Error(result.error || "기록을 처리하지 못했어요. 다시 시도해 주세요.");
    return result;
  }

  const pending = new Map();
  let readyResolve;
  let initialData = null;
  let initialError = null;
  let consumedInitial = false;
  const ready = new Promise((resolve) => { readyResolve = resolve; });
  let queue = Promise.resolve();

  function post(type, payload) {
    window.parent.postMessage({ isStreamlitMessage: true, type, ...payload }, "*");
  }
  function rpc(action, payload) {
    const run = async () => {
      await ready;
      return new Promise((resolve, reject) => {
        const request_id = uuid();
        const timer = window.setTimeout(() => {
          pending.delete(request_id);
          reject(new Error("서버의 저장 응답이 늦어지고 있어요. 다시 등록해도 같은 글은 중복 저장되지 않아요."));
        }, 25000);
        pending.set(request_id, { resolve, reject, timer });
        post("streamlit:setComponentValue", { dataType: "json", value: { request_id, action, payload } });
      });
    };
    const next = queue.then(run, run);
    queue = next.catch(() => {});
    return next;
  }

  if (mode === "streamlit") {
    let lastHeight = 0;
    let frameRequested = false;
    const resize = () => {
      if (frameRequested) return;
      frameRequested = true;
      requestAnimationFrame(() => {
        frameRequested = false;
        const height = Math.ceil(document.body.getBoundingClientRect().height + 24);
        if (height !== lastHeight) {
          lastHeight = height;
          post("streamlit:setFrameHeight", { height });
        }
      });
    };
    window.addEventListener("message", (event) => {
      if (event.source !== window.parent || event.data?.type !== "streamlit:render") return;
      const args = event.data.args || {};
      if (args.storage_label) storageLabel = args.storage_label;
      if (args.initial_data) initialData = args.initial_data;
      initialError = typeof args.initial_error === "string" ? args.initial_error : null;
      readyResolve();
      const response = args.response;
      const waiting = response && pending.get(response.request_id);
      if (waiting) {
        clearTimeout(waiting.timer);
        pending.delete(response.request_id);
        if (response.ok) waiting.resolve(response.result);
        else waiting.reject(new Error(response.error || "저장하지 못했어요. 입력한 내용을 확인해 주세요."));
      }
      resize();
    });
    new ResizeObserver(resize).observe(document.body);
    window.addEventListener("resize", resize);
    post("streamlit:componentReady", { apiVersion: 1 });
    resize();
  }

  const offlineKey = "secant-lab-comments-offline-v3";
  function offlineRecords() {
    try {
      const data = JSON.parse(localStorage.getItem(offlineKey) || "[]");
      if (!Array.isArray(data)) throw new Error();
      return data;
    } catch (_) {
      throw new Error("이 기기의 저장 공간을 읽지 못했어요. 브라우저 저장 설정을 확인해 주세요.");
    }
  }

  const transport = {
    mode,
    get storageLabel() { return storageLabel; },
    async list({ before_id = null } = {}) {
      if (mode === "streamlit") {
        await ready;
        if (!consumedInitial && before_id === null) {
          consumedInitial = true;
          if (initialError) throw new Error(initialError);
          if (initialData) return initialData;
        }
        return rpc("list", { before_id });
      }
      if (mode === "offline") {
        const all = offlineRecords().sort((a, b) => b.id - a.id);
        const eligible = before_id === null ? all : all.filter((r) => r.id < before_id);
        const comments = eligible.slice(0, 50);
        return { comments, total: all.length, next_before_id: eligible.length > 50 ? comments.at(-1).id : null };
      }
      const query = before_id === null ? "" : `?before_id=${encodeURIComponent(before_id)}`;
      return api(`/api/comments${query}`);
    },
    async create(payload) {
      if (mode === "streamlit") return rpc("create", payload);
      if (mode === "offline") {
        const records = offlineRecords();
        const existing = records.find((r) => r.request_id === payload.request_id);
        if (existing) return { comment: existing, duplicate: true };
        const comment = { ...payload, id: records.reduce((n, r) => Math.max(n, r.id), 0) + 1, created_at: new Date().toISOString() };
        try { localStorage.setItem(offlineKey, JSON.stringify([...records, comment])); }
        catch (_) { throw new Error("저장 공간이 부족해요. 기록을 CSV로 내려받은 뒤 저장 공간을 확인해 주세요."); }
        return { comment, duplicate: false };
      }
      return api("/api/comments", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) });
    },
    async exportAll() {
      if (mode === "streamlit") return rpc("export", {});
      if (mode === "offline") return { comments: offlineRecords().sort((a, b) => b.id - a.id) };
      return api("/api/comments/export");
    }
  };
  window.CommentTransport = Object.freeze(transport);
})();

</script>
  <script>
/* Observation board UI. Storage and networking belong to CommentTransport. */
(() => {
  "use strict";

  function start() {
    const $ = (id) => document.getElementById(id);
    const form = $("comment-form");
    if (!form) return;
    const fields = $("comment-fields");
    const grade = $("comment-grade");
    const classroom = $("comment-class");
    const name = $("comment-name");
    const content = $("experiment-note");
    const submit = $("comment-submit");
    const refresh = $("comments-refresh");
    const more = $("comments-more");
    const exporter = $("comments-export");
    const transport = window.CommentTransport;
    let comments = [];
    let total = 0;
    let nextBefore = null;
    let loaded = false;
    let loading = false;
    let submitting = false;
    let exporting = false;
    let loadGeneration = 0;
    let pendingSubmission = null;

    function status(id, message, kind = "info") {
      const node = $(id);
      node.textContent = message;
      node.dataset.kind = kind;
    }

    function countCharacters() {
      $("comment-length").textContent = `${content.value.length.toLocaleString("ko-KR")} / 2,000`;
    }

    function syncStorageLabel() {
      const mode = String(transport.mode || "");
      const label = String(transport.storageLabel || "");
      $("comment-storage").dataset.mode = mode;
      $("comment-storage").textContent = mode === "offline"
        ? `이 기기에만 저장됩니다.${label ? ` ${label}` : " 다른 기기와는 공유되지 않아요."}`
        : label || "이 게시판에서 등록한 관찰을 함께 확인할 수 있어요.";
    }

    function syncButtons() {
      fields.disabled = submitting;
      submit.disabled = submitting;
      submit.textContent = submitting ? "등록하는 중…" : "관찰 등록";
      form.setAttribute("aria-busy", String(submitting));
      refresh.disabled = loading || submitting;
      more.disabled = loading || submitting;
      more.hidden = nextBefore === null;
      more.textContent = loading ? "불러오는 중…" : "이전 관찰 더 보기";
      exporter.disabled = exporting || submitting;
      exporter.textContent = exporting ? "CSV 준비 중…" : "CSV 저장";
      $("comments-list").setAttribute("aria-busy", String(loading));
    }

    function createNode(tag, className, text) {
      const node = document.createElement(tag);
      if (className) node.className = className;
      if (text !== undefined) node.textContent = String(text);
      return node;
    }

    const seoulFormatter = new Intl.DateTimeFormat("ko-KR", {
      timeZone: "Asia/Seoul", year: "numeric", month: "2-digit", day: "2-digit",
      hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23"
    });

    function seoulTime(raw) {
      const date = new Date(raw);
      if (!Number.isFinite(date.getTime())) return "작성 시각 확인 불가";
      const values = Object.fromEntries(seoulFormatter.formatToParts(date).map((part) => [part.type, part.value]));
      return `${values.year}.${values.month}.${values.day} ${values.hour}:${values.minute}:${values.second}`;
    }

    function functionLabel(id) {
      const entry = window.MathLab && Object.prototype.hasOwnProperty.call(window.MathLab.FUNCTIONS, id)
        ? window.MathLab.FUNCTIONS[id] : null;
      return entry ? entry.formula : String(id || "함수 정보 없음");
    }

    function numberLabel(value) {
      return typeof value === "number" && Number.isFinite(value)
        ? window.MathLab.formatNumber(value, 9) : "—";
    }

    function renderComment(comment) {
      const card = createNode("li", "comment-card");
      card.dataset.commentId = String(comment.id);
      const header = createNode("div", "comment-card-header");
      header.append(createNode("strong", "comment-author", `${comment.grade}학년 ${comment.classroom}반 ${comment.name}`));
      const time = createNode("time", "comment-time", `${seoulTime(comment.created_at)} · 한국 시간`);
      if (Number.isFinite(Date.parse(comment.created_at))) time.dateTime = comment.created_at;
      header.append(time);
      card.append(header, createNode("p", "comment-content", comment.content));
      const context = createNode("div", "comment-context");
      context.setAttribute("aria-label", "등록할 때의 실험 조건");
      context.append(
        createNode("span", "", functionLabel(comment.fn)),
        createNode("span", "", `a = ${numberLabel(comment.a)}`),
        createNode("span", "", `h = ${numberLabel(comment.h)}`)
      );
      card.append(context);
      return card;
    }

    function renderList() {
      const sorted = [...comments].sort((left, right) => Number(right.id) - Number(left.id));
      $("comments-list").replaceChildren(...sorted.map(renderComment));
      $("comment-count").textContent = loaded ? `${total.toLocaleString("ko-KR")}개` : "—";
      $("comments-empty").hidden = !loaded || comments.length > 0 || total > 0;
      syncButtons();
    }

    function uniqueComments(records) {
      const byId = new Map();
      records.forEach((comment) => {
        if (!comment || !Number.isSafeInteger(Number(comment.id)) || Number(comment.id) <= 0 ||
          typeof comment.content !== "string" || typeof comment.name !== "string") {
          throw new Error("Invalid comment response");
        }
        byId.set(String(comment.id), comment);
      });
      return [...byId.values()];
    }

    async function loadComments(reset = true) {
      if (!reset && (loading || nextBefore === null)) return false;
      const generation = ++loadGeneration;
      const before = reset ? null : nextBefore;
      loading = true;
      status("comment-list-status", reset ? "관찰 목록을 불러오는 중이에요." : "이전 관찰을 불러오는 중이에요.");
      syncButtons();
      try {
        const page = await transport.list({ before_id: before });
        if (generation !== loadGeneration) return false;
        if (!page || !Array.isArray(page.comments) || !Number.isSafeInteger(Number(page.total)) || Number(page.total) < 0) {
          throw new Error("Invalid list response");
        }
        const records = uniqueComments(reset ? page.comments : [...comments, ...page.comments]);
        comments = records;
        total = Number(page.total);
        nextBefore = page.next_before_id == null ? null : Number(page.next_before_id);
        if (!Number.isSafeInteger(nextBefore) || nextBefore <= 0) nextBefore = null;
        loaded = true;
        syncStorageLabel();
        renderList();
        status("comment-list-status", total === 0 ? "" : `${comments.length.toLocaleString("ko-KR")}개 표시 · 최신순`);
        return true;
      } catch (_) {
        if (generation === loadGeneration) {
          syncStorageLabel();
          status("comment-list-status", "관찰 목록을 불러오지 못했어요. 새로고침을 눌러 다시 시도해 주세요.", "error");
        }
        return false;
      } finally {
        if (generation === loadGeneration) {
          loading = false;
          syncButtons();
        }
      }
    }

    function requestId() {
      if (typeof window.crypto.randomUUID === "function") return window.crypto.randomUUID();
      const bytes = window.crypto.getRandomValues(new Uint8Array(16));
      bytes[6] = (bytes[6] & 15) | 64;
      bytes[8] = (bytes[8] & 63) | 128;
      const hex = Array.from(bytes, (b) => b.toString(16).padStart(2, "0")).join("");
      return `${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(12, 16)}-${hex.slice(16, 20)}-${hex.slice(20)}`;
    }

    function readFields() {
      const values = {
        grade: Number(grade.value), classroom: Number(classroom.value),
        name: name.value.trim(), content: content.value.trim()
      };
      grade.setCustomValidity(Number.isInteger(values.grade) && values.grade >= 1 && values.grade <= 6 ? "" : "학년을 선택해 주세요.");
      classroom.setCustomValidity(Number.isInteger(values.classroom) && values.classroom >= 1 && values.classroom <= 99 ? "" : "반을 1부터 99까지의 정수로 입력해 주세요.");
      name.setCustomValidity(values.name.length >= 1 && values.name.length <= 30 ? "" : "이름을 1자부터 30자까지 입력해 주세요.");
      content.setCustomValidity(values.content.length >= 1 && values.content.length <= 2000 ? "" : "관찰 내용을 1자부터 2,000자까지 입력해 주세요.");
      return form.reportValidity() ? values : null;
    }

    function experimentSnapshot() {
      const snapshot = window.SecantExperiment && window.SecantExperiment.snapshot();
      if (!snapshot || typeof snapshot.fn !== "string" || !Number.isFinite(snapshot.a) || !Number.isFinite(snapshot.h) || snapshot.h <= 0) {
        throw new Error("Experiment state unavailable");
      }
      return { fn: snapshot.fn, a: snapshot.a, h: snapshot.h };
    }

    [grade, classroom, name, content].forEach((input) => {
      input.addEventListener("input", () => {
        input.setCustomValidity("");
        pendingSubmission = null;
        countCharacters();
      });
      input.addEventListener("change", () => {
        input.setCustomValidity("");
        pendingSubmission = null;
      });
    });

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (submitting) return;
      const values = readFields();
      if (!values) return;
      const fingerprint = JSON.stringify(values);
      if (!pendingSubmission || pendingSubmission.fingerprint !== fingerprint) {
        try {
          pendingSubmission = {
            fingerprint,
            payload: { request_id: requestId(), ...values, ...experimentSnapshot() }
          };
        } catch (_) {
          status("comment-form-status", "현재 실험 정보를 확인하지 못했어요. 입력한 내용은 그대로 두고 잠시 후 다시 시도해 주세요.", "error");
          return;
        }
      }
      submitting = true;
      syncButtons();
      status("comment-form-status", "관찰을 등록하는 중이에요.");
      try {
        const result = await transport.create(pendingSubmission.payload);
        if (!result || !result.comment) throw new Error("Invalid create response");
        const nextComments = uniqueComments([result.comment, ...comments]);
        const wasPresent = comments.some((comment) => String(comment.id) === String(result.comment.id));
        comments = nextComments;
        total = Math.max(comments.length, total + (wasPresent || result.duplicate ? 0 : 1));
        loaded = true;
        pendingSubmission = null;
        form.reset();
        [grade, classroom, name, content].forEach((input) => input.setCustomValidity(""));
        countCharacters();
        syncStorageLabel();
        renderList();
        status("comment-form-status", result.duplicate ? "이미 등록된 관찰을 확인했어요. 입력란을 비웠어요." : "관찰을 등록했어요. 다음 사람을 위해 입력란을 비웠어요.", "success");
        await loadComments(true);
      } catch (_) {
        status("comment-form-status", "등록을 확인하지 못했어요. 입력한 내용은 그대로 남아 있으니 다시 등록해 주세요.", "error");
      } finally {
        submitting = false;
        syncButtons();
      }
    });

    function csvCell(value) {
      let text = value == null ? "" : String(value);
      // Keep student-entered text as text when opened in spreadsheet apps.
      if (typeof value !== "number" && /^[\s]*[=+\-@]/u.test(text)) text = "'" + text;
      return `"${text.replaceAll('"', '""')}"`;
    }

    function downloadCSV(records) {
      const header = ["번호", "작성 시각 (한국 시간)", "작성 시각 (UTC)", "학년", "반", "이름", "관찰 내용", "함수", "기준점 a", "거리 h"];
      const rows = records.map((comment) => [
        Number(comment.id), seoulTime(comment.created_at), comment.created_at,
        Number(comment.grade), Number(comment.classroom), comment.name, comment.content,
        functionLabel(comment.fn), comment.a, comment.h
      ]);
      const csv = "\uFEFF" + [header, ...rows].map((row) => row.map(csvCell).join(",")).join("\r\n");
      const url = URL.createObjectURL(new Blob([csv], { type: "text/csv;charset=utf-8" }));
      const link = createNode("a", "");
      link.href = url;
      link.download = `secant-observations-${seoulTime(new Date().toISOString()).slice(0, 10).replaceAll(".", "-")}.csv`;
      link.style.display = "none";
      document.body.append(link);
      link.click();
      link.remove();
      window.setTimeout(() => URL.revokeObjectURL(url), 1500);
    }

    refresh.addEventListener("click", () => loadComments(true));
    more.addEventListener("click", () => loadComments(false));
    exporter.addEventListener("click", async () => {
      if (exporting) return;
      exporting = true;
      syncButtons();
      status("comment-list-status", "전체 관찰을 CSV로 준비하는 중이에요.");
      try {
        const result = await transport.exportAll();
        if (!result || !Array.isArray(result.comments)) throw new Error("Invalid export response");
        const records = uniqueComments(result.comments).sort((left, right) => Number(right.id) - Number(left.id));
        syncStorageLabel();
        if (records.length === 0) status("comment-list-status", "저장할 관찰이 아직 없어요.");
        else {
          downloadCSV(records);
          status("comment-list-status", `${records.length.toLocaleString("ko-KR")}개의 관찰을 CSV로 저장했어요.`, "success");
        }
      } catch (_) {
        status("comment-list-status", "CSV를 준비하지 못했어요. 잠시 후 다시 시도해 주세요.", "error");
      } finally {
        exporting = false;
        syncButtons();
      }
    });

    countCharacters();
    if (!transport || !["list", "create", "exportAll"].every((key) => typeof transport[key] === "function")) {
      fields.disabled = true;
      submit.disabled = true;
      refresh.disabled = true;
      exporter.disabled = true;
      status("comment-storage", "게시판 연결을 확인하지 못했어요. 페이지를 새로고침해 주세요.", "error");
      status("comment-list-status", "관찰 목록을 불러올 수 없어요.", "error");
      return;
    }
    // No automatic submission or migration of old private browser notes.
    loadComments(true);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start, { once: true });
  else start();
})();

</script>
</body>
</html>
"""



"""Shared comment storage; standard library only, suitable for inlining in app.py."""
import contextlib
import datetime
import json
import math
from pathlib import Path
import sqlite3
import urllib.error
import urllib.parse
import urllib.request
import uuid


COMMENT_PAGE_SIZE = 50
COMMENT_FIELDS = ("request_id", "grade", "classroom", "name", "content", "fn", "a", "h")
COMMENT_COLUMNS = "id," + ",".join(COMMENT_FIELDS) + ",created_at"
COMMENT_FUNCTIONS = {"quadratic", "cubic", "absolute", "piecewise"}


class CommentError(Exception):
    """Only this deliberately public message may be sent to the browser."""
    def __init__(self, message):
        self.public_message = message
        super().__init__(message)


class CommentValidationError(CommentError):
    pass


class CommentConflictError(CommentError):
    pass


class CommentStorageError(CommentError):
    pass


def _comment_uuid(value):
    if not isinstance(value, str):
        raise CommentValidationError("요청 번호가 올바르지 않습니다. 다시 시도해 주세요.")
    try:
        return str(uuid.UUID(value.strip()))
    except (ValueError, AttributeError):
        raise CommentValidationError("요청 번호가 올바르지 않습니다. 다시 시도해 주세요.") from None


def _comment_integer(value, minimum, maximum, label):
    if type(value) is not int or not minimum <= value <= maximum:
        raise CommentValidationError(f"{label}은 {minimum}부터 {maximum} 사이의 정수로 입력해 주세요.")
    return value


def _comment_text(value, maximum, label):
    if not isinstance(value, str):
        raise CommentValidationError(f"{label}을 입력해 주세요.")
    value = value.strip()
    if not value or len(value) > maximum or "\x00" in value:
        raise CommentValidationError(f"{label}은 공백을 제외하고 1~{maximum}자 이내로 입력해 주세요.")
    return value


def _comment_number(value, minimum, maximum, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise CommentValidationError(f"{label} 값이 올바르지 않습니다.")
    try:
        value = float(value)
    except (OverflowError, ValueError):
        raise CommentValidationError(f"{label} 값이 올바르지 않습니다.") from None
    if not math.isfinite(value) or not minimum <= value <= maximum:
        raise CommentValidationError(f"{label} 값이 허용 범위를 벗어났습니다.")
    return 0.0 if value == 0 else value


def validate_comment(payload):
    if not isinstance(payload, dict):
        raise CommentValidationError("댓글 입력 형식이 올바르지 않습니다.")
    fn = payload.get("fn")
    if not isinstance(fn, str) or fn not in COMMENT_FUNCTIONS:
        raise CommentValidationError("탐구할 함수를 먼저 선택해 주세요.")
    # Client-controlled id/created_at and unknown fields are never inserted.
    return {
        "request_id": _comment_uuid(payload.get("request_id")),
        "grade": _comment_integer(payload.get("grade"), 1, 6, "학년"),
        "classroom": _comment_integer(payload.get("classroom"), 1, 99, "반"),
        "name": _comment_text(payload.get("name"), 30, "이름"),
        "content": _comment_text(payload.get("content"), 2000, "댓글"),
        "fn": fn,
        "a": _comment_number(payload.get("a"), -3, 3, "기준점 a"),
        "h": _comment_number(payload.get("h"), 1e-6, 2, "거리 h"),
    }


def _comment_cursor(before_id):
    if before_id is None:
        return None
    return _comment_integer(before_id, 1, 9223372036854775807, "이전 댓글 번호")


def _public_comment(row):
    try:
        row = dict(row)
        stamp = datetime.datetime.fromisoformat(str(row["created_at"]).replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            raise ValueError("Missing timezone")
        return {
            "id": int(row["id"]),
            "request_id": str(row["request_id"]),
            "grade": int(row["grade"]),
            "classroom": int(row["classroom"]),
            "name": str(row["name"]),
            "content": str(row["content"]),
            "fn": str(row["fn"]),
            "a": float(row["a"]),
            "h": float(row["h"]),
            "created_at": stamp.astimezone(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        }
    except (KeyError, TypeError, ValueError, OverflowError):
        raise CommentStorageError("저장된 댓글을 읽을 수 없습니다. 관리자에게 문의해 주세요.") from None


def _duplicate_comment(existing, payload):
    if any(existing[field] != payload[field] for field in COMMENT_FIELDS):
        raise CommentConflictError("이미 사용한 요청 번호에 다른 내용이 담겨 있습니다. 새 댓글로 다시 등록해 주세요.")
    return {"comment": existing, "duplicate": True}


_COMMENT_SQLITE_SCHEMA = """
CREATE TABLE IF NOT EXISTS observation_comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id TEXT NOT NULL UNIQUE,
    grade INTEGER NOT NULL CHECK (grade BETWEEN 1 AND 6),
    classroom INTEGER NOT NULL CHECK (classroom BETWEEN 1 AND 99),
    name TEXT NOT NULL CHECK (length(trim(name)) BETWEEN 1 AND 30),
    content TEXT NOT NULL CHECK (length(trim(content)) BETWEEN 1 AND 2000),
    fn TEXT NOT NULL CHECK (fn IN ('quadratic','cubic','absolute','piecewise')),
    a REAL NOT NULL CHECK (a BETWEEN -3 AND 3),
    h REAL NOT NULL CHECK (h BETWEEN 0.000001 AND 2),
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
"""


class CommentStore:
    """A single shared SQLite file; each operation owns a short connection."""
    def __init__(self, db_path, timeout=10.0):
        try:
            self.db_path = Path(db_path).resolve()
            self.timeout = float(timeout)
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            with contextlib.closing(self._connect()) as connection:
                connection.execute("PRAGMA journal_mode=WAL")
                connection.executescript(_COMMENT_SQLITE_SCHEMA)
        except (OSError, sqlite3.Error, TypeError, ValueError):
            raise CommentStorageError("댓글 저장소를 준비하지 못했습니다. 관리자에게 문의해 주세요.") from None

    def _connect(self):
        connection = sqlite3.connect(str(self.db_path), timeout=self.timeout, isolation_level=None)
        connection.row_factory = sqlite3.Row
        return connection

    def create(self, payload):
        data = validate_comment(payload)
        try:
            with contextlib.closing(self._connect()) as connection:
                # Serialize duplicate-check + insert across threads/processes.
                connection.execute("BEGIN IMMEDIATE")
                try:
                    row = connection.execute(
                        f"SELECT {COMMENT_COLUMNS} FROM observation_comments WHERE request_id = ?",
                        (data["request_id"],),
                    ).fetchone()
                    if row is not None:
                        result = _duplicate_comment(_public_comment(row), data)
                    else:
                        cursor = connection.execute(
                            "INSERT INTO observation_comments (request_id,grade,classroom,name,content,fn,a,h) "
                            "VALUES (?,?,?,?,?,?,?,?)", tuple(data[field] for field in COMMENT_FIELDS),
                        )
                        row = connection.execute(
                            f"SELECT {COMMENT_COLUMNS} FROM observation_comments WHERE id = ?", (cursor.lastrowid,),
                        ).fetchone()
                        result = {"comment": _public_comment(row), "duplicate": False}
                    connection.commit()
                    return result
                except Exception:
                    connection.rollback()
                    raise
        except sqlite3.Error:
            raise CommentStorageError("댓글을 저장하지 못했습니다. 잠시 후 다시 시도해 주세요.") from None

    def list(self, before_id=None):
        before_id = _comment_cursor(before_id)
        try:
            with contextlib.closing(self._connect()) as connection:
                connection.execute("BEGIN")
                total = connection.execute("SELECT count(*) FROM observation_comments").fetchone()[0]
                condition = " WHERE id < ?" if before_id is not None else ""
                parameters = (before_id, COMMENT_PAGE_SIZE + 1) if before_id is not None else (COMMENT_PAGE_SIZE + 1,)
                rows = connection.execute(
                    f"SELECT {COMMENT_COLUMNS} FROM observation_comments{condition} ORDER BY id DESC LIMIT ?", parameters,
                ).fetchall()
                connection.commit()
            comments = [_public_comment(row) for row in rows[:COMMENT_PAGE_SIZE]]
            return {
                "comments": comments,
                "total": total,
                "next_before_id": comments[-1]["id"] if len(rows) > COMMENT_PAGE_SIZE else None,
            }
        except sqlite3.Error:
            raise CommentStorageError("댓글 목록을 읽지 못했습니다. 잠시 후 다시 시도해 주세요.") from None

    def export_all(self):
        try:
            with contextlib.closing(self._connect()) as connection:
                rows = connection.execute(f"SELECT {COMMENT_COLUMNS} FROM observation_comments ORDER BY id DESC").fetchall()
            return {"comments": [_public_comment(row) for row in rows]}
        except sqlite3.Error:
            raise CommentStorageError("댓글을 내려받지 못했습니다. 잠시 후 다시 시도해 주세요.") from None


class _CommentRemoteConflict(Exception):
    pass


class SupabaseCommentStore:
    """Server-only REST adapter. It never falls back to a different database."""
    def __init__(self, supabase_url, service_role_key, timeout=10.0, opener=None):
        if not isinstance(supabase_url, str) or not isinstance(service_role_key, str):
            raise CommentStorageError("외부 댓글 저장소 설정을 확인해 주세요.")
        try:
            parsed = urllib.parse.urlsplit(supabase_url.strip())
        except ValueError:
            raise CommentStorageError("외부 댓글 저장소 설정을 확인해 주세요.") from None
        if (parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password
                or parsed.query or parsed.fragment or parsed.path not in ("", "/") or not service_role_key.strip()):
            raise CommentStorageError("외부 댓글 저장소 설정을 확인해 주세요.")
        self._url = supabase_url.strip().rstrip("/") + "/rest/v1/observation_comments"
        self._key = service_role_key.strip()
        self._timeout = float(timeout)
        self._opener = opener or urllib.request.urlopen

    def _request(self, method="GET", parameters=(), body=None, prefer="count=exact"):
        url = self._url + ("?" + urllib.parse.urlencode(parameters) if parameters else "")
        headers = {"apikey": self._key, "Accept": "application/json", "Prefer": prefer}
        # Legacy service_role keys are JWTs. New sb_secret keys use apikey
        # alone; sending a non-JWT secret in Authorization would be invalid.
        if not self._key.startswith("sb_secret_"):
            headers["Authorization"] = "Bearer " + self._key
        encoded = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            encoded = json.dumps(body, ensure_ascii=False, allow_nan=False).encode("utf-8")
        request = urllib.request.Request(url, data=encoded, headers=headers, method=method)
        try:
            with self._opener(request, timeout=self._timeout) as response:
                content = response.read(2_000_001)
                if len(content) > 2_000_000:
                    raise CommentStorageError("댓글 저장소의 응답을 처리하지 못했습니다.")
                return json.loads(content.decode("utf-8")) if content else None, response.headers
        except urllib.error.HTTPError as error:
            status = error.code
            error.close()
            if status == 409 and method == "POST":
                raise _CommentRemoteConflict() from None
            raise CommentStorageError("외부 댓글 저장소에 연결하지 못했습니다. 관리자에게 문의해 주세요.") from None
        except (urllib.error.URLError, OSError, TimeoutError, ValueError, UnicodeError):
            raise CommentStorageError("외부 댓글 저장소에 연결하지 못했습니다. 잠시 후 다시 시도해 주세요.") from None

    @staticmethod
    def _count(headers):
        value = next((str(v) for k, v in headers.items() if k.lower() == "content-range"), "")
        count = value.rsplit("/", 1)[-1].strip()
        if not count.isdigit():
            raise CommentStorageError("댓글 수를 확인하지 못했습니다. 관리자에게 문의해 주세요.")
        return int(count)

    @staticmethod
    def _rows(value):
        if not isinstance(value, list):
            raise CommentStorageError("댓글 저장소의 응답을 처리하지 못했습니다.")
        return [_public_comment(row) for row in value]

    def create(self, payload):
        data = validate_comment(payload)
        try:
            value, _ = self._request("POST", body=data, prefer="return=representation")
        except _CommentRemoteConflict:
            value, _ = self._request(parameters=(("select", COMMENT_COLUMNS), ("request_id", "eq." + data["request_id"]), ("limit", 1)))
            rows = self._rows(value)
            if len(rows) != 1:
                raise CommentStorageError("댓글 저장 결과를 확인하지 못했습니다. 같은 내용으로 다시 시도해 주세요.")
            return _duplicate_comment(rows[0], data)
        rows = self._rows(value)
        if len(rows) != 1:
            raise CommentStorageError("댓글 저장 결과를 확인하지 못했습니다. 같은 내용으로 다시 시도해 주세요.")
        return {"comment": rows[0], "duplicate": False}

    def list(self, before_id=None):
        before_id = _comment_cursor(before_id)
        parameters = [("select", COMMENT_COLUMNS), ("order", "id.desc"), ("limit", COMMENT_PAGE_SIZE)]
        if before_id is not None:
            parameters.append(("id", "lt." + str(before_id)))
        value, headers = self._request(parameters=parameters)
        comments = self._rows(value)
        remaining = self._count(headers)
        total = remaining
        if before_id is not None:
            _, total_headers = self._request(parameters=(("select", "id"), ("limit", 1)))
            total = self._count(total_headers)
        return {
            "comments": comments,
            "total": total,
            "next_before_id": comments[-1]["id"] if comments and remaining > len(comments) else None,
        }

    def export_all(self):
        comments = []
        before_id = None
        while True:
            parameters = [("select", COMMENT_COLUMNS), ("order", "id.desc"), ("limit", COMMENT_PAGE_SIZE)]
            if before_id is not None:
                parameters.append(("id", "lt." + str(before_id)))
            value, _ = self._request(parameters=parameters)
            rows = self._rows(value)
            if not rows:
                return {"comments": comments}
            next_id = rows[-1]["id"]
            if before_id is not None and next_id >= before_id:
                raise CommentStorageError("댓글 전체 목록을 읽지 못했습니다. 다시 시도해 주세요.")
            comments.extend(rows)
            before_id = next_id



"""Streamlit bridge, inlined after comments_store.py; no server-package imports."""
import hashlib
import os
import tempfile
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
from streamlit.errors import StreamlitSecretNotFoundError


@st.cache_resource(show_spinner=False)
def _comment_component(html):
    digest = hashlib.sha256(html.encode("utf-8")).hexdigest()
    directory = Path(tempfile.gettempdir()) / "secant-lab-components" / digest
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / "index.html"
    if not target.exists():
        temporary = directory / ("index-" + uuid.uuid4().hex + ".tmp")
        temporary.write_text(html, encoding="utf-8")
        os.replace(temporary, target)
    return components.declare_component("secant_lab_shared_board", path=str(directory))


@st.cache_resource(show_spinner=False)
def _comment_store_resource(backend, location, credential):
    if backend == "supabase":
        return SupabaseCommentStore(location, credential)
    return CommentStore(location)


def _configured_comment_store():
    try:
        configuration = st.secrets.get("comments", {})
    except (StreamlitSecretNotFoundError, FileNotFoundError):
        configuration = {}
    if not hasattr(configuration, "get"):
        raise CommentStorageError("댓글 저장소 설정을 확인해 주세요.")
    url = configuration.get("supabase_url")
    key = configuration.get("service_role_key")
    if url is not None or key is not None:
        if not isinstance(url, str) or not url.strip() or not isinstance(key, str) or not key.strip():
            raise CommentStorageError("외부 댓글 저장소 주소와 서버 키를 모두 설정해 주세요.")
        store = _comment_store_resource("supabase", url.strip(), key.strip())
        identity = "supabase:" + hashlib.sha256(url.strip().encode()).hexdigest()
        return store, "공유 서버 저장 · 외부 데이터베이스", identity
    app_file = globals().get("__file__", str(Path.cwd() / "app.py"))
    location = os.environ.get("SECANT_COMMENTS_DB") or str(Path(app_file).resolve().parent / ".data" / "observation_comments.sqlite3")
    location = str(Path(location).resolve())
    return _comment_store_resource("sqlite", location, ""), "공유 서버 저장 · 재배포 시 보존이 보장되지 않음", "sqlite:" + location


def _comment_rpc(store, event):
    """The RPC UUID and the create payload's persistent UUID are separate."""
    if not isinstance(event, dict):
        raise CommentValidationError("댓글 요청 형식이 올바르지 않습니다.")
    _comment_uuid(event.get("request_id"))
    action = event.get("action")
    payload = event.get("payload", {})
    if not isinstance(payload, dict):
        raise CommentValidationError("댓글 요청 형식이 올바르지 않습니다.")
    if action == "create":
        return store.create(payload)
    if action == "list":
        return store.list(before_id=payload.get("before_id"))
    if action == "export":
        return store.export_all()
    raise CommentValidationError("지원하지 않는 댓글 요청입니다.")


def run_comment_lab(HTML):
    """Render the stable component and acknowledge each request only once."""
    try:
        component = _comment_component(HTML)
    except Exception:
        st.error("체험 화면을 준비하지 못했습니다. 잠시 후 새로고침해 주세요.")
        return
    store = None
    startup_error = None
    storage_label = "댓글 저장소 연결 확인 필요"
    identity = "unavailable"
    try:
        store, storage_label, identity = _configured_comment_store()
    except CommentError as error:
        startup_error = error.public_message
    except Exception:
        startup_error = "댓글 저장소 설정을 읽지 못했습니다. 관리자에게 문의해 주세요."

    if st.session_state.get("_secant_comments_identity") != identity:
        st.session_state["_secant_comments_identity"] = identity
        st.session_state["_secant_comments_responses"] = {}
        st.session_state["_secant_comments_response"] = None
        st.session_state.pop("_secant_comments_initial", None)
    initial_data = st.session_state.get("_secant_comments_initial")
    if initial_data is None:
        if store is not None:
            try:
                initial_data = store.list()
                st.session_state["_secant_comments_initial"] = initial_data
            except CommentError as error:
                startup_error = error.public_message
            except Exception:
                startup_error = "댓글 목록을 읽지 못했습니다. 잠시 후 다시 시도해 주세요."
    if startup_error:
        st.error(startup_error)

    response = st.session_state.get("_secant_comments_response")
    event = component(
        initial_data=initial_data,
        initial_error=startup_error,
        response=response,
        storage_label=storage_label,
        key="secant_lab_shared_board_v3",
        default=None,
    )
    if event is None:
        return
    raw_id = event.get("request_id") if isinstance(event, dict) else None
    # Keep correlation identifiers bounded; never stringify a whole request.
    request_id = raw_id if isinstance(raw_id, str) and len(raw_id) <= 64 else None
    cache_key = request_id or "invalid-request"
    cache = st.session_state["_secant_comments_responses"]
    if cache_key in cache:
        if response != cache[cache_key]:
            st.session_state["_secant_comments_response"] = cache[cache_key]
            st.rerun()
        return

    answer = {"request_id": request_id, "ok": False, "result": None, "error": None}
    try:
        if store is None or startup_error:
            raise CommentStorageError(startup_error or "댓글 저장소에 연결하지 못했습니다.")
        answer["result"] = _comment_rpc(store, event)
        answer["ok"] = True
        if event.get("action") == "list" and event.get("payload", {}).get("before_id") is None:
            st.session_state["_secant_comments_initial"] = answer["result"]
        elif event.get("action") == "create":
            # A later iframe reload should start with the current board.
            # A failed list refresh must not turn a committed write into a failure.
            try:
                st.session_state["_secant_comments_initial"] = store.list()
            except Exception:
                st.session_state.pop("_secant_comments_initial", None)
    except CommentError as error:
        answer["error"] = error.public_message
    except Exception:
        answer["error"] = "댓글 요청을 처리하지 못했습니다. 잠시 후 다시 시도해 주세요."
    cache[cache_key] = answer
    # Recent acknowledgements cover reruns/retries without retaining unbounded
    # copies of every list/export response in each student's session.
    while len(cache) > 8:
        del cache[next(iter(cache))]
    st.session_state["_secant_comments_response"] = answer
    st.rerun()


run_comment_lab(HTML)
