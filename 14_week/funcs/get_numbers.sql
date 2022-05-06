CREATE OR REPLACE FUNCTION get_numbers_by_names()
  RETURNS TABLE(person_name VARCHAR, person_number VARCHAR) AS
$$
BEGIN
 RETURN QUERY

 SELECT phonebook.person_name, phonebook.person_number
 FROM phonebook
 
 WHERE phonebook.person_name LIKE 'An%';
 RETURN;
END;  $$

LANGUAGE plpgsql;