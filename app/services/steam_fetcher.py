import httpx

#API URL Structure: https://store.steampowered.com/api/appdetails?appids={GAME_ID}&cc=us&filters=price_overview

#SUCCESSFUL REQUEST
#   GAME_ID = steam id
#   PRICE = final price after discount in the form 2499 ($24.99)
#{"{GAME_ID}": {"success":true, "data":{"price_overview":{"final":"{PRICE}"}}}}


#UNSUCCESSFUL REQUEST
#   GAME_ID = steam id
#{"{GAME_ID}": {"success": false}}

#FREE GAME
#   GAME_ID = steam id
#{"{GAME_ID}": {"success":true, "data":[]}}


def fetch_steam_price(app_id: str) -> float | None:

    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&cc=us&filters=price_overview"

    try:

        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        data = response.json()  

        success = data.get(app_id, {}).get('success')

        if success == True:

            game_data = data.get(app_id, {}).get('data')

            #Paid game
            if isinstance(game_data, dict):
                return (data.get(app_id, {}).get('data', {}).get("price_overview", {}).get("final"))/100
            
            #Free game
            elif isinstance(game_data, list):
                return 0.0
        else:
            return None
        

    
    except httpx.TimeoutException:
        print(f"Request timed out for {app_id}")
        return None
    
    except httpx.HTTPStatusError as e:
        print(f"HTTP error {e.response.status_code} for {app_id}")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


