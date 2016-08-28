SELECT pi.id, p.nombreDelPlatillo, i.nombreDelProducto
FROM lacasona.platillo_ingredientes pi, lacasona.inventario i, lacasona.platillo p
where pi.inventario_id=i.idProducto
and pi.platillo_id=p.idPlatillo; 
