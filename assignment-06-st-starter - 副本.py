# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# show the title
st.title('Titanic Data Analysis by Yiran Lu')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.write(df)



# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 绘制 PClass = 1 的票价箱线图
df[df['Pclass'] == 1]['Fare'].plot(kind='box', ax=axes[0])
axes[0].set_title('Fare - PClass 1')
axes[0].set_xlabel('Pclass')
axes[0].set_ylabel('Fare')

# 绘制 PClass = 2 的票价箱线图
df[df['Pclass'] == 2]['Fare'].plot(kind='box', ax=axes[1])
axes[1].set_title('Fare - PClass 2')
axes[1].set_xlabel('Pclass')
axes[1].set_ylabel('Fare')

# 绘制 PClass = 3 的票价箱线图
df[df['Pclass'] == 3]['Fare'].plot(kind='box', ax=axes[2])
axes[2].set_title('Fare - PClass 3')
axes[2].set_xlabel('Pclass')
axes[2].set_ylabel('Fare')

# 自动调整子图参数，使之填充整个图像区域
plt.tight_layout()

# 显示图形
st.pyplot(fig)
