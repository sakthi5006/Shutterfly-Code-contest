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
    """input_file = "C:/Users/sgp/Documents/PycharmProjects/events.txt"""
    """ Open the file """
    """ Read a file """
    """ Split the lines into a list """
    """with open(filename_lkp, 'r') as infile:
        data = infile.read()
        my_list = data.splitlines()"""
    first_arg = inp_file_path
    print(first_arg)
    #print(out_file_path)
    #filename_lkp = "C:/Users/sgp/Documents/events.txt"
    with open(first_arg, 'r') as inp_file:
        """data_file = inp_file.read()"""
        """ my_list = data_file.splitlines()"""

        #print("sakthivasan")
        #data_normal = inp_file.read()

        data = json.loads(inp_file.read())
        #with open('C:/Users/sgp/Documents/events.txt', 'r') as f:
        #line = f.readline()
        #print(pd.read_json(line).shape)
        # m = json_normalize(data)

        #cust_data = data[0]

        #print(type(data))
        print(data)

        counter = int(data.__len__())
        print(counter)
        i = 0

        #s = [i for x in data.values() for i in data.values() if i["type"] == 'CUSTOMER']
        #print(s)
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
            #n = data[i].split(",")
            #print(n)
            #print(type(m))
            #print(m)
            #print(m.keys())
            #print(m.values())
            print(" Data of m inside the loop start")
            print(m)
            print(" Data of m inside the loop end")
            #cust_li =[]

            #unique = []
            #for elem in m:
               # if elem['type'] == 'CUSTOMER':
                 #   unique.append(elem)
            #print(unique)

            #for i in x.values()

            customer={}
            site_visit={}
            image={}
            order={}

            for x,v in m.items():
                if m["type"] == 'CUSTOMER':
                    customer_inp = {}
                    customer_inp = {x:v}
                    customer.update(customer_inp)
                    print("This is inside for loop")
                    print(customer)
                elif m["type"] == 'SITE_VISIT':
                    site_visit_inp = {}
                    site_visit_inp = {x:v}
                    site_visit.update(site_visit_inp)
                    print(site_visit)
                elif m["type"] == 'IMAGE':
                    image_inp={}
                    image_inp = {x:v}
                    image.update(image_inp)
                    print(image)
                else:
                    order_inp={}
                    order_inp = {x: v}
                    order.update(order_inp)
                    print(order)

            """
            customer_inp={}
            customer_inp = { x:v for x,v in m.items() if m["type"] == 'CUSTOMER' }
            customer.update(customer_inp)
            print(" Data of customer inside the loop start")
            print(customer)
            print(" Data of customer inside the loop end")
            #print(type(customer))

            site_visit_inp= { x:v for x,v in m.items() if m["type"] == 'SITE_VISIT'}
            site_visit.update(site_visit_inp)
            #print(site_visit)
            #print(type(site_visit))

            image_inp= { x:v for x,v in m.items() if m["type"] == 'IMAGE'}
            image.update(image_inp)
            #print(image)
            #print(type(image))

            order_inp= { x:v for x,v in m.items() if m["type"] == 'ORDER'}
            order.update(order_inp)
            #print(order)
            #print(type(order))

            #my_list = filter(lambda x: x.attribute == 'CUSTOMER', data[i])
            #print( "my list filter value is given below")
           # print(my_list)
           # y = cust_li.append(my_list)
            #print(" watch out begin")
            #print(y)
            #print(" watch out End")
            #for k,v in m.items():

                #if k["TYPE"] == "CUSTOMER":
                    #print(dict(k,v))

            #d2 = dict(((k, v) for (k, v) in m.items() if k["TYPE"][0] == "CUSTOMER"))
            #print(d2)
                #filter_str= 'TYPE'
                #filtered_dict = dict(filter(lambda items: filter_str in k[0], m.items()))
                #print(filtered_dict)

                #p= k['TYPE']
                #print(p)
                    #cust_dict = list(filter(lambda d: d['type'] in k, m))
                    #print(cust_dict)

                #print(k,v)

            """
            i = i + 1

            customer_temp.append(customer)
            print(" This is outside final loop for customer temp")
            print(customer_temp)


            site_visit_temp.append(site_visit)
            print(" This is outside final loop for site_visit temp")
            print(site_visit_temp)


            image_temp.append(image)
            print(" This is outside final loop for image temp")
            print(image_temp)


            order_temp.append(order)
            print(" This is outside final loop for order temp")
            print(order_temp)


        return customer_temp,site_visit_temp,image_temp,order_temp
