import httpx
import logging
from app.services.base_fetcher import BasePriceFetcher

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

logger = logging.getLogger(__name__)


class SteamPriceFetcher(BasePriceFetcher):

    def __init__(self, timeout = 10.0, country="us"):
        self.TIMEOUT = timeout
        self.COUNTRY_CODE = country


    def price_fetch(self, external_id: str) -> float | None:

        logger.info(f"Fetching price for Steam app {external_id}")
        url = f"https://store.steampowered.com/api/appdetails?appids={external_id}&cc={self.COUNTRY_CODE}&filters=price_overview"

        if not isinstance(external_id, str) or not(external_id.isdigit()):
            logger.warning(f"Invalid external_id format or type: {external_id}")
            return None

        try:

            response = httpx.get(url, timeout=self.TIMEOUT)
            response.raise_for_status()
            data = response.json()  

            logger.debug(f"Raw API Response: {data}")

            success = data.get(external_id, {}).get('success')

            if success == True:

                game_data = data.get(external_id, {}).get('data')

                #Paid game
                if isinstance(game_data, dict):
                    return (game_data.get("price_overview", {}).get("final"))/100
                
                #Free game
                elif isinstance(game_data, list):
                    return 0.0
                else:
                    return None
            else:
                logger.warning(f"Unsuccessful price fetch for app {external_id} (game doesn't exist or fetch failed)")
                return None
            

        
        except httpx.TimeoutException:
            logger.error(f"Price fetch timed out for {external_id}")
            return None
        
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error {e.response.status_code} for app {external_id}")
            return None

        except Exception as e:
            logger.error(f"Unexpected error fetching price for {external_id}: {e}")
            return None
    
    def get_vendor_name(self) -> str:
        return "Steam"

