-- Selects band_name and computes lifespan for bands with Glam Rock as their main style
-- Results are ordered by lifespan in descending order
SELECT
    band_name,
    (IFNULL(split, 2022) - formed) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
