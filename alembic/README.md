# Alembic Operations
- Generic single-database configuration.
- Database shema modification and data migration
## Handy commands
- `pip install alembic`
- `alembic init alembic`
- `alembic revision --autogenerate -m "Initial migration"`
- `alembic revision -m "Add new column to users table"`
- `alembic upgrade head`
- `alembic downgrade <previous_revision_id>`