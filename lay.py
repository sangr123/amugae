import streamlit as st

# 타이틀 출력
st.title("기업 토픽")

# 사이드바 타이틀
st.sidebar.title("기업 검색")

# 검색어 입력 받기
search_query = st.sidebar.text_input("검색")

# 검색어를 메인에 출력
if search_query:
    st.header(search_query)

# 레이아웃 만들기
# 3개의 열을 생성
col1, col2, col3 = st.columns(3)

# 첫 번째 열에 내용 추가
with col1:
    st.header("2020")
    st.write("이 열은 왼쪽에 위치합니다.")

# 두 번째 열에 내용 추가
with col2:
    st.header("2021")
    st.write("이 열은 중앙에 위치합니다.")

# 세 번째 열에 내용 추가
with col3:
    st.header("2022")
    st.write("이 열은 오른쪽에 위치합니다.")

# streamlit run lay.py