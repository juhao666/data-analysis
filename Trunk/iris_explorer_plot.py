import pandas
import seaborn

iris = pandas.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
iris.columns=['sepal_length','sepal_width','petal_length','petal_width','species']

# show the data 
# %matplotlib inline
# 直方图，每种类型花的数量
seaborn.countplot(x="species",data=iris)
# 条形图，每种花的花瓣宽度
seaborn.barplot(x='species',y='petal_width',data=iris)
# 箱型图，同上
seaborn.boxplot(x='species',y='petal_width',data=iris)
# 直方图，花瓣宽度
seaborn.distplot(iris['petal_width'])
###
#Pandas库对类别进行选取，然后进行画图
iris_vir=iris[iris.species == 'Iris-virginica']
iris_s=iris[iris.species == 'Iris-setosa']
iris_ver=iris[iris.species =='Iris-versicolor']
#参数赋值，加上label&图例&设置坐标轴范围，xlim设置x轴范围，ylim设置y轴范围
seaborn.distplot(iris_vir['petal_width'],label='vir').set(ylim=(0,15))
seaborn.distplot(iris_s['petal_width'],label='s')
seaborn.distplot(iris_ver['petal_width'],label='ver').legend()
###
#FacetGrid 从数据集不同的侧面进行画图，hue指定用于分类的字段，使得代码会更加简洁
#尝试修改row/col参数，替代hue参数，row:按行展示，col：按列展示
g=seaborn.FacetGrid(iris,hue='species')
g.map(seaborn.distplot,'petal_width').add_legend()

#散点图，画出线性回归的曲线
seaborn.regplot(x='petal_width',y='petal_length',data=iris)

#散点图，分类画线性回归
g = seaborn.FacetGrid(iris,hue='species')
#设置坐标轴范围
g.set(xlim=(0,2.5))
g.map(seaborn.regplot,'petal_width','petal_length').add_legend()

#散点图， 不显示拟合曲线,用matplotlib画散点图
import matplotlib.pyplot as plt
g = seaborn.FacetGrid(iris,hue='species')
g.map(plt.scatter,'petal_width','petal_length').add_legend()