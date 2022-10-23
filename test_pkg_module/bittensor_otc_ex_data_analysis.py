import pandas as pd
import settings


def reformat_orders_df(orders_df):
    orders_df.drop(columns=orders_df.columns[0], axis=1, inplace=True)
    reformated_orders_df = orders_df.rename(columns={orders_df.columns[0]: "TickIndex"})
    return reformated_orders_df

def get_non_dt_xmins_res_df_rows(orders_df, dt_xmins_res=5):
    valid_dt_mins = [f":{item}" for item in list(range(61)) if item % dt_xmins_res == 0]
    non_dt_xmins_res_df_rows = orders_df[orders_df["Datetime"].str.contains('|'.join(valid_dt_mins))]
    return non_dt_xmins_res_df_rows

def group_orders_df_by_tick_dt_res(orders_df, freq_min="5Min", df_col_name="Datetime"):
    grouped_orders_df = orders_df.groupby(pd.Grouper(key=df_col_name, freq=freq_min))
    return grouped_orders_df

def group_orders_df_by_unique_tick_dts(orders_df, df_col_name="Datetime"):
    grouped_orders_df = orders_df.groupby(df_col_name, group_keys=True).apply(lambda x: x)
    return grouped_orders_df

def get_ob_tick_dts(df):
    grouped_df = group_orders_df_by_unique_tick_dts(df)
    tick_dts = grouped_df.index.levels[0].to_list()



sell_df = pd.read_csv(f"{settings.SCRAPED_DATASETS_DIR}/sell_orders.csv")
buy_df = pd.read_csv(f"{settings.SCRAPED_DATASETS_DIR}/buy_orders.csv")

sell_df_copy = sell_df.copy()
buy_df_copy = buy_df.copy()

sdf = reformat_orders_df(sell_df_copy)
bdf = reformat_orders_df(buy_df_copy)

# sdf["Datetime"] = pd.to_datetime(sdf["Datetime"], format="%d/%m/%Y %H:%M")
# bdf["Datetime"] = pd.to_datetime(bdf["Datetime"], format="%d/%m/%Y %H:%M")
res = get_non_dt_xmins_res_df_rows(sell_df)