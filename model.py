def get_full_dataset():
    """
        Load in the full dataset scraped from btcinfocharts
        Extract and return only a dataframe with the selected features
    """

    import pandas as pd

    path = './Merged_Unconverted_BTC_Data.csv'
    full_df = pd.read_csv(path)

    features = [
            'median_transaction_fee3momUSD',
            'fee_to_reward7momUSD',
            'top100cap7mom',
            'mining_profitability7rsi',
            'top100cap14mom',
            'price3wmaUSD',
            'transactionvalue90emaUSD',
            'difficulty30sma',
            'fee_to_reward90smaUSD'
            ]

    # combine date and features
    columns = ['Date'] + features

    # extract only the data from the features desired
    select_df = full_df[columns]

    return select_df


def preprocess_the_data():
    """
        Takes in a dataframe of all the data
        to fit the scaler using MinMaxScaler and RobustScaler
        Then transform the new data using the scaler and retun it as a vector
    """

    from btcinfocharts_scraper import grab_the_data
    import joblib

    # load the scaler
    scale = joblib.load('./scaler/scaler.save') 

    # get the new dataset for the most recent data
    new_df, todays_date = grab_the_data()

    # scale the new data
    transformed_new_data = scale.transform(new_df)

    return transformed_new_data, todays_date


def prediction():

    """
        Takes in the current data scraped from btcinfocharts.org
        and returns a price prediction for tomorrow
        Output is a 2D array
        Example array([[59300.715]], dtype=float32)
    """

    from keras.models import load_model

    # load the best model from the training and testing
    ann_model = load_model('./trained_models/ANN4_reg_nextday300Adam0-01relu64Int4_341.hdf5')

    # load the current scaled data
    current_scaled_data, todays_date = preprocess_the_data()

    # make the prediction
    pred_next_day_price = ann_model.predict(current_scaled_data)

    return pred_next_day_price, todays_date
