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

## wget jdbc plugins
```
wget https://packages.confluent.io/maven/io/confluent/kafka-connect-jdbc/10.7.0/kafka-connect-jdbc-10.7.0.jar
wget https://jdbc.postgresql.org/download/postgresql-42.6.0.jar -P ./plugins/jdbc/
```