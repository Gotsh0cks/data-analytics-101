-- ============================================================
-- Lesson 3: CREATE, INSERT, UPDATE, DELETE
-- ============================================================
-- Run these in DB Browser for SQLite with analytics.db open.
-- Work through them one section at a time.
-- ============================================================


-- ============================================================
-- CREATE a new table
-- ============================================================

-- First, drop it if it already exists (safe to re-run)
DROP TABLE IF EXISTS projects;

CREATE TABLE projects (
    project_id   INTEGER PRIMARY KEY,  -- Auto-incrementing ID
    project_name TEXT NOT NULL,         -- Required: project name
    department   TEXT,                  -- Which department owns it
    budget       REAL,                  -- Budget in dollars
    start_date   TEXT,                  -- Start date as text (YYYY-MM-DD)
    status       TEXT DEFAULT 'Active'  -- Default to 'Active'
);

-- Verify the table was created
PRAGMA table_info(projects);


-- ============================================================
-- INSERT data into the table
-- ============================================================

-- Insert one row (notice: no project_id — it auto-fills)
INSERT INTO projects (project_name, department, budget, start_date)
VALUES ('Website Redesign', 'Marketing', 25000.00, '2024-06-01');

-- Insert multiple rows at once
INSERT INTO projects (project_name, department, budget, start_date, status)
VALUES
    ('Data Pipeline',   'Engineering', 50000.00, '2024-07-15', 'Active'),
    ('Office Move',     'HR',          15000.00, '2024-08-01', 'Planning'),
    ('Q3 Campaign',     'Marketing',   35000.00, '2024-09-01', 'Planning'),
    ('Security Audit',  'Engineering', 20000.00, '2024-06-15', 'Active'),
    ('New Hire Training','HR',         10000.00, '2024-10-01', 'Planning');

-- See what we have
SELECT * FROM projects;


-- ============================================================
-- UPDATE existing data
-- ============================================================

-- Give the Website Redesign a bigger budget
UPDATE projects
SET budget = 30000.00
WHERE project_name = 'Website Redesign';

-- Mark the Data Pipeline as in progress with a budget increase
UPDATE projects
SET status = 'In Progress',
    budget = 55000.00
WHERE project_name = 'Data Pipeline';

-- Mark all Planning projects as In Progress
UPDATE projects
SET status = 'In Progress'
WHERE status = 'Planning';

-- See the changes
SELECT project_name, budget, status FROM projects;


-- ============================================================
-- DELETE rows
-- ============================================================

-- Delete a specific project
DELETE FROM projects
WHERE project_name = 'Office Move';

-- Verify it's gone
SELECT * FROM projects;

-- Count remaining projects
SELECT COUNT(*) AS remaining_projects FROM projects;


-- ============================================================
-- ALTER TABLE — add a column
-- ============================================================

-- Add an end_date column
ALTER TABLE projects ADD COLUMN end_date TEXT;

-- Set end dates for some projects
UPDATE projects
SET end_date = '2024-12-31'
WHERE department = 'Marketing';

UPDATE projects
SET end_date = '2025-01-15'
WHERE project_name = 'Data Pipeline';

-- Final state of the table
SELECT * FROM projects;


-- ============================================================
-- PRACTICE: Try these on your own!
-- ============================================================

-- 1. Insert a new project for the Finance department
-- 2. Update all Engineering projects to have a 10% budget increase
--    Hint: SET budget = budget * 1.10
-- 3. Delete all projects with a budget under 15000
-- 4. Add a "priority" column with ALTER TABLE