"""
def remove_empty_from_dict(d):

    unwanted = ['', u'', None, False, [],{} ,'SPAM']

    #unwanted_keys = [k for k, v in d.items() if any([v is i for i in unwanted])]
    #for k in unwanted_keys: del d[k]


    counter = int(d.__len__())
    print(counter)
    l = 0

    while l < counter:
        m = d[l]
        print("inside dict counter loop")
        print(type(m))

        new_dict = {k:v for k,v in m.items() if not any([v is i for i in m] or [k is i for i in m] )}
        """ """
        new_dict = {}
        for k, v in d.items():
        if isinstance(v, dict):
            v = remove_empty_from_dict(v)
        if not v in (u'', None, {}):
            new_dict[k] = v
        print (new_dict)
        return new_dict
        
        l = l + 1
        print(new_dict)
    return new_dict
        #return unwanted_keys
"""
def convert_dicts():
    inp_file_path=sys.argv[1]
    customer_raw, site_visit_raw, image_raw, order_raw = read_input_file(inp_file_path)
    print(" This is customer raw data")
    print(customer_raw)

    print(" This is Site visit raw data")
    print(site_visit_raw)

    print(" This is Image raw data")
    print(image_raw)

    print(" This is order raw data")
    print(order_raw)

    #cust_dict=remove_empty_from_dict(customer_raw)
    cust_dict = []
    cust_dict = [i for i in customer_raw if i]
    print("This is final dict for cust without nulls")
    print(cust_dict)

    #site_visit_dict=remove_empty_from_dict(site_visit_raw)
    site_visit_dict = []
    site_visit_dict = [i for i in site_visit_raw if i]

    print("This is final dict for site without nulls")
    print(site_visit_dict)

    #image_dict=remove_empty_from_dict(image_raw)
    image_dict = []
    image_dict = [i for i in image_raw if i]
    print("This is final dict for image without nulls")
    print(image_dict)

    #order_dict=remove_empty_from_dict(order_raw)
    order_dict = []
    order_dict = [i for i in order_raw if i]
    print("This is final dict for order without nulls")
    print(order_dict)

    return cust_dict,site_visit_dict,image_dict,order_dict
    inp_file.close()
