__all__ = ['getCurDir', 'getDatasetPath', 'getKaggleJson', 'getModelPath', 'r_mse', 'm_rmse', 'rf', 'rf_feat_importance', 'plot_fi', 'get_oob', 'normalize']

import fastbook

from fastbook import *
from fastai.tabular.all import Path
from sklearn.ensemble import RandomForestRegressor
from scipy.special import erfinv

def getCurDir():
    sysPath = sys.path
    return sysPath[0]

def getDatasetPath(dir):
    return Path(dir + '/prudential-life-insurance-assessment')

def getKaggleJson(dir):
    return Path(dir + '/kaggle.json')

def getModelPath(dir):
    return Path(dir + '/models')

def r_mse(pred,y): 
    return round(math.sqrt(((pred-y)**2).mean()), 6)

def m_rmse(m, xs, y): 
    return r_mse(m.predict(xs), y)

def rf(xs, y, n_estimators=40, max_samples=200_000,
       max_features=0.5, min_samples_leaf=5, **kwargs):
    return RandomForestRegressor(n_jobs=-1, n_estimators=n_estimators,
        max_samples=max_samples, max_features=max_features,
        min_samples_leaf=min_samples_leaf, oob_score=True).fit(xs, y)

def rf_feat_importance(m, df):
    return pd.DataFrame({'cols':df.columns, 'imp':m.feature_importances_}
                       ).sort_values('imp', ascending=False)

def plot_fi(fi, w, h):
    return fi.plot('cols', 'imp', 'barh', figsize=(w, h), legend=False)

def get_oob(df, trainY, max_samples=50000):
    m = RandomForestRegressor(n_estimators=40, min_samples_leaf=15,
        max_samples=max_samples, max_features=0.5, n_jobs=-1, oob_score=True)
    m.fit(df, trainY)
    return m.oob_score_


def to_gauss(x): return np.sqrt(2)*erfinv(x)  #from scipy

def normalize(data, exclude=None):
    # if not binary, normalize it
    norm_cols = [n for n, c in data.drop(exclude, 1).items() if len(np.unique(c)) > 2]
    n = data.shape[0]
    for col in norm_cols:
        sorted_idx = data[col].sort_values().index.tolist()# list of sorted index
        uniform = np.linspace(start=-0.99, stop=0.99, num=n) # linsapce
        normal = to_gauss(uniform) # apply gauss to linspace
        normalized_col = pd.Series(index=sorted_idx, data=normal) # sorted idx and normalized space
        data[col] = normalized_col # column receives its corresponding rank
    return data
