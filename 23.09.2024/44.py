st=input().lower()
print({i:st.count(i) for i in st if st.count(i)>=2})