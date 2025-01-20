from sqlalchemy import MetaData
from sqlalchemy.orm import registry

convention = {
    # INDEX
    "ix": "ix_%(column_0_label)s",
    # UNIQUE
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    # CHECK
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    # FOREIGN KEY
    "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",
    # PRIMARY KEY
    "pk": "pk_%(table_name)s",
}
_metadata = MetaData(naming_convention=convention)
mapper_registry = registry(metadata=_metadata)
