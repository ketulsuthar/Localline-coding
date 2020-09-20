import pandas as pd


def find_customers_suppliers(suppliers_file,buyers_file):
    """
    :param suppliers_file:
    :param buyers_file:
    :return: It return { supplier_id , buyer_id } list of objects
    """
    #Load the supplier data
    supplier_df = pd.read_json(suppliers_file)
    #Load the Buyer data
    buyer_df = pd.read_json(buyers_file)
    #Inner Join based on Product_Category_ID
    a = pd.merge(supplier_df,buyer_df,how='inner',left_on=["product_category_id"],right_on=["product_category_id"])
    return a[['supplier_id', 'buyer_id']].to_json(orient ='records')


#print(find_customers_suppliers("product.json","customer.json"))
