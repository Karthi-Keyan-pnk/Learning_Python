class Order:

    def __init__( self, customer_name:str,items :list[dict],
        discount_percent :float
    ):
        self.customer_name= customer_name
        self.items=items
        self.discount_percent= discount_percent