# Nudge Theory to Prevent Diabetes
한양대학교 Data Science Project 수업의 팀 프로젝트입니다. 건강한 식품 선택을 유도하는 넛지 아이디어를 설문·색상 선호·뉴스 데이터로 탐색했습니다.

## 분석 구성
| 파일 | 내용 |
| --- | --- |
| [Association_analysis_and_z_test.ipynb](Association_analysis_and_z_test.ipynb) | 할인 설문 분석, 비율 Z 검정, 코사인 유사도, Apriori 연관 규칙 |
| [color_preference_analysis.ipynb](color_preference_analysis.ipynb) | 색상 선호 집계 및 시각화 |
| [time_series_analysis.ipynb](time_series_analysis.ipynb) | 뉴스 키워드 월별 집계, 이동평균, SARIMA 24개월 예측 |
| [webcrawling_dsp_final.py](webcrawling_dsp_final.py) | YTN 검색 결과 비동기 수집 |
| [discount_survey.csv](discount_survey.csv) | 할인 선택 설문 데이터 |
| [color - Sheet1 (2).csv](color%20-%20Sheet1%20%282%29.csv) | 색상 선호 데이터 |
| [ytn_combined_with_keywords.csv](ytn_combined_with_keywords.csv) | 키워드가 가공된 통합 뉴스 데이터 |

## 시작하기
Python 가상환경에서 저장소 루트를 작업 디렉터리로 사용합니다.

```sh
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter lab
```

의존성 목록은 코드의 import를 기준으로 정리한 시작점이며, 당시 실행 환경을 고정한 lockfile은 아닙니다.

- **할인 설문:** 앞부분의 `diabetes_data.csv`는 이 저장소에 없습니다. 해당 데이터를 사용하는 셀은 별도 준비가 필요하며, 할인 분석은 `discount_survey.csv`를 읽는 셀부터 의존 순서에 맞춰 실행합니다.
- **색상 분석:** 포함된 CSV를 그대로 사용합니다.
- **시계열 분석:** 첫 번째 원본 CSV 병합 셀은 건너뛰고, 포함된 `ytn_combined_with_keywords.csv`를 읽는 셀부터 실행할 수 있습니다.
- **크롤러:** 기본 검색어는 '당뇨'이며 코드에 2024년 11·12월을 제외하는 조건이 있습니다. 재수집에는 검색어·기간과 현재 사이트 구조를 확인해야 합니다. 기존 분석을 읽는 데 재수집은 필요하지 않습니다.

## 해석 범위
설문과 뉴스 키워드의 탐색적 분석입니다. 당뇨 예방의 임상적 효과나 인과관계를 검증한 실험으로 해석하지 않습니다. 시계열은 중앙 이동평균을 사용하므로, 미래 예측 성능을 평가하려면 시간 순서 분리와 전처리를 별도로 설계해야 합니다.

## 재현 상태
이번 정리는 파일 구성과 소스 코드를 기준으로 문서를 보강한 작업입니다. 전체 노트북 재실행, 데이터 재수집, 예측 성능 재검증은 수행하지 않았습니다.
