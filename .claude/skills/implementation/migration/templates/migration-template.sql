-- ============================================================================
-- Migration Template
-- ============================================================================
-- Description: [Brief description of what this migration does]
-- Created:     [YYYY-MM-DD]
-- Author:      [Name/Team]
-- Ticket:      [JIRA/Issue number if applicable]
--
-- IMPORTANT: Always test this migration on a copy of production data before
-- running in production. Ensure the DOWN migration works correctly.
-- ============================================================================

-- ============================================================================
-- UP MIGRATION
-- ============================================================================
-- Run this section to apply the migration
-- ============================================================================

BEGIN;

-- ----------------------------------------------------------------------------
-- 1. Create new tables
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS example_table (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    status VARCHAR(50) NOT NULL DEFAULT 'active',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Add comment for documentation
COMMENT ON TABLE example_table IS 'Example table for demonstration';
COMMENT ON COLUMN example_table.status IS 'User status: active, inactive, suspended';

-- ----------------------------------------------------------------------------
-- 2. Add columns to existing tables
-- ----------------------------------------------------------------------------
-- ALTER TABLE existing_table
--     ADD COLUMN IF NOT EXISTS new_column VARCHAR(255),
--     ADD COLUMN IF NOT EXISTS another_column INTEGER DEFAULT 0;

-- ----------------------------------------------------------------------------
-- 3. Create indexes
-- ----------------------------------------------------------------------------
-- Use CONCURRENTLY for large tables to avoid locking
-- Note: CONCURRENTLY cannot be used inside a transaction

-- For small tables (inside transaction):
CREATE INDEX IF NOT EXISTS idx_example_table_email
    ON example_table(email);

CREATE INDEX IF NOT EXISTS idx_example_table_status
    ON example_table(status)
    WHERE status = 'active';

-- For large tables (run separately, outside transaction):
-- CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_large_table_column
--     ON large_table(column);

-- ----------------------------------------------------------------------------
-- 4. Add constraints
-- ----------------------------------------------------------------------------
-- ALTER TABLE example_table
--     ADD CONSTRAINT check_status
--     CHECK (status IN ('active', 'inactive', 'suspended'));

-- ----------------------------------------------------------------------------
-- 5. Data migrations (if needed)
-- ----------------------------------------------------------------------------
-- UPDATE example_table
--     SET new_column = 'default_value'
--     WHERE new_column IS NULL;

-- ----------------------------------------------------------------------------
-- 6. Create triggers (if needed)
-- ----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_example_table_updated_at
    BEFORE UPDATE ON example_table
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at();

COMMIT;

-- ============================================================================
-- DOWN MIGRATION
-- ============================================================================
-- Run this section to rollback the migration
-- ============================================================================

-- Uncomment and run to rollback:

-- BEGIN;
--
-- -- Drop triggers
-- DROP TRIGGER IF EXISTS trigger_example_table_updated_at ON example_table;
--
-- -- Drop functions
-- DROP FUNCTION IF EXISTS update_updated_at();
--
-- -- Drop indexes
-- DROP INDEX IF EXISTS idx_example_table_email;
-- DROP INDEX IF EXISTS idx_example_table_status;
--
-- -- Drop constraints
-- -- ALTER TABLE example_table DROP CONSTRAINT IF EXISTS check_status;
--
-- -- Remove columns
-- -- ALTER TABLE existing_table
-- --     DROP COLUMN IF EXISTS new_column,
-- --     DROP COLUMN IF EXISTS another_column;
--
-- -- Drop tables
-- DROP TABLE IF EXISTS example_table;
--
-- COMMIT;

-- ============================================================================
-- VERIFICATION QUERIES
-- ============================================================================
-- Run these queries to verify the migration was successful

-- Check table exists
-- SELECT EXISTS (
--     SELECT FROM information_schema.tables
--     WHERE table_name = 'example_table'
-- );

-- Check columns exist
-- SELECT column_name, data_type, is_nullable
-- FROM information_schema.columns
-- WHERE table_name = 'example_table';

-- Check indexes exist
-- SELECT indexname, indexdef
-- FROM pg_indexes
-- WHERE tablename = 'example_table';

-- ============================================================================
-- NOTES
-- ============================================================================
-- - This migration creates the example_table with basic fields
-- - Indexes are added for common query patterns
-- - The updated_at trigger automatically updates timestamps
-- - Review the DOWN migration before running in production
-- ============================================================================
