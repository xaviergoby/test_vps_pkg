import pandas as pd
import settings
import os



sell_orders = pd.read_csv(os.path.join(settings.CMPLT_ORDERS_DATASET_DIR, "sell_orders.csv"))
buy_orders = pd.read_csv(os.path.join(settings.CMPLT_ORDERS_DATASET_DIR, "buy_orders.csv"))


sell_n_buy_orders_dl_cnt = tuple(map(lambda OB_side: OB_side.shape[0], (sell_orders, buy_orders)))

print(sell_n_buy_orders_dl_cnt)