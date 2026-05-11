Curso de CosmosDB

En este repositorio de GitHub podrás encontrar los ejercicios y recuroso para dominar CosmosDB.

Autores:
Dámaris :)

Pasos para crear base de datos en cosmosdb by adrian
2. Crear la Cuenta de Cosmos DB
az cosmosdb create \
    --name mi-cuenta-cosmos \
    --resource-group MiGrupoRecursos \
    --kind GlobalDocumentDB \
    --locations regionName=eastus failoverPriority=0

3. Crear la Base de Datos
az cosmosdb sql database create \
    --account-name mi-cuenta-cosmos \
    --resource-group MiGrupoRecursos \
    --name MiBaseDeDatos
