from azure.cosmos import PartitionKey
from azure.cosmos.aio import CosmosClient
import asyncio

# Reemplaza esta cadena de conexión por la tuya
connection_string = ""

async def main():
    async with CosmosClient.from_connection_string(connection_string) as client:
        # Ejemplo: acceder a la base de datos y contenedor
        database = await client.create_database_if_not_exists(id="cosmicworks")
        container = await database.create_container_if_not_exists(
            id="products",
            partition_key=PartitionKey(path="/categoryId")
        )

        # saddle = {
        #    "id": "706cd7c6-db8b-41f9-aea2-0e0c7e8eb009",
        #    "categoryId": "9603ca6c-9e28-4a02-9194-51cdb7fea816",
        #   "name": "Road Saddle",
        #   "price": 45.99,
        #   "tags": ["tan", "new", "crisp"]
        # }
            
        # await container.create_item(body=saddle)

        item_id = "706cd7c6-db8b-41f9-aea2-0e0c7e8eb009"
        partition_key = "9603ca6c-9e28-4a02-9194-51cdb7fea816"

        # Read item    
        saddle = await container.read_item(item=item_id, partition_key=partition_key)
        # print(f'[{saddle["id"]}]\t{saddle["name"]} ({saddle["price"]})')

        # saddle["price"] = 32.55
        # saddle["name"] = "Road LL Saddle"
        # await container.replace_item(item=saddle, body=saddle)

        # Delete the item
        await container.delete_item(item=item_id, partition_key=partition_key)



if __name__ == "__main__":
    asyncio.run(main())