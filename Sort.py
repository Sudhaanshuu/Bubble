import json
import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 = st.columns(2)
with col1:

    st.markdown("""## Bubble Sort by Sudhanshu""")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)



with col1:
    lottie_now = load_lottiefile("file/code.json")
st_lottie(
    lottie_now,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height=400,
    key=None,

)
st.success("Enter elements you want to sort, separated by space")
arr = [int(x) for x in st.text_input("").split()]
n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

st.write("Sorted list:")
st.success(arr)
