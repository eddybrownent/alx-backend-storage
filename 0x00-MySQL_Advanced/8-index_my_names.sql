-- Create index idx_name_first on first letter of name column in names table
-- Create the index
CREATE INDEX idx_name_first
ON names (name(1));
