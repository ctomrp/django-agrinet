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

/* Insert de Regiones */
INSERT INTO location_region(name) VALUES('Tarapacá')
                                ,('Antofagasta')
                                ,('Atacama')
                                ,('Coquimbo')
                                ,('Valparaíso')
                                ,('Libertador General Bernardo O"Higgins')
                                ,('Maule')
                                ,('Biobío')
                                ,('La Araucanía')
                                ,('Los Lagos')
                                ,('Aysén del General Carlos Ibáñez del Campo')
                                ,('Magallanes y de la Antártica Chilena')
                                ,('Metropolitana de Santiago')
                                ,('Los Ríos')
                                ,('Arica y Parinacota')
                                ,('Ñuble');

/* Insert de Comunas */
INSERT INTO location_commune (name, region_id) VALUES('Alto Hospicio',1)
                                            ,('Iquique',1)
                                            ,('Camiña',1)
                                            ,('Colchane',1)
                                            ,('Huara',1)
                                            ,('Pica',1)
                                            ,('Pozo Almonte',1)
                                            ,('Antofagasta',2)
                                            ,('Mejillones',2)
                                            ,('Sierra Gorda',2)
                                            ,('Taltal',2)
                                            ,('Calama',2)
                                            ,('Ollagüe',2)
                                            ,('San Pedro de Atacama',2)
                                            ,('María Elena',2)
                                            ,('Tocopilla',2)
                                            ,('Chañaral',3)
                                            ,('Diego de Almagro',3)
                                            ,('Caldera',3)
                                            ,('Copiapó',3)
                                            ,('Tierra Amarilla',3)
                                            ,('Alto del Carmen',3)
                                            ,('Freirina',3)
                                            ,('Huasco',3)
                                            ,('Vallenar',3)              
                                            ,('Andacollo',4)
                                            ,('Coquimbo',4)
                                            ,('La Higuera',4)
                                            ,('La Serena',4)
                                            ,('Paihuano',4)
                                            ,('Vicuña',4)
                                            ,('Combarbalá',4)
                                            ,('Monte Patria',4)
                                            ,('Ovalle',4)
                                            ,('Punitaqui',4)
                                            ,('Río Hurtado',4)
                                            ,('Canela',4)
                                            ,('Illapel',4)
                                            ,('Los Vilos',4)
                                            ,('Salamanca',4)                                       
                                            ,('Rapa Nui',5)
                                            ,('Calle Larga',5)
                                            ,('Los Andes',5)
                                            ,('Rinconada',5)
                                            ,('San Esteban',5)
                                            ,('Cabildo',5)
                                            ,('La Ligua',5)
                                            ,('Papudo',5)
                                            ,('Petorca',5)
                                            ,('Zapallar',5)
                                            ,('Hijuelas',5)
                                            ,('La Calera',5)
                                            ,('La Cruz',5)
                                            ,('Nogales',5)
                                            ,('Quillota',5)
                                            ,('Algarrobo',5)
                                            ,('Cartagena',5)
                                            ,('El Quisco',5)
                                            ,('El Tabo',5)
                                            ,('San Antonio',5)
                                            ,('Santo Domingo',5)
                                            ,('Catemu',5)
                                            ,('Llay-Llay',5)
                                            ,('Panquehue',5)
                                            ,('Putaendo',5)
                                            ,('San Felipe',5)
                                            ,('Santa María',5)
                                            ,('Casablanca',5)
                                            ,('Concón',5)
                                            ,('Juan Fernández',5)
                                            ,('Puchuncaví',5)
                                            ,('Quintero',5)
                                            ,('Valparaíso',5)
                                            ,('Viña del Mar',5)
                                            ,('Limache',5)
                                            ,('Olmué',5)
                                            ,('Quilpué',5)
                                            ,('Villa Alemana',5)                                     
                                            ,('Codegua',6)
                                            ,('Coinco',6)
                                            ,('Coltauco',6)
                                            ,('Doñihue',6)
                                            ,('Graneros',6)
                                            ,('Las Cabras',6)
                                            ,('Machalí',6)
                                            ,('Malloa',6)
                                            ,('Mostazal',6)
                                            ,('Olivar',6)
                                            ,('Peumo',6)
                                            ,('Pichidegua',6)
                                            ,('Quinta de Tilcoco',6)
                                            ,('Rancagua',6)
                                            ,('Rengo',6)
                                            ,('Requínoa',6)
                                            ,('San Vicente de Tagua Tagua',6)
                                            ,('La Estrella',6)
                                            ,('Litueche',6)
                                            ,('Marchigüe',6)
                                            ,('Navidad',6)
                                            ,('Paredones',6)
                                            ,('Pichilemu',6)
                                            ,('Chépica',6)
                                            ,('Chimbarongo',6)
                                            ,('Lolol',6)
                                            ,('Nancagua',6)
                                            ,('Palmilla',6)
                                            ,('Peralillo',6)
                                            ,('Placilla',6)
                                            ,('Pumanque',6)
                                            ,('San Fernando',6)
                                            ,('Santa Cruz',6)                                         
                                            ,('Cauquenes',7)
                                            ,('Chanco',7)
                                            ,('Pelluhue',7)
                                            ,('Curicó',7)
                                            ,('Hualañé',7)
                                            ,('Licantén',7)
                                            ,('Molina',7)
                                            ,('Rauco',7)
                                            ,('Romeral',7)
                                            ,('Sagrada Familia',7)
                                            ,('Teno',7)
                                            ,('Vichuquén',7)
                                            ,('Colbún',7)
                                            ,('Linares',7)
                                            ,('Longaví',7)
                                            ,('Parral',7)
                                            ,('Retiro',7)
                                            ,('San Javier',7)
                                            ,('Villa Alegre',7)
                                            ,('Yerbas Buenas',7)
                                            ,('Constitución',7)
                                            ,('Curepto',7)
                                            ,('Empedrado',7)
                                            ,('Maule',7)
                                            ,('Pelarco',7)
                                            ,('Pencahue',7)
                                            ,('Río Claro',7)
                                            ,('San Clemente',7)
                                            ,('San Rafael',7)
                                            ,('Talca',7)                                       
                                            ,('Arauco',8)
                                            ,('Cañete',8)
                                            ,('Contulmo',8)
                                            ,('Curanilahue',8)
                                            ,('Lebu',8)
                                            ,('Los Álamos',8)
                                            ,('Tirúa',8)
                                            ,('Alto Biobío',8)
                                            ,('Antuco',8)
                                            ,('Cabrero',8)
                                            ,('Laja',8)
                                            ,('Los Ángeles',8)
                                            ,('Mulchén',8)
                                            ,('Nacimiento',8)
                                            ,('Negrete',8)
                                            ,('Quilaco',8)
                                            ,('Quilleco',8)
                                            ,('San Rosendo',8)
                                            ,('Santa Bárbara',8)
                                            ,('Tucapel',8)
                                            ,('Yumbel',8)
                                            ,('Chiguayante',8)
                                            ,('Concepción',8)
                                            ,('Coronel',8)
                                            ,('Florida',8)
                                            ,('Hualpén',8)
                                            ,('Hualqui',8)
                                            ,('Lota',8)
                                            ,('Penco',8)
                                            ,('San Pedro de la Paz',8)
                                            ,('Santa Juana',8)
                                            ,('Talcahuano',8)
                                            ,('Tomé',8)                                        
                                            ,('Carahue',9)
                                            ,('Cholchol',9)
                                            ,('Cunco',9)
                                            ,('Curarrehue',9)
                                            ,('Freire',9)
                                            ,('Galvarino',9)
                                            ,('Gorbea',9)
                                            ,('Lautaro',9)
                                            ,('Loncoche',9)
                                            ,('Melipeuco',9)
                                            ,('Nueva Imperial',9)
                                            ,('Padre Las Casas',9)
                                            ,('Perquenco',9)
                                            ,('Pitrufquén',9)
                                            ,('Pucón',9)
                                            ,('Puerto Saavedra',9)
                                            ,('Temuco',9)
                                            ,('Teodoro Schmidt',9)
                                            ,('Toltén',9)
                                            ,('Vilcún',9)
                                            ,('Villarrica',9)
                                            ,('Angol',9)
                                            ,('Collipulli',9)
                                            ,('Curacautín',9)
                                            ,('Ercilla',9)
                                            ,('Lonquimay',9)
                                            ,('Los Sauces',9)
                                            ,('Lumaco',9)
                                            ,('Purén',9)
                                            ,('Renaico',9)
                                            ,('Traiguén',9)
                                            ,('Victoria',9)                                        
                                            ,('Ancud',10)
                                            ,('Castro',10)
                                            ,('Chonchi',10)
                                            ,('Curaco de Vélez',10)
                                            ,('Dalcahue',10)
                                            ,('Puqueldón',10)
                                            ,('Queilén',10)
                                            ,('Quemchi',10)
                                            ,('Quellón',10)
                                            ,('Quinchao',10)
                                            ,('Calbuco',10)
                                            ,('Cochamó',10)
                                            ,('Fresia',10)
                                            ,('Frutillar',10)
                                            ,('Llanquihue',10)
                                            ,('Los Muermos',10)
                                            ,('Maullín',10)
                                            ,('Puerto Montt',10)
                                            ,('Puerto Varas',10)
                                            ,('Osorno',10)
                                            ,('Puerto Octay',10)
                                            ,('Purranque',10)
                                            ,('Puyehue',10)
                                            ,('Río Negro',10)
                                            ,('San Juan de la Costa',10)
                                            ,('San Pablo',10)
                                            ,('Chaitén',10)
                                            ,('Futaleufú',10)
                                            ,('Hualaihué',10)
                                            ,('Palena',10)                                      
                                            ,('Cisnes',11)
                                            ,('Guaitecas',11)
                                            ,('Aysén',11)
                                            ,('Cochrane',11)
                                            ,('O"Higgins',11)
                                            ,('Tortel',11)
                                            ,('Coyhaique',11)
                                            ,('Lago Verde',11)
                                            ,('Chile Chico',11)
                                            ,('Río Ibáñez',11)                                       
                                            ,('Antártica',12)
                                            ,('Cabo de Hornos',12)
                                            ,('Laguna Blanca',12)
                                            ,('Punta Arenas',12)
                                            ,('Río Verde',12)
                                            ,('San Gregorio',12)
                                            ,('Porvenir',12)
                                            ,('Primavera',12)
                                            ,('Timaukel',12)
                                            ,('Natales',12)
                                            ,('Torres del Paine',12)                            
                                            ,('Colina',13)
                                            ,('Lampa',13)
                                            ,('Til Til',13)
                                            ,('Pirque',13)
                                            ,('Puente Alto',13)
                                            ,('San José de Maipo',13)
                                            ,('Buin',13)
                                            ,('Calera de Tango',13)
                                            ,('Paine',13)
                                            ,('San Bernardo',13)
                                            ,('Alhué',13)
                                            ,('Curacaví',13)
                                            ,('María Pinto',13)
                                            ,('Melipilla',13)
                                            ,('San Pedro',13)
                                            ,('Cerrillos',13)
                                            ,('Cerro Navia',13)
                                            ,('Conchalí',13)
                                            ,('El Bosque',13)
                                            ,('Estación Central',13)
                                            ,('Huechuraba',13)
                                            ,('Independencia',13)
                                            ,('La Cisterna',13)
                                            ,('La Granja',13)
                                            ,('La Florida',13)
                                            ,('La Pintana',13)
                                            ,('La Reina',13)
                                            ,('Las Condes',13)
                                            ,('Lo Barnechea',13)
                                            ,('Lo Espejo',13)
                                            ,('Lo Prado',13)
                                            ,('Macul',13)
                                            ,('Maipú',13)
                                            ,('Ñuñoa',13)
                                            ,('Pedro Aguirre Cerda',13)
                                            ,('Peñalolén',13)
                                            ,('Providencia',13)
                                            ,('Pudahuel',13)
                                            ,('Quilicura',13)
                                            ,('Quinta Normal',13)
                                            ,('Recoleta',13)
                                            ,('Renca',13)
                                            ,('San Miguel',13)
                                            ,('San Joaquín',13)
                                            ,('San Ramón',13)
                                            ,('Santiago',13)
                                            ,('Vitacura',13)
                                            ,('El Monte',13)
                                            ,('Isla de Maipo',13)
                                            ,('Padre Hurtado',13)
                                            ,('Peñaflor',13)
                                            ,('Talagante',13)                                  
                                            ,('Mariquina',14)
                                            ,('Lanco',14)
                                            ,('Máfil',14)
                                            ,('Valdivia',14)
                                            ,('Corral',14)
                                            ,('Paillaco',14)
                                            ,('Los Lagos',14)
                                            ,('Panguipulli',14)
                                            ,('La Unión',14)
                                            ,('Río Bueno',14)
                                            ,('Lago Ranco',14)
                                            ,('Futrono',14)                                    
                                            ,('Arica',15)
                                            ,('Camarones',15)
                                            ,('General Lagos',15)
                                            ,('Putre',15)                                  
                                            ,('Cobquecura',16)
                                            ,('Coelemu',16)
                                            ,('Ninhue',16)
                                            ,('Portezuelo',16)
                                            ,('Quirihue',16)
                                            ,('Ránquil',16)
                                            ,('Trehuaco',16)
                                            ,('Bulnes',16)
                                            ,('Chillán Viejo',16)
                                            ,('Chillán',16)
                                            ,('El Carmen',16)
                                            ,('Pemuco',16)
                                            ,('Pinto',16)
                                            ,('Quillón',16)
                                            ,('San Ignacio',16)
                                            ,('Yungay',16)
                                            ,('Coihueco',16)
                                            ,('Ñiquén',16)
                                            ,('San Carlos',16)
                                            ,('San Fabián',16)
                                            ,('San Nicolás',16);
