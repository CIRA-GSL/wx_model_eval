"""Setup file for wx_model_eval."""

from setuptools import setup

PACKAGE_NAMES = [
    'wx_model_eval', 'wx_model_eval.io', 'wx_model_eval.utils',
    'wx_model_eval.plotting', 'wx_model_eval.scripts',
    'wx_model_eval.outside_code'
]
KEYWORDS = [
    'machine learning', 'deep learning', 'artificial intelligence',
    'data-mining',
    'weather', 'meteorology',
    'model evaluation', 'forecast evaluation',
    'NWP', 'numerical weather prediction',
    'AIWP', 'artificial-intelligence weather prediction',
    'DLWP', 'deep-learning weather prediction',
    'uncertainty quantification', 'uncertainty evaluation'
]
SHORT_DESCRIPTION = (
    'End-to-end evaluation pipeline for any weather model that produces '
    'gridded fields (NWP, AIWP, etc.).'
)
LONG_DESCRIPTION = (
    'wx_model_eval is an end-to-end pipeline for evaluating any weather model '
    'that produces fields on a horizontal grid.  wx_model_eval is agnostic to '
    'the grid specifications, i.e., the grid can be lat/long or in a projected '
    'coordinate system.  However, for global models, wx_model_eval might have '
    'problems with domains that cross the International Date Line.  '
    'wx_model_eval allows for spatial (by grid point), temporal (by time of '
    'day [hour] or time of year [month]), and spatiotemporal (both) '
    'stratification of forecast evaluation.  wx_model_eval also includes '
    '"deep dive" evaluation methods, such as the attributes diagram, Taylor '
    'diagram, comparison of full distributions, comparison of distribution '
    'tails (left or right), plotting the full error distribution as a function '
    'of predicted or observed value, spread-skill plot, discard test, rank '
    'histogram (aka PIT histogram).  The last three of these methods evaluate '
    'uncertainty quantification (UQ), considering the full distribution of '
    'model predictions.  However, note that the UQ method *must* produce an '
    'ensemble.  If your UQ method produces something else -- like quantiles, '
    'parameters of a canonical distribution, etc. -- these will need to be '
    'converted to an ensemble.'
)

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3'
]

PACKAGE_REQUIREMENTS = [
    'numpy',
    'scipy',
    'numba',
    'matplotlib',
    'scikit-learn',
    'dill',
    'netCDF4',
    'pandas',
    'pyproj',
    'xarray',
    'shapely'
]

if __name__ == '__main__':
    setup(
        name='wx_model_eval',
        version='0.1',
        description=SHORT_DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author='Ryan Lagerquist',
        author_email='ralager@colostate.edu',
        url='https://github.com/thunderhoser/wx_model_eval',
        packages=PACKAGE_NAMES,
        scripts=[],
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        include_package_data=True,
        zip_safe=False,
        install_requires=PACKAGE_REQUIREMENTS
    )
