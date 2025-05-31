# 필요한 라이브러리 임포트
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- 1. 데이터 준비 (이 부분은 여러분의 실제 데이터로 대체되어야 합니다!) ---
# KBO 성적표 항목과 기존 예측 요소를 결합한 예시 데이터 생성
# 실제 데이터는 더 많은 행(경기 수)과 정확한 값들로 구성되어야 합니다.
# 'is_homerun': 0 또는 1 (홈런이 아니면 0, 홈런이면 1)
data = {
    # 구장/날씨/시프트 관련 기존 특성
    'stadium_size': [100, 98, 102, 95, 100, 98, 102, 95, 100, 98, 100, 98, 102, 95, 100, 98, 102, 95, 100, 98],
    'wind_speed': [3, 5, 2, 8, 4, 6, 3, 7, 5, 2, 3, 5, 2, 8, 4, 6, 3, 7, 5, 2],
    'wind_direction_is_outfield': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'shift_on_batter': [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1],

    # KBO 성적표 타자 데이터 (예시 값)
    'AVG': [0.330, 0.280, 0.350, 0.250, 0.300, 0.270, 0.360, 0.260, 0.310, 0.290,
            0.330, 0.280, 0.350, 0.250, 0.300, 0.270, 0.360, 0.260, 0.310, 0.290],
    'PA': [111, 100, 120, 90, 115, 105, 125, 95, 110, 100,
           111, 100, 120, 90, 115, 105, 125, 95, 110, 100],
    'HR': [7, 5, 8, 4, 6, 3, 9, 5, 7, 4,
           7, 5, 8, 4, 6, 3, 9, 5, 7, 4], # 현재 시즌 홈런 개수
    'SLG': [0.630, 0.550, 0.680, 0.500, 0.600, 0.520, 0.700, 0.510, 0.650, 0.580,
            0.630, 0.550, 0.680, 0.500, 0.600, 0.520, 0.700, 0.510, 0.650, 0.580],
    'OBP': [0.378, 0.340, 0.400, 0.300, 0.360, 0.330, 0.410, 0.310, 0.380, 0.350,
            0.378, 0.340, 0.400, 0.300, 0.360, 0.330, 0.410, 0.310, 0.380, 0.350],
    'OPS': [1.008, 0.890, 1.080, 0.800, 0.960, 0.850, 1.110, 0.820, 1.030, 0.930,
            1.008, 0.890, 1.080, 0.800, 0.960, 0.850, 1.110, 0.820, 1.030, 0.930],
    'SO': [18, 25, 15, 30, 20, 28, 12, 32, 17, 23,
           18, 25, 15, 30, 20, 28, 12, 32, 17, 23], # 삼진 (StrikeOut)
    'BB': [9, 5, 10, 3, 8, 4, 11, 4, 9, 5,
           9, 5, 10, 3, 8, 4, 11, 4, 9, 5], # 볼넷 (Base on Balls)

    # 새로 추가된 투수 지표 및 방향성 지표 (예시 값)
    'pitcher_homerun_allowed_rate': [0.03, 0.05, 0.02, 0.06, 0.04, 0.07, 0.03, 0.05, 0.04, 0.06,
                                     0.03, 0.05, 0.02, 0.06, 0.04, 0.07, 0.03, 0.05, 0.04, 0.06],
    'pitcher_era': [3.5, 4.2, 2.8, 5.0, 3.8, 4.5, 2.5, 5.2, 3.2, 4.0,
                    3.5, 4.2, 2.8, 5.0, 3.8, 4.5, 2.5, 5.2, 3.2, 4.0],
    'pitcher_k_per_9': [8.5, 7.0, 9.0, 6.5, 8.0, 7.5, 9.5, 6.0, 8.2, 7.8,
                        8.5, 7.0, 9.0, 6.5, 8.0, 7.5, 9.5, 6.0, 8.2, 7.8],
    'wind_angle_diff_to_homerun_direction': [10, 90, 20, 170, 45, 120, 0, 150, 60, 100,
                                             10, 90, 20, 170, 45, 120, 0, 150, 60, 100], # 0-180도
    'pitcher_facing_batter_side': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                                   1, 0, 1, 0, 1, 0, 1, 0, 1, 0], # 우투 vs 우타 or 좌투 vs 좌타 = 1

    # 타겟 변수
    'is_homerun': [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

print("--- 원본 데이터프레임 (예시) ---")
print(df.head())
print("\n")

# 특성과 타겟 분리
X = df.drop('is_homerun', axis=1) # 'is_homerun' 컬럼을 제외한 모든 컬럼이 특성
y = df['is_homerun']             # 'is_homerun' 컬럼이 타겟

# --- 2. 데이터 분할 (학습용과 테스트용) ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"학습 데이터 샘플 수: {len(X_train)}")
print(f"테스트 데이터 샘플 수: {len(X_test)}\n")

# --- 3. 모델 학습 (로지스틱 회귀) ---
print("--- 로지스틱 회귀 모델 학습 시작 ---")
model = LogisticRegression(solver='liblinear', random_state=42)
model.fit(X_train, y_train)
print("--- 모델 학습 완료 ---\n")

# --- 4. 예측 수행 및 5. 모델 평가 (기존 코드와 동일) ---
y_pred = model.predict(X_test)
print(f'정확도: {accuracy_score(y_test, y_pred):.4f}')
# ... (모델 평가 지표 출력 코드는 생략) ...

# --- 6. 새로운 GUI 기능 추가 ---
import tkinter as tk
from tkinter import messagebox

# 예측 버튼 클릭 시 실행될 함수
def predict_homerun_probability():
    try:
        # 입력 필드에서 값 가져오기 (기존)
        stadium_size = float(entry_stadium_size.get())
        wind_speed = float(entry_wind_speed.get())
        wind_direction_is_outfield = int(var_wind_direction.get())
        shift_on_batter = int(var_shift.get())

        # KBO 성적표 타자 항목 값 가져오기 (기존)
        avg_val = float(entry_avg.get())
        pa_val = float(entry_pa.get())
        hr_val = float(entry_hr.get())
        slg_val = float(entry_slg.get())
        obp_val = float(entry_obp.get())
        ops_val = float(entry_ops.get())
        so_val = float(entry_so.get())
        bb_val = float(entry_bb.get())

        # 새로 추가된 투수 지표 및 방향성 지표 값 가져오기
        pitcher_homerun_allowed_rate_val = float(entry_pitcher_homerun_allowed_rate.get())
        pitcher_era_val = float(entry_pitcher_era.get())
        pitcher_k_per_9_val = float(entry_pitcher_k_per_9.get())
        wind_angle_diff_val = float(entry_wind_angle_diff.get()) # 슬라이더 값
        pitcher_facing_batter_side_val = int(var_pitcher_facing_batter_side.get()) # 체크박스 값

        # 입력값을 DataFrame 형태로 변환 (모델 학습 시 사용한 컬럼 순서 및 이름 일치 중요!)
        new_data_input = pd.DataFrame([[
            stadium_size,
            wind_speed,
            wind_direction_is_outfield,
            shift_on_batter,
            avg_val,
            pa_val,
            hr_val,
            slg_val,
            obp_val,
            ops_val,
            so_val,
            bb_val,
            pitcher_homerun_allowed_rate_val,
            pitcher_era_val,
            pitcher_k_per_9_val,
            wind_angle_diff_val,
            pitcher_facing_batter_side_val
        ]], columns=X.columns) # X는 학습에 사용된 Feature DataFrame입니다.

        # 모델을 사용하여 홈런 확률 예측
        predicted_proba = model.predict_proba(new_data_input)[:, 1] # 1(홈런)일 확률

        # 결과 표시
        result_label.config(text=f"예측된 홈런 확률: {predicted_proba[0]*100:.2f}%", fg="blue")

    except ValueError:
        messagebox.showerror("입력 오류", "모든 필드에 올바른 숫자를 입력해주세요.\n(예: 비율은 0.0~1.0 사이, 각도는 0~180 등)")
    except Exception as e:
        messagebox.showerror("오류 발생", f"예측 중 오류가 발생했습니다: {e}")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("KBO 홈런 확률 예측기 v2.0")
root.geometry("500x850") # 창 크기 조정 (필드가 더 많아져서 더 크게)

# 입력 필드 및 레이블 생성 (그리드 형태로 배치)
row_idx = 0

# --- 경기 환경 데이터 ---
tk.Label(root, text="[경기 환경 데이터]", font=("Helvetica", 11, "bold")).grid(row=row_idx, column=0, columnspan=2, padx=10, pady=5, sticky='w')
row_idx += 1

tk.Label(root, text="구장 크기 (펜스 거리 등, m):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_stadium_size = tk.Entry(root)
entry_stadium_size.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

tk.Label(root, text="풍속 (m/s):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_wind_speed = tk.Entry(root)
entry_wind_speed.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

var_wind_direction = tk.IntVar()
tk.Checkbutton(root, text="외야 방향 바람 여부 (1:예, 0:아니오)", variable=var_wind_direction).grid(row=row_idx, column=0, columnspan=2, padx=10, pady=2, sticky='w')
row_idx += 1

tk.Label(root, text="풍향-홈런 방향 각도 차이 (0~180도):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
# 슬라이더로 각도 입력받기 (더 직관적)
entry_wind_angle_diff = tk.Scale(root, from_=0, to=180, orient="horizontal", length=200)
entry_wind_angle_diff.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

var_shift = tk.IntVar()
tk.Checkbutton(root, text="시프트 적용 여부 (1:예, 0:아니오)", variable=var_shift).grid(row=row_idx, column=0, columnspan=2, padx=10, pady=2, sticky='w')
row_idx += 1

# --- 타자 성적 데이터 ---
tk.Label(root, text="\n[타자 성적 데이터]", font=("Helvetica", 11, "bold")).grid(row=row_idx, column=0, columnspan=2, padx=10, pady=5, sticky='w')
row_idx += 1

tk.Label(root, text="타율 (AVG, 0.0-1.0):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_avg = tk.Entry(root)
entry_avg.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

tk.Label(root, text="타석 (PA):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_pa = tk.Entry(root)
entry_pa.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

tk.Label(root, text="홈런 (HR, 현재 시즌):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_hr = tk.Entry(root)
entry_hr.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

tk.Label(root, text="장타율 (SLG, 0.0-1.0):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_slg = tk.Entry(root)
entry_slg.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

tk.Label(root, text="출루율 (OBP, 0.0-1.0):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_obp = tk.Entry(root)
entry_obp.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

tk.Label(root, text="OPS (0.0-2.0 이상):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_ops = tk.Entry(root)
entry_ops.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

tk.Label(root, text="삼진 (SO):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_so = tk.Entry(root)
entry_so.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

tk.Label(root, text="볼넷 (BB):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_bb = tk.Entry(root)
entry_bb.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

# --- 투수 성적 데이터 ---
tk.Label(root, text="\n[투수 성적 데이터 (상대 투수)]", font=("Helvetica", 11, "bold")).grid(row=row_idx, column=0, columnspan=2, padx=10, pady=5, sticky='w')
row_idx += 1

tk.Label(root, text="피홈런율 (0.0-1.0):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_pitcher_homerun_allowed_rate = tk.Entry(root)
entry_pitcher_homerun_allowed_rate.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

tk.Label(root, text="평균자책점 (ERA, 0.0 이상):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_pitcher_era = tk.Entry(root)
entry_pitcher_era.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

tk.Label(root, text="9이닝당 삼진 (K/9):").grid(row=row_idx, column=0, padx=10, pady=2, sticky='w')
entry_pitcher_k_per_9 = tk.Entry(root)
entry_pitcher_k_per_9.grid(row=row_idx, column=1, padx=10, pady=2, sticky='ew')
row_idx += 1

var_pitcher_facing_batter_side = tk.IntVar()
tk.Checkbutton(root, text="투타 동일 방향 (우투-우타/좌투-좌타):", variable=var_pitcher_facing_batter_side).grid(row=row_idx, column=0, columnspan=2, padx=10, pady=2, sticky='w')
row_idx += 1


# 예측 버튼
predict_button = tk.Button(root, text="홈런 확률 예측", command=predict_homerun_probability, font=("Helvetica", 12, "bold"), bg="lightblue", fg="darkblue")
predict_button.grid(row=row_idx, column=0, columnspan=2, pady=20)
row_idx += 1

# 결과 표시 레이블
result_label = tk.Label(root, text="예측 결과: ", font=("Helvetica", 16, "bold"), fg="red")
result_label.grid(row=row_idx, column=0, columnspan=2, pady=10)

# 그리드 컬럼 비율 설정 (입력 필드가 더 넓게)
root.grid_columnconfigure(1, weight=1)

# 윈도우 실행
root.mainloop()