def calc():
        #print(data_normal.find('CUSTOMER',0))


        #with open('C:/Users/sgp/Documents/events.txt', 'r') as inp_file:
            ##data_file = inp_file.read()
            #my_list = data_file.splitlines()

        #print("sakthivasan")
            # data_normal = inp_file.read()

            #data = json.loads(inp_file.read())
            # with open('C:/Users/sgp/Documents/

        customer,site_visit,image,order = convert_dicts()
        #customer = data[0]
        #index = data.find('CUSTOMER', 0)

        #print(" hey guess error here below Sakthi")
        #print(customer)
        #print(type(customer))
        #cust_out = json_normalize(customer)
        #print(cust_out)

        #df = pd.DataFrame(customer.items(), columns=['Date', 'DateValue'])
        cust_dfs = []
        counter = int(customer.__len__())
        #print(counter)
        i = 0
        while i < counter:

            customer_x = customer[i]
            #print(" this data type for customer x")
            #print(type(customer_x))
            columns = list(customer_x.keys())
            values = list(customer_x.values())
            arr_len = len(values)
            cust_df = pd.DataFrame(np.array(values, dtype=object).reshape(1, arr_len), columns=columns)
            cust_dfs.append(cust_df)
            #print(" this data type for cust df")
            #print(type(cust_df))
            #print(cust_df)
            i = i + 1
        print(" this data type for cust final dfs")
        print(cust_dfs)
        print(type(cust_dfs))

        #cust_df = pd.DataFrame(np.array(values, dtype=object).reshape(1, arr_len), columns=columns)
        #print("hey GP:Cust df is here")
        #print(cust_df)


        cust_d = pd.DataFrame.from_dict(customer)
        print(" this data type for one line dfs for cust")
        print(cust_d)
        print(type(cust_d))


 
        #Here the data frame is troubled .Need to handle the nested dictionary issue here.
   
        #site_visit = data[1]
        #print(site_visit)
        #print(type(site_visit))
        #sv_out = json_normalize(site_visit)
        #print(sv_out)

        #print(site_visit)
        #print(type(site_visit))
        #cust_out = json_normalize(customer)
        #print(cust_out)

        #df = pd.DataFrame(customer.items(), columns=['Date', 'DateValue'])
        site_visit_dfs = []
        counter = int(site_visit.__len__())
        #print(counter)
        i = 0
        while i < counter:

            site_visit_x = site_visit[i]
            #print(" this data type for customer x")
            #print(type(site_visit_x))

            columns_site = list(site_visit_x.keys())
            values_site = list(site_visit_x.values())
            arr_len_site = len(values_site)

            site_visit_df = pd.DataFrame(np.array(values_site, dtype=object).reshape(1, arr_len_site), columns=columns_site)
            site_visit_dfs.append(site_visit_df)
            #print("hey GP:Site_visit df is here")
            #print(site_visit_df)
            #print(" this data type for site_visit df")
            #print(type(site_visit_df))
            #print(site_visit_df)
            i = i + 1
        print(" this data type for site visit final dfs")
        print(site_visit_dfs)
        print(type(site_visit_dfs))

        site_visit_d = pd.DataFrame.from_dict(site_visit)
        print(" this data type for one line dfs for site visit")
        print(site_visit_d)
        print(type(site_visit_d))

        site_visit_d['date'] = site_visit_d.event_time.str[0:10]
        #site_visit_d[['date']] = site_visit_d[['date']].date
        print(site_visit_d)
        #print(image)
        #print(type(order))
        #image = data[2]
        #print(image)
        #image_out = json_normalize(image)
        image_dfs=[]
        counter = int(image.__len__())
        #print(counter)
        i = 0
        while i < counter:
            image_x = image[i]
            #print(" this data type for customer x")
            #print(type(image))

            columns_image = list(image_x.keys())
            values_image = list(image_x.values())
            arr_len_image = len(values_image)

            image_df = pd.DataFrame(np.array(values_image, dtype=object).reshape(1, arr_len_image), columns=columns_image)
            image_dfs.append(image_df)
            #print("hey GP:Image df is here")
            #print(image_df)
            #print(" this data type for site_visit df")
            #print(type(image_df))
            #print(image_df)
            i = i + 1
        print(" this data type for site visit final dfs")
        print(image_dfs)
        print(type(image_dfs))

        image_d = pd.DataFrame.from_dict(image)
        print(" this data type for one line dfs for image visit")
        print(image_d)
        print(type(image_d))



        #print(order)
        #print(type(order))
        #order = data[3]
        #print(order)
        #order_out = json_normalize(order)
        order_dfs = []
        counter = int(order.__len__())
        #print(counter)
        i = 0
        while i < counter:
            order_x = order[i]
            #print(" this data type for customer x")
            #print(type(order_x))
            columns_order = list(order_x.keys())
            values_order = list(order_x.values())
            #print(values_order)
            arr_len_order = len(values_order)
            #print(arr_len_order)
            order_df = pd.DataFrame(np.array(values_order, dtype=object).reshape(1, arr_len_order), columns=columns_order)
            order_dfs.append(order_df)
            #print(len(order_df))
            #print("hey GP:order df is here")
            #print(" this data type for site_visit df")
            #print(type(order_df))
            #print(order_df)
            i = i + 1
        print(" this data type for site visit final dfs")
        print(order_dfs)
        print(type(order_dfs))
        order_out= pd.DataFrame(order_dfs)
        print(order_out)
        print(type(order_out))

        order_d = pd.DataFrame.from_dict(order)
        print(" this data type for one line dfs for image visit")
        print(order_d)
        print(type(order_d))

        order_d['date'] = order_d.event_time.str[0:10]
        order_d['total_amount_new'] = order_d.total_amount.str[0:5]
        #df = df.applymap(lambda x: re.sub(r'[^0-9^\-\.]+', '', x)).replace('', np.float64(0)).astype('float64')

        order_d[['total_amount_new']] = order_d[['total_amount_new']].applymap(lambda x: re.sub(r'[^0-9^\-\.]+', '', x)).replace('', np.float64(0)).astype('float64')

        order_d['order_scd'] =  order_d.groupby(['customer_id','date'])['verb'].rank(numeric_only=None,ascending=True)

        #order_scd_df = (order_d[(order_d['order_scd'].max)])







        #date_fil_df = (df_merge[(df_merge['date'] >= '2017-06-04') & (df_merge['date'] <= '2017-06-10')])

        #order_d['Date'] = order_d.total_amount.str[0:5]

        #order_df[['total_amount_new']] = order_df[['total_amount_new']].astype(float)


        #print(order_df)
        #print(type(order_df))

        #print("""""""""""""""'""""")
        #print("The pandas merge value is given below")

        #print("""""""""""""""'""""")

        df_merge = pd.merge(site_visit_d, order_d, on=['customer_id','date'], how='inner')
        print("This is merged db")
        print(df_merge)

        print("new order scdf")
        #order_scd_df = (df_merge[df_merge.groupby(['customer_id','date'], sort=False)['order_scd'].max().astype(int)])
        #print(order_scd_df)
        order_scd_df=df_merge.loc[df_merge.groupby(['customer_id', 'date'])['order_scd'].idxmax()]
        print(order_scd_df)
        #df_visits =df_merge.groupby('customer_id').agg({'customer_id':'count'})

        #df = df_merge.groupby('customer_id')['ID'].nunique()
        df_visits=site_visit_d.groupby(['customer_id','date'])['date'].value_counts().sum()
        #df_visits=df_merge.customer_id.value_counts()
        print("This is for no of visits")
        print(df_visits)


        #result = df_merge.groupby('customer_id').agg({'total_amount':'sum'})

        result = df_merge.groupby('customer_id')['total_amount_new'].sum()

        #print(result)

        date_fil_df = (order_scd_df[(order_scd_df['date'] >= '2017-06-04') & (order_scd_df['date'] <= '2017-06-10')])

        comb_df =date_fil_df.groupby(['customer_id']).agg(
            {'total_amount_new': ['sum'],  # find the min, max, and sum of the duration column
             'customer_id': ['nunique'],
              'date':['nunique']})
        comb_df.columns = ["_".join(q) for q in comb_df.columns.ravel()]

        print(comb_df)

        #print(comb_df[(comb_df['date'] > '2017-06-01') & (comb_df['date'] < '2017-06-06')])

        #df_date = pd.DataFrame({'date': pd.date_range(start=dt.datetime(2017, 6, 1), end=dt.datetime.now())})
        #df[(df['date'] > '2015-02-04') & (df['date'] < '2015-02-10')]


        print(comb_df)

        #t = 10.00
        #comb_df['CLTV'] = comb_df['total_amount_new_sum'] * (comb_df['customer_id_nunique'] * 52 * t)
        """s= Customre expenditure per visit : total_amount_new_sum  / (date_nunique) i,e ==> total amount spent divided by no of visits
           c = total no visits per week : date_nunique
           t = 1ife span of the shutterfly
           simple customer LTV = s*c = a ==> 52 (a) * t """
        comb_df.eval( 'CLTV = (total_amount_new_sum / (date_nunique))* date_nunique *  52 * 10', inplace=True)
        #def ret_calc(inp):
        #inp['']

        print(comb_df)

        #final_df = comb_df[['customer_id','CLTV']]

        colsToDrop = ['customer_id_nunique','total_amount_new_sum','date_nunique']
        inter_df = comb_df.drop(colsToDrop, axis=1)

        print(inter_df)

        inter_df['Top_rnk'] = inter_df['CLTV'].rank(ascending=True)
        inter_df.sort_values('CLTV', ascending=False,inplace=True)
        #inter_df.sort_values(['Top_rnk'], inplace=True)
        print(inter_df)
        return inter_df
        #comb_df['topxCLTV'] = comb_df.groupby(['customer_id','customer_id_nunique'])['CLTV'].sum()
        #print(comb_df)


        #d,y,z=result
        #print(d,y,z)




        #df1 = pd.DataFrame(dict(customer))
        #print(df1)
        #print(df1.loc[df1['type'] == 'CUSTOMER'])






def main():
    script, inp_file_path, out_file_path = argv

    print("sakthi")
    x = read_input_file(inp_file_path)
    #print(x)
    y = calc()
    # m,n,p,o = convert_dicts()
    #print("new cust output starts here")
    #print(m)
    #print("new site for order  starts here")
    #print(n)
    #print("new image for order  starts here")
    #print(p)
    #print("new dicts for order  starts here")
    #print(o)
    file = open(out_file_path, 'w')
    print("Dear User")
    value = str(y) + '\n'
    file.write(value)
    print("The output is written " + str(out_file_path))
    file.close()


if __name__ == "__main__":
     main()