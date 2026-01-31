from abc import ABC, abstractmethod

class BasePriceFetcher(ABC):
    @abstractmethod
    def price_fetch(self, external_id: str) -> float | None:
        """
        Fetch price for a product from this vendor.
        
        Args:
            external_id: Vendor-specific product identifier
            
        Returns:
            Price as float, or None if not found/error
        """
        pass

    @abstractmethod
    def get_vendor_name(self) -> str:
        """Return the vendor name (e.g., 'Steam')"""
        pass

