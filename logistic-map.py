import numpy as np
import pandas as pd
import streamlit as st


def update_logistic_map_value(x, alpha):
    return alpha * x * (1 - x)


st.title('Logistic Map')
st.markdown('[learning material](https://rocs.hu-berlin.de/courses/complex-systems-2021/script/the-logistic-map/)')

st.latex(r''' x_{n+1} = \alpha x_n(1 - x_n), n = 0,1,2,3...''')

x_0 = st.slider('x_0', min_value=0.0, max_value=1.0)
alpha = st.slider('alpha', min_value=1e-2, max_value=4-1e-2)
n = st.slider('n', min_value=0, max_value=100)

x_data = [x_0]


for i in range(n):
    x_data.append(update_logistic_map_value(x_data[i], alpha))

st.line_chart(
    pd.DataFrame(
        np.array(x_data),
        columns=['x']
    )
)
