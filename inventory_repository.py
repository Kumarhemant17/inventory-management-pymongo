from pymongo.errors import PyMongoError
from db_connection import initialize_database

#add product
def add_product(product_data):
    try:
        collection=initialize_database()
        collection.insert_one(product_data)
        return True
    except PyMongoError as e:
        return False, str(e)
    
#get all product
def get_all_products():
    try:
        collection=initialize_database()
        products=list(collection.find())  
        return products
    except PyMongoError:
        return []
    
#get products by filter
def get_products_by_filter(filter_conditions):
    try:
        collection = initialize_database()
        products =list(collection.find(filter_conditions))
        return products
    except PyMongoError:
        return []
    
#get single product
def get_product_by_id(product_identifier):
    try:
        collection = initialize_database()
        product= collection.find_one(product_identifier)
        return product
    except PyMongoError:
        return None
    
#update product fields
def update_product_fields(product_identifier, updated_fields):
    try:
        collection = initialize_database()
        result = collection.update_one(
            product_identifier,
            {"$set": updated_fields}
        )
        return result.modifed_count>0
    except PyMongoError:
        return False
    
#delete product
def delete_product(product_identifier):
    try:
        collection = initialize_database()
        result = collection.delete_one(product_identifier)
        return result.deleted_count > 0
    except PyMongoError:
        return False