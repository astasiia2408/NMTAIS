import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def count_gender_based_on_height(data: pd.DataFrame) -> dict[str, int]:
    data['gender'] = data['gender'].map({2: 'Male', 1: 'Female'})

    female_count = len(data[(data['gender'] == 'Female') & (data['height'] > 0)])  # Підраховуємо жінок
    male_count = len(data[(data['gender'] == 'Male') & (data['height'] > 0)])  # Підраховуємо чоловіків

    return {'female': female_count, 'male': male_count}


def alcohol_consumption_by_gender(data: pd.DataFrame) -> str:
    female_alcohol = data[data['gender'] == 'female']['alco'].sum()
    male_alcohol = data[data['gender'] == 'male']['alco'].sum()

    if female_alcohol > male_alcohol:
        return 'Female'
    else:
        return 'Male'


def smoking_percentage_difference_by_gender(data: pd.DataFrame) -> float:
    male_smokers = data[(data['gender'] == 1) & (data['smoke'] == 1)].shape[0]
    female_smokers = data[(data['gender'] == 2) & (data['smoke'] == 1)].shape[0]
    male_percentage = male_smokers / data[data['gender'] == 1].shape[0] * 100
    female_percentage = female_smokers / data[data['gender'] == 2].shape[0] * 100
    return round(abs(male_percentage - female_percentage))


def age_difference_between_smokers_and_nonsmokers(data: pd.DataFrame) -> int:
    smokers_age = data[data['smoke'] == 1]['age']
    nonsmokers_age = data[data['smoke'] == 0]['age']
    return abs(smokers_age.median() - nonsmokers_age.median()) // 30  # Перевести в місяці


def bmi_comparison_healthy_nondrinkers(data: pd.DataFrame) -> str:
    """
    Створіть колонку з ІМТ та порівняйте ІМТ здорових непитущих чоловіків та жінок.
    """
    data['bmi'] = data['weight'] / ((data['height'] / 100) ** 2)
    healthy_nondrinkers = data[(data['alco'] == 0) & (data['bmi'] > 18.5) & (data['bmi'] < 25)]
    male_bmi = healthy_nondrinkers[healthy_nondrinkers['gender'] == 1]['bmi'].mean()
    female_bmi = healthy_nondrinkers[healthy_nondrinkers['gender'] == 2]['bmi'].mean()
    return 'Yes' if male_bmi > female_bmi else 'No'

def find_min_age_with_more_cardio(data: pd.DataFrame) -> int:
    cardio_data = data[data['cardio'] == 1]

    # Знаходимо мінімальний вік серед цих людей
    min_age = cardio_data['age'].min()

    # Перетворюємо вік з мілісекунд в роки (припустимо, що це час у мілісекундах)
    min_age_years = min_age // 365  # перетворюємо в роки, якщо дані в мілісекундах
    return min_age_years



def cholesterol_vs_cardio(data: pd.DataFrame) -> pd.Series:
    """
    Обчисліть відсоток людей із ССЗ для кожного рівня холестерину.
    """
    cholesterol_cardio = data.groupby('cholesterol')['cardio'].mean() * 100
    return cholesterol_cardio

def calculate_blood_pressure_correlation(data: pd.DataFrame) -> float:
    """
    Обчисліть кореляцію між артеріальним тиском та ССЗ.
    """
    return data[['ap_hi', 'ap_lo', 'cardio']].corr().iloc[0, 2]

def physical_activity_vs_cardio(data: pd.DataFrame) -> pd.Series:
    """
    Порівняйте відсоток людей із ССЗ серед тих, хто займається фізичною активністю, і тих, хто не займається.
    """
    activity_cardio = data.groupby('active')['cardio'].mean() * 100
    return activity_cardio

def violin_plot_height_by_gender(data: pd.DataFrame) -> None:
    data_long = pd.melt(data, id_vars=['gender'], value_vars=['height'],
                        var_name='variable', value_name='value')

    # Створюємо violin plot
    plt.figure(figsize=(8, 6))
    sns.violinplot(x="variable", y="value", hue="gender", data=data_long)

    # Відображаємо графік (без блокування)
    plt.show(block=False)

def countplot_age_vs_cardio(data: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 6))
    sns.countplot(x="age", hue="cardio", data=data)
    plt.show()

def blood_pressure_vs_cardio(data: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="ap_hi", y="ap_lo", hue="cardio", data=data)
    plt.show()

if name == 'main':
    data = pd.read_csv('cardio.zip', compression='zip', sep=";")
    print(f"Task 1:\n{count_gender_based_on_height(data)}\n")
    print(f"Task 2:\n{alcohol_consumption_by_gender(data)}\n")
    print(f"Task 3:\n{smoking_percentage_difference_by_gender(data)}\n")
    print(f"Task 4:\n{age_difference_between_smokers_and_nonsmokers(data)}\n")
    print(f"Task 5:\n{bmi_comparison_healthy_nondrinkers(data)}\n")
    print(f"Task 6:\n{find_min_age_with_more_cardio(data)}\n")
    print(f"Task 7:\n{cholesterol_vs_cardio(data)}\n")
    print(f"Task 8:\n{calculate_blood_pressure_correlation(data)}\n")
    print(f"Task 9:\n{physical_activity_vs_cardio(data)}\n")
    violin_plot_height_by_gender(data)
    countplot_age_vs_cardio(data)
    blood_pressure_vs_cardio(data)
    input("Press any key to stop the script")