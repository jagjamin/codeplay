# 필요한 라이브러리 임포트
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- 1. 데이터 준비 (이 부분은 여러분의 실제 데이터로 대체되어야 합니다!) ---
# 예시 데이터 생성 (실제 데이터 형태를 가정하여 만듦)
# 실제 데이터는 KBO 경기 기록, 선수 데이터, 구장 특성, 날씨 데이터 등을 조합해야 합니다.
# 'is_homerun': 0 또는 1 (홈런이 아니면 0, 홈런이면 1)
data = {
    'stadium_size': [100, 98, 102, 95, 100, 98, 102, 95, 100, 98], # 펜스 거리 등 (예시)
    'wind_speed': [3, 5, 2, 8, 4, 6, 3, 7, 5, 2], # 풍속 (m/s)
    'wind_direction_is_outfield': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], # 외야 방향 바람 여부 (1:예, 0:아니오)
    'batter_power_rating': [80, 90, 75, 95, 85, 70, 92, 78, 88, 72], # 타자 장타력 지표 (예시)
    'batter_recent_homerun_rate': [0.05, 0.08, 0.03, 0.1, 0.06, 0.02, 0.09, 0.04, 0.07, 0.03], # 최근 홈런 비율
    'pitcher_homerun_allowed_rate': [0.03, 0.05, 0.02, 0.06, 0.04, 0.07, 0.03, 0.05, 0.04, 0.06], # 투수 피홈런율
    'shift_on_batter': [1, 0, 1, 1, 0, 1, 0, 0, 1, 1], # 타자에게 시프트 적용 여부 (1:예, 0:아니오)
    'is_homerun': [0, 1, 0, 1, 0, 0, 1, 0, 1, 0] # 실제 홈런 발생 여부 (타겟 변수)
}
df = pd.DataFrame(data)

print("--- 원본 데이터프레임 (예시) ---")
print(df.head())
print("\n")

# 특성과 타겟 분리
X = df.drop('is_homerun', axis=1) # 'is_homerun' 컬럼을 제외한 모든 컬럼이 특성
y = df['is_homerun']             # 'is_homerun' 컬럼이 타겟

# --- 2. 데이터 분할 (학습용과 테스트용) ---
# test_size=0.2는 전체 데이터의 20%를 테스트 데이터로 사용하겠다는 의미
# random_state는 재현 가능한 결과를 위해 설정
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# stratify=y는 타겟 변수의 비율을 학습/테스트 세트에 동일하게 유지 (홈런 데이터가 적을 때 중요)

print(f"학습 데이터 샘플 수: {len(X_train)}")
print(f"테스트 데이터 샘플 수: {len(X_test)}\n")

# --- 3. 모델 학습 (로지스틱 회귀) ---
print("--- 로지스틱 회귀 모델 학습 시작 ---")
model = LogisticRegression(solver='liblinear', random_state=42) # solver='liblinear'는 작은 데이터셋에 적합하고 L1/L2 정규화를 지원
model.fit(X_train, y_train)
print("--- 모델 학습 완료 ---\n")

# --- 4. 예측 수행 ---
# 테스트 데이터에 대한 예측
y_pred = model.predict(X_test)
# 홈런 칠 확률 (확률 값) 예측
y_pred_proba = model.predict_proba(X_test)[:, 1] # 1(홈런)일 확률만 가져옴

print("--- 예측 결과 (일부) ---")
print(f"실제값 (테스트): {list(y_test)}")
print(f"예측값 (0 또는 1): {list(y_pred)}")
print(f"예측 확률 (홈런일 확률): {[f'{p:.4f}' for p in y_pred_proba]}\n")


# --- 5. 모델 평가 ---
print("--- 모델 성능 평가 ---")
# 정확도 (Accuracy)
accuracy = accuracy_score(y_test, y_pred)
print(f'정확도 (Accuracy): {accuracy:.4f}')

# 분류 보고서 (Classification Report) - 정밀도, 재현율, F1-score
print('\n분류 보고서 (Classification Report):')
print(classification_report(y_test, y_pred))

# 혼동 행렬 (Confusion Matrix)
cm = confusion_matrix(y_test, y_pred)
print('\n혼동 행렬 (Confusion Matrix):')
print(cm)

# 혼동 행렬 시각화
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['예측: 비홈런', '예측: 홈런'], yticklabels=['실제: 비홈런', '실제: 홈런'])
plt.xlabel('예측값')
plt.ylabel('실제값')
plt.title('혼동 행렬 (Confusion Matrix)')
plt.show()

# ROC 곡선 및 AUC 값 (예측 성능 평가 지표)
# ROC 곡선은 0과 1 분류 모델의 성능을 시각적으로 보여줍니다.
# AUC(Area Under the Curve) 값은 1에 가까울수록 좋은 모델입니다.
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
auc_score = roc_auc_score(y_test, y_pred_proba)

plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {auc_score:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()
print(f'AUC (Area Under the Curve): {auc_score:.4f}\n')


# --- 6. 새로운 데이터로 홈런 확률 예측하기 (모듈 활용 예시) ---
print("--- 새로운 데이터로 홈런 확률 예측 ---")
# 경기 당일의 새로운 데이터 (실제 값은 다를 수 있음)
# 컬럼 순서는 학습할 때 사용한 X와 동일해야 합니다.
new_game_data = pd.DataFrame([[100, 5, 1, 90, 0.07, 0.03, 0]],
                             columns=X.columns)

# 홈런 칠 확률 예측
predicted_proba_new = model.predict_proba(new_game_data)[:, 1]

print(f"새로운 경기에서 이 선수가 홈런을 칠 확률: {predicted_proba_new[0]:.4f}")


