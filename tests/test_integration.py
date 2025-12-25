import pytest
import os

@pytest.mark.skipif(not os.getenv('DATABASE_URL'), reason="Database not configured")
def test_database_connection():
    """Test actual database connection if env var is set."""
    # This would contain actual DB connection logic
    pass
