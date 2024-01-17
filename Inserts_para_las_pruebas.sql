/* Insert de Categorias de Productos */
INSERT INTO products_productcategory  VALUES (1, 'Fruta');
INSERT INTO products_productcategory  VALUES (2, 'Verdura');
INSERT INTO products_productcategory  VALUES (3, 'Tuberculo');
INSERT INTO products_productcategory  VALUES (4, 'Legumbre');
INSERT INTO products_productcategory  VALUES (5, 'Hortaliza');

/* Insert de Estados de Postulacion */
INSERT INTO producer_application_applicationformstate  VALUES(10, 'Pendiente');
INSERT INTO producer_application_applicationformstate VALUES(20, 'Aprobado');
INSERT INTO producer_application_applicationformstate VALUES(30, 'Rechazado');

/* Insert de Métodos de Pago */
INSERT INTO sales_paymentmethod VALUES(1, 'Tarjeta de Débito');
INSERT INTO sales_paymentmethod VALUES(2, 'Tarjeta de Crédito');
INSERT INTO sales_paymentmethod VALUES(3, 'Transferencia Bancaria');

/* Insert de Métodos de Envío */
INSERT INTO sales_shippingmethod VALUES (1, 'Encomienda');
INSERT INTO sales_shippingmethod VALUES (2, 'Retiro');

/* Insert de Tipos de Recibo */
INSERT INTO sales_receipttype VALUES (1, 'Boleta');
INSERT INTO sales_receipttype VALUES (2, 'Factura');