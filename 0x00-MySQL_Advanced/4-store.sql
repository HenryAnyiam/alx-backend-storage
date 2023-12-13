-- Create a trigger to decrease items after order

DELIMITER // ;

CREATE TRIGGER decreaseItems
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER ; //
