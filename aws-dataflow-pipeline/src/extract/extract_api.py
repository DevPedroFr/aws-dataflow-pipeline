import requests
import pandas as pd

def extract_users_from_api():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)
        response.raise_for_status()  #erro caso a requuisição falhe

        users = response.json()

        data = []
        for user in users:
            data.append({
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"],    
            })

        df = pd.DataFrame(data)
        print(" Dados extraídos da api:")
        print(df.head())

        df.to_csv('data_api_users.csv', index=False)

        return df
    
    except Exception as e:
        print(f"Erro ao extrairt dados da api: {e}")

if __name__ == "__main__":
    extract_users_from_api()
