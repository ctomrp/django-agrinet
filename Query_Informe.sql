SELECT 
	pp.name, /*Producto*/
	pp2.name, /*Categoría producto*/
	SUM(ss2.quantity), /*Cantidad vendida*/
	SUM(ss2.quantity)*pp.price /*Total recaudado por producto*/
FROM 
	sales_sales ss 
	INNER JOIN
	sales_salesproducts ss2
	ON(ss.id = ss2.sale_id) 
	INNER JOIN products_product pp
	ON(pp.id = ss2.product_id)
	INNER JOIN products_productcategory pp2 
	ON(pp.category_id = pp2.id)
WHERE
	pp.producer_id = 2 /*Aquí se reemplaza el 2 por el id del productor que va a ejecutar el informe*/
	AND
	ss.date_sale BETWEEN '2024-01-18' AND '2024-01-24' /*Aquí se reemplaza por las fechas que indique el productor en la vista*/
GROUP BY
	pp.name, pp2.name
ORDER BY
	3 DESC
;
