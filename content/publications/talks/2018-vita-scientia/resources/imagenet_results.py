import pandas
import matplotlib.pyplot as plt
import seaborn as sns
sns.reset_orig()

df = [(2010, 28.191),
        (2011, 25.770),
        (2012, 16.422),
        (2013, 11.743),
        (2014, 6.656),
        (2015, 3.567),
        (2016, 2.991),
        (2017, 2.251)]

df = pandas.DataFrame(df, columns=['year', '% top 5 error'])
# df['performance'] = 100 - df['% top 5 error']
sns.factorplot(data=df, x='year', y='% top 5 error')
# plt.ylim([0,100])
plt.savefig('../img/imagenet_results.png', dpi=300)
plt.show()