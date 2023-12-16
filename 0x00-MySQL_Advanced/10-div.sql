-- Creates function SafeDiv that divides first number by second number or returns 0 if 2nd num is == 0

-- Create the function
DELIMITER $$;

CREATE FUNCTION SafeDiv(
    a INT,
    b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;

    IF b = 0 THEN
        RETURN 0;
    END IF;

    SET result = (a * 1.0) / b;
    RETURN result;
END;
$$;
DELIMITER ;
