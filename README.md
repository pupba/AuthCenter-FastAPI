# 🔒 Auth Center

## Skills
<img src="https://img.shields.io/badge/Python-3.11.0-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /> 
<img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white" /> 
<img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white" />
<img src="    https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" /> 

## 기능
1. 사용자 인증
    - 사용자의 계정 인증을 위한 DB

2. API Key 발급 및 인증
    - 사용자 계정별 API Key를 저장

## 실행 방법
1. 의존성 설치
    ```bash
    conda create --yes -n <your-env-name> python=3.11.0
    conda activate <your-env-name>
    pip install -r requirements.txt
    ```
2. 실행 
``
python -m auth_server
python3 -m auth_server
``
3. 테스트
``
python -m test
python3 -m test
``

# Endpoint

## /login
- **URL**: `/login`
- **Method**: `POST`
- **요청 본문**:
  - `application/x-www-form-urlencoded`
    - `username`: 사용자 이름 (필수)
    - `password`: 비밀번호 (필수)
    - `grant_type`: (선택) "password" 또는 null
    - `scope`: (선택) 기본값은 빈 문자열
    - `client_id`: (선택) 문자열 또는 null
    - `client_secret`: (선택) 문자열 또는 null

- **응답**:
  - **200 OK**: 로그인 성공
    - 응답 본문:
      ```json
      {
        "username": "사용자 이름",
        "token": "토큰" // null일 수 있음
      }
      ```
  - **422 Unprocessable Entity**: 유효성 검사 오류
    - 응답 본문:
      ```json
      {
        "detail": [
          {
            "loc": ["위치"],
            "msg": "메시지",
            "type": "오류 유형"
          }
        ]
      }
      ```

## /get-api-key
- **URL**: `/get-api-key`
- **Method**: `GET`
- **보안**: OAuth2 인증 필요

- **응답**:
  - **200 OK**: API 키 가져오기 성공
    - 응답 본문:
      ```json
      {
        "username": "사용자 이름",
        "apikey": "API 키" // null일 수 있음
      }
      ```
## /auth-api-key
- **URL**: `/auth-api-key`
- **Method**: `POST`
- **요청 본문**:
  - `application/x-www-form-urlencoded`
    - `username`: 사용자 이름 (필수)
    - `api_key`: API 키 (필수)

- **응답**:
  - **200 OK**: API 키 인증 성공
    - 응답 본문:
      ```json
      {
        "username": "사용자 이름",
        "apikey": "API 키",
        "success": true
      }
      ```
  - **422 Unprocessable Entity**: 유효성 검사 오류
    - 응답 본문:
      ```json
      {
        "detail": [
          {
            "loc": ["위치"],
            "msg": "메시지",
            "type": "오류 유형"
          }
        ]
      }
      ```

