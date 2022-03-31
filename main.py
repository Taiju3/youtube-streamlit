import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')
#st.write('DataFrame')
#st.write('Display Image')
st.write('interactiveなウィジェット')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# st.dataframe(df.style.highlight_max(axis=1), width=200, height=200)

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """


# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.line_chart(df)


# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)




# if st.checkbox('Show Image'):
#     img = Image.open(r'C:\Users\taiju\OneDrive\画像\Saved Pictures\IMG_9776.jpg')
#     st.image(img, caption='sunset with MAZDA2', use_column_width=True)

# option = st.selectbox(
#     'あなたの誕生月を教えてください。',
#     list(range(1, 13))
# )

# 'あなたの誕生月は', option, '月ですね。'

# text = st.text_input('What is your hobby?')
# 'your hobby is :', text


# condition = st.sidebar.slider('今のあなたの調子はどう？', 0, 100, 50)
# '今のあなたのコンディション:', condition


# left_column, right_column = st.columns(2)

# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
    

'Done!!!!!'

expander = st.expander('この商品は何か月で壊れますか？')
expander.write('私が使った感じだと、三か月はもちます。それ以降は使い方によると思います。')

