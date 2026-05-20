from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential

endpoint = "https://fanogarcosmosdb.documents.azure.com:443/"
credential = DefaultAzureCredential()

client = CosmosClient(endpoint, credential=credential)

def main():
    account_info = client.get_database_account()
    print(f"Consistency Policy:	{account_info.ConsistencyPolicy}")
    print(f"Primary Region: {account_info.WritableLocations[0]['name']}")

if __name__ == "__main__":
    main()