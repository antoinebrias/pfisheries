import matplotlib.pyplot as plt
import pandas as pd
import warnings

def fish_plot(x, linecolor="steelblue", linesize=0.9, title=None, species_code_data=None, country_code_data=None, **kwargs):
    if not isinstance(x, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame")

    if x.empty:
        raise ValueError("Input data should not be empty")

    if len(x.columns) != 3:
        raise ValueError("Input data should have exactly 3 columns")

    x.columns = x.columns.str.upper()

    species_dataset = ["CATCH", "YEAR", "SPECIES"]
    country_dataset = ["CATCH", "YEAR", "COUNTRY"]

    old_theme = plt.rcParams.copy()

    plt.rcParams.update({
        'axes.facecolor': 'white',
        'axes.edgecolor': 'black',
        'grid.color': 'white'
    })

    if all(col in x.columns for col in species_dataset):
        if title is None:
            english_name = species_code_data.loc[species_code_data['a3_code'] == x['SPECIES'].unique()[0], 'english_name'].values[0]
            title = f"Landings for {english_name} ({x['SPECIES'].unique()[0]})"
        fish_plot = x.plot(x='YEAR', y='CATCH', color=linecolor, linewidth=linesize, title=title)
        fish_plot.set_xlabel("Year")
        fish_plot.set_ylabel("Catch (in tonnes)")
    elif all(col in x.columns for col in country_dataset):
        if title is None:
            country_name = country_code_data.loc[country_code_data['iso3c'] == x['COUNTRY'].unique()[0], 'country'].values[0]
            title = f"Landings for {country_name} ({x['COUNTRY'].unique()[0]})"
        fish_plot = x.plot(x='YEAR', y='CATCH', color=linecolor, linewidth=linesize, title=title)
        fish_plot.set_xlabel("Year")
        fish_plot.set_ylabel("Catch (in tonnes)")
    else:
        raise ValueError("Input data columns do not match expected format")

    plt.rcParams.update(old_theme)

    return fish_plot

