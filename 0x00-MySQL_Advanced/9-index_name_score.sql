-- Create index idx_name_first_score on first letter of name and score column in names table
-- Create the index
CREATE INDEX idx_name_first_score
ON names(name(1), score);
