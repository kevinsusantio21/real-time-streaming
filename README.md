# CDC with PostgreSQL and Debezium

## Real-time streaming
to do real time streaming, you need data source, the connector
- data source: PostgreSQL
- connector: Debezium connector

## connector
```
{
  "topic.prefix": "cdc",
  "database.hostname": "postgres",
  "database.user": "postgres",
  "database.password": "********",
  "database.dbname": "financial_db",
  "plugin.name": "pgoutput"
}
```