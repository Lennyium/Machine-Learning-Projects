import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knick_pts_10 = nba_2010.pts[nba.fran_id=='Knicks']
nets_pts_10 = nba_2010.pts[nba.fran_id=='Nets']

diff_means_2010 = knick_pts_10.mean() - nets_pts_10.mean()
print(diff_means_2010)

# Histograms of both team points 2010
plt.hist(knick_pts_10, alpha=0.5, normed=True, label='Knicks')
plt.hist(nets_pts_10, alpha=0.5, normed=True, label='Nets')
plt.show()
plt.close()

knicks_pts_14 = nba_2014.pts[nba_2014.fran_id=='Knicks']
nets_pts_14 = nba_2014.pts[nba_2014.fran_id=='Nets']

# Histograms 2014
diff_means_2014 = knicks_pts_14.mean() - nets_pts_14.mean()
print(diff_means_2014)
plt.hist(knicks_pts_14, alpha=0.5, normed=True, label='Knicks')
plt.hist(nets_pts_14, alpha=0.5, normed=True, label='Nets')
plt.show()
plt.close()

# Boxplots

sns.boxplot(x='fran_id', y='pts', data=nba_2010)
plt.show()
plt.close()

location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)

#Chi Square statistic

chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)

point_diff_forecast_cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_cov)

point_diff_forecast_corr, p = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

# Scatterplot
plt.scatter(x='forecast', y='point_diff', data=nba_2010)
plt.xlabel('Forecast')
plt.ylabel('Point Difference')
plt.show()
plt.close()
