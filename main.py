from fastapi import FastAPI, HTTPException, Header, Response
import pandas as pd

app = FastAPI()

# define api_key
api_key = "secret123"


# @app.get("/")
# def root():



# # define url --> endpoint
# @app.get("/")
# def root(key: str = Header(None)):
#     # cek api_key
#     if key == None or key != api_key:
#         raise HTTPException(status_code=401, detail="Invalid API Key") # raise = return
#     # Get all data from dataframe
#     df = pd.read_csv('data.csv')
#     return df.to_dict(orient='records') # Bisa .to_json (sama saja)



@app.get("/")
def root(key: str = Header(None)):
    # cek api_key
    if key == None or key != api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key") # raise = return
    # Get all data from dataframe
    df = pd.read_csv('data.csv')
    return df.to_dict(orient='records') # Bisa .to_json (sama saja)



@app.get("/detail/{id}") # {id} merupakan parameter, sebuah value yang bisa ditentukan secara dinamis
def root(id: int): # Memberikan parameter yang sama dengan yang atas
    # Get all data from dataframe
    df = pd.read_csv('data.csv')
    # filter berdasarkan id
        # df[kondisi]
        # df.query[kondisi]
    filter = df[df.id == id] # Hati-hati id bisa jadi dalam bentuk string cek lagi di def root

    # cek apakah filter kosong?
    if len(filter) == 0:
        # return pesan eror
        raise HTTPException(status_code=404, detail='data tidak ditemukan')
        
    # Menampilkan filter sebagai respon
    return filter.to_dict(orient='records')







# @app.get("/data")
# def root():
#     return {"message": "ini halaman data"}

# Untuk run gunakan (uvicorn <filename-without-the-extension>:<fast-api-instance> --reload)
# Untuk matikan server ctrl + c

