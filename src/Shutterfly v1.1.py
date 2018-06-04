import os
import sys
import re
import json
import pandas as pd
import numpy as np
from datetime import datetime
#
from sys import argv

def read_input_file(inp_file_path):
    """ Read a file into the variables """

    first_arg = inp_file_path
    print(first_arg)
    with open(first_arg, 'r') as inp_file:

        data = json.loads(inp_file.read())

        counter = int(data.__len__())
        i = 0

        customer = {}
        site_visit = {}
        image = {}
        order = {}

        customer_temp = []
        site_visit_temp = []
        image_temp = []
        order_temp = []

        while i < counter:
            m=data[i]

            customer={}
            site_visit={}
            image={}
            order={}

            for x,v in m.items():
                if m["type"] == 'CUSTOMER':
                    customer_inp = {}
                    customer_inp = {x:v}
                    customer.update(customer_inp)
                elif m["type"] == 'SITE_VISIT':
                    site_visit_inp = {}
                    site_visit_inp = {x:v}
                    site_visit.update(site_visit_inp)
                elif m["type"] == 'IMAGE':
                    image_inp={}
                    image_inp = {x:v}
                    image.update(image_inp)

                else:
                    order_inp={}
                    order_inp = {x: v}
                    order.update(order_inp)

            i = i + 1

            customer_temp.append(customer)

            site_visit_temp.append(site_visit)

            image_temp.append(image)

            order_temp.append(order)


        return customer_temp,site_visit_temp,image_temp,order_temp

def convert_dicts():

    inp_file_path=sys.argv[1]

    customer_raw, site_visit_raw, image_raw, order_raw = read_input_file(inp_file_path)

    cust_dict = []

    cust_dict = [i for i in customer_raw if i]


    site_visit_dict = []

    site_visit_dict = [i for i in site_visit_raw if i]


    image_dict = []

    image_dict = [i for i in image_raw if i]


    order_dict = []

    order_dict = [i for i in order_raw if i]

    return cust_dict,site_visit_dict,image_dict,order_dict

    inp_file.close()

def calc():

        customer,site_visit,image,order = convert_dicts()

        cust_d = pd.DataFrame.from_dict(customer)

        cust_d.rename(columns={'key': 'customer_id', 'last_name': 'Customer_name'}, inplace=True)

        colsToDrop_cust = ['adr_city','adr_state','event_time','type','verb']

        cust_df = cust_d.drop(colsToDrop_cust, axis=1)

        site_visit_d = pd.DataFrame.from_dict(site_visit)

        site_visit_d['date'] = site_visit_d.event_time.str[0:10]

        image_d = pd.DataFrame.from_dict(image)

        order_d = pd.DataFrame.from_dict(order)

        order_d['date'] = order_d.event_time.str[0:10]
        order_d['total_amount_new'] = order_d.total_amount.str[0:5]

        order_d[['total_amount_new']] = order_d[['total_amount_new']].applymap(lambda x: re.sub(r'[^0-9^\-\.]+', '', x)).replace('', np.float64(0)).astype('float64')

        order_d['order_scd'] =  order_d.groupby(['customer_id','date'])['verb'].rank(numeric_only=None,ascending=True)

        df_merge = pd.merge(site_visit_d, order_d, on=['customer_id','date'], how='inner').merge(cust_df,on='customer_id')

        order_scd_df=df_merge.loc[df_merge.groupby(['customer_id', 'date'])['order_scd'].idxmax()]

        df_visits=site_visit_d.groupby(['customer_id','date'])['date'].value_counts().sum()

        date_fil_df = (order_scd_df[(order_scd_df['date'] >= '2017-06-04') & (order_scd_df['date'] <= '2017-06-10')])

        comb_df =date_fil_df.groupby(['customer_id','Customer_name',]).agg(
            {'total_amount_new': ['sum'],  # find the min, max, and sum of the duration column
             'customer_id': ['nunique'],
              'date':['nunique']})
        comb_df.columns = ["_".join(q) for q in comb_df.columns.ravel()]

        """s= Customre expenditure per visit : total_amount_new_sum  / (date_nunique) i,e ==> total amount spent divided by no of visits
           c = total no visits per week : date_nunique
           t = 1ife span of the shutterfly
           simple customer LTV = s*c = a ==> 52 (a) * t """
        comb_df.eval( 'CLTV = (total_amount_new_sum / (date_nunique))* date_nunique *  52 * 10', inplace=True)

        colsToDrop = ['customer_id_nunique','total_amount_new_sum','date_nunique']

        inter_df = comb_df.drop(colsToDrop, axis=1)

        inter_df['Top_rnk'] = inter_df['CLTV'].rank(ascending=True)

        inter_df.sort_values('CLTV', ascending=False,inplace=True)

        return inter_df


def main():

    script, inp_file_path, out_file_path = argv

    x = read_input_file(inp_file_path)

    y = calc()

    file = open(out_file_path, 'w')

    print("Dear User")

    value = str(y) + '\n'

    file.write(value)

    print("The output is written " + str(out_file_path))

    file.close()


if __name__ == "__main__":
     main